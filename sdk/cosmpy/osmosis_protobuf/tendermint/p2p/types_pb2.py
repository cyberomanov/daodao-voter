"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1atendermint/p2p/types.proto\x12\x0etendermint.p2p\x1a\x14gogoproto/gogo.proto"B\n\nNetAddress\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe2\xde\x1f\x02ID\x12\x12\n\x02ip\x18\x02 \x01(\tB\x06\xe2\xde\x1f\x02IP\x12\x0c\n\x04port\x18\x03 \x01(\r"C\n\x0fProtocolVersion\x12\x14\n\x03p2p\x18\x01 \x01(\x04B\x07\xe2\xde\x1f\x03P2P\x12\r\n\x05block\x18\x02 \x01(\x04\x12\x0b\n\x03app\x18\x03 \x01(\x04"\x93\x02\n\x0fDefaultNodeInfo\x12?\n\x10protocol_version\x18\x01 \x01(\x0b2\x1f.tendermint.p2p.ProtocolVersionB\x04\xc8\xde\x1f\x00\x12*\n\x0fdefault_node_id\x18\x02 \x01(\tB\x11\xe2\xde\x1f\rDefaultNodeID\x12\x13\n\x0blisten_addr\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x10\n\x08channels\x18\x06 \x01(\x0c\x12\x0f\n\x07moniker\x18\x07 \x01(\t\x129\n\x05other\x18\x08 \x01(\x0b2$.tendermint.p2p.DefaultNodeInfoOtherB\x04\xc8\xde\x1f\x00"M\n\x14DefaultNodeInfoOther\x12\x10\n\x08tx_index\x18\x01 \x01(\t\x12#\n\x0brpc_address\x18\x02 \x01(\tB\x0e\xe2\xde\x1f\nRPCAddressB7Z5github.com/tendermint/tendermint/proto/tendermint/p2pb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.p2p.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/tendermint/tendermint/proto/tendermint/p2p'
    _NETADDRESS.fields_by_name['id']._options = None
    _NETADDRESS.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _NETADDRESS.fields_by_name['ip']._options = None
    _NETADDRESS.fields_by_name['ip']._serialized_options = b'\xe2\xde\x1f\x02IP'
    _PROTOCOLVERSION.fields_by_name['p2p']._options = None
    _PROTOCOLVERSION.fields_by_name['p2p']._serialized_options = b'\xe2\xde\x1f\x03P2P'
    _DEFAULTNODEINFO.fields_by_name['protocol_version']._options = None
    _DEFAULTNODEINFO.fields_by_name['protocol_version']._serialized_options = b'\xc8\xde\x1f\x00'
    _DEFAULTNODEINFO.fields_by_name['default_node_id']._options = None
    _DEFAULTNODEINFO.fields_by_name['default_node_id']._serialized_options = b'\xe2\xde\x1f\rDefaultNodeID'
    _DEFAULTNODEINFO.fields_by_name['other']._options = None
    _DEFAULTNODEINFO.fields_by_name['other']._serialized_options = b'\xc8\xde\x1f\x00'
    _DEFAULTNODEINFOOTHER.fields_by_name['rpc_address']._options = None
    _DEFAULTNODEINFOOTHER.fields_by_name['rpc_address']._serialized_options = b'\xe2\xde\x1f\nRPCAddress'
    _globals['_NETADDRESS']._serialized_start = 68
    _globals['_NETADDRESS']._serialized_end = 134
    _globals['_PROTOCOLVERSION']._serialized_start = 136
    _globals['_PROTOCOLVERSION']._serialized_end = 203
    _globals['_DEFAULTNODEINFO']._serialized_start = 206
    _globals['_DEFAULTNODEINFO']._serialized_end = 481
    _globals['_DEFAULTNODEINFOOTHER']._serialized_start = 483
    _globals['_DEFAULTNODEINFOOTHER']._serialized_end = 560