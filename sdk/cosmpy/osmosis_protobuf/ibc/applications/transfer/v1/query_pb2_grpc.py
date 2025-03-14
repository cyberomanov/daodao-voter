"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....ibc.applications.transfer.v1 import query_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DenomTrace = channel.unary_unary('/ibc.applications.transfer.v1.Query/DenomTrace', request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.FromString)
        self.DenomTraces = channel.unary_unary('/ibc.applications.transfer.v1.Query/DenomTraces', request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.FromString)
        self.Params = channel.unary_unary('/ibc.applications.transfer.v1.Query/Params', request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.DenomHash = channel.unary_unary('/ibc.applications.transfer.v1.Query/DenomHash', request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.FromString)
        self.EscrowAddress = channel.unary_unary('/ibc.applications.transfer.v1.Query/EscrowAddress', request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.SerializeToString, response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service.
    """

    def DenomTrace(self, request, context):
        """DenomTrace queries a denomination trace information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomTraces(self, request, context):
        """DenomTraces queries all denomination traces.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters of the ibc-transfer module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomHash(self, request, context):
        """DenomHash queries a denomination hash information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EscrowAddress(self, request, context):
        """EscrowAddress returns the escrow address for a particular port and channel id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'DenomTrace': grpc.unary_unary_rpc_method_handler(servicer.DenomTrace, request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.FromString, response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.SerializeToString), 'DenomTraces': grpc.unary_unary_rpc_method_handler(servicer.DenomTraces, request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.FromString, response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'DenomHash': grpc.unary_unary_rpc_method_handler(servicer.DenomHash, request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.FromString, response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.SerializeToString), 'EscrowAddress': grpc.unary_unary_rpc_method_handler(servicer.EscrowAddress, request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.FromString, response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ibc.applications.transfer.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service.
    """

    @staticmethod
    def DenomTrace(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Query/DenomTrace', ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.SerializeToString, ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomTraces(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Query/DenomTraces', ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.SerializeToString, ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Query/Params', ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomHash(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Query/DenomHash', ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.SerializeToString, ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EscrowAddress(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.applications.transfer.v1.Query/EscrowAddress', ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.SerializeToString, ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)