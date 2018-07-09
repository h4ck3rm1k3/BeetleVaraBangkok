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

    
def r(x) :
  parts=[["root","root",x]  ]
  while len(parts) > 0:
    t1 = parts.pop()

    ##
    sid = t1[0] # subject is passed as a string that is looked pu
    s_blank_id = cache (RdfGraph.models.SoBlank,blank=sid) # the object representing the subject
    
    p_uri_id=cache(RdfGraph.models.PUris,url=t1[1]) # predicate


    t = t1[2] # subject is passed as a string that is looked up

    # object created
    no = None

    # statemente created
    st = None


    #

    if isinstance(t,collections.OrderedDict) or isinstance(t,dict):

        strv = str(t)
        obj_id = hashlib.md5(strv.encode('utf-8')).hexdigest() # calculate a md5sun
        #str(id(t))
        
        o_blank_id=cache(RdfGraph.models.SoBlank,blank=obj_id) # object

        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_blank_id=o_blank_id
        )
        for x,v in t.items():
            parts.append([obj_id,x, v])
            
    elif isinstance(t,list):
        # the list is disolved into a set ok kv pairs with the element number
      nm = 1
      for v in t:
        parts.append([obj_id,"list_element_{0}".format(nm), v])
        nm = nm + 1
        
    elif isinstance(t,bool):
        no = cache(RdfGraph.models.BLiteral,value=t)
        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_blit_id=no
        )
    elif isinstance(t,int):
        no = cache(RdfGraph.models.IntLiteral,value=t)
        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_intlit_id=no
        )
    elif isinstance(t,float):
        no = cache(RdfGraph.models.FloatLiteral,value=t)
        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_flit_id=no
        )
    elif isinstance(t,str):
        no = cache(RdfGraph.models.StrLiteral,text=t) # object
        
        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_strlit_id=no
        )
    elif isinstance(t,unicode):
        no = cache(RdfGraph.models.StrLiteral,text=t) # object
        st = RdfGraph.models.Triple(
            s_blank_id = s_blank_id,
            p_uri_id= p_uri_id,
            o_strlit_id=no
        )
    else:
      print (type(t))

    if no:
        #pprint.pprint (no.__dict__)
        no.save()

    if st:
        #pprint.pprint (st.__dict__)
        st.save()
        
with open("test.json") as inf:
    tree =json.load(inf)
    with transaction.atomic():
        r(tree)

def report():
    cl = {'k':keys,'t':texts,'a':attrs}
    for c in cl :
        for x in cl[c]:
            print (c, x, cl[c][x])

