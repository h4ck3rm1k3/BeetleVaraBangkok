from django.db import models

from model_utils.models import StatusModel
from model_utils import Choices

class NamedModel(models.Model):
    """ A base model with a name """

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class SourceSite(NamedModel, StatusModel):
    objects = InheritanceManager()
    website = models.CharField(max_length=200)

class ApiSourceSite(SourceSite):
    

class Authentication(NamedModel, StatusModel):
    STATUS = Choices('new','working','failed','compromised')
    class Meta:
        abstract = True
    
class SimpleAuthentication(Authentication):
    password = models.CharField(max_length=200)
    userid = models.CharField(max_length=100)

class TokenAuthentication(Authentication):
    token = models.CharField(max_length=255)
    userid = models.BigIntegerField(unique=True)
    
class OAuth2Authentication(Authentication):
    token = models.CharField(max_length=255)
    userid = models.BigIntegerField(unique=True)
    

class AccessSession(models.Model):    
     name = models.CharField(max_length=100)
