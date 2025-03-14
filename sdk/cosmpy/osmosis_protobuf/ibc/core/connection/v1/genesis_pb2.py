"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ibc/core/connection/v1/genesis.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\'ibc/core/connection/v1/connection.proto"\xc6\x02\n\x0cGenesisState\x12G\n\x0bconnections\x18\x01 \x03(\x0b2,.ibc.core.connection.v1.IdentifiedConnectionB\x04\xc8\xde\x1f\x00\x12p\n\x17client_connection_paths\x18\x02 \x03(\x0b2\'.ibc.core.connection.v1.ConnectionPathsB&\xc8\xde\x1f\x00\xf2\xde\x1f\x1eyaml:"client_connection_paths"\x12E\n\x18next_connection_sequence\x18\x03 \x01(\x04B#\xf2\xde\x1f\x1fyaml:"next_connection_sequence"\x124\n\x06params\x18\x04 \x01(\x0b2\x1e.ibc.core.connection.v1.ParamsB\x04\xc8\xde\x1f\x00B>Z<github.com/cosmos/ibc-go/v4/modules/core/03-connection/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.connection.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v4/modules/core/03-connection/types'
    _GENESISSTATE.fields_by_name['connections']._options = None
    _GENESISSTATE.fields_by_name['connections']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['client_connection_paths']._options = None
    _GENESISSTATE.fields_by_name['client_connection_paths']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1eyaml:"client_connection_paths"'
    _GENESISSTATE.fields_by_name['next_connection_sequence']._options = None
    _GENESISSTATE.fields_by_name['next_connection_sequence']._serialized_options = b'\xf2\xde\x1f\x1fyaml:"next_connection_sequence"'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 128
    _globals['_GENESISSTATE']._serialized_end = 454