# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message_pb2 as message__pb2


class MessagingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.streamingMessage = channel.stream_stream(
                '/MessagingService/streamingMessage',
                request_serializer=message__pb2.StreamingMessageRequest.SerializeToString,
                response_deserializer=message__pb2.StreamingMessageResponse.FromString,
                )


class MessagingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def streamingMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessagingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'streamingMessage': grpc.stream_stream_rpc_method_handler(
                    servicer.streamingMessage,
                    request_deserializer=message__pb2.StreamingMessageRequest.FromString,
                    response_serializer=message__pb2.StreamingMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessagingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessagingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def streamingMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/MessagingService/streamingMessage',
            message__pb2.StreamingMessageRequest.SerializeToString,
            message__pb2.StreamingMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)