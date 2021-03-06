# codename : BeetleVaraBangkok

Social media tool used to create a conference via access to various apis.

# Sprints

1. Collection of web resources, bookmarks.
2. Import bookmarks
3. Crawl pages
4. Find wikipedia/wikidata articles that reference pages

# Big Long Term Goals
Collect information about target locations, people, audience, speakers, topics
and present them to curation team for selection, evaluation, ranking and decision.
Resource scheduling and planning algorithms are needed.
Feedback from public needs to be collected.
Tokens are used to measure resource usage, votes and other key measurements.
Decentralized system, run your own node, federate, share data as needed.
Compile the python code to run as a mobile app. https://kivy.org/#home maybe


# Data Sources
List of Sites that provide APIs, each api would have a form of data Model

* Yacy like network of search
http://search.yacy.net/

* Common crawl like repository of needed websites.
https://commoncrawl.org/

* Wikidata
https://github.com/putmantime/CMOD.Django

* Wikipedia
https://github.com/gunyarakun/django-wikipedia-search

* Openstreetmap
https://github.com/willemarcel/osmcha-django/
  
* Github
* Reddit
* Twitter
* Lanyard
* Eventbrite


* Facebook
https://github.com/tschellenbach/Django-facebook/blob/master/django_facebook/models.py

# Model
* Locations
  https://github.com/caioariede/django-location-field
  https://github.com/andymboyle/EasyMapper/blob/master/easymapper/models.py
  https://github.com/kirchenreich/kirchenreich

* Institutions
* Roles
* People
* Contacts
* Websites

  html,parser
  Markdown, parser
  mediawiki,
  pandoc
  
* APIS

  * APIS with openapi/swagger interfaces
    Be able to build swagger interfaces for other apis by describing them

  * be able to search for apis
  like this
    https://www.programmableweb.com/search/wikipedia
    
  * Other APIS for wikidata
    https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual
    * SPARQL
      https://query.wikidata.org/sparql?query=SPARQL
      Triples
      https://query.wikidata.org/bigdata/ldf?subject=http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ146

      
    * Mediawiki
    open search    https://www.mediawiki.org/wiki/API:Opensearch
    mediawiki rest api https://www.mediawiki.org/wiki/REST_API

  * Apis with existing python interfaces
    Extract information from existing python code, introspection
    Capture network packages and decode them
    Capture log files and messages
    Intercept functions at runtime
    Be able to generate reprsentations :
       1. urls, abs and relative
       2. files and network packages
       3. Blobs and strings in memory, lines or parts string
       4. Parsing of strings and splitting them, giving types
       5. Handling of ast data as needed, transforming to different forms.

       Json Schema
       	    be able to extract out properties and types from json schema and map them onto Model classes in django
	    like the xsdtodjgno https://github.com/tuffnatty/xsd_to_django_model

* Topics
* Tracks
* Speakers
* Projects
* Committers
* Commits

# Operations
* Searching for items
* Displaying lists of items
* Displaying item
  * Follow link to show original
* Display items on Map
* Selection of key instances
* Relating instances betweeen each other
* Description of Classes
* Description of Properties
* Mapping of tags or properties onto each other.
* Creation of simple relational models that map the graph data
* Managing the updating of the data, syncing of the changes.
* Editing instance
* Updating back end data

# Apps
* Sites a list of sites with descriptions of the interfaces


# History 

* Sources
https://github.com/mbrochh/django-graphql-apollo-react-demo
https://github.com/graphql-python/swapi-graphene/blob/master/starwars/models.py

Docs
	https://docs.djangoproject.com/en/2.0/intro/tutorial01/
	https://codeinthehole.com/tips/using-pip-and-requirementstxt-to-install-from-the-head-of-a-github-branch/

Inheritance
	https://github.com/jazzband/django-model-utils
	https://stackoverflow.com/questions/47619535/django-model-inheritance-get-child
	
    ~/.local/bin/django-admin startproject BeetleVaraBangkok
     cd BeetleVaraBangkok/
     git init
     download  .gitignore 
     git add *
     python3.7 ./manage.py  migrate
     git commit -m 'v1'
     git status
     ./manage.py

Create source sites
     ./manage.py startapp SourceSites

     python3.7 -m pip install -r requirements.txt

     ./manage.py createsuperuser
     ./manage.py makemigrations
     ./manage.py migrate

# Populate some links

     pandoc Readme.md  | grep http | cut "-d " -f2 | grep https | cut '-d<' -f1  > links.txt
     for x in `cat links.txt`; do sed -e "s%<\$1>%$x%g" SourceSites/fixtures/sites.tt; done  > SourceSites/fixtures/baresites.yaml
     ./manage.py loaddata baresites

     cat requirements.txt | cut -d/ -f3- | cut -d\# -f1 | sed -e's/.git//g' | grep git >> gitlinks.txt
     for x in `cat gitlinks.txt`; do sed -e "s%<\$1>%$x%g" SourceSites/fixtures/sites.tt; done  > SourceSites/fixtures/gitsites.yaml
     ./manage.py loaddata gitsites
 
Projects to evaluate
https://github.com/MattBroach/DjangoRestMultipleModels.git
https://docs.djangoproject.com/en/2.0/topics/settings/
https://github.com/beda-software/drf-writable-nested
https://github.com/zmathew/django-backbone
https://github.com/wq/wq.db

Docs to eval:
https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/



# Celery

## install rabbit mq
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags myuser mytag
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

## setup config
edit flowerconfig.py

## start  flower
python3.7 -m flower  --port=5555

## start worker
python3.7 -m  celery -A process2 worker --loglevel=info


# TODO
remove the _id from field names because they are double


# debug django backend
import logging
log = logging.getLogger('django.db.backends')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


# processing

# 
# provision server
# setup server
# checkout git workspace


# CMDB
python tool
https://github.com/allegro/ralph

to eval
https://sourceforge.net/projects/i-doit/files/i-doit/1.11/
https://sourceforge.net/projects/itop/files/itop/2.5.0/
https://github.com/tumblr/collins
https://github.com/clusto/clusto

List of projects:
https://github.com/kahun/awesome-sysadmin#


# airflow
https://github.com/apache/incubator-airflow