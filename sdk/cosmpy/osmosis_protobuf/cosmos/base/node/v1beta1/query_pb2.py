"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/base/node/v1beta1/query.proto\x12\x18cosmos.base.node.v1beta1\x1a\x1cgoogle/api/annotations.proto"\x0f\n\rConfigRequest"+\n\x0eConfigResponse\x12\x19\n\x11minimum_gas_price\x18\x01 \x01(\t2\x91\x01\n\x07Service\x12\x85\x01\n\x06Config\x12\'.cosmos.base.node.v1beta1.ConfigRequest\x1a(.cosmos.base.node.v1beta1.ConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/configB/Z-github.com/cosmos/cosmos-sdk/client/grpc/nodeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.node.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/client/grpc/node'
    _SERVICE.methods_by_name['Config']._options = None
    _SERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/config'
    _globals['_CONFIGREQUEST']._serialized_start = 96
    _globals['_CONFIGREQUEST']._serialized_end = 111
    _globals['_CONFIGRESPONSE']._serialized_start = 113
    _globals['_CONFIGRESPONSE']._serialized_end = 156
    _globals['_SERVICE']._serialized_start = 159
    _globals['_SERVICE']._serialized_end = 304