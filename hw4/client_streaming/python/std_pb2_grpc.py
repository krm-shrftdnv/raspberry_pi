# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import std_pb2 as std__pb2


class StandardDeviationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StandardDeviation = channel.stream_unary(
                '/StandardDeviation/StandardDeviation',
                request_serializer=std__pb2.Number.SerializeToString,
                response_deserializer=std__pb2.Number.FromString,
                )


class StandardDeviationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StandardDeviation(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StandardDeviationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StandardDeviation': grpc.stream_unary_rpc_method_handler(
                    servicer.StandardDeviation,
                    request_deserializer=std__pb2.Number.FromString,
                    response_serializer=std__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'StandardDeviation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StandardDeviation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StandardDeviation(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/StandardDeviation/StandardDeviation',
            std__pb2.Number.SerializeToString,
            std__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
