# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fipa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fipa.proto',
  package='fetch.aea.fipa',
  syntax='proto3',
  serialized_pb=_b('\n\nfipa.proto\x12\x0e\x66\x65tch.aea.fipa\"\xb1\x07\n\x0b\x46IPAMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64ialogue_id\x18\x02 \x01(\x05\x12\x0e\n\x06target\x18\x03 \x01(\x05\x12.\n\x03\x63\x66p\x18\x04 \x01(\x0b\x32\x1f.fetch.aea.fipa.FIPAMessage.CFPH\x00\x12\x36\n\x07propose\x18\x05 \x01(\x0b\x32#.fetch.aea.fipa.FIPAMessage.ProposeH\x00\x12\x34\n\x06\x61\x63\x63\x65pt\x18\x06 \x01(\x0b\x32\".fetch.aea.fipa.FIPAMessage.AcceptH\x00\x12?\n\x0cmatch_accept\x18\x07 \x01(\x0b\x32\'.fetch.aea.fipa.FIPAMessage.MatchAcceptH\x00\x12\x36\n\x07\x64\x65\x63line\x18\x08 \x01(\x0b\x32#.fetch.aea.fipa.FIPAMessage.DeclineH\x00\x12\x34\n\x06inform\x18\t \x01(\x0b\x32\".fetch.aea.fipa.FIPAMessage.InformH\x00\x12\x46\n\x10\x61\x63\x63\x65pt_w_address\x18\n \x01(\x0b\x32*.fetch.aea.fipa.FIPAMessage.AcceptWAddressH\x00\x12Q\n\x16match_accept_w_address\x18\x0b \x01(\x0b\x32/.fetch.aea.fipa.FIPAMessage.MatchAcceptWAddressH\x00\x1a}\n\x03\x43\x46P\x12\x0f\n\x05\x62ytes\x18\x01 \x01(\x0cH\x00\x12:\n\x07nothing\x18\x02 \x01(\x0b\x32\'.fetch.aea.fipa.FIPAMessage.CFP.NothingH\x00\x12\x15\n\x0bquery_bytes\x18\x03 \x01(\x0cH\x00\x1a\t\n\x07NothingB\x07\n\x05query\x1a\x1b\n\x07Propose\x12\x10\n\x08proposal\x18\x01 \x03(\x0c\x1a\x08\n\x06\x41\x63\x63\x65pt\x1a\r\n\x0bMatchAccept\x1a#\n\x10\x41\x63\x63\x65pt_W_Address\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1a(\n\x15MatchAccept_W_Address\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1a\t\n\x07\x44\x65\x63line\x1a\x17\n\x06Inform\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\x1a!\n\x0e\x41\x63\x63\x65ptWAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x1a&\n\x13MatchAcceptWAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x0e\n\x0cperformativeb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FIPAMESSAGE_CFP_NOTHING = _descriptor.Descriptor(
  name='Nothing',
  full_name='fetch.aea.fipa.FIPAMessage.CFP.Nothing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=707,
)

_FIPAMESSAGE_CFP = _descriptor.Descriptor(
  name='CFP',
  full_name='fetch.aea.fipa.FIPAMessage.CFP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='fetch.aea.fipa.FIPAMessage.CFP.bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nothing', full_name='fetch.aea.fipa.FIPAMessage.CFP.nothing', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_bytes', full_name='fetch.aea.fipa.FIPAMessage.CFP.query_bytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FIPAMESSAGE_CFP_NOTHING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='query', full_name='fetch.aea.fipa.FIPAMessage.CFP.query',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=591,
  serialized_end=716,
)

_FIPAMESSAGE_PROPOSE = _descriptor.Descriptor(
  name='Propose',
  full_name='fetch.aea.fipa.FIPAMessage.Propose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='fetch.aea.fipa.FIPAMessage.Propose.proposal', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=745,
)

_FIPAMESSAGE_ACCEPT = _descriptor.Descriptor(
  name='Accept',
  full_name='fetch.aea.fipa.FIPAMessage.Accept',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=747,
  serialized_end=755,
)

_FIPAMESSAGE_MATCHACCEPT = _descriptor.Descriptor(
  name='MatchAccept',
  full_name='fetch.aea.fipa.FIPAMessage.MatchAccept',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=770,
)

_FIPAMESSAGE_ACCEPT_W_ADDRESS = _descriptor.Descriptor(
  name='Accept_W_Address',
  full_name='fetch.aea.fipa.FIPAMessage.Accept_W_Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='fetch.aea.fipa.FIPAMessage.Accept_W_Address.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=807,
)

_FIPAMESSAGE_MATCHACCEPT_W_ADDRESS = _descriptor.Descriptor(
  name='MatchAccept_W_Address',
  full_name='fetch.aea.fipa.FIPAMessage.MatchAccept_W_Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='fetch.aea.fipa.FIPAMessage.MatchAccept_W_Address.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=849,
)

