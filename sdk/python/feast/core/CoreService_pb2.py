# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/CoreService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.specs import EntitySpec_pb2 as feast_dot_specs_dot_EntitySpec__pb2
from feast.specs import FeatureSpec_pb2 as feast_dot_specs_dot_FeatureSpec__pb2
from feast.specs import FeatureGroupSpec_pb2 as feast_dot_specs_dot_FeatureGroupSpec__pb2
from feast.specs import StorageSpec_pb2 as feast_dot_specs_dot_StorageSpec__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/CoreService.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=_b('\n\nfeast.coreB\020CoreServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/core'),
  serialized_pb=_b('\n\x1c\x66\x65\x61st/core/CoreService.proto\x12\nfeast.core\x1a\x1c\x66\x65\x61st/specs/EntitySpec.proto\x1a\x1d\x66\x65\x61st/specs/FeatureSpec.proto\x1a\"feast/specs/FeatureGroupSpec.proto\x1a\x1d\x66\x65\x61st/specs/StorageSpec.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xc9\x05\n\x10\x43oreServiceTypes\x1a!\n\x12GetEntitiesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a@\n\x13GetEntitiesResponse\x12)\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x17.feast.specs.EntitySpec\x1a\x41\n\x14ListEntitiesResponse\x12)\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x17.feast.specs.EntitySpec\x1a!\n\x12GetFeaturesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x41\n\x13GetFeaturesResponse\x12*\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x18.feast.specs.FeatureSpec\x1a\x42\n\x14ListFeaturesResponse\x12*\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x18.feast.specs.FeatureSpec\x1a \n\x11GetStorageRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x1a\x44\n\x12GetStorageResponse\x12.\n\x0cstorageSpecs\x18\x01 \x03(\x0b\x32\x18.feast.specs.StorageSpec\x1a\x45\n\x13ListStorageResponse\x12.\n\x0cstorageSpecs\x18\x01 \x03(\x0b\x32\x18.feast.specs.StorageSpec\x1a)\n\x13\x41pplyEntityResponse\x12\x12\n\nentityName\x18\x01 \x01(\t\x1a)\n\x14\x41pplyFeatureResponse\x12\x11\n\tfeatureId\x18\x01 \x01(\t\x1a\x33\n\x19\x41pplyFeatureGroupResponse\x12\x16\n\x0e\x66\x65\x61tureGroupId\x18\x01 \x01(\t\x1a)\n\x14\x41pplyStorageResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t2\x83\x08\n\x0b\x43oreService\x12r\n\x0bGetEntities\x12/.feast.core.CoreServiceTypes.GetEntitiesRequest\x1a\x30.feast.core.CoreServiceTypes.GetEntitiesResponse\"\x00\x12[\n\x0cListEntities\x12\x16.google.protobuf.Empty\x1a\x31.feast.core.CoreServiceTypes.ListEntitiesResponse\"\x00\x12r\n\x0bGetFeatures\x12/.feast.core.CoreServiceTypes.GetFeaturesRequest\x1a\x30.feast.core.CoreServiceTypes.GetFeaturesResponse\"\x00\x12[\n\x0cListFeatures\x12\x16.google.protobuf.Empty\x1a\x31.feast.core.CoreServiceTypes.ListFeaturesResponse\"\x00\x12o\n\nGetStorage\x12..feast.core.CoreServiceTypes.GetStorageRequest\x1a/.feast.core.CoreServiceTypes.GetStorageResponse\"\x00\x12Y\n\x0bListStorage\x12\x16.google.protobuf.Empty\x1a\x30.feast.core.CoreServiceTypes.ListStorageResponse\"\x00\x12]\n\x0c\x41pplyFeature\x12\x18.feast.specs.FeatureSpec\x1a\x31.feast.core.CoreServiceTypes.ApplyFeatureResponse\"\x00\x12l\n\x11\x41pplyFeatureGroup\x12\x1d.feast.specs.FeatureGroupSpec\x1a\x36.feast.core.CoreServiceTypes.ApplyFeatureGroupResponse\"\x00\x12Z\n\x0b\x41pplyEntity\x12\x17.feast.specs.EntitySpec\x1a\x30.feast.core.CoreServiceTypes.ApplyEntityResponse\"\x00\x12]\n\x0c\x41pplyStorage\x12\x18.feast.specs.StorageSpec\x1a\x31.feast.core.CoreServiceTypes.ApplyStorageResponse\"\x00\x42U\n\nfeast.coreB\x10\x43oreServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/coreb\x06proto3')
  ,
  dependencies=[feast_dot_specs_dot_EntitySpec__pb2.DESCRIPTOR,feast_dot_specs_dot_FeatureSpec__pb2.DESCRIPTOR,feast_dot_specs_dot_FeatureGroupSpec__pb2.DESCRIPTOR,feast_dot_specs_dot_StorageSpec__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CORESERVICETYPES_GETENTITIESREQUEST = _descriptor.Descriptor(
  name='GetEntitiesRequest',
  full_name='feast.core.CoreServiceTypes.GetEntitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetEntitiesRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=255,
)

_CORESERVICETYPES_GETENTITIESRESPONSE = _descriptor.Descriptor(
  name='GetEntitiesResponse',
  full_name='feast.core.CoreServiceTypes.GetEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.CoreServiceTypes.GetEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=321,
)

_CORESERVICETYPES_LISTENTITIESRESPONSE = _descriptor.Descriptor(
  name='ListEntitiesResponse',
  full_name='feast.core.CoreServiceTypes.ListEntitiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.CoreServiceTypes.ListEntitiesResponse.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=388,
)

_CORESERVICETYPES_GETFEATURESREQUEST = _descriptor.Descriptor(
  name='GetFeaturesRequest',
  full_name='feast.core.CoreServiceTypes.GetFeaturesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetFeaturesRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=423,
)

_CORESERVICETYPES_GETFEATURESRESPONSE = _descriptor.Descriptor(
  name='GetFeaturesResponse',
  full_name='feast.core.CoreServiceTypes.GetFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.CoreServiceTypes.GetFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=490,
)

_CORESERVICETYPES_LISTFEATURESRESPONSE = _descriptor.Descriptor(
  name='ListFeaturesResponse',
  full_name='feast.core.CoreServiceTypes.ListFeaturesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.CoreServiceTypes.ListFeaturesResponse.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=558,
)

_CORESERVICETYPES_GETSTORAGEREQUEST = _descriptor.Descriptor(
  name='GetStorageRequest',
  full_name='feast.core.CoreServiceTypes.GetStorageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='feast.core.CoreServiceTypes.GetStorageRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=592,
)

_CORESERVICETYPES_GETSTORAGERESPONSE = _descriptor.Descriptor(
  name='GetStorageResponse',
  full_name='feast.core.CoreServiceTypes.GetStorageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storageSpecs', full_name='feast.core.CoreServiceTypes.GetStorageResponse.storageSpecs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=662,
)

_CORESERVICETYPES_LISTSTORAGERESPONSE = _descriptor.Descriptor(
  name='ListStorageResponse',
  full_name='feast.core.CoreServiceTypes.ListStorageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storageSpecs', full_name='feast.core.CoreServiceTypes.ListStorageResponse.storageSpecs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=664,
  serialized_end=733,
)

_CORESERVICETYPES_APPLYENTITYRESPONSE = _descriptor.Descriptor(
  name='ApplyEntityResponse',
  full_name='feast.core.CoreServiceTypes.ApplyEntityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityName', full_name='feast.core.CoreServiceTypes.ApplyEntityResponse.entityName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=776,
)

_CORESERVICETYPES_APPLYFEATURERESPONSE = _descriptor.Descriptor(
  name='ApplyFeatureResponse',
  full_name='feast.core.CoreServiceTypes.ApplyFeatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureId', full_name='feast.core.CoreServiceTypes.ApplyFeatureResponse.featureId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=819,
)

_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE = _descriptor.Descriptor(
  name='ApplyFeatureGroupResponse',
  full_name='feast.core.CoreServiceTypes.ApplyFeatureGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureGroupId', full_name='feast.core.CoreServiceTypes.ApplyFeatureGroupResponse.featureGroupId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=872,
)

_CORESERVICETYPES_APPLYSTORAGERESPONSE = _descriptor.Descriptor(
  name='ApplyStorageResponse',
  full_name='feast.core.CoreServiceTypes.ApplyStorageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storageId', full_name='feast.core.CoreServiceTypes.ApplyStorageResponse.storageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=874,
  serialized_end=915,
)

_CORESERVICETYPES = _descriptor.Descriptor(
  name='CoreServiceTypes',
  full_name='feast.core.CoreServiceTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_CORESERVICETYPES_GETENTITIESREQUEST, _CORESERVICETYPES_GETENTITIESRESPONSE, _CORESERVICETYPES_LISTENTITIESRESPONSE, _CORESERVICETYPES_GETFEATURESREQUEST, _CORESERVICETYPES_GETFEATURESRESPONSE, _CORESERVICETYPES_LISTFEATURESRESPONSE, _CORESERVICETYPES_GETSTORAGEREQUEST, _CORESERVICETYPES_GETSTORAGERESPONSE, _CORESERVICETYPES_LISTSTORAGERESPONSE, _CORESERVICETYPES_APPLYENTITYRESPONSE, _CORESERVICETYPES_APPLYFEATURERESPONSE, _CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE, _CORESERVICETYPES_APPLYSTORAGERESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=915,
)

_CORESERVICETYPES_GETENTITIESREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETENTITIESRESPONSE.fields_by_name['entities'].message_type = feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC
_CORESERVICETYPES_GETENTITIESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTENTITIESRESPONSE.fields_by_name['entities'].message_type = feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC
_CORESERVICETYPES_LISTENTITIESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETFEATURESREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETFEATURESRESPONSE.fields_by_name['features'].message_type = feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC
_CORESERVICETYPES_GETFEATURESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTFEATURESRESPONSE.fields_by_name['features'].message_type = feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC
_CORESERVICETYPES_LISTFEATURESRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETSTORAGEREQUEST.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_GETSTORAGERESPONSE.fields_by_name['storageSpecs'].message_type = feast_dot_specs_dot_StorageSpec__pb2._STORAGESPEC
_CORESERVICETYPES_GETSTORAGERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_LISTSTORAGERESPONSE.fields_by_name['storageSpecs'].message_type = feast_dot_specs_dot_StorageSpec__pb2._STORAGESPEC
_CORESERVICETYPES_LISTSTORAGERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYENTITYRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYFEATURERESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE.containing_type = _CORESERVICETYPES
_CORESERVICETYPES_APPLYSTORAGERESPONSE.containing_type = _CORESERVICETYPES
DESCRIPTOR.message_types_by_name['CoreServiceTypes'] = _CORESERVICETYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CoreServiceTypes = _reflection.GeneratedProtocolMessageType('CoreServiceTypes', (_message.Message,), dict(

  GetEntitiesRequest = _reflection.GeneratedProtocolMessageType('GetEntitiesRequest', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETENTITIESREQUEST,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetEntitiesRequest)
    ))
  ,

  GetEntitiesResponse = _reflection.GeneratedProtocolMessageType('GetEntitiesResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETENTITIESRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetEntitiesResponse)
    ))
  ,

  ListEntitiesResponse = _reflection.GeneratedProtocolMessageType('ListEntitiesResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_LISTENTITIESRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListEntitiesResponse)
    ))
  ,

  GetFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetFeaturesRequest', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETFEATURESREQUEST,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetFeaturesRequest)
    ))
  ,

  GetFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetFeaturesResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETFEATURESRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetFeaturesResponse)
    ))
  ,

  ListFeaturesResponse = _reflection.GeneratedProtocolMessageType('ListFeaturesResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_LISTFEATURESRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListFeaturesResponse)
    ))
  ,

  GetStorageRequest = _reflection.GeneratedProtocolMessageType('GetStorageRequest', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETSTORAGEREQUEST,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetStorageRequest)
    ))
  ,

  GetStorageResponse = _reflection.GeneratedProtocolMessageType('GetStorageResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_GETSTORAGERESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.GetStorageResponse)
    ))
  ,

  ListStorageResponse = _reflection.GeneratedProtocolMessageType('ListStorageResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_LISTSTORAGERESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ListStorageResponse)
    ))
  ,

  ApplyEntityResponse = _reflection.GeneratedProtocolMessageType('ApplyEntityResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYENTITYRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyEntityResponse)
    ))
  ,

  ApplyFeatureResponse = _reflection.GeneratedProtocolMessageType('ApplyFeatureResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYFEATURERESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeatureResponse)
    ))
  ,

  ApplyFeatureGroupResponse = _reflection.GeneratedProtocolMessageType('ApplyFeatureGroupResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyFeatureGroupResponse)
    ))
  ,

  ApplyStorageResponse = _reflection.GeneratedProtocolMessageType('ApplyStorageResponse', (_message.Message,), dict(
    DESCRIPTOR = _CORESERVICETYPES_APPLYSTORAGERESPONSE,
    __module__ = 'feast.core.CoreService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes.ApplyStorageResponse)
    ))
  ,
  DESCRIPTOR = _CORESERVICETYPES,
  __module__ = 'feast.core.CoreService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.CoreServiceTypes)
  ))
