"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/bank/v1beta1/tx.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xfb\x01\n\x07MsgSend\x12.\n\x0cfrom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12`\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:0\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*\x12cosmos-sdk/MsgSend"\x11\n\x0fMsgSendResponse"\xab\x01\n\x0cMsgMultiSend\x125\n\x06inputs\x18\x01 \x03(\x0b2\x1a.cosmos.bank.v1beta1.InputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x127\n\x07outputs\x18\x02 \x03(\x0b2\x1b.cosmos.bank.v1beta1.OutputB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:+\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06inputs\x8a\xe7\xb0*\x17cosmos-sdk/MsgMultiSend"\x16\n\x14MsgMultiSendResponse"\xac\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x06params\x18\x02 \x01(\x0b2\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:4\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/bank/MsgUpdateParams"\x19\n\x17MsgUpdateParamsResponse"\xc2\x01\n\x11MsgSetSendEnabled\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x126\n\x0csend_enabled\x18\x02 \x03(\x0b2 .cosmos.bank.v1beta1.SendEnabled\x12\x17\n\x0fuse_default_for\x18\x03 \x03(\t:/\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1ccosmos-sdk/MsgSetSendEnabled"\x1b\n\x19MsgSetSendEnabledResponse2\x81\x03\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponse\x12b\n\x0cUpdateParams\x12$.cosmos.bank.v1beta1.MsgUpdateParams\x1a,.cosmos.bank.v1beta1.MsgUpdateParamsResponse\x12h\n\x0eSetSendEnabled\x12&.cosmos.bank.v1beta1.MsgSetSendEnabled\x1a..cosmos.bank.v1beta1.MsgSetSendEnabledResponse\x1a\x05\x80\xe7\xb0*\x01B+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _MSGSEND.fields_by_name['from_address']._options = None
    _MSGSEND.fields_by_name['from_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSEND.fields_by_name['to_address']._options = None
    _MSGSEND.fields_by_name['to_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSEND.fields_by_name['amount']._options = None
    _MSGSEND.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01'
    _MSGSEND._options = None
    _MSGSEND._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x0cfrom_address\x8a\xe7\xb0*\x12cosmos-sdk/MsgSend'
    _MSGMULTISEND.fields_by_name['inputs']._options = None
    _MSGMULTISEND.fields_by_name['inputs']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGMULTISEND.fields_by_name['outputs']._options = None
    _MSGMULTISEND.fields_by_name['outputs']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGMULTISEND._options = None
    _MSGMULTISEND._serialized_options = b'\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06inputs\x8a\xe7\xb0*\x17cosmos-sdk/MsgMultiSend'
    _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
    _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEPARAMS.fields_by_name['params']._options = None
    _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGUPDATEPARAMS._options = None
    _MSGUPDATEPARAMS._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/bank/MsgUpdateParams'
    _MSGSETSENDENABLED.fields_by_name['authority']._options = None
    _MSGSETSENDENABLED.fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSETSENDENABLED._options = None
    _MSGSETSENDENABLED._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1ccosmos-sdk/MsgSetSendEnabled'
    _MSG._options = None
    _MSG._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGSEND']._serialized_start = 211
    _globals['_MSGSEND']._serialized_end = 462
    _globals['_MSGSENDRESPONSE']._serialized_start = 464
    _globals['_MSGSENDRESPONSE']._serialized_end = 481
    _globals['_MSGMULTISEND']._serialized_start = 484
    _globals['_MSGMULTISEND']._serialized_end = 655
    _globals['_MSGMULTISENDRESPONSE']._serialized_start = 657
    _globals['_MSGMULTISENDRESPONSE']._serialized_end = 679
    _globals['_MSGUPDATEPARAMS']._serialized_start = 682
    _globals['_MSGUPDATEPARAMS']._serialized_end = 854
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 856
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 881
    _globals['_MSGSETSENDENABLED']._serialized_start = 884
    _globals['_MSGSETSENDENABLED']._serialized_end = 1078
    _globals['_MSGSETSENDENABLEDRESPONSE']._serialized_start = 1080
    _globals['_MSGSETSENDENABLEDRESPONSE']._serialized_end = 1107
    _globals['_MSG']._serialized_start = 1110
    _globals['_MSG']._serialized_end = 1495