"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....amino import amino_pb2 as amino_dot_amino__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/crypto/secp256k1/keys.proto\x12\x17cosmos.crypto.secp256k1\x1a\x11amino/amino.proto\x1a\x14gogoproto/gogo.proto"H\n\x06PubKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:1\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1atendermint/PubKeySecp256k1\x92\xe7\xb0*\tkey_field"F\n\x07PrivKey\x12\x0b\n\x03key\x18\x01 \x01(\x0c:.\x8a\xe7\xb0*\x1btendermint/PrivKeySecp256k1\x92\xe7\xb0*\tkey_fieldB4Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256k1.keys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1'
    _PUBKEY._options = None
    _PUBKEY._serialized_options = b'\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1atendermint/PubKeySecp256k1\x92\xe7\xb0*\tkey_field'
    _PRIVKEY._options = None
    _PRIVKEY._serialized_options = b'\x8a\xe7\xb0*\x1btendermint/PrivKeySecp256k1\x92\xe7\xb0*\tkey_field'
    _globals['_PUBKEY']._serialized_start = 104
    _globals['_PUBKEY']._serialized_end = 176
    _globals['_PRIVKEY']._serialized_start = 178
    _globals['_PRIVKEY']._serialized_end = 248