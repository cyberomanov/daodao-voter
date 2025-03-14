"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.mint.v1beta1 import query_pb2 as cosmos_dot_mint_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/cosmos.mint.v1beta1.Query/Params', request_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.Inflation = channel.unary_unary('/cosmos.mint.v1beta1.Query/Inflation', request_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationRequest.SerializeToString, response_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationResponse.FromString)
        self.AnnualProvisions = channel.unary_unary('/cosmos.mint.v1beta1.Query/AnnualProvisions', request_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsRequest.SerializeToString, response_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params returns the total set of minting parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Inflation(self, request, context):
        """Inflation returns the current minting inflation value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnnualProvisions(self, request, context):
        """AnnualProvisions current minting annual provisions value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'Inflation': grpc.unary_unary_rpc_method_handler(servicer.Inflation, request_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationRequest.FromString, response_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationResponse.SerializeToString), 'AnnualProvisions': grpc.unary_unary_rpc_method_handler(servicer.AnnualProvisions, request_deserializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsRequest.FromString, response_serializer=cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.mint.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.mint.v1beta1.Query/Params', cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Inflation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.mint.v1beta1.Query/Inflation', cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationRequest.SerializeToString, cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryInflationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnnualProvisions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.mint.v1beta1.Query/AnnualProvisions', cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsRequest.SerializeToString, cosmos_dot_mint_dot_v1beta1_dot_query__pb2.QueryAnnualProvisionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)