_sym_db.RegisterMessage(CoreServiceTypes)
_sym_db.RegisterMessage(CoreServiceTypes.GetEntitiesRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetEntitiesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListEntitiesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetFeaturesRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetFeaturesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListFeaturesResponse)
_sym_db.RegisterMessage(CoreServiceTypes.GetStorageRequest)
_sym_db.RegisterMessage(CoreServiceTypes.GetStorageResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ListStorageResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyEntityResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeatureResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyFeatureGroupResponse)
_sym_db.RegisterMessage(CoreServiceTypes.ApplyStorageResponse)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
  name='CoreService',
  full_name='feast.core.CoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=918,
  serialized_end=1945,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetEntities',
    full_name='feast.core.CoreService.GetEntities',
    index=0,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETENTITIESREQUEST,
    output_type=_CORESERVICETYPES_GETENTITIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListEntities',
    full_name='feast.core.CoreService.ListEntities',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTENTITIESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFeatures',
    full_name='feast.core.CoreService.GetFeatures',
    index=2,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETFEATURESREQUEST,
    output_type=_CORESERVICETYPES_GETFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListFeatures',
    full_name='feast.core.CoreService.ListFeatures',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTFEATURESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStorage',
    full_name='feast.core.CoreService.GetStorage',
    index=4,
    containing_service=None,
    input_type=_CORESERVICETYPES_GETSTORAGEREQUEST,
    output_type=_CORESERVICETYPES_GETSTORAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListStorage',
    full_name='feast.core.CoreService.ListStorage',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CORESERVICETYPES_LISTSTORAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeature',
    full_name='feast.core.CoreService.ApplyFeature',
    index=6,
    containing_service=None,
    input_type=feast_dot_specs_dot_FeatureSpec__pb2._FEATURESPEC,
    output_type=_CORESERVICETYPES_APPLYFEATURERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyFeatureGroup',
    full_name='feast.core.CoreService.ApplyFeatureGroup',
    index=7,
    containing_service=None,
    input_type=feast_dot_specs_dot_FeatureGroupSpec__pb2._FEATUREGROUPSPEC,
    output_type=_CORESERVICETYPES_APPLYFEATUREGROUPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyEntity',
    full_name='feast.core.CoreService.ApplyEntity',
    index=8,
    containing_service=None,
    input_type=feast_dot_specs_dot_EntitySpec__pb2._ENTITYSPEC,
    output_type=_CORESERVICETYPES_APPLYENTITYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyStorage',
    full_name='feast.core.CoreService.ApplyStorage',
    index=9,
    containing_service=None,
    input_type=feast_dot_specs_dot_StorageSpec__pb2._STORAGESPEC,
    output_type=_CORESERVICETYPES_APPLYSTORAGERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name['CoreService'] = _CORESERVICE

# @@protoc_insertion_point(module_scope)
