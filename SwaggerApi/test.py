w = python_jsonschema_objects.ObjectBuilder('./src/openapi-specification/schemas/v2.0/schema.json')
[[p, w._schema['properties'][p]['type']] for p in w._schema['properties'] if 'type' in w._schema['properties'][p]]
[['swagger', 'string'], ['host', 'string'], ['basePath', 'string'], ['tags', 'array']]

[p for p in w._schema['properties'] ][46D
['swagger', 'info', 'host', 'basePath', 'schemes', 'consumes', 'produces', 'paths', 'definitions', 'parameters', 'responses', 'security', 'securityDefinitions', 'tags', 'externalDocs']


defs = ['info', 'contact', 'license', 'paths', 'definitions', 'parameterDefinitions', 'responseDefinitions', 'externalDocs', 'examples', 'mimeType', 'operation', 'pathItem', 'responses', 'responseValue', 'response', 'headers', 'header', 'vendorExtension', 'bodyParameter', 'headerParameterSubSchema', 'queryParameterSubSchema', 'formDataParameterSubSchema', 'pathParameterSubSchema', 'nonBodyParameter', 'parameter', 'schema', 'fileSchema', 'primitivesItems', 'security', 'securityRequirement', 'xml', 'tag', 'securityDefinitions', 'basicAuthenticationSecurity', 'apiKeySecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity', 'oauth2ApplicationSecurity', 'oauth2AccessCodeSecurity', 'oauth2Scopes', 'mediaTypeList', 'parametersList', 'schemesList', 'collectionFormat', 'collectionFormatWithMulti', 'title', 'description', 'default', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'jsonReference']


properties = [['info', dict_keys(['title', 'version', 'description', 'termsOfService', 'contact', 'license'])], ['contact', dict_keys(['name', 'url', 'email'])], ['license', dict_keys(['name', 'url'])], ['externalDocs', dict_keys(['description', 'url'])], ['operation', dict_keys(['tags', 'summary', 'description', 'externalDocs', 'operationId', 'produces', 'consumes', 'parameters', 'responses', 'schemes', 'deprecated', 'security'])], ['pathItem', dict_keys(['$ref', 'get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'parameters'])], ['response', dict_keys(['description', 'schema', 'headers', 'examples'])], ['header', dict_keys(['type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf', 'description'])], ['bodyParameter', dict_keys(['description', 'name', 'in', 'required', 'schema'])], ['headerParameterSubSchema', dict_keys(['required', 'in', 'description', 'name', 'type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf'])], ['queryParameterSubSchema', dict_keys(['required', 'in', 'description', 'name', 'allowEmptyValue', 'type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf'])], ['formDataParameterSubSchema', dict_keys(['required', 'in', 'description', 'name', 'allowEmptyValue', 'type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf'])], ['pathParameterSubSchema', dict_keys(['required', 'in', 'description', 'name', 'type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf'])], ['schema', dict_keys(['$ref', 'format', 'title', 'description', 'default', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'maxProperties', 'minProperties', 'required', 'enum', 'additionalProperties', 'type', 'items', 'allOf', 'properties', 'discriminator', 'readOnly', 'xml', 'externalDocs', 'example'])], ['fileSchema', dict_keys(['format', 'title', 'description', 'default', 'required', 'type', 'readOnly', 'externalDocs', 'example'])], ['primitivesItems', dict_keys(['type', 'format', 'items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf'])], ['xml', dict_keys(['name', 'namespace', 'prefix', 'attribute', 'wrapped'])], ['tag', dict_keys(['name', 'description', 'externalDocs'])], ['basicAuthenticationSecurity', dict_keys(['type', 'description'])], ['apiKeySecurity', dict_keys(['type', 'name', 'in', 'description'])], ['oauth2ImplicitSecurity', dict_keys(['type', 'flow', 'scopes', 'authorizationUrl', 'description'])], ['oauth2PasswordSecurity', dict_keys(['type', 'flow', 'scopes', 'tokenUrl', 'description'])], ['oauth2ApplicationSecurity', dict_keys(['type', 'flow', 'scopes', 'tokenUrl', 'description'])], ['oauth2AccessCodeSecurity', dict_keys(['type', 'flow', 'scopes', 'authorizationUrl', 'tokenUrl', 'description'])], ['jsonReference', dict_keys(['$ref'])]]                                        

pt = [[d,[ [p,w._schema['definitions'][d]['properties'][p]['type']] for p in  w._schema['definitions'][d]['properties'].keys() if 'type' in w._schema['definitions'][d]['properties'][p]] ] for d in w._schema['definitions'] if 'properties' in w._schema['definitions'][d]]
pt2 = [
    ['info', [['title', 'string'], ['version', 'string'], ['description', 'string'], ['termsOfService', 'string']]],
    ['contact', [['name', 'string'], ['url', 'string'], ['email', 'string']]], ['license', [['name', 'string'], ['url', 'string']]], ['externalDocs', [['description', 'string'], ['url', 'string']]],
    ['operation', [['tags', 'array'], ['summary', 'string'], ['description', 'string'], ['operationId', 'string'], ['deprecated', 'boolean']]], ['pathItem', [['$ref', 'string']]],
    ['response', [['description', 'string']]],
    ['header', [['type', 'string'], ['format', 'string'], ['description', 'string']]],
    ['bodyParameter', [['description', 'string'], ['name', 'string'], ['in', 'string'], ['required', 'boolean']]],
    ['headerParameterSubSchema', [['required', 'boolean'], ['in', 'string'], ['description', 'string'], ['name', 'string'], ['type', 'string'], ['format', 'string']]],
    ['queryParameterSubSchema', [['required', 'boolean'], ['in', 'string'], ['description', 'string'], ['name', 'string'], ['allowEmptyValue', 'boolean'], ['type', 'string'], ['format', 'string']]],
    ['formDataParameterSubSchema', [['required', 'boolean'], ['in', 'string'], ['description', 'string'], ['name', 'string'], ['allowEmptyValue', 'boolean'], ['type', 'string'], ['format', 'string']]],
    ['pathParameterSubSchema', [['required', 'boolean'], ['in', 'string'], ['description', 'string'], ['name', 'string'], ['type', 'string'], ['format', 'string']]],
    ['schema', [['$ref', 'string'], ['format', 'string'], ['allOf', 'array'], ['properties', 'object'], ['discriminator', 'string'], ['readOnly', 'boolean']]],
    ['fileSchema', [['format', 'string'], ['type', 'string'], ['readOnly', 'boolean']]],
    ['primitivesItems', [['type', 'string'], ['format', 'string']]],
    ['xml', [['name', 'string'], ['namespace', 'string'], ['prefix', 'string'], ['attribute', 'boolean'], ['wrapped', 'boolean']]],
    ['tag', [['name', 'string'], ['description', 'string']]],
    ['basicAuthenticationSecurity', [['type', 'string'], ['description', 'string']]],
    ['apiKeySecurity', [['type', 'string'], ['name', 'string'], ['in', 'string'], ['description', 'string']]],
    ['oauth2ImplicitSecurity', [['type', 'string'], ['flow', 'string'], ['authorizationUrl', 'string'], ['description', 'string']]],
    ['oauth2PasswordSecurity', [['type', 'string'], ['flow', 'string'], ['tokenUrl', 'string'], ['description', 'string']]],
    ['oauth2ApplicationSecurity', [['type', 'string'], ['flow', 'string'], ['tokenUrl', 'string'], ['description', 'string']]],
    ['oauth2AccessCodeSecurity', [['type', 'string'], ['flow', 'string'], ['authorizationUrl', 'string'], ['tokenUrl', 'string'], ['description', 'string']]],
    ['jsonReference', [['$ref', 'string']]]
]


get_untyped= [[d,[ p for p in  w._schema['definitions'][d]['properties'].keys() if 'type' not in w._schema['definitions'][d]['properties'][p]] ] for d in w._schema['definitions'] if 'properties' in w._schema['definitions'][d]]
untyped = [['info', ['contact', 'license']],
           ['contact', []],
           ['license', []],
           ['externalDocs', []],
           ['operation', ['externalDocs', 'produces', 'consumes', 'parameters', 'responses', 'schemes', 'security']],
           ['pathItem', ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'parameters']],
           ['response', ['schema', 'headers', 'examples']],
           ['header', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['bodyParameter', ['schema']],
           ['headerParameterSubSchema', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['queryParameterSubSchema', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['formDataParameterSubSchema', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['pathParameterSubSchema', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['schema', ['title', 'description', 'default', 'multipleOf', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'maxProperties', 'minProperties', 'required', 'enum', 'additionalProperties', 'type', 'items', 'xml', 'externalDocs', 'example']],
           ['fileSchema', ['title', 'description', 'default', 'required', 'externalDocs', 'example']],
           ['primitivesItems', ['items', 'collectionFormat', 'default', 'maximum', 'exclusiveMaximum', 'minimum', 'exclusiveMinimum', 'maxLength', 'minLength', 'pattern', 'maxItems', 'minItems', 'uniqueItems', 'enum', 'multipleOf']],
           ['xml', []],
           ['tag', ['externalDocs']],
           ['basicAuthenticationSecurity', []],
           ['apiKeySecurity', []],
           ['oauth2ImplicitSecurity', ['scopes']],
           ['oauth2PasswordSecurity', ['scopes']],
           ['oauth2ApplicationSecurity', ['scopes']],
           ['oauth2AccessCodeSecurity', ['scopes']],
           ['jsonReference', []]]


                                        
schema = {'$schema': 'http://json-schema.org/draft-04/schema#',
 'additionalProperties': False,
 'definitions': {'apiKeySecurity': {'additionalProperties': False,
                                    'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                    'properties': {'description': {'type': 'string'},
                                                   'in': {'enum': ['header',
                                                                   'query'],
                                                          'type': 'string'},
                                                   'name': {'type': 'string'},
                                                   'type': {'enum': ['apiKey'],
                                                            'type': 'string'}},
                                    'required': ['type', 'name', 'in'],
                                    'type': 'object'},
                 'basicAuthenticationSecurity': {'additionalProperties': False,
                                                 'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                                 'properties': {'description': {'type': 'string'},
                                                                'type': {'enum': ['basic'],
                                                                         'type': 'string'}},
                                                 'required': ['type'],
                                                 'type': 'object'},
                 'bodyParameter': {'additionalProperties': False,
                                   'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                   'properties': {'description': {'description': 'A '
                                                                                 'brief '
                                                                                 'description '
                                                                                 'of '
                                                                                 'the '
                                                                                 'parameter. '
                                                                                 'This '
                                                                                 'could '
                                                                                 'contain '
                                                                                 'examples '
                                                                                 'of '
                                                                                 'use.  '
                                                                                 'GitHub '
                                                                                 'Flavored '
                                                                                 'Markdown '
                                                                                 'is '
                                                                                 'allowed.',
                                                                  'type': 'string'},
                                                  'in': {'description': 'Determines '
                                                                        'the '
                                                                        'location '
                                                                        'of '
                                                                        'the '
                                                                        'parameter.',
                                                         'enum': ['body'],
                                                         'type': 'string'},
                                                  'name': {'description': 'The '
                                                                          'name '
                                                                          'of '
                                                                          'the '
                                                                          'parameter.',
                                                           'type': 'string'},
                                                  'required': {'default': False,
                                                               'description': 'Determines '
                                                                              'whether '
                                                                              'or '
                                                                              'not '
                                                                              'this '
                                                                              'parameter '
                                                                              'is '
                                                                              'required '
                                                                              'or '
                                                                              'optional.',
                                                               'type': 'boolean'},
                                                  'schema': {'$ref': '#/definitions/schema'}},
                                   'required': ['name', 'in', 'schema'],
                                   'type': 'object'},
                 'collectionFormat': {'default': 'csv',
                                      'enum': ['csv', 'ssv', 'tsv', 'pipes'],
                                      'type': 'string'},
                 'collectionFormatWithMulti': {'default': 'csv',
                                               'enum': ['csv',
                                                        'ssv',
                                                        'tsv',
                                                        'pipes',
                                                        'multi'],
                                               'type': 'string'},
                 'contact': {'additionalProperties': False,
                             'description': 'Contact information for the '
                                            'owners of the API.',
                             'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                             'properties': {'email': {'description': 'The '
                                                                     'email '
                                                                     'address '
                                                                     'of the '
                                                                     'contact '
                                                                     'person/organization.',
                                                      'format': 'email',
                                                      'type': 'string'},
                                            'name': {'description': 'The '
                                                                    'identifying '
                                                                    'name of '
                                                                    'the '
                                                                    'contact '
                                                                    'person/organization.',
                                                     'type': 'string'},
                                            'url': {'description': 'The URL '
                                                                   'pointing '
                                                                   'to the '
                                                                   'contact '
                                                                   'information.',
                                                    'format': 'uri',
                                                    'type': 'string'}},
                             'type': 'object'},
                 'default': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/default'},
                 'definitions': {'additionalProperties': {'$ref': '#/definitions/schema'},
                                 'description': 'One or more JSON objects '
                                                'describing the schemas being '
                                                'consumed and produced by the '
                                                'API.',
                                 'type': 'object'},
                 'description': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/description'},
                 'enum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/enum'},
                 'examples': {'additionalProperties': True, 'type': 'object'},
                 'exclusiveMaximum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/exclusiveMaximum'},
                 'exclusiveMinimum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/exclusiveMinimum'},
                 'externalDocs': {'additionalProperties': False,
                                  'description': 'information about external '
                                                 'documentation',
                                  'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                  'properties': {'description': {'type': 'string'},
                                                 'url': {'format': 'uri',
                                                         'type': 'string'}},
                                  'required': ['url'],
                                  'type': 'object'},
                 'fileSchema': {'additionalProperties': False,
                                'description': 'A deterministic version of a '
                                               'JSON Schema object.',
                                'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                'properties': {'default': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/default'},
                                               'description': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/description'},
                                               'example': {},
                                               'externalDocs': {'$ref': '#/definitions/externalDocs'},
                                               'format': {'type': 'string'},
                                               'readOnly': {'default': False,
                                                            'type': 'boolean'},
                                               'required': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/stringArray'},
                                               'title': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/title'},
                                               'type': {'enum': ['file'],
                                                        'type': 'string'}},
                                'required': ['type'],
                                'type': 'object'},
                 'formDataParameterSubSchema': {'additionalProperties': False,
                                                'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                                'properties': {'allowEmptyValue': {'default': False,
                                                                                   'description': 'allows '
                                                                                                  'sending '
                                                                                                  'a '
                                                                                                  'parameter '
                                                                                                  'by '
                                                                                                  'name '
                                                                                                  'only '
                                                                                                  'or '
                                                                                                  'with '
                                                                                                  'an '
                                                                                                  'empty '
                                                                                                  'value.',
                                                                                   'type': 'boolean'},
                                                               'collectionFormat': {'$ref': '#/definitions/collectionFormatWithMulti'},
                                                               'default': {'$ref': '#/definitions/default'},
                                                               'description': {'description': 'A '
                                                                                              'brief '
                                                                                              'description '
                                                                                              'of '
                                                                                              'the '
                                                                                              'parameter. '
                                                                                              'This '
                                                                                              'could '
                                                                                              'contain '
                                                                                              'examples '
                                                                                              'of '
                                                                                              'use.  '
                                                                                              'GitHub '
                                                                                              'Flavored '
                                                                                              'Markdown '
                                                                                              'is '
                                                                                              'allowed.',
                                                                               'type': 'string'},
                                                               'enum': {'$ref': '#/definitions/enum'},
                                                               'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                                               'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                                               'format': {'type': 'string'},
                                                               'in': {'description': 'Determines '
                                                                                     'the '
                                                                                     'location '
                                                                                     'of '
                                                                                     'the '
                                                                                     'parameter.',
                                                                      'enum': ['formData'],
                                                                      'type': 'string'},
                                                               'items': {'$ref': '#/definitions/primitivesItems'},
                                                               'maxItems': {'$ref': '#/definitions/maxItems'},
                                                               'maxLength': {'$ref': '#/definitions/maxLength'},
                                                               'maximum': {'$ref': '#/definitions/maximum'},
                                                               'minItems': {'$ref': '#/definitions/minItems'},
                                                               'minLength': {'$ref': '#/definitions/minLength'},
                                                               'minimum': {'$ref': '#/definitions/minimum'},
                                                               'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                                               'name': {'description': 'The '
                                                                                       'name '
                                                                                       'of '
                                                                                       'the '
                                                                                       'parameter.',
                                                                        'type': 'string'},
                                                               'pattern': {'$ref': '#/definitions/pattern'},
                                                               'required': {'default': False,
                                                                            'description': 'Determines '
                                                                                           'whether '
                                                                                           'or '
                                                                                           'not '
                                                                                           'this '
                                                                                           'parameter '
                                                                                           'is '
                                                                                           'required '
                                                                                           'or '
                                                                                           'optional.',
                                                                            'type': 'boolean'},
                                                               'type': {'enum': ['string',
                                                                                 'number',
                                                                                 'boolean',
                                                                                 'integer',
                                                                                 'array',
                                                                                 'file'],
                                                                        'type': 'string'},
                                                               'uniqueItems': {'$ref': '#/definitions/uniqueItems'}}},
                 'header': {'additionalProperties': False,
                            'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                            'properties': {'collectionFormat': {'$ref': '#/definitions/collectionFormat'},
                                           'default': {'$ref': '#/definitions/default'},
                                           'description': {'type': 'string'},
                                           'enum': {'$ref': '#/definitions/enum'},
                                           'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                           'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                           'format': {'type': 'string'},
                                           'items': {'$ref': '#/definitions/primitivesItems'},
                                           'maxItems': {'$ref': '#/definitions/maxItems'},
                                           'maxLength': {'$ref': '#/definitions/maxLength'},
                                           'maximum': {'$ref': '#/definitions/maximum'},
                                           'minItems': {'$ref': '#/definitions/minItems'},
                                           'minLength': {'$ref': '#/definitions/minLength'},
                                           'minimum': {'$ref': '#/definitions/minimum'},
                                           'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                           'pattern': {'$ref': '#/definitions/pattern'},
                                           'type': {'enum': ['string',
                                                             'number',
                                                             'integer',
                                                             'boolean',
                                                             'array'],
                                                    'type': 'string'},
                                           'uniqueItems': {'$ref': '#/definitions/uniqueItems'}},
                            'required': ['type'],
                            'type': 'object'},
                 'headerParameterSubSchema': {'additionalProperties': False,
                                              'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                              'properties': {'collectionFormat': {'$ref': '#/definitions/collectionFormat'},
                                                             'default': {'$ref': '#/definitions/default'},
                                                             'description': {'description': 'A '
                                                                                            'brief '
                                                                                            'description '
                                                                                            'of '
                                                                                            'the '
                                                                                            'parameter. '
                                                                                            'This '
                                                                                            'could '
                                                                                            'contain '
                                                                                            'examples '
                                                                                            'of '
                                                                                            'use.  '
                                                                                            'GitHub '
                                                                                            'Flavored '
                                                                                            'Markdown '
                                                                                            'is '
                                                                                            'allowed.',
                                                                             'type': 'string'},
                                                             'enum': {'$ref': '#/definitions/enum'},
                                                             'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                                             'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                                             'format': {'type': 'string'},
                                                             'in': {'description': 'Determines '
                                                                                   'the '
                                                                                   'location '
                                                                                   'of '
                                                                                   'the '
                                                                                   'parameter.',
                                                                    'enum': ['header'],
                                                                    'type': 'string'},
                                                             'items': {'$ref': '#/definitions/primitivesItems'},
                                                             'maxItems': {'$ref': '#/definitions/maxItems'},
                                                             'maxLength': {'$ref': '#/definitions/maxLength'},
                                                             'maximum': {'$ref': '#/definitions/maximum'},
                                                             'minItems': {'$ref': '#/definitions/minItems'},
                                                             'minLength': {'$ref': '#/definitions/minLength'},
                                                             'minimum': {'$ref': '#/definitions/minimum'},
                                                             'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                                             'name': {'description': 'The '
                                                                                     'name '
                                                                                     'of '
                                                                                     'the '
                                                                                     'parameter.',
                                                                      'type': 'string'},
                                                             'pattern': {'$ref': '#/definitions/pattern'},
                                                             'required': {'default': False,
                                                                          'description': 'Determines '
                                                                                         'whether '
                                                                                         'or '
                                                                                         'not '
                                                                                         'this '
                                                                                         'parameter '
                                                                                         'is '
                                                                                         'required '
                                                                                         'or '
                                                                                         'optional.',
                                                                          'type': 'boolean'},
                                                             'type': {'enum': ['string',
                                                                               'number',
                                                                               'boolean',
                                                                               'integer',
                                                                               'array'],
                                                                      'type': 'string'},
                                                             'uniqueItems': {'$ref': '#/definitions/uniqueItems'}}},
                 'headers': {'additionalProperties': {'$ref': '#/definitions/header'},
                             'type': 'object'},
                 'info': {'additionalProperties': False,
                          'description': 'General information about the API.',
                          'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                          'properties': {'contact': {'$ref': '#/definitions/contact'},
                                         'description': {'description': 'A '
                                                                        'longer '
                                                                        'description '
                                                                        'of '
                                                                        'the '
                                                                        'API. '
                                                                        'Should '
                                                                        'be '
                                                                        'different '
                                                                        'from '
                                                                        'the '
                                                                        'title.  '
                                                                        'GitHub '
                                                                        'Flavored '
                                                                        'Markdown '
                                                                        'is '
                                                                        'allowed.',
                                                         'type': 'string'},
                                         'license': {'$ref': '#/definitions/license'},
                                         'termsOfService': {'description': 'The '
                                                                           'terms '
                                                                           'of '
                                                                           'service '
                                                                           'for '
                                                                           'the '
                                                                           'API.',
                                                            'type': 'string'},
                                         'title': {'description': 'A unique '
                                                                  'and precise '
                                                                  'title of '
                                                                  'the API.',
                                                   'type': 'string'},
                                         'version': {'description': 'A '
                                                                    'semantic '
                                                                    'version '
                                                                    'number of '
                                                                    'the API.',
                                                     'type': 'string'}},
                          'required': ['version', 'title'],
                          'type': 'object'},
                 'jsonReference': {'additionalProperties': False,
                                   'properties': {'$ref': {'type': 'string'}},
                                   'required': ['$ref'],
                                   'type': 'object'},
                 'license': {'additionalProperties': False,
                             'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                             'properties': {'name': {'description': 'The name '
                                                                    'of the '
                                                                    'license '
                                                                    'type. '
                                                                    "It's "
                                                                    'encouraged '
                                                                    'to use an '
                                                                    'OSI '
                                                                    'compatible '
                                                                    'license.',
                                                     'type': 'string'},
                                            'url': {'description': 'The URL '
                                                                   'pointing '
                                                                   'to the '
                                                                   'license.',
                                                    'format': 'uri',
                                                    'type': 'string'}},
                             'required': ['name'],
                             'type': 'object'},
                 'maxItems': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveInteger'},
                 'maxLength': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveInteger'},
                 'maximum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/maximum'},
                 'mediaTypeList': {'items': {'$ref': '#/definitions/mimeType'},
                                   'type': 'array',
                                   'uniqueItems': True},
                 'mimeType': {'description': 'The MIME type of the HTTP '
                                             'message.',
                              'type': 'string'},
                 'minItems': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveIntegerDefault0'},
                 'minLength': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveIntegerDefault0'},
                 'minimum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/minimum'},
                 'multipleOf': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/multipleOf'},
                 'nonBodyParameter': {'oneOf': [{'$ref': '#/definitions/headerParameterSubSchema'},
                                                {'$ref': '#/definitions/formDataParameterSubSchema'},
                                                {'$ref': '#/definitions/queryParameterSubSchema'},
                                                {'$ref': '#/definitions/pathParameterSubSchema'}],
                                      'required': ['name', 'in', 'type'],
                                      'type': 'object'},
                 'oauth2AccessCodeSecurity': {'additionalProperties': False,
                                              'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                              'properties': {'authorizationUrl': {'format': 'uri',
                                                                                  'type': 'string'},
                                                             'description': {'type': 'string'},
                                                             'flow': {'enum': ['accessCode'],
                                                                      'type': 'string'},
                                                             'scopes': {'$ref': '#/definitions/oauth2Scopes'},
                                                             'tokenUrl': {'format': 'uri',
                                                                          'type': 'string'},
                                                             'type': {'enum': ['oauth2'],
                                                                      'type': 'string'}},
                                              'required': ['type',
                                                           'flow',
                                                           'authorizationUrl',
                                                           'tokenUrl'],
                                              'type': 'object'},
                 'oauth2ApplicationSecurity': {'additionalProperties': False,
                                               'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                               'properties': {'description': {'type': 'string'},
                                                              'flow': {'enum': ['application'],
                                                                       'type': 'string'},
                                                              'scopes': {'$ref': '#/definitions/oauth2Scopes'},
                                                              'tokenUrl': {'format': 'uri',
                                                                           'type': 'string'},
                                                              'type': {'enum': ['oauth2'],
                                                                       'type': 'string'}},
                                               'required': ['type',
                                                            'flow',
                                                            'tokenUrl'],
                                               'type': 'object'},
                 'oauth2ImplicitSecurity': {'additionalProperties': False,
                                            'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                            'properties': {'authorizationUrl': {'format': 'uri',
                                                                                'type': 'string'},
                                                           'description': {'type': 'string'},
                                                           'flow': {'enum': ['implicit'],
                                                                    'type': 'string'},
                                                           'scopes': {'$ref': '#/definitions/oauth2Scopes'},
                                                           'type': {'enum': ['oauth2'],
                                                                    'type': 'string'}},
                                            'required': ['type',
                                                         'flow',
                                                         'authorizationUrl'],
                                            'type': 'object'},
                 'oauth2PasswordSecurity': {'additionalProperties': False,
                                            'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                            'properties': {'description': {'type': 'string'},
                                                           'flow': {'enum': ['password'],
                                                                    'type': 'string'},
                                                           'scopes': {'$ref': '#/definitions/oauth2Scopes'},
                                                           'tokenUrl': {'format': 'uri',
                                                                        'type': 'string'},
                                                           'type': {'enum': ['oauth2'],
                                                                    'type': 'string'}},
                                            'required': ['type',
                                                         'flow',
                                                         'tokenUrl'],
                                            'type': 'object'},
                 'oauth2Scopes': {'additionalProperties': {'type': 'string'},
                                  'type': 'object'},
                 'operation': {'additionalProperties': False,
                               'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                               'properties': {'consumes': {'allOf': [{'$ref': '#/definitions/mediaTypeList'}],
                                                           'description': 'A '
                                                                          'list '
                                                                          'of '
                                                                          'MIME '
                                                                          'types '
                                                                          'the '
                                                                          'API '
                                                                          'can '
                                                                          'consume.'},
                                              'deprecated': {'default': False,
                                                             'type': 'boolean'},
                                              'description': {'description': 'A '
                                                                             'longer '
                                                                             'description '
                                                                             'of '
                                                                             'the '
                                                                             'operation, '
                                                                             'GitHub '
                                                                             'Flavored '
                                                                             'Markdown '
                                                                             'is '
                                                                             'allowed.',
                                                              'type': 'string'},
                                              'externalDocs': {'$ref': '#/definitions/externalDocs'},
                                              'operationId': {'description': 'A '
                                                                             'unique '
                                                                             'identifier '
                                                                             'of '
                                                                             'the '
                                                                             'operation.',
                                                              'type': 'string'},
                                              'parameters': {'$ref': '#/definitions/parametersList'},
                                              'produces': {'allOf': [{'$ref': '#/definitions/mediaTypeList'}],
                                                           'description': 'A '
                                                                          'list '
                                                                          'of '
                                                                          'MIME '
                                                                          'types '
                                                                          'the '
                                                                          'API '
                                                                          'can '
                                                                          'produce.'},
                                              'responses': {'$ref': '#/definitions/responses'},
                                              'schemes': {'$ref': '#/definitions/schemesList'},
                                              'security': {'$ref': '#/definitions/security'},
                                              'summary': {'description': 'A '
                                                                         'brief '
                                                                         'summary '
                                                                         'of '
                                                                         'the '
                                                                         'operation.',
                                                          'type': 'string'},
                                              'tags': {'items': {'type': 'string'},
                                                       'type': 'array',
                                                       'uniqueItems': True}},
                               'required': ['responses'],
                               'type': 'object'},
                 'parameter': {'oneOf': [{'$ref': '#/definitions/bodyParameter'},
                                         {'$ref': '#/definitions/nonBodyParameter'}]},
                 'parameterDefinitions': {'additionalProperties': {'$ref': '#/definitions/parameter'},
                                          'description': 'One or more JSON '
                                                         'representations for '
                                                         'parameters',
                                          'type': 'object'},
                 'parametersList': {'additionalItems': False,
                                    'description': 'The parameters needed to '
                                                   'send a valid API call.',
                                    'items': {'oneOf': [{'$ref': '#/definitions/parameter'},
                                                        {'$ref': '#/definitions/jsonReference'}]},
                                    'type': 'array',
                                    'uniqueItems': True},
                 'pathItem': {'additionalProperties': False,
                              'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                              'properties': {'$ref': {'type': 'string'},
                                             'delete': {'$ref': '#/definitions/operation'},
                                             'get': {'$ref': '#/definitions/operation'},
                                             'head': {'$ref': '#/definitions/operation'},
                                             'options': {'$ref': '#/definitions/operation'},
                                             'parameters': {'$ref': '#/definitions/parametersList'},
                                             'patch': {'$ref': '#/definitions/operation'},
                                             'post': {'$ref': '#/definitions/operation'},
                                             'put': {'$ref': '#/definitions/operation'}},
                              'type': 'object'},
                 'pathParameterSubSchema': {'additionalProperties': False,
                                            'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                            'properties': {'collectionFormat': {'$ref': '#/definitions/collectionFormat'},
                                                           'default': {'$ref': '#/definitions/default'},
                                                           'description': {'description': 'A '
                                                                                          'brief '
                                                                                          'description '
                                                                                          'of '
                                                                                          'the '
                                                                                          'parameter. '
                                                                                          'This '
                                                                                          'could '
                                                                                          'contain '
                                                                                          'examples '
                                                                                          'of '
                                                                                          'use.  '
                                                                                          'GitHub '
                                                                                          'Flavored '
                                                                                          'Markdown '
                                                                                          'is '
                                                                                          'allowed.',
                                                                           'type': 'string'},
                                                           'enum': {'$ref': '#/definitions/enum'},
                                                           'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                                           'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                                           'format': {'type': 'string'},
                                                           'in': {'description': 'Determines '
                                                                                 'the '
                                                                                 'location '
                                                                                 'of '
                                                                                 'the '
                                                                                 'parameter.',
                                                                  'enum': ['path'],
                                                                  'type': 'string'},
                                                           'items': {'$ref': '#/definitions/primitivesItems'},
                                                           'maxItems': {'$ref': '#/definitions/maxItems'},
                                                           'maxLength': {'$ref': '#/definitions/maxLength'},
                                                           'maximum': {'$ref': '#/definitions/maximum'},
                                                           'minItems': {'$ref': '#/definitions/minItems'},
                                                           'minLength': {'$ref': '#/definitions/minLength'},
                                                           'minimum': {'$ref': '#/definitions/minimum'},
                                                           'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                                           'name': {'description': 'The '
                                                                                   'name '
                                                                                   'of '
                                                                                   'the '
                                                                                   'parameter.',
                                                                    'type': 'string'},
                                                           'pattern': {'$ref': '#/definitions/pattern'},
                                                           'required': {'description': 'Determines '
                                                                                       'whether '
                                                                                       'or '
                                                                                       'not '
                                                                                       'this '
                                                                                       'parameter '
                                                                                       'is '
                                                                                       'required '
                                                                                       'or '
                                                                                       'optional.',
                                                                        'enum': [True],
                                                                        'type': 'boolean'},
                                                           'type': {'enum': ['string',
                                                                             'number',
                                                                             'boolean',
                                                                             'integer',
                                                                             'array'],
                                                                    'type': 'string'},
                                                           'uniqueItems': {'$ref': '#/definitions/uniqueItems'}},
                                            'required': ['required']},
                 'paths': {'additionalProperties': False,
                           'description': 'Relative paths to the individual '
                                          'endpoints. They must be relative to '
                                          "the 'basePath'.",
                           'patternProperties': {'^/': {'$ref': '#/definitions/pathItem'},
                                                 '^x-': {'$ref': '#/definitions/vendorExtension'}},
                           'type': 'object'},
                 'pattern': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/pattern'},
                 'primitivesItems': {'additionalProperties': False,
                                     'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                     'properties': {'collectionFormat': {'$ref': '#/definitions/collectionFormat'},
                                                    'default': {'$ref': '#/definitions/default'},
                                                    'enum': {'$ref': '#/definitions/enum'},
                                                    'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                                    'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                                    'format': {'type': 'string'},
                                                    'items': {'$ref': '#/definitions/primitivesItems'},
                                                    'maxItems': {'$ref': '#/definitions/maxItems'},
                                                    'maxLength': {'$ref': '#/definitions/maxLength'},
                                                    'maximum': {'$ref': '#/definitions/maximum'},
                                                    'minItems': {'$ref': '#/definitions/minItems'},
                                                    'minLength': {'$ref': '#/definitions/minLength'},
                                                    'minimum': {'$ref': '#/definitions/minimum'},
                                                    'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                                    'pattern': {'$ref': '#/definitions/pattern'},
                                                    'type': {'enum': ['string',
                                                                      'number',
                                                                      'integer',
                                                                      'boolean',
                                                                      'array'],
                                                             'type': 'string'},
                                                    'uniqueItems': {'$ref': '#/definitions/uniqueItems'}},
                                     'type': 'object'},
                 'queryParameterSubSchema': {'additionalProperties': False,
                                             'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                             'properties': {'allowEmptyValue': {'default': False,
                                                                                'description': 'allows '
                                                                                               'sending '
                                                                                               'a '
                                                                                               'parameter '
                                                                                               'by '
                                                                                               'name '
                                                                                               'only '
                                                                                               'or '
                                                                                               'with '
                                                                                               'an '
                                                                                               'empty '
                                                                                               'value.',
                                                                                'type': 'boolean'},
                                                            'collectionFormat': {'$ref': '#/definitions/collectionFormatWithMulti'},
                                                            'default': {'$ref': '#/definitions/default'},
                                                            'description': {'description': 'A '
                                                                                           'brief '
                                                                                           'description '
                                                                                           'of '
                                                                                           'the '
                                                                                           'parameter. '
                                                                                           'This '
                                                                                           'could '
                                                                                           'contain '
                                                                                           'examples '
                                                                                           'of '
                                                                                           'use.  '
                                                                                           'GitHub '
                                                                                           'Flavored '
                                                                                           'Markdown '
                                                                                           'is '
                                                                                           'allowed.',
                                                                            'type': 'string'},
                                                            'enum': {'$ref': '#/definitions/enum'},
                                                            'exclusiveMaximum': {'$ref': '#/definitions/exclusiveMaximum'},
                                                            'exclusiveMinimum': {'$ref': '#/definitions/exclusiveMinimum'},
                                                            'format': {'type': 'string'},
                                                            'in': {'description': 'Determines '
                                                                                  'the '
                                                                                  'location '
                                                                                  'of '
                                                                                  'the '
                                                                                  'parameter.',
                                                                   'enum': ['query'],
                                                                   'type': 'string'},
                                                            'items': {'$ref': '#/definitions/primitivesItems'},
                                                            'maxItems': {'$ref': '#/definitions/maxItems'},
                                                            'maxLength': {'$ref': '#/definitions/maxLength'},
                                                            'maximum': {'$ref': '#/definitions/maximum'},
                                                            'minItems': {'$ref': '#/definitions/minItems'},
                                                            'minLength': {'$ref': '#/definitions/minLength'},
                                                            'minimum': {'$ref': '#/definitions/minimum'},
                                                            'multipleOf': {'$ref': '#/definitions/multipleOf'},
                                                            'name': {'description': 'The '
                                                                                    'name '
                                                                                    'of '
                                                                                    'the '
                                                                                    'parameter.',
                                                                     'type': 'string'},
                                                            'pattern': {'$ref': '#/definitions/pattern'},
                                                            'required': {'default': False,
                                                                         'description': 'Determines '
                                                                                        'whether '
                                                                                        'or '
                                                                                        'not '
                                                                                        'this '
                                                                                        'parameter '
                                                                                        'is '
                                                                                        'required '
                                                                                        'or '
                                                                                        'optional.',
                                                                         'type': 'boolean'},
                                                            'type': {'enum': ['string',
                                                                              'number',
                                                                              'boolean',
                                                                              'integer',
                                                                              'array'],
                                                                     'type': 'string'},
                                                            'uniqueItems': {'$ref': '#/definitions/uniqueItems'}}},
                 'response': {'additionalProperties': False,
                              'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                              'properties': {'description': {'type': 'string'},
                                             'examples': {'$ref': '#/definitions/examples'},
                                             'headers': {'$ref': '#/definitions/headers'},
                                             'schema': {'oneOf': [{'$ref': '#/definitions/schema'},
                                                                  {'$ref': '#/definitions/fileSchema'}]}},
                              'required': ['description'],
                              'type': 'object'},
                 'responseDefinitions': {'additionalProperties': {'$ref': '#/definitions/response'},
                                         'description': 'One or more JSON '
                                                        'representations for '
                                                        'responses',
                                         'type': 'object'},
                 'responseValue': {'oneOf': [{'$ref': '#/definitions/response'},
                                             {'$ref': '#/definitions/jsonReference'}]},
                 'responses': {'additionalProperties': False,
                               'description': 'Response objects names can '
                                              'either be any valid HTTP status '
                                              "code or 'default'.",
                               'minProperties': 1,
                               'not': {'additionalProperties': False,
                                       'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                                       'type': 'object'},
                               'patternProperties': {'^([0-9]{3})$|^(default)$': {'$ref': '#/definitions/responseValue'},
                                                     '^x-': {'$ref': '#/definitions/vendorExtension'}},
                               'type': 'object'},
                 'schema': {'additionalProperties': False,
                            'description': 'A deterministic version of a JSON '
                                           'Schema object.',
                            'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                            'properties': {'$ref': {'type': 'string'},
                                           'additionalProperties': {'anyOf': [{'$ref': '#/definitions/schema'},
                                                                              {'type': 'boolean'}],
                                                                    'default': {}},
                                           'allOf': {'items': {'$ref': '#/definitions/schema'},
                                                     'minItems': 1,
                                                     'type': 'array'},
                                           'default': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/default'},
                                           'description': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/description'},
                                           'discriminator': {'type': 'string'},
                                           'enum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/enum'},
                                           'example': {},
                                           'exclusiveMaximum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/exclusiveMaximum'},
                                           'exclusiveMinimum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/exclusiveMinimum'},
                                           'externalDocs': {'$ref': '#/definitions/externalDocs'},
                                           'format': {'type': 'string'},
                                           'items': {'anyOf': [{'$ref': '#/definitions/schema'},
                                                               {'items': {'$ref': '#/definitions/schema'},
                                                                'minItems': 1,
                                                                'type': 'array'}],
                                                     'default': {}},
                                           'maxItems': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveInteger'},
                                           'maxLength': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveInteger'},
                                           'maxProperties': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveInteger'},
                                           'maximum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/maximum'},
                                           'minItems': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveIntegerDefault0'},
                                           'minLength': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveIntegerDefault0'},
                                           'minProperties': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/positiveIntegerDefault0'},
                                           'minimum': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/minimum'},
                                           'multipleOf': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/multipleOf'},
                                           'pattern': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/pattern'},
                                           'properties': {'additionalProperties': {'$ref': '#/definitions/schema'},
                                                          'default': {},
                                                          'type': 'object'},
                                           'readOnly': {'default': False,
                                                        'type': 'boolean'},
                                           'required': {'$ref': 'http://json-schema.org/draft-04/schema#/definitions/stringArray'},
                                           'title': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/title'},
                                           'type': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/type'},
                                           'uniqueItems': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/uniqueItems'},
                                           'xml': {'$ref': '#/definitions/xml'}},
                            'type': 'object'},
                 'schemesList': {'description': 'The transfer protocol of the '
                                                'API.',
                                 'items': {'enum': ['http',
                                                    'https',
                                                    'ws',
                                                    'wss'],
                                           'type': 'string'},
                                 'type': 'array',
                                 'uniqueItems': True},
                 'security': {'items': {'$ref': '#/definitions/securityRequirement'},
                              'type': 'array',
                              'uniqueItems': True},
                 'securityDefinitions': {'additionalProperties': {'oneOf': [{'$ref': '#/definitions/basicAuthenticationSecurity'},
                                                                            {'$ref': '#/definitions/apiKeySecurity'},
                                                                            {'$ref': '#/definitions/oauth2ImplicitSecurity'},
                                                                            {'$ref': '#/definitions/oauth2PasswordSecurity'},
                                                                            {'$ref': '#/definitions/oauth2ApplicationSecurity'},
                                                                            {'$ref': '#/definitions/oauth2AccessCodeSecurity'}]},
                                         'type': 'object'},
                 'securityRequirement': {'additionalProperties': {'items': {'type': 'string'},
                                                                  'type': 'array',
                                                                  'uniqueItems': True},
                                         'type': 'object'},
                 'tag': {'additionalProperties': False,
                         'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                         'properties': {'description': {'type': 'string'},
                                        'externalDocs': {'$ref': '#/definitions/externalDocs'},
                                        'name': {'type': 'string'}},
                         'required': ['name'],
                         'type': 'object'},
                 'title': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/title'},
                 'uniqueItems': {'$ref': 'http://json-schema.org/draft-04/schema#/properties/uniqueItems'},
                 'vendorExtension': {'additionalItems': True,
                                     'additionalProperties': True,
                                     'description': 'Any property starting '
                                                    'with x- is valid.'},
                 'xml': {'additionalProperties': False,
                         'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
                         'properties': {'attribute': {'default': False,
                                                      'type': 'boolean'},
                                        'name': {'type': 'string'},
                                        'namespace': {'type': 'string'},
                                        'prefix': {'type': 'string'},
                                        'wrapped': {'default': False,
                                                    'type': 'boolean'}},
                         'type': 'object'}},
 'id': 'http://swagger.io/v2/schema.json#',
 'patternProperties': {'^x-': {'$ref': '#/definitions/vendorExtension'}},
 'properties': {'basePath': {'description': 'The base path to the API. '
                                            "Example: '/api'.",
                             'pattern': '^/',
                             'type': 'string'},
                'consumes': {'allOf': [{'$ref': '#/definitions/mediaTypeList'}],
                             'description': 'A list of MIME types accepted by '
                                            'the API.'},
                'definitions': {'$ref': '#/definitions/definitions'},
                'externalDocs': {'$ref': '#/definitions/externalDocs'},
                'host': {'description': 'The host (name or ip) of the API. '
                                        "Example: 'swagger.io'",
                         'pattern': '^[^{}/ :\\\\]+(?::\\d+)?$',
                         'type': 'string'},
                'info': {'$ref': '#/definitions/info'},
                'parameters': {'$ref': '#/definitions/parameterDefinitions'},
                'paths': {'$ref': '#/definitions/paths'},
                'produces': {'allOf': [{'$ref': '#/definitions/mediaTypeList'}],
                             'description': 'A list of MIME types the API can '
                                            'produce.'},
                'responses': {'$ref': '#/definitions/responseDefinitions'},
                'schemes': {'$ref': '#/definitions/schemesList'},
                'security': {'$ref': '#/definitions/security'},
                'securityDefinitions': {'$ref': '#/definitions/securityDefinitions'},
                'swagger': {'description': 'The Swagger version of this '
                                           'document.',
                            'enum': ['2.0'],
                            'type': 'string'},
                'tags': {'items': {'$ref': '#/definitions/tag'},
                         'type': 'array',
                         'uniqueItems': True}},
 'required': ['swagger', 'info', 'paths'],
 'title': 'A JSON Schema for Swagger 2.0 API.',
 'type': 'object'}
