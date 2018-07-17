from celery import Celery
app = Celery()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BeetleVaraBangkok.settings')
import hashlib
import django
django.setup()

import json
import collections
import RdfGraph.models
from django.db import transaction
import pprint
from django.core.exceptions import ObjectDoesNotExist
import html5lib
#import serpy
import requests
import collections
from xmljson import badgerfish as bf
import json

# global cache
seen = {}

def cache(c, **kv):

    key_name = list(kv.keys())[0]
    x = kv[key_name]
    #print ('cache',x)
    # is it cached?
    ckey = str(c) + str(x)
    
    if ckey in seen :
        return seen[ckey]
    # look in the database
    try :
        o = c.objects.get(**kv)
    except ObjectDoesNotExist:
        o=c(**kv)
        o.save()
        print ("created"+ckey)
    seen[ckey]=o
    return o

# test create_node(RdfGraph.models.SoBlank,'s_blank_id','p_uri_id',blank, 'oblank_id', 'obj_id' )
def create_node(node_type, s_blank_id, p_uri_id, ckey, oname, cvalue):
    cvalues = { ckey : cvalue }
    no = cache(node_type,**cvalues)
    ovalues={ oname : no }
    st = RdfGraph.models.Triple(
        s_blank_id = s_blank_id,
        p_uri_id= p_uri_id,
        **ovalues
        )
    if no:
        #pprint.pprint (no.__dict__)
        no.save()
    return st

def r(x) :
  """
    Recurse over json tree
  """

  # start with a simple root
  parts=[["root","root",x]  ]

  # iterate over the parts in a non recursive fashion
  while len(parts) > 0:
      
    # pop the last one off, is array of [parent, predicate, child]       
    t1 = parts.pop()

    sid = t1[0] # subject is passed as a string

    # cache the string id
    s_blank_id = cache (RdfGraph.models.SoBlank,blank=sid) # the object representing the subject

    # cache the predicate
    p_uri_id=cache(RdfGraph.models.PUris,url=t1[1]) # predicate


    t = t1[2] # target

    # object created
    no = None

    # statement created
    st = None


    if isinstance(t,collections.OrderedDict) or isinstance(t,dict):

        # if the object is a dictionary object, a complex object
        
        strv = str(t) # convert the entire object to a string, this could be slow for large object
        obj_id = hashlib.md5(strv.encode('utf-8')).hexdigest() # calculate a md5sun of the entire object

        st = create_node(RdfGraph.models.SoBlank,s_blank_id,p_uri_id,'blank', 'o_blank_id', obj_id )

        # go over all the key value pairs
        for x,v in t.items():
            parts.append([obj_id,x, v])
            
    elif isinstance(t,list):
        # the list is disolved into a set ok kv pairs with the element number
      nm = 1
      for v in t:
        parts.append([obj_id,"list_element_{0}".format(nm), v])
        nm = nm + 1
        
    elif isinstance(t,bool):
        st = create_node(RdfGraph.models.BLiteral,s_blank_id,p_uri_id,'value', 'o_blit_id', t )

    elif isinstance(t,int):
        if abs(t)>9223372036854776000: # huge number
            # store as string
            st = create_node(RdfGraph.models.StrLiteral,s_blank_id,p_uri_id,'text', 'o_strlit_id', t )
        else:
            st = create_node(RdfGraph.models.IntLiteral,s_blank_id,p_uri_id,'value', 'o_intlit_id', t )
            
    elif isinstance(t,float):
        if abs(t)>9223372036854776000.0: # huge number
            # store as string
            st = create_node(RdfGraph.models.StrLiteral,s_blank_id,p_uri_id,'text', 'o_strlit_id', t )
        else:
            st = create_node(RdfGraph.models.FloatLiteral,s_blank_id,p_uri_id,'value', 'o_flit_id', t )

    elif isinstance(t,str):
        st = create_node(RdfGraph.models.StrLiteral,s_blank_id,p_uri_id,'text', 'o_strlit_id', t )

    elif isinstance(t,unicode):
        st = create_node(RdfGraph.models.StrLiteral,s_blank_id,p_uri_id,'text', 'o_strlit_id', t )

    else:
      print (type(t))


    if st:
        #pprint.pprint (st.__dict__)
        st.save()

@app.task
def load_json(fn):
    with open(fn) as inf:
        tree =json.load(inf)
        with transaction.atomic():
            r(tree)

def report():
    cl = {'k':keys,'t':texts,'a':attrs}
    for c in cl :
        for x in cl[c]:
            print (c, x, cl[c][x])


@app.task
def parse_html_url(url, outfile):
    s = requests.get(url)
    h = s.text
    document = html5lib.parse(h)
    tree = bf.data(document)
    with open(outfile,'w') as of:
        json.dump(fp=of,obj=tree)

@app.task
def parse_html_file(path, outfile):
    s = open(path)
    h = ""
    for x in s:
        h = h + x
    document = html5lib.parse(h)
    tree = bf.data(document)
    with open(outfile,'w') as of:
        json.dump(fp=of,obj=tree)

if __name__ == '__main__':
    #app.worker_main()
    j = "test.json"
    #parse_html_file("./SourceSites/fixtures/std.html", j)
    load_json(j)
