"""
Simple django representation of the librdf/redland graph database
"""
from django.db import models

# derived from 
# https://github.com/mro/librdf.sqlite/blob/3a21a87c1d8ef3fa9fbe90849a359c813f37cc82/sql/add/db.sql

class BaseUris(models.Model):
    url = models.URLField(max_length=200, unique=True, null=False)
    class Meta:
        abstract = True
        
class SoUris(BaseUris):
    "SubjectObjectUri"
    
class PUris(BaseUris):
    "PredicateUri"

class CUris(BaseUris):
    "ContextUri"

class TUris(BaseUris):
    "LiteralTypeUri"
    
class SoBlank(models.Model):
    blank = models.TextField(unique=True, null=False)

class OLiteral(models.Model):
    ntype = models.ForeignKey(TUris, null=True, on_delete=models.SET_NULL)
    lang = models.CharField(max_length=10)
    text = models.TextField(unique=True, null=False)

class StrLiteral(models.Model):
    lang = models.CharField(max_length=10)
    text = models.TextField(unique=True, null=False)
    
class BLiteral(models.Model):
    value = models.BooleanField(null=False)

class IntLiteral(models.Model):
    value = models.IntegerField(null=False)

class FloatLiteral(models.Model):
    value = models.FloatField(null=False)

class Triple(models.Model):

    # subject
    s_uri_id = models.ForeignKey(SoUris, null=True, on_delete=models.SET_NULL, related_name="source_triple")
    s_blank_id = models.ForeignKey(SoBlank, null=True, on_delete=models.SET_NULL, related_name="source_triple")

    # predicate
    p_uri_id = models.ForeignKey(PUris, null=False, on_delete=models.PROTECT)

    # object
    o_uri_id = models.ForeignKey(SoUris, null=True, on_delete=models.SET_NULL, related_name="object_triple")
    o_blank_id = models.ForeignKey(SoBlank, null=True, on_delete=models.SET_NULL, related_name="object_triple")
    o_lit_id = models.ForeignKey(OLiteral, null=True, on_delete=models.SET_NULL)
    o_blit_id = models.ForeignKey(BLiteral, null=True, on_delete=models.SET_NULL)
    o_intlit_id = models.ForeignKey(IntLiteral, null=True, on_delete=models.SET_NULL)
    o_flit_id = models.ForeignKey(FloatLiteral, null=True, on_delete=models.SET_NULL)
    o_strlit_id = models.ForeignKey(StrLiteral, null=True, on_delete=models.SET_NULL)

    # context
    c_uri_id = models.ForeignKey(CUris, null=True, on_delete=models.SET_NULL)    

