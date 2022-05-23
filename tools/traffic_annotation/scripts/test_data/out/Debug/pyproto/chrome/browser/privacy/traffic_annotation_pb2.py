# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traffic_annotation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import chrome_settings_full_runtime_pb2 as chrome__settings__full__runtime__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='traffic_annotation.proto',
  package='traffic_annotation',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18traffic_annotation.proto\x12\x12traffic_annotation\x1a\"chrome_settings_full_runtime.proto\"\xda\x07\n\x18NetworkTrafficAnnotation\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12J\n\x06source\x18\x02 \x01(\x0b\x32:.traffic_annotation.NetworkTrafficAnnotation.TrafficSource\x12P\n\tsemantics\x18\x03 \x01(\x0b\x32=.traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics\x12J\n\x06policy\x18\x04 \x01(\x0b\x32:.traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy\x12\x10\n\x08\x63omments\x18\x05 \x01(\t\x1a@\n\rTrafficSource\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x03 \x01(\x05\x12\x13\n\x0b\x63\x61ll_number\x18\x04 \x01(\x05\x1a\xaf\x02\n\x10TrafficSemantics\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07trigger\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12^\n\x0b\x64\x65stination\x18\x05 \x01(\x0e\x32I.traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.Destination\x12\x19\n\x11\x64\x65stination_other\x18\x06 \x01(\t\"\\\n\x0b\x44\x65stination\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07WEBSITE\x10\x01\x12\x18\n\x14GOOGLE_OWNED_SERVICE\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12\n\n\x05OTHER\x10\xe8\x07\x1a\xba\x02\n\rTrafficPolicy\x12\x62\n\x0f\x63ookies_allowed\x18\x01 \x01(\x0e\x32I.traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.CookiesAllowed\x12\x15\n\rcookies_store\x18\x02 \x01(\t\x12\x0f\n\x07setting\x18\x03 \x01(\t\x12\x41\n\rchrome_policy\x18\x04 \x03(\x0b\x32*.enterprise_management.ChromeSettingsProto\x12&\n\x1epolicy_exception_justification\x18\x05 \x01(\t\"2\n\x0e\x43ookiesAllowed\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x06\n\x02NO\x10\x01\x12\x07\n\x03YES\x10\x02\"u\n!ExtractedNetworkTrafficAnnotation\x12P\n\x1anetwork_traffic_annotation\x18\x01 \x03(\x0b\x32,.traffic_annotation.NetworkTrafficAnnotation\"x\n$WhitelistedNetworkTrafficAnnotations\x12P\n\x1anetwork_traffic_annotation\x18\x01 \x03(\x0b\x32,.traffic_annotation.NetworkTrafficAnnotation\"\xec\x01\n\x19NetworkTrafficAnnotations\x12\x64\n%extracted_network_traffic_annotations\x18\x01 \x01(\x0b\x32\x35.traffic_annotation.ExtractedNetworkTrafficAnnotation\x12i\n\'whitelisted_network_traffic_annotations\x18\x02 \x01(\x0b\x32\x38.traffic_annotation.WhitelistedNetworkTrafficAnnotationsb\x06proto3'
  ,
  dependencies=[chrome__settings__full__runtime__pb2.DESCRIPTOR,])



_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS_DESTINATION = _descriptor.EnumDescriptor(
  name='Destination',
  full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.Destination',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEBSITE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_OWNED_SERVICE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=4, number=1000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=662,
  serialized_end=754,
)
_sym_db.RegisterEnumDescriptor(_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS_DESTINATION)

_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY_COOKIESALLOWED = _descriptor.EnumDescriptor(
  name='CookiesAllowed',
  full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.CookiesAllowed',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='YES', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1021,
  serialized_end=1071,
)
_sym_db.RegisterEnumDescriptor(_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY_COOKIESALLOWED)


_NETWORKTRAFFICANNOTATION_TRAFFICSOURCE = _descriptor.Descriptor(
  name='TrafficSource',
  full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSource.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSource.line', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call_number', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSource.call_number', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=384,
  serialized_end=448,
)

_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS = _descriptor.Descriptor(
  name='TrafficSemantics',
  full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.trigger', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.destination', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_other', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics.destination_other', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS_DESTINATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=754,
)