_FIPAMESSAGE_DECLINE = _descriptor.Descriptor(
  name='Decline',
  full_name='fetch.aea.fipa.FIPAMessage.Decline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=860,
)

_FIPAMESSAGE_INFORM = _descriptor.Descriptor(
  name='Inform',
  full_name='fetch.aea.fipa.FIPAMessage.Inform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='fetch.aea.fipa.FIPAMessage.Inform.bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=885,
)

_FIPAMESSAGE_ACCEPTWADDRESS = _descriptor.Descriptor(
  name='AcceptWAddress',
  full_name='fetch.aea.fipa.FIPAMessage.AcceptWAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='fetch.aea.fipa.FIPAMessage.AcceptWAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=920,
)

_FIPAMESSAGE_MATCHACCEPTWADDRESS = _descriptor.Descriptor(
  name='MatchAcceptWAddress',
  full_name='fetch.aea.fipa.FIPAMessage.MatchAcceptWAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='fetch.aea.fipa.FIPAMessage.MatchAcceptWAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=922,
  serialized_end=960,
)

_FIPAMESSAGE = _descriptor.Descriptor(
  name='FIPAMessage',
  full_name='fetch.aea.fipa.FIPAMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='fetch.aea.fipa.FIPAMessage.message_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dialogue_id', full_name='fetch.aea.fipa.FIPAMessage.dialogue_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='fetch.aea.fipa.FIPAMessage.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cfp', full_name='fetch.aea.fipa.FIPAMessage.cfp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='propose', full_name='fetch.aea.fipa.FIPAMessage.propose', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accept', full_name='fetch.aea.fipa.FIPAMessage.accept', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_accept', full_name='fetch.aea.fipa.FIPAMessage.match_accept', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decline', full_name='fetch.aea.fipa.FIPAMessage.decline', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inform', full_name='fetch.aea.fipa.FIPAMessage.inform', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accept_w_address', full_name='fetch.aea.fipa.FIPAMessage.accept_w_address', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_accept_w_address', full_name='fetch.aea.fipa.FIPAMessage.match_accept_w_address', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FIPAMESSAGE_CFP, _FIPAMESSAGE_PROPOSE, _FIPAMESSAGE_ACCEPT, _FIPAMESSAGE_MATCHACCEPT, _FIPAMESSAGE_ACCEPT_W_ADDRESS, _FIPAMESSAGE_MATCHACCEPT_W_ADDRESS, _FIPAMESSAGE_DECLINE, _FIPAMESSAGE_INFORM, _FIPAMESSAGE_ACCEPTWADDRESS, _FIPAMESSAGE_MATCHACCEPTWADDRESS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='performative', full_name='fetch.aea.fipa.FIPAMessage.performative',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=31,
  serialized_end=976,
)

_FIPAMESSAGE_CFP_NOTHING.containing_type = _FIPAMESSAGE_CFP
_FIPAMESSAGE_CFP.fields_by_name['nothing'].message_type = _FIPAMESSAGE_CFP_NOTHING
_FIPAMESSAGE_CFP.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_CFP.oneofs_by_name['query'].fields.append(
  _FIPAMESSAGE_CFP.fields_by_name['bytes'])
_FIPAMESSAGE_CFP.fields_by_name['bytes'].containing_oneof = _FIPAMESSAGE_CFP.oneofs_by_name['query']
_FIPAMESSAGE_CFP.oneofs_by_name['query'].fields.append(
  _FIPAMESSAGE_CFP.fields_by_name['nothing'])
_FIPAMESSAGE_CFP.fields_by_name['nothing'].containing_oneof = _FIPAMESSAGE_CFP.oneofs_by_name['query']
_FIPAMESSAGE_CFP.oneofs_by_name['query'].fields.append(
  _FIPAMESSAGE_CFP.fields_by_name['query_bytes'])
