from django.db import models

# schema 
# https://github.com/OAI/OpenAPI-Specification/blob/master/schemas/v2.0/schema.json

class SwaggerObject:
    pass

# Create your models here.
class OpenAPIObject(SwaggerObject):
    pass

class InfoObject(SwaggerObject):
    pass

class ContactObject(SwaggerObject):
    pass

class LicenseObject(SwaggerObject):
    pass

class ServerObject(SwaggerObject):
    pass

class ServerVariableObject(SwaggerObject):
    pass

class ComponentsObject(SwaggerObject):
    pass

class PathsObject(SwaggerObject):
    pass

class PathItemObject(SwaggerObject):
    pass

class OperationObject(SwaggerObject):
    pass

class ExternalDocumentationObject(SwaggerObject):
    pass

class ParameterObject(SwaggerObject):
    pass

class RequestBodyObject(SwaggerObject):
    pass

class MediaTypeObject(SwaggerObject):
    pass

class EncodingObject(SwaggerObject):
    pass

class ResponsesObject(SwaggerObject):
    pass

class ResponseObject(SwaggerObject):
    pass

class CallbackObject(SwaggerObject):
    pass

class ExampleObject(SwaggerObject):
    pass

class LinkObject(SwaggerObject):
    pass

class HeaderObject(SwaggerObject):
    pass

class TagObject(SwaggerObject):
    pass

class ReferenceObject(SwaggerObject):
    pass

class SchemaObject(SwaggerObject):
    pass

class DiscriminatorObject(SwaggerObject):
    pass

class XMLObject(SwaggerObject):
    pass

class SecuritySchemeObject(SwaggerObject):
    pass

class OAuthFlowsObject(SwaggerObject):
    pass

class OAuthFlowObject(SwaggerObject):
    pass

class SecurityRequirementObject(SwaggerObject):
    pass
