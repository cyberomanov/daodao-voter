"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8ibc/applications/interchain_accounts/host/v1/query.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x1cgoogle/api/annotations.proto\x1a7ibc/applications/interchain_accounts/host/v1/host.proto"\x14\n\x12QueryParamsRequest"[\n\x13QueryParamsResponse\x12D\n\x06params\x18\x01 \x01(\x0b24.ibc.applications.interchain_accounts.host.v1.Params2\xcd\x01\n\x05Query\x12\xc3\x01\n\x06Params\x12@.ibc.applications.interchain_accounts.host.v1.QueryParamsRequest\x1aA.ibc.applications.interchain_accounts.host.v1.QueryParamsResponse"4\x82\xd3\xe4\x93\x02.\x12,/ibc/apps/interchain_accounts/host/v1/paramsBLZJgithub.com/cosmos/ibc-go/v4/modules/apps/27-interchain-accounts/host/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v4/modules/apps/27-interchain-accounts/host/types'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/ibc/apps/interchain_accounts/host/v1/params'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 193
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 213
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 215
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 306
    _globals['_QUERY']._serialized_start = 309
    _globals['_QUERY']._serialized_end = 514