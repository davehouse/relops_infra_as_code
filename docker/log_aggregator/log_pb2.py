# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from google.logging.v2 import log_entry_pb2 as google_dot_logging_dot_v2_dot_log__entry__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='log.proto',
  package='google.logging.v2',
  syntax='proto3',
  serialized_pb=_b('\n\tlog.proto\x12\x11google.logging.v2\x1a\x1cgoogle/api/annotations.proto\x1a#google/api/monitored_resource.proto\x1a!google/logging/v2/log_entry.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"$\n\x10\x44\x65leteLogRequest\x12\x10\n\x08log_name\x18\x01 \x01(\t\"\xa9\x02\n\x16WriteLogEntriesRequest\x12\x10\n\x08log_name\x18\x01 \x01(\t\x12/\n\x08resource\x18\x02 \x01(\x0b\x32\x1d.google.api.MonitoredResource\x12\x45\n\x06labels\x18\x03 \x03(\x0b\x32\x35.google.logging.v2.WriteLogEntriesRequest.LabelsEntry\x12,\n\x07\x65ntries\x18\x04 \x03(\x0b\x32\x1b.google.logging.v2.LogEntry\x12\x17\n\x0fpartial_success\x18\x05 \x01(\x08\x12\x0f\n\x07\x64ry_run\x18\x06 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x19\n\x17WriteLogEntriesResponse\"\xc8\x01\n\x1cWriteLogEntriesPartialErrors\x12]\n\x10log_entry_errors\x18\x01 \x03(\x0b\x32\x43.google.logging.v2.WriteLogEntriesPartialErrors.LogEntryErrorsEntry\x1aI\n\x13LogEntryErrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status:\x02\x38\x01\"\x91\x01\n\x15ListLogEntriesRequest\x12\x17\n\x0bproject_ids\x18\x01 \x03(\tB\x02\x18\x01\x12\x16\n\x0eresource_names\x18\x08 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"_\n\x16ListLogEntriesResponse\x12,\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1b.google.logging.v2.LogEntry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"P\n\'ListMonitoredResourceDescriptorsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"\x8a\x01\n(ListMonitoredResourceDescriptorsResponse\x12\x45\n\x14resource_descriptors\x18\x01 \x03(\x0b\x32\'.google.api.MonitoredResourceDescriptor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"H\n\x0fListLogsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\">\n\x10ListLogsResponse\x12\x11\n\tlog_names\x18\x03 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd8\x07\n\x10LoggingServiceV2\x12\xeb\x01\n\tDeleteLog\x12#.google.logging.v2.DeleteLogRequest\x1a\x16.google.protobuf.Empty\"\xa0\x01\x82\xd3\xe4\x93\x02\x99\x01* /v2/{log_name=projects/*/logs/*}Z\'*%/v2/{log_name=organizations/*/logs/*}Z!*\x1f/v2/{log_name=folders/*/logs/*}Z)*\'/v2/{log_name=billingAccounts/*/logs/*}\x12\x86\x01\n\x0fWriteLogEntries\x12).google.logging.v2.WriteLogEntriesRequest\x1a*.google.logging.v2.WriteLogEntriesResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v2/entries:write:\x01*\x12\x82\x01\n\x0eListLogEntries\x12(.google.logging.v2.ListLogEntriesRequest\x1a).google.logging.v2.ListLogEntriesResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/entries:list:\x01*\x12\xc5\x01\n ListMonitoredResourceDescriptors\x12:.google.logging.v2.ListMonitoredResourceDescriptorsRequest\x1a;.google.logging.v2.ListMonitoredResourceDescriptorsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v2/monitoredResourceDescriptors\x12\xff\x01\n\x08ListLogs\x12\".google.logging.v2.ListLogsRequest\x1a#.google.logging.v2.ListLogsResponse\"\xa9\x01\x82\xd3\xe4\x93\x02\xa2\x01\x12\x15/v2/{parent=*/*}/logsZ\x1e\x12\x1c/v2/{parent=projects/*}/logsZ#\x12!/v2/{parent=organizations/*}/logsZ\x1d\x12\x1b/v2/{parent=folders/*}/logsZ%\x12#/v2/{parent=billingAccounts/*}/logsB\x98\x01\n\x15\x63om.google.logging.v2B\x0cLoggingProtoP\x01Z8google.golang.org/genproto/googleapis/logging/v2;logging\xf8\x01\x01\xaa\x02\x17Google.Cloud.Logging.V2\xca\x02\x17Google\\Cloud\\Logging\\V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,google_dot_logging_dot_v2_dot_log__entry__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_DELETELOGREQUEST = _descriptor.Descriptor(
  name='DeleteLogRequest',
  full_name='google.logging.v2.DeleteLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_name', full_name='google.logging.v2.DeleteLogRequest.log_name', index=0,
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
  serialized_start=253,
  serialized_end=289,
)


_WRITELOGENTRIESREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.logging.v2.WriteLogEntriesRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.logging.v2.WriteLogEntriesRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.logging.v2.WriteLogEntriesRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=589,
)

_WRITELOGENTRIESREQUEST = _descriptor.Descriptor(
  name='WriteLogEntriesRequest',
  full_name='google.logging.v2.WriteLogEntriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_name', full_name='google.logging.v2.WriteLogEntriesRequest.log_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.logging.v2.WriteLogEntriesRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.logging.v2.WriteLogEntriesRequest.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='google.logging.v2.WriteLogEntriesRequest.entries', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partial_success', full_name='google.logging.v2.WriteLogEntriesRequest.partial_success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dry_run', full_name='google.logging.v2.WriteLogEntriesRequest.dry_run', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WRITELOGENTRIESREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=589,
)


_WRITELOGENTRIESRESPONSE = _descriptor.Descriptor(
  name='WriteLogEntriesResponse',
  full_name='google.logging.v2.WriteLogEntriesResponse',
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
  serialized_start=591,
  serialized_end=616,
)


_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY = _descriptor.Descriptor(
  name='LogEntryErrorsEntry',
  full_name='google.logging.v2.WriteLogEntriesPartialErrors.LogEntryErrorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.logging.v2.WriteLogEntriesPartialErrors.LogEntryErrorsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.logging.v2.WriteLogEntriesPartialErrors.LogEntryErrorsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=746,
  serialized_end=819,
)

_WRITELOGENTRIESPARTIALERRORS = _descriptor.Descriptor(
  name='WriteLogEntriesPartialErrors',
  full_name='google.logging.v2.WriteLogEntriesPartialErrors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_entry_errors', full_name='google.logging.v2.WriteLogEntriesPartialErrors.log_entry_errors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=819,
)


_LISTLOGENTRIESREQUEST = _descriptor.Descriptor(
  name='ListLogEntriesRequest',
  full_name='google.logging.v2.ListLogEntriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_ids', full_name='google.logging.v2.ListLogEntriesRequest.project_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='resource_names', full_name='google.logging.v2.ListLogEntriesRequest.resource_names', index=1,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.logging.v2.ListLogEntriesRequest.filter', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.logging.v2.ListLogEntriesRequest.order_by', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.logging.v2.ListLogEntriesRequest.page_size', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.logging.v2.ListLogEntriesRequest.page_token', index=5,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=822,
  serialized_end=967,
)


_LISTLOGENTRIESRESPONSE = _descriptor.Descriptor(
  name='ListLogEntriesResponse',
  full_name='google.logging.v2.ListLogEntriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='google.logging.v2.ListLogEntriesResponse.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.logging.v2.ListLogEntriesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=969,
  serialized_end=1064,
)


_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST = _descriptor.Descriptor(
  name='ListMonitoredResourceDescriptorsRequest',
  full_name='google.logging.v2.ListMonitoredResourceDescriptorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.logging.v2.ListMonitoredResourceDescriptorsRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.logging.v2.ListMonitoredResourceDescriptorsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1066,
  serialized_end=1146,
)


_LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE = _descriptor.Descriptor(
  name='ListMonitoredResourceDescriptorsResponse',
  full_name='google.logging.v2.ListMonitoredResourceDescriptorsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_descriptors', full_name='google.logging.v2.ListMonitoredResourceDescriptorsResponse.resource_descriptors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.logging.v2.ListMonitoredResourceDescriptorsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1149,
  serialized_end=1287,
)


_LISTLOGSREQUEST = _descriptor.Descriptor(
  name='ListLogsRequest',
  full_name='google.logging.v2.ListLogsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.logging.v2.ListLogsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.logging.v2.ListLogsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.logging.v2.ListLogsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1289,
  serialized_end=1361,
)


_LISTLOGSRESPONSE = _descriptor.Descriptor(
  name='ListLogsResponse',
  full_name='google.logging.v2.ListLogsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_names', full_name='google.logging.v2.ListLogsResponse.log_names', index=0,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.logging.v2.ListLogsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1363,
  serialized_end=1425,
)