_FIPAMESSAGE_CFP.fields_by_name['query_bytes'].containing_oneof = _FIPAMESSAGE_CFP.oneofs_by_name['query']
_FIPAMESSAGE_PROPOSE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCHACCEPT.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT_W_ADDRESS.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCHACCEPT_W_ADDRESS.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_DECLINE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_INFORM.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPTWADDRESS.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCHACCEPTWADDRESS.containing_type = _FIPAMESSAGE
_FIPAMESSAGE.fields_by_name['cfp'].message_type = _FIPAMESSAGE_CFP
_FIPAMESSAGE.fields_by_name['propose'].message_type = _FIPAMESSAGE_PROPOSE
_FIPAMESSAGE.fields_by_name['accept'].message_type = _FIPAMESSAGE_ACCEPT
_FIPAMESSAGE.fields_by_name['match_accept'].message_type = _FIPAMESSAGE_MATCHACCEPT
_FIPAMESSAGE.fields_by_name['decline'].message_type = _FIPAMESSAGE_DECLINE
_FIPAMESSAGE.fields_by_name['inform'].message_type = _FIPAMESSAGE_INFORM
_FIPAMESSAGE.fields_by_name['accept_w_address'].message_type = _FIPAMESSAGE_ACCEPTWADDRESS
_FIPAMESSAGE.fields_by_name['match_accept_w_address'].message_type = _FIPAMESSAGE_MATCHACCEPTWADDRESS
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['cfp'])
_FIPAMESSAGE.fields_by_name['cfp'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['propose'])
_FIPAMESSAGE.fields_by_name['propose'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['accept'])
_FIPAMESSAGE.fields_by_name['accept'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['match_accept'])
_FIPAMESSAGE.fields_by_name['match_accept'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['decline'])
_FIPAMESSAGE.fields_by_name['decline'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['inform'])
_FIPAMESSAGE.fields_by_name['inform'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['accept_w_address'])
_FIPAMESSAGE.fields_by_name['accept_w_address'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
_FIPAMESSAGE.oneofs_by_name['performative'].fields.append(
  _FIPAMESSAGE.fields_by_name['match_accept_w_address'])
_FIPAMESSAGE.fields_by_name['match_accept_w_address'].containing_oneof = _FIPAMESSAGE.oneofs_by_name['performative']
DESCRIPTOR.message_types_by_name['FIPAMessage'] = _FIPAMESSAGE

FIPAMessage = _reflection.GeneratedProtocolMessageType('FIPAMessage', (_message.Message,), dict(

  CFP = _reflection.GeneratedProtocolMessageType('CFP', (_message.Message,), dict(

    Nothing = _reflection.GeneratedProtocolMessageType('Nothing', (_message.Message,), dict(
      DESCRIPTOR = _FIPAMESSAGE_CFP_NOTHING,
      __module__ = 'fipa_pb2'
      # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.CFP.Nothing)
      ))
    ,
    DESCRIPTOR = _FIPAMESSAGE_CFP,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.CFP)
    ))
  ,

  Propose = _reflection.GeneratedProtocolMessageType('Propose', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_PROPOSE,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.Propose)
    ))
  ,

  Accept = _reflection.GeneratedProtocolMessageType('Accept', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_ACCEPT,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.Accept)
    ))
  ,

  MatchAccept = _reflection.GeneratedProtocolMessageType('MatchAccept', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_MATCHACCEPT,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.MatchAccept)
    ))
  ,

  Accept_W_Address = _reflection.GeneratedProtocolMessageType('Accept_W_Address', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_ACCEPT_W_ADDRESS,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.Accept_W_Address)
    ))
  ,

  MatchAccept_W_Address = _reflection.GeneratedProtocolMessageType('MatchAccept_W_Address', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_MATCHACCEPT_W_ADDRESS,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.MatchAccept_W_Address)
    ))
  ,

  Decline = _reflection.GeneratedProtocolMessageType('Decline', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_DECLINE,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.Decline)
    ))
  ,

  Inform = _reflection.GeneratedProtocolMessageType('Inform', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_INFORM,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.Inform)
    ))
  ,

  AcceptWAddress = _reflection.GeneratedProtocolMessageType('AcceptWAddress', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_ACCEPTWADDRESS,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.AcceptWAddress)
    ))
  ,

  MatchAcceptWAddress = _reflection.GeneratedProtocolMessageType('MatchAcceptWAddress', (_message.Message,), dict(
    DESCRIPTOR = _FIPAMESSAGE_MATCHACCEPTWADDRESS,
    __module__ = 'fipa_pb2'
    # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage.MatchAcceptWAddress)
    ))
  ,
  DESCRIPTOR = _FIPAMESSAGE,
  __module__ = 'fipa_pb2'
  # @@protoc_insertion_point(class_scope:fetch.aea.fipa.FIPAMessage)
  ))
_sym_db.RegisterMessage(FIPAMessage)
_sym_db.RegisterMessage(FIPAMessage.CFP)
_sym_db.RegisterMessage(FIPAMessage.CFP.Nothing)
_sym_db.RegisterMessage(FIPAMessage.Propose)
_sym_db.RegisterMessage(FIPAMessage.Accept)
_sym_db.RegisterMessage(FIPAMessage.MatchAccept)
_sym_db.RegisterMessage(FIPAMessage.Accept_W_Address)
_sym_db.RegisterMessage(FIPAMessage.MatchAccept_W_Address)
_sym_db.RegisterMessage(FIPAMessage.Decline)
_sym_db.RegisterMessage(FIPAMessage.Inform)
_sym_db.RegisterMessage(FIPAMessage.AcceptWAddress)
_sym_db.RegisterMessage(FIPAMessage.MatchAcceptWAddress)


# @@protoc_insertion_point(module_scope)