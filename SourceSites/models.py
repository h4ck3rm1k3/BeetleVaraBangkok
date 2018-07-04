from django.db import models
from django.contrib import admin
from model_utils.models import StatusModel, TimeFramedModel, TimeStampedModel
from model_utils import Choices
from model_utils.managers import InheritanceManager

class NamedModel(models.Model):
    """ A base model with a name """

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class SourceSite(NamedModel, StatusModel):
#    class Meta:
#        app_label = 'cal'

    STATUS = Choices('new','working','failed','not resolving','not responding','noaccess', 'overloaded')
        
    objects = InheritanceManager()
    website = models.CharField(max_length=500,unique=True)

    #categories = models.ManyToManyField(
    #    'category.Category',
    #    help_text='Categorize this item.'
    #)
    
    #tags = models.ManyToManyField(
    #    'category.Tag',
    #    help_text='Tag this item.'
    #)
class SourceSiteAdmin(admin.ModelAdmin):
     list_display = ('name', 'website')
        
class ApiSourceSite(SourceSite):

    # what does this api provide
    # https://www.programmableweb.com/apis/directory
    # https://github.com/toddmotto/public-apis
    description = models.CharField(max_length=200)
    https = models.BooleanField(default=1)
    cors = models.BooleanField(default=1)
    
    

class Authentication(NamedModel, StatusModel, TimeFramedModel, TimeStampedModel):
    """
    Authentication is the base class of all types of authentication, it has a status and time information.
    The end time is set when the auth is no longer valid.
    """
    STATUS = Choices('new','working','failed','compromised')
    TYPE = Choices('oauth2','simple','ssh')

    password = models.CharField(max_length=200)
    userid = models.CharField(max_length=100)
    token = models.CharField(max_length=255)
    
    

class Profile(NamedModel, StatusModel, TimeFramedModel, TimeStampedModel):
    """
    The Profile is an account on many sites that has a status.
    """
    #sites2 = models.ManyToManyField(SourceSite)
    auth = models.ForeignKey(Authentication, null=True, on_delete=models.SET_NULL)
    STATUS = Choices('new','working','failed','disabled','comprimised')
    
class Agent(NamedModel, StatusModel, TimeFramedModel, TimeStampedModel):
    """
    A host/process that runs access to other hosts
    """
    STATUS = Choices('new','working','failed','not resolving','not responding','noaccess', 'overloaded')    

class AccessSession(StatusModel, TimeFramedModel, TimeStampedModel):
    """
    Session to access a website, 
    """
    STATUS = Choices('new','working','failed','not resolving','not responding','noaccess')
    site = models.ForeignKey(SourceSite,null=True, on_delete=models.SET_NULL)
    auth = models.ForeignKey(Authentication, null=True, on_delete=models.SET_NULL)
    agent = models.ForeignKey(Agent,null=True, on_delete=models.SET_NULL)
