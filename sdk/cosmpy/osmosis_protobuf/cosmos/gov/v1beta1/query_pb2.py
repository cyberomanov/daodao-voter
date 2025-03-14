"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/gov/v1beta1/query.proto\x12\x12cosmos.gov.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ccosmos/gov/v1beta1/gov.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x11amino/amino.proto"+\n\x14QueryProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"R\n\x15QueryProposalResponse\x129\n\x08proposal\x18\x01 \x01(\x0b2\x1c.cosmos.gov.v1beta1.ProposalB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\xf0\x01\n\x15QueryProposalsRequest\x12;\n\x0fproposal_status\x18\x01 \x01(\x0e2".cosmos.gov.v1beta1.ProposalStatus\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12+\n\tdepositor\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x91\x01\n\x16QueryProposalsResponse\x12:\n\tproposals\x18\x01 \x03(\x0b2\x1c.cosmos.gov.v1beta1.ProposalB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Z\n\x10QueryVoteRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"F\n\x11QueryVoteResponse\x121\n\x04vote\x18\x01 \x01(\x0b2\x18.cosmos.gov.v1beta1.VoteB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"d\n\x11QueryVotesRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x85\x01\n\x12QueryVotesResponse\x122\n\x05votes\x18\x01 \x03(\x0b2\x18.cosmos.gov.v1beta1.VoteB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse")\n\x12QueryParamsRequest\x12\x13\n\x0bparams_type\x18\x01 \x01(\t"\xe1\x01\n\x13QueryParamsResponse\x12B\n\rvoting_params\x18\x01 \x01(\x0b2 .cosmos.gov.v1beta1.VotingParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12D\n\x0edeposit_params\x18\x02 \x01(\x0b2!.cosmos.gov.v1beta1.DepositParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12@\n\x0ctally_params\x18\x03 \x01(\x0b2\x1f.cosmos.gov.v1beta1.TallyParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"a\n\x13QueryDepositRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"O\n\x14QueryDepositResponse\x127\n\x07deposit\x18\x01 \x01(\x0b2\x1b.cosmos.gov.v1beta1.DepositB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"g\n\x14QueryDepositsRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8e\x01\n\x15QueryDepositsResponse\x128\n\x08deposits\x18\x01 \x03(\x0b2\x1b.cosmos.gov.v1beta1.DepositB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse".\n\x17QueryTallyResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04"U\n\x18QueryTallyResultResponse\x129\n\x05tally\x18\x01 \x01(\x0b2\x1f.cosmos.gov.v1beta1.TallyResultB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x012\xd4\t\n\x05Query\x12\x94\x01\n\x08Proposal\x12(.cosmos.gov.v1beta1.QueryProposalRequest\x1a).cosmos.gov.v1beta1.QueryProposalResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/gov/v1beta1/proposals/{proposal_id}\x12\x89\x01\n\tProposals\x12).cosmos.gov.v1beta1.QueryProposalsRequest\x1a*.cosmos.gov.v1beta1.QueryProposalsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/gov/v1beta1/proposals\x12\x96\x01\n\x04Vote\x12$.cosmos.gov.v1beta1.QueryVoteRequest\x1a%.cosmos.gov.v1beta1.QueryVoteResponse"A\x82\xd3\xe4\x93\x02;\x129/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}\x12\x91\x01\n\x05Votes\x12%.cosmos.gov.v1beta1.QueryVotesRequest\x1a&.cosmos.gov.v1beta1.QueryVotesResponse"9\x82\xd3\xe4\x93\x023\x121/cosmos/gov/v1beta1/proposals/{proposal_id}/votes\x12\x8b\x01\n\x06Params\x12&.cosmos.gov.v1beta1.QueryParamsRequest\x1a\'.cosmos.gov.v1beta1.QueryParamsResponse"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/gov/v1beta1/params/{params_type}\x12\xa6\x01\n\x07Deposit\x12\'.cosmos.gov.v1beta1.QueryDepositRequest\x1a(.cosmos.gov.v1beta1.QueryDepositResponse"H\x82\xd3\xe4\x93\x02B\x12@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}\x12\x9d\x01\n\x08Deposits\x12(.cosmos.gov.v1beta1.QueryDepositsRequest\x1a).cosmos.gov.v1beta1.QueryDepositsResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits\x12\xa3\x01\n\x0bTallyResult\x12+.cosmos.gov.v1beta1.QueryTallyResultRequest\x1a,.cosmos.gov.v1beta1.QueryTallyResultResponse"9\x82\xd3\xe4\x93\x023\x121/cosmos/gov/v1beta1/proposals/{proposal_id}/tallyB2Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1'
    _QUERYPROPOSALRESPONSE.fields_by_name['proposal']._options = None
    _QUERYPROPOSALRESPONSE.fields_by_name['proposal']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYPROPOSALSREQUEST.fields_by_name['voter']._options = None
    _QUERYPROPOSALSREQUEST.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._options = None
    _QUERYPROPOSALSREQUEST.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYPROPOSALSREQUEST._options = None
    _QUERYPROPOSALSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYPROPOSALSRESPONSE.fields_by_name['proposals']._options = None
    _QUERYPROPOSALSRESPONSE.fields_by_name['proposals']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYVOTEREQUEST.fields_by_name['voter']._options = None
    _QUERYVOTEREQUEST.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYVOTEREQUEST._options = None
    _QUERYVOTEREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYVOTERESPONSE.fields_by_name['vote']._options = None
    _QUERYVOTERESPONSE.fields_by_name['vote']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYVOTESRESPONSE.fields_by_name['votes']._options = None
    _QUERYVOTESRESPONSE.fields_by_name['votes']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYPARAMSRESPONSE.fields_by_name['voting_params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['voting_params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYPARAMSRESPONSE.fields_by_name['deposit_params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['deposit_params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYPARAMSRESPONSE.fields_by_name['tally_params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['tally_params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYDEPOSITREQUEST.fields_by_name['depositor']._options = None
    _QUERYDEPOSITREQUEST.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYDEPOSITREQUEST._options = None
    _QUERYDEPOSITREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYDEPOSITRESPONSE.fields_by_name['deposit']._options = None
    _QUERYDEPOSITRESPONSE.fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYDEPOSITSRESPONSE.fields_by_name['deposits']._options = None
    _QUERYDEPOSITSRESPONSE.fields_by_name['deposits']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._options = None
    _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _QUERY.methods_by_name['Proposal']._options = None
    _QUERY.methods_by_name['Proposal']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/gov/v1beta1/proposals/{proposal_id}'
    _QUERY.methods_by_name['Proposals']._options = None
    _QUERY.methods_by_name['Proposals']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/gov/v1beta1/proposals'
    _QUERY.methods_by_name['Vote']._options = None
    _QUERY.methods_by_name['Vote']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}'
    _QUERY.methods_by_name['Votes']._options = None
    _QUERY.methods_by_name['Votes']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/cosmos/gov/v1beta1/proposals/{proposal_id}/votes'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/cosmos/gov/v1beta1/params/{params_type}'
    _QUERY.methods_by_name['Deposit']._options = None
    _QUERY.methods_by_name['Deposit']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x12@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}'
    _QUERY.methods_by_name['Deposits']._options = None
    _QUERY.methods_by_name['Deposits']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits'
    _QUERY.methods_by_name['TallyResult']._options = None
    _QUERY.methods_by_name['TallyResult']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/cosmos/gov/v1beta1/proposals/{proposal_id}/tally'
    _globals['_QUERYPROPOSALREQUEST']._serialized_start = 226
    _globals['_QUERYPROPOSALREQUEST']._serialized_end = 269
    _globals['_QUERYPROPOSALRESPONSE']._serialized_start = 271
    _globals['_QUERYPROPOSALRESPONSE']._serialized_end = 353
    _globals['_QUERYPROPOSALSREQUEST']._serialized_start = 356
    _globals['_QUERYPROPOSALSREQUEST']._serialized_end = 596
    _globals['_QUERYPROPOSALSRESPONSE']._serialized_start = 599
    _globals['_QUERYPROPOSALSRESPONSE']._serialized_end = 744
    _globals['_QUERYVOTEREQUEST']._serialized_start = 746
    _globals['_QUERYVOTEREQUEST']._serialized_end = 836
    _globals['_QUERYVOTERESPONSE']._serialized_start = 838
    _globals['_QUERYVOTERESPONSE']._serialized_end = 908
    _globals['_QUERYVOTESREQUEST']._serialized_start = 910
    _globals['_QUERYVOTESREQUEST']._serialized_end = 1010
    _globals['_QUERYVOTESRESPONSE']._serialized_start = 1013
    _globals['_QUERYVOTESRESPONSE']._serialized_end = 1146
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1148
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1189
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1192
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1417
    _globals['_QUERYDEPOSITREQUEST']._serialized_start = 1419
    _globals['_QUERYDEPOSITREQUEST']._serialized_end = 1516
    _globals['_QUERYDEPOSITRESPONSE']._serialized_start = 1518
    _globals['_QUERYDEPOSITRESPONSE']._serialized_end = 1597
    _globals['_QUERYDEPOSITSREQUEST']._serialized_start = 1599
    _globals['_QUERYDEPOSITSREQUEST']._serialized_end = 1702
    _globals['_QUERYDEPOSITSRESPONSE']._serialized_start = 1705
    _globals['_QUERYDEPOSITSRESPONSE']._serialized_end = 1847
    _globals['_QUERYTALLYRESULTREQUEST']._serialized_start = 1849
    _globals['_QUERYTALLYRESULTREQUEST']._serialized_end = 1895
    _globals['_QUERYTALLYRESULTRESPONSE']._serialized_start = 1897
    _globals['_QUERYTALLYRESULTRESPONSE']._serialized_end = 1982
    _globals['_QUERY']._serialized_start = 1985
    _globals['_QUERY']._serialized_end = 3221