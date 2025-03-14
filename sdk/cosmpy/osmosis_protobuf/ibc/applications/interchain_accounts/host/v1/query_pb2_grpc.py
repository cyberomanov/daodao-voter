"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ......ibc.applications.interchain_accounts.host.v1 import query_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/ibc.applications.interchain_accounts.host.v1.Query/Params', request_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params queries all parameters of the ICA host submodule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ibc.applications.interchain_accounts.host.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service.
    """

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.interchain_accounts.host.v1.Query/Params', ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)