_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY = _descriptor.Descriptor(
  name='TrafficPolicy',
  full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cookies_allowed', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.cookies_allowed', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cookies_store', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.cookies_store', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setting', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.setting', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chrome_policy', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.chrome_policy', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy_exception_justification', full_name='traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy.policy_exception_justification', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY_COOKIESALLOWED,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=1071,
)

_NETWORKTRAFFICANNOTATION = _descriptor.Descriptor(
  name='NetworkTrafficAnnotation',
  full_name='traffic_annotation.NetworkTrafficAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='traffic_annotation.NetworkTrafficAnnotation.unique_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='traffic_annotation.NetworkTrafficAnnotation.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='semantics', full_name='traffic_annotation.NetworkTrafficAnnotation.semantics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy', full_name='traffic_annotation.NetworkTrafficAnnotation.policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comments', full_name='traffic_annotation.NetworkTrafficAnnotation.comments', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NETWORKTRAFFICANNOTATION_TRAFFICSOURCE, _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS, _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=1071,
)


_EXTRACTEDNETWORKTRAFFICANNOTATION = _descriptor.Descriptor(
  name='ExtractedNetworkTrafficAnnotation',
  full_name='traffic_annotation.ExtractedNetworkTrafficAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_traffic_annotation', full_name='traffic_annotation.ExtractedNetworkTrafficAnnotation.network_traffic_annotation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1073,
  serialized_end=1190,
)


_WHITELISTEDNETWORKTRAFFICANNOTATIONS = _descriptor.Descriptor(
  name='WhitelistedNetworkTrafficAnnotations',
  full_name='traffic_annotation.WhitelistedNetworkTrafficAnnotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_traffic_annotation', full_name='traffic_annotation.WhitelistedNetworkTrafficAnnotations.network_traffic_annotation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1192,
  serialized_end=1312,
)


_NETWORKTRAFFICANNOTATIONS = _descriptor.Descriptor(
  name='NetworkTrafficAnnotations',
  full_name='traffic_annotation.NetworkTrafficAnnotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='extracted_network_traffic_annotations', full_name='traffic_annotation.NetworkTrafficAnnotations.extracted_network_traffic_annotations', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='whitelisted_network_traffic_annotations', full_name='traffic_annotation.NetworkTrafficAnnotations.whitelisted_network_traffic_annotations', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1315,
  serialized_end=1551,
)

