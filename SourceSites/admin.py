from django.contrib import admin

# Register your models here.
import SourceSites.models
import inspect
for x in [
        'AccessSession',
        'Agent',
        'ApiSourceSite',
        'Authentication',
        #'Choices',
        #'InheritanceManager',
        #'NamedModel',
        'Profile',
        'SourceSite',
        #'StatusModel',
        #'TimeFramedModel',
        #'TimeStampedModel'
]:
    admin.site.register(getattr(SourceSites.models, x))

#
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
