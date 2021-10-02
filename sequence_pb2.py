# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sequence.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import note_type_pb2 as note__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sequence.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0esequence.proto\x1a\x0fnote_type.proto\"a\n\x04Note\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.NoteType\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\x0e\n\x06length\x18\x03 \x01(\x02\x12\x12\n\ninstrument\x18\x04 \x01(\x05\x12\x0e\n\x06volume\x18\x05 \x01(\x02\"Y\n\x06Marker\x12\x0c\n\x04time\x18\x01 \x01(\x02\x12\x0f\n\x07setting\x18\x02 \x01(\x05\x12\x12\n\ninstrument\x18\x03 \x01(\x05\x12\r\n\x05value\x18\x04 \x01(\x02\x12\r\n\x05\x62lend\x18\x05 \x01(\x08\"\xa4\x01\n\x12InstrumentSettings\x12\x0e\n\x06volume\x18\x01 \x01(\x02\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x08\x12\x0e\n\x06reverb\x18\x03 \x01(\x08\x12\x0b\n\x03pan\x18\x04 \x01(\x02\x12\x11\n\tenable_eq\x18\x05 \x01(\x08\x12\x0e\n\x06\x65q_low\x18\x06 \x01(\x02\x12\x0e\n\x06\x65q_mid\x18\x07 \x01(\x02\x12\x0f\n\x07\x65q_high\x18\x08 \x01(\x02\x12\x0e\n\x06\x64\x65tune\x18\t \x01(\x02\"\xd3\x01\n\x10SequenceSettings\x12\x0b\n\x03\x62pm\x18\x01 \x01(\x05\x12\x16\n\x0etime_signature\x18\x02 \x01(\x05\x12\x37\n\x0binstruments\x18\x03 \x03(\x0b\x32\".SequenceSettings.InstrumentsEntry\x12\x18\n\x10one_minus_volume\x18\x04 \x01(\x02\x1aG\n\x10InstrumentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.InstrumentSettings:\x02\x38\x01\"_\n\x08Sequence\x12#\n\x08settings\x18\x01 \x01(\x0b\x32\x11.SequenceSettings\x12\x14\n\x05notes\x18\x02 \x03(\x0b\x32\x05.Note\x12\x18\n\x07markers\x18\x03 \x03(\x0b\x32\x07.Markerb\x06proto3'
  ,
  dependencies=[note__type__pb2.DESCRIPTOR,])




_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Note.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='Note.time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='Note.length', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='Note.instrument', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='Note.volume', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=35,
  serialized_end=132,
)


_MARKER = _descriptor.Descriptor(
  name='Marker',
  full_name='Marker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='Marker.time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setting', full_name='Marker.setting', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='Marker.instrument', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Marker.value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blend', full_name='Marker.blend', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=134,
  serialized_end=223,
)


_INSTRUMENTSETTINGS = _descriptor.Descriptor(
  name='InstrumentSettings',
  full_name='InstrumentSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='InstrumentSettings.volume', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay', full_name='InstrumentSettings.delay', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reverb', full_name='InstrumentSettings.reverb', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pan', full_name='InstrumentSettings.pan', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_eq', full_name='InstrumentSettings.enable_eq', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eq_low', full_name='InstrumentSettings.eq_low', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eq_mid', full_name='InstrumentSettings.eq_mid', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eq_high', full_name='InstrumentSettings.eq_high', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detune', full_name='InstrumentSettings.detune', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=226,
  serialized_end=390,
)


_SEQUENCESETTINGS_INSTRUMENTSENTRY = _descriptor.Descriptor(
  name='InstrumentsEntry',
  full_name='SequenceSettings.InstrumentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SequenceSettings.InstrumentsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='SequenceSettings.InstrumentsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=604,
)

_SEQUENCESETTINGS = _descriptor.Descriptor(
  name='SequenceSettings',
  full_name='SequenceSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bpm', full_name='SequenceSettings.bpm', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_signature', full_name='SequenceSettings.time_signature', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instruments', full_name='SequenceSettings.instruments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='one_minus_volume', full_name='SequenceSettings.one_minus_volume', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEQUENCESETTINGS_INSTRUMENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=604,
)


_SEQUENCE = _descriptor.Descriptor(
  name='Sequence',
  full_name='Sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='Sequence.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes', full_name='Sequence.notes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='markers', full_name='Sequence.markers', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=606,
  serialized_end=701,
)

_NOTE.fields_by_name['type'].enum_type = note__type__pb2._NOTETYPE
_SEQUENCESETTINGS_INSTRUMENTSENTRY.fields_by_name['value'].message_type = _INSTRUMENTSETTINGS
_SEQUENCESETTINGS_INSTRUMENTSENTRY.containing_type = _SEQUENCESETTINGS
_SEQUENCESETTINGS.fields_by_name['instruments'].message_type = _SEQUENCESETTINGS_INSTRUMENTSENTRY
_SEQUENCE.fields_by_name['settings'].message_type = _SEQUENCESETTINGS
_SEQUENCE.fields_by_name['notes'].message_type = _NOTE
_SEQUENCE.fields_by_name['markers'].message_type = _MARKER
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['Marker'] = _MARKER
DESCRIPTOR.message_types_by_name['InstrumentSettings'] = _INSTRUMENTSETTINGS
DESCRIPTOR.message_types_by_name['SequenceSettings'] = _SEQUENCESETTINGS
DESCRIPTOR.message_types_by_name['Sequence'] = _SEQUENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
  'DESCRIPTOR' : _NOTE,
  '__module__' : 'sequence_pb2'
  # @@protoc_insertion_point(class_scope:Note)
  })
_sym_db.RegisterMessage(Note)

Marker = _reflection.GeneratedProtocolMessageType('Marker', (_message.Message,), {
  'DESCRIPTOR' : _MARKER,
  '__module__' : 'sequence_pb2'
  # @@protoc_insertion_point(class_scope:Marker)
  })
_sym_db.RegisterMessage(Marker)

InstrumentSettings = _reflection.GeneratedProtocolMessageType('InstrumentSettings', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUMENTSETTINGS,
  '__module__' : 'sequence_pb2'
  # @@protoc_insertion_point(class_scope:InstrumentSettings)
  })
_sym_db.RegisterMessage(InstrumentSettings)

SequenceSettings = _reflection.GeneratedProtocolMessageType('SequenceSettings', (_message.Message,), {

  'InstrumentsEntry' : _reflection.GeneratedProtocolMessageType('InstrumentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SEQUENCESETTINGS_INSTRUMENTSENTRY,
    '__module__' : 'sequence_pb2'
    # @@protoc_insertion_point(class_scope:SequenceSettings.InstrumentsEntry)
    })
  ,
  'DESCRIPTOR' : _SEQUENCESETTINGS,
  '__module__' : 'sequence_pb2'
  # @@protoc_insertion_point(class_scope:SequenceSettings)
  })
_sym_db.RegisterMessage(SequenceSettings)
_sym_db.RegisterMessage(SequenceSettings.InstrumentsEntry)

Sequence = _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCE,
  '__module__' : 'sequence_pb2'
  # @@protoc_insertion_point(class_scope:Sequence)
  })
_sym_db.RegisterMessage(Sequence)


_SEQUENCESETTINGS_INSTRUMENTSENTRY._options = None
# @@protoc_insertion_point(module_scope)