_WRITELOGENTRIESREQUEST_LABELSENTRY.containing_type = _WRITELOGENTRIESREQUEST
_WRITELOGENTRIESREQUEST.fields_by_name['resource'].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCE
_WRITELOGENTRIESREQUEST.fields_by_name['labels'].message_type = _WRITELOGENTRIESREQUEST_LABELSENTRY
_WRITELOGENTRIESREQUEST.fields_by_name['entries'].message_type = google_dot_logging_dot_v2_dot_log__entry__pb2._LOGENTRY
_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY.fields_by_name['value'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY.containing_type = _WRITELOGENTRIESPARTIALERRORS
_WRITELOGENTRIESPARTIALERRORS.fields_by_name['log_entry_errors'].message_type = _WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY
_LISTLOGENTRIESRESPONSE.fields_by_name['entries'].message_type = google_dot_logging_dot_v2_dot_log__entry__pb2._LOGENTRY
_LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE.fields_by_name['resource_descriptors'].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCEDESCRIPTOR
DESCRIPTOR.message_types_by_name['DeleteLogRequest'] = _DELETELOGREQUEST
DESCRIPTOR.message_types_by_name['WriteLogEntriesRequest'] = _WRITELOGENTRIESREQUEST
DESCRIPTOR.message_types_by_name['WriteLogEntriesResponse'] = _WRITELOGENTRIESRESPONSE
DESCRIPTOR.message_types_by_name['WriteLogEntriesPartialErrors'] = _WRITELOGENTRIESPARTIALERRORS
DESCRIPTOR.message_types_by_name['ListLogEntriesRequest'] = _LISTLOGENTRIESREQUEST
DESCRIPTOR.message_types_by_name['ListLogEntriesResponse'] = _LISTLOGENTRIESRESPONSE
DESCRIPTOR.message_types_by_name['ListMonitoredResourceDescriptorsRequest'] = _LISTMONITOREDRESOURCEDESCRIPTORSREQUEST
DESCRIPTOR.message_types_by_name['ListMonitoredResourceDescriptorsResponse'] = _LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE
DESCRIPTOR.message_types_by_name['ListLogsRequest'] = _LISTLOGSREQUEST
DESCRIPTOR.message_types_by_name['ListLogsResponse'] = _LISTLOGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteLogRequest = _reflection.GeneratedProtocolMessageType('DeleteLogRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETELOGREQUEST,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.DeleteLogRequest)
  ))
_sym_db.RegisterMessage(DeleteLogRequest)

WriteLogEntriesRequest = _reflection.GeneratedProtocolMessageType('WriteLogEntriesRequest', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _WRITELOGENTRIESREQUEST_LABELSENTRY,
    __module__ = 'log_pb2'
    # @@protoc_insertion_point(class_scope:google.logging.v2.WriteLogEntriesRequest.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _WRITELOGENTRIESREQUEST,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.WriteLogEntriesRequest)
  ))
_sym_db.RegisterMessage(WriteLogEntriesRequest)
_sym_db.RegisterMessage(WriteLogEntriesRequest.LabelsEntry)

WriteLogEntriesResponse = _reflection.GeneratedProtocolMessageType('WriteLogEntriesResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITELOGENTRIESRESPONSE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.WriteLogEntriesResponse)
  ))
_sym_db.RegisterMessage(WriteLogEntriesResponse)

WriteLogEntriesPartialErrors = _reflection.GeneratedProtocolMessageType('WriteLogEntriesPartialErrors', (_message.Message,), dict(

  LogEntryErrorsEntry = _reflection.GeneratedProtocolMessageType('LogEntryErrorsEntry', (_message.Message,), dict(
    DESCRIPTOR = _WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY,
    __module__ = 'log_pb2'
    # @@protoc_insertion_point(class_scope:google.logging.v2.WriteLogEntriesPartialErrors.LogEntryErrorsEntry)
    ))
  ,
  DESCRIPTOR = _WRITELOGENTRIESPARTIALERRORS,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.WriteLogEntriesPartialErrors)
  ))
_sym_db.RegisterMessage(WriteLogEntriesPartialErrors)
_sym_db.RegisterMessage(WriteLogEntriesPartialErrors.LogEntryErrorsEntry)

ListLogEntriesRequest = _reflection.GeneratedProtocolMessageType('ListLogEntriesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTLOGENTRIESREQUEST,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogEntriesRequest)
  ))
