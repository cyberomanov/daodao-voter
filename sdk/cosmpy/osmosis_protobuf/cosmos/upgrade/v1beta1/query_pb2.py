"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/upgrade/v1beta1/query.proto\x12\x16cosmos.upgrade.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto"\x19\n\x17QueryCurrentPlanRequest"F\n\x18QueryCurrentPlanResponse\x12*\n\x04plan\x18\x01 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.Plan"\'\n\x17QueryAppliedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"*\n\x18QueryAppliedPlanResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03"=\n"QueryUpgradedConsensusStateRequest\x12\x13\n\x0blast_height\x18\x01 \x01(\x03:\x02\x18\x01"Q\n#QueryUpgradedConsensusStateResponse\x12 \n\x18upgraded_consensus_state\x18\x02 \x01(\x0c:\x02\x18\x01J\x04\x08\x01\x10\x02"1\n\x1aQueryModuleVersionsRequest\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t"]\n\x1bQueryModuleVersionsResponse\x12>\n\x0fmodule_versions\x18\x01 \x03(\x0b2%.cosmos.upgrade.v1beta1.ModuleVersion"\x17\n\x15QueryAuthorityRequest")\n\x16QueryAuthorityResponse\x12\x0f\n\x07address\x18\x01 \x01(\t2\xf4\x06\n\x05Query\x12\x9e\x01\n\x0bCurrentPlan\x12/.cosmos.upgrade.v1beta1.QueryCurrentPlanRequest\x1a0.cosmos.upgrade.v1beta1.QueryCurrentPlanResponse",\x82\xd3\xe4\x93\x02&\x12$/cosmos/upgrade/v1beta1/current_plan\x12\xa5\x01\n\x0bAppliedPlan\x12/.cosmos.upgrade.v1beta1.QueryAppliedPlanRequest\x1a0.cosmos.upgrade.v1beta1.QueryAppliedPlanResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/upgrade/v1beta1/applied_plan/{name}\x12\xdc\x01\n\x16UpgradedConsensusState\x12:.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateRequest\x1a;.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateResponse"I\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}\x12\xaa\x01\n\x0eModuleVersions\x122.cosmos.upgrade.v1beta1.QueryModuleVersionsRequest\x1a3.cosmos.upgrade.v1beta1.QueryModuleVersionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/upgrade/v1beta1/module_versions\x12\x95\x01\n\tAuthority\x12-.cosmos.upgrade.v1beta1.QueryAuthorityRequest\x1a..cosmos.upgrade.v1beta1.QueryAuthorityResponse")\x82\xd3\xe4\x93\x02#\x12!/cosmos/upgrade/v1beta1/authorityB.Z,github.com/cosmos/cosmos-sdk/x/upgrade/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types'
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._options = None
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_options = b'\x18\x01'
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._options = None
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_options = b'\x18\x01'
    _QUERY.methods_by_name['CurrentPlan']._options = None
    _QUERY.methods_by_name['CurrentPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/cosmos/upgrade/v1beta1/current_plan'
    _QUERY.methods_by_name['AppliedPlan']._options = None
    _QUERY.methods_by_name['AppliedPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/upgrade/v1beta1/applied_plan/{name}'
    _QUERY.methods_by_name['UpgradedConsensusState']._options = None
    _QUERY.methods_by_name['UpgradedConsensusState']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}'
    _QUERY.methods_by_name['ModuleVersions']._options = None
    _QUERY.methods_by_name['ModuleVersions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/upgrade/v1beta1/module_versions"
    _QUERY.methods_by_name['Authority']._options = None
    _QUERY.methods_by_name['Authority']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/cosmos/upgrade/v1beta1/authority'
    _globals['_QUERYCURRENTPLANREQUEST']._serialized_start = 130
    _globals['_QUERYCURRENTPLANREQUEST']._serialized_end = 155
    _globals['_QUERYCURRENTPLANRESPONSE']._serialized_start = 157
    _globals['_QUERYCURRENTPLANRESPONSE']._serialized_end = 227
    _globals['_QUERYAPPLIEDPLANREQUEST']._serialized_start = 229
    _globals['_QUERYAPPLIEDPLANREQUEST']._serialized_end = 268
    _globals['_QUERYAPPLIEDPLANRESPONSE']._serialized_start = 270
    _globals['_QUERYAPPLIEDPLANRESPONSE']._serialized_end = 312
    _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_start = 314
    _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_end = 375
    _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_start = 377
    _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_end = 458
    _globals['_QUERYMODULEVERSIONSREQUEST']._serialized_start = 460
    _globals['_QUERYMODULEVERSIONSREQUEST']._serialized_end = 509
    _globals['_QUERYMODULEVERSIONSRESPONSE']._serialized_start = 511
    _globals['_QUERYMODULEVERSIONSRESPONSE']._serialized_end = 604
    _globals['_QUERYAUTHORITYREQUEST']._serialized_start = 606
    _globals['_QUERYAUTHORITYREQUEST']._serialized_end = 629
    _globals['_QUERYAUTHORITYRESPONSE']._serialized_start = 631
    _globals['_QUERYAUTHORITYRESPONSE']._serialized_end = 672
    _globals['_QUERY']._serialized_start = 675
    _globals['_QUERY']._serialized_end = 1559