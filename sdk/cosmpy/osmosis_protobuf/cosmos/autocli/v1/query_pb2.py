"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.autocli.v1 import options_pb2 as cosmos_dot_autocli_dot_v1_dot_options__pb2
from ....cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcosmos/autocli/v1/query.proto\x12\x11cosmos.autocli.v1\x1a\x1fcosmos/autocli/v1/options.proto\x1a\x1bcosmos/query/v1/query.proto"\x13\n\x11AppOptionsRequest"\xbe\x01\n\x12AppOptionsResponse\x12P\n\x0emodule_options\x18\x01 \x03(\x0b28.cosmos.autocli.v1.AppOptionsResponse.ModuleOptionsEntry\x1aV\n\x12ModuleOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b2 .cosmos.autocli.v1.ModuleOptions:\x028\x012i\n\x05Query\x12`\n\nAppOptions\x12$.cosmos.autocli.v1.AppOptionsRequest\x1a%.cosmos.autocli.v1.AppOptionsResponse"\x05\x88\xe7\xb0*\x00B+Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.autocli.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)cosmossdk.io/api/cosmos/base/cli/v1;cliv1'
    _APPOPTIONSRESPONSE_MODULEOPTIONSENTRY._options = None
    _APPOPTIONSRESPONSE_MODULEOPTIONSENTRY._serialized_options = b'8\x01'
    _QUERY.methods_by_name['AppOptions']._options = None
    _QUERY.methods_by_name['AppOptions']._serialized_options = b'\x88\xe7\xb0*\x00'
    _globals['_APPOPTIONSREQUEST']._serialized_start = 114
    _globals['_APPOPTIONSREQUEST']._serialized_end = 133
    _globals['_APPOPTIONSRESPONSE']._serialized_start = 136
    _globals['_APPOPTIONSRESPONSE']._serialized_end = 326
    _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_start = 240
    _globals['_APPOPTIONSRESPONSE_MODULEOPTIONSENTRY']._serialized_end = 326
    _globals['_QUERY']._serialized_start = 328
    _globals['_QUERY']._serialized_end = 433