_NETWORKTRAFFICANNOTATION_TRAFFICSOURCE.containing_type = _NETWORKTRAFFICANNOTATION
_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS.fields_by_name['destination'].enum_type = _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS_DESTINATION
_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS.containing_type = _NETWORKTRAFFICANNOTATION
_NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS_DESTINATION.containing_type = _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS
_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY.fields_by_name['cookies_allowed'].enum_type = _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY_COOKIESALLOWED
_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY.fields_by_name['chrome_policy'].message_type = chrome__settings__full__runtime__pb2._CHROMESETTINGSPROTO
_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY.containing_type = _NETWORKTRAFFICANNOTATION
_NETWORKTRAFFICANNOTATION_TRAFFICPOLICY_COOKIESALLOWED.containing_type = _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY
_NETWORKTRAFFICANNOTATION.fields_by_name['source'].message_type = _NETWORKTRAFFICANNOTATION_TRAFFICSOURCE
_NETWORKTRAFFICANNOTATION.fields_by_name['semantics'].message_type = _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS
_NETWORKTRAFFICANNOTATION.fields_by_name['policy'].message_type = _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY
_EXTRACTEDNETWORKTRAFFICANNOTATION.fields_by_name['network_traffic_annotation'].message_type = _NETWORKTRAFFICANNOTATION
_WHITELISTEDNETWORKTRAFFICANNOTATIONS.fields_by_name['network_traffic_annotation'].message_type = _NETWORKTRAFFICANNOTATION
_NETWORKTRAFFICANNOTATIONS.fields_by_name['extracted_network_traffic_annotations'].message_type = _EXTRACTEDNETWORKTRAFFICANNOTATION
_NETWORKTRAFFICANNOTATIONS.fields_by_name['whitelisted_network_traffic_annotations'].message_type = _WHITELISTEDNETWORKTRAFFICANNOTATIONS
DESCRIPTOR.message_types_by_name['NetworkTrafficAnnotation'] = _NETWORKTRAFFICANNOTATION
DESCRIPTOR.message_types_by_name['ExtractedNetworkTrafficAnnotation'] = _EXTRACTEDNETWORKTRAFFICANNOTATION
DESCRIPTOR.message_types_by_name['WhitelistedNetworkTrafficAnnotations'] = _WHITELISTEDNETWORKTRAFFICANNOTATIONS
DESCRIPTOR.message_types_by_name['NetworkTrafficAnnotations'] = _NETWORKTRAFFICANNOTATIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkTrafficAnnotation = _reflection.GeneratedProtocolMessageType('NetworkTrafficAnnotation', (_message.Message,), {

  'TrafficSource' : _reflection.GeneratedProtocolMessageType('TrafficSource', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKTRAFFICANNOTATION_TRAFFICSOURCE,
    '__module__' : 'traffic_annotation_pb2'
    # @@protoc_insertion_point(class_scope:traffic_annotation.NetworkTrafficAnnotation.TrafficSource)
    })
  ,

  'TrafficSemantics' : _reflection.GeneratedProtocolMessageType('TrafficSemantics', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKTRAFFICANNOTATION_TRAFFICSEMANTICS,
    '__module__' : 'traffic_annotation_pb2'
    # @@protoc_insertion_point(class_scope:traffic_annotation.NetworkTrafficAnnotation.TrafficSemantics)
    })
  ,

  'TrafficPolicy' : _reflection.GeneratedProtocolMessageType('TrafficPolicy', (_message.Message,), {
    'DESCRIPTOR' : _NETWORKTRAFFICANNOTATION_TRAFFICPOLICY,
    '__module__' : 'traffic_annotation_pb2'
    # @@protoc_insertion_point(class_scope:traffic_annotation.NetworkTrafficAnnotation.TrafficPolicy)
    })
  ,
  'DESCRIPTOR' : _NETWORKTRAFFICANNOTATION,
  '__module__' : 'traffic_annotation_pb2'
  # @@protoc_insertion_point(class_scope:traffic_annotation.NetworkTrafficAnnotation)
  })
_sym_db.RegisterMessage(NetworkTrafficAnnotation)
_sym_db.RegisterMessage(NetworkTrafficAnnotation.TrafficSource)
_sym_db.RegisterMessage(NetworkTrafficAnnotation.TrafficSemantics)
_sym_db.RegisterMessage(NetworkTrafficAnnotation.TrafficPolicy)

ExtractedNetworkTrafficAnnotation = _reflection.GeneratedProtocolMessageType('ExtractedNetworkTrafficAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTEDNETWORKTRAFFICANNOTATION,
  '__module__' : 'traffic_annotation_pb2'
  # @@protoc_insertion_point(class_scope:traffic_annotation.ExtractedNetworkTrafficAnnotation)
  })
_sym_db.RegisterMessage(ExtractedNetworkTrafficAnnotation)

WhitelistedNetworkTrafficAnnotations = _reflection.GeneratedProtocolMessageType('WhitelistedNetworkTrafficAnnotations', (_message.Message,), {
  'DESCRIPTOR' : _WHITELISTEDNETWORKTRAFFICANNOTATIONS,
  '__module__' : 'traffic_annotation_pb2'
  # @@protoc_insertion_point(class_scope:traffic_annotation.WhitelistedNetworkTrafficAnnotations)
  })
_sym_db.RegisterMessage(WhitelistedNetworkTrafficAnnotations)

NetworkTrafficAnnotations = _reflection.GeneratedProtocolMessageType('NetworkTrafficAnnotations', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTRAFFICANNOTATIONS,
  '__module__' : 'traffic_annotation_pb2'
  # @@protoc_insertion_point(class_scope:traffic_annotation.NetworkTrafficAnnotations)
  })
_sym_db.RegisterMessage(NetworkTrafficAnnotations)


# @@protoc_insertion_point(module_scope)