_sym_db.RegisterMessage(ListLogEntriesRequest)

ListLogEntriesResponse = _reflection.GeneratedProtocolMessageType('ListLogEntriesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTLOGENTRIESRESPONSE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogEntriesResponse)
  ))
_sym_db.RegisterMessage(ListLogEntriesResponse)

ListMonitoredResourceDescriptorsRequest = _reflection.GeneratedProtocolMessageType('ListMonitoredResourceDescriptorsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMONITOREDRESOURCEDESCRIPTORSREQUEST,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListMonitoredResourceDescriptorsRequest)
  ))
_sym_db.RegisterMessage(ListMonitoredResourceDescriptorsRequest)

ListMonitoredResourceDescriptorsResponse = _reflection.GeneratedProtocolMessageType('ListMonitoredResourceDescriptorsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListMonitoredResourceDescriptorsResponse)
  ))
_sym_db.RegisterMessage(ListMonitoredResourceDescriptorsResponse)

ListLogsRequest = _reflection.GeneratedProtocolMessageType('ListLogsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTLOGSREQUEST,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogsRequest)
  ))
_sym_db.RegisterMessage(ListLogsRequest)

ListLogsResponse = _reflection.GeneratedProtocolMessageType('ListLogsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTLOGSRESPONSE,
  __module__ = 'log_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListLogsResponse)
  ))
_sym_db.RegisterMessage(ListLogsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.logging.v2B\014LoggingProtoP\001Z8google.golang.org/genproto/googleapis/logging/v2;logging\370\001\001\252\002\027Google.Cloud.Logging.V2\312\002\027Google\\Cloud\\Logging\\V2'))
_WRITELOGENTRIESREQUEST_LABELSENTRY.has_options = True
_WRITELOGENTRIESREQUEST_LABELSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY.has_options = True
_WRITELOGENTRIESPARTIALERRORS_LOGENTRYERRORSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_LISTLOGENTRIESREQUEST.fields_by_name['project_ids'].has_options = True
_LISTLOGENTRIESREQUEST.fields_by_name['project_ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))

_LOGGINGSERVICEV2 = _descriptor.ServiceDescriptor(
  name='LoggingServiceV2',
  full_name='google.logging.v2.LoggingServiceV2',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1428,
  serialized_end=2412,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeleteLog',
    full_name='google.logging.v2.LoggingServiceV2.DeleteLog',
    index=0,
    containing_service=None,
    input_type=_DELETELOGREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\231\001* /v2/{log_name=projects/*/logs/*}Z\'*%/v2/{log_name=organizations/*/logs/*}Z!*\037/v2/{log_name=folders/*/logs/*}Z)*\'/v2/{log_name=billingAccounts/*/logs/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='WriteLogEntries',
    full_name='google.logging.v2.LoggingServiceV2.WriteLogEntries',
    index=1,
    containing_service=None,
    input_type=_WRITELOGENTRIESREQUEST,
    output_type=_WRITELOGENTRIESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\026\"\021/v2/entries:write:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='ListLogEntries',
    full_name='google.logging.v2.LoggingServiceV2.ListLogEntries',
    index=2,
    containing_service=None,
    input_type=_LISTLOGENTRIESREQUEST,
    output_type=_LISTLOGENTRIESRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\025\"\020/v2/entries:list:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='ListMonitoredResourceDescriptors',
    full_name='google.logging.v2.LoggingServiceV2.ListMonitoredResourceDescriptors',
    index=3,
    containing_service=None,
    input_type=_LISTMONITOREDRESOURCEDESCRIPTORSREQUEST,
    output_type=_LISTMONITOREDRESOURCEDESCRIPTORSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\"\022 /v2/monitoredResourceDescriptors')),
  ),
  _descriptor.MethodDescriptor(
    name='ListLogs',
    full_name='google.logging.v2.LoggingServiceV2.ListLogs',
    index=4,
    containing_service=None,
    input_type=_LISTLOGSREQUEST,
    output_type=_LISTLOGSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\242\001\022\025/v2/{parent=*/*}/logsZ\036\022\034/v2/{parent=projects/*}/logsZ#\022!/v2/{parent=organizations/*}/logsZ\035\022\033/v2/{parent=folders/*}/logsZ%\022#/v2/{parent=billingAccounts/*}/logs')),
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGGINGSERVICEV2)

DESCRIPTOR.services_by_name['LoggingServiceV2'] = _LOGGINGSERVICEV2

# @@protoc_insertion_point(module_scope)
