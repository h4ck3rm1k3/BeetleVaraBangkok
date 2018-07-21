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
    "URIS that can be subjects or objects"
    
class PUris(BaseUris):
    "PredicateUri predicates are fields"

class CUris(BaseUris):
    "ContextUri a context is used to group triples"

class TUris(BaseUris):
    "LiteralTypeUri types of literals, can refer to types of strings, types of integers and floats etc"
    
class SoBlank(models.Model):
    """
    Blanks are used for intermediate objects with no name or uri
    """
    blank = models.TextField(unique=True, null=False)


class OLiteral(models.Model):
    """
    Typed literal strings
    """
    ntype = models.ForeignKey(TUris, null=True, on_delete=models.SET_NULL)
    lang = models.CharField(max_length=10)
    text = models.TextField(unique=True, null=False)

    
class IntLiteral(models.Model):
    ntype = models.ForeignKey(TUris, null=True, on_delete=models.SET_NULL)
    value = models.IntegerField(null=False)

class FloatLiteral(models.Model):
    ntype = models.ForeignKey(TUris, null=True, on_delete=models.SET_NULL)
    value = models.FloatField(null=False)

class Triple(models.Model):

    # subject
    s_uri = models.ForeignKey(SoUris, null=True, on_delete=models.SET_NULL, related_name="source_triple")
    s_blank = models.ForeignKey(SoBlank, null=True, on_delete=models.SET_NULL, related_name="source_triple")

    # predicate
    predicate = models.ForeignKey(PUris, null=False, on_delete=models.PROTECT,related_name="triple")

    # object
    o_uri = models.ForeignKey(SoUris, null=True, on_delete=models.SET_NULL, related_name="object_triple")
    o_blank = models.ForeignKey(SoBlank, null=True, on_delete=models.SET_NULL, related_name="object_triple")
    o_literal = models.ForeignKey(OLiteral, null=True, on_delete=models.SET_NULL,related_name="object_triple")
    o_boolean = models.BooleanField( null=True)
    o_integer = models.ForeignKey(IntLiteral, null=True, on_delete=models.SET_NULL,related_name="object_triple")
    o_float = models.ForeignKey(FloatLiteral, null=True, on_delete=models.SET_NULL,related_name="object_triple")

    # context
    context = models.ForeignKey(CUris, null=True, on_delete=models.SET_NULL,related_name="context_triple")    

