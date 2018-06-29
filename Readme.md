# codename : BeetleVaraBangkok
Model for an api access tool used to create a conference

# Data Sources
List of Sites that provide APIs, each api would have a form of data Model
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
* APIS
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


Projects to evaluate
https://github.com/MattBroach/DjangoRestMultipleModels.git
https://docs.djangoproject.com/en/2.0/topics/settings/
https://github.com/beda-software/drf-writable-nested
https://github.com/zmathew/django-backbone
https://github.com/wq/wq.db

Docs to eval:
https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/

