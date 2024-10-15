# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import natural_join_pb2 as natural__join__pb2


class MasterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
            '/Master/Register',
            request_serializer=natural__join__pb2.Empty.SerializeToString,
            response_deserializer=natural__join__pb2.RegisterResponse.FromString,
        )
        self.Start = channel.unary_unary(
            '/Master/Start',
            request_serializer=natural__join__pb2.Empty.SerializeToString,
            response_deserializer=natural__join__pb2.Empty.FromString,
        )


class MasterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Register': grpc.unary_unary_rpc_method_handler(
            servicer.Register,
            request_deserializer=natural__join__pb2.Empty.FromString,
            response_serializer=natural__join__pb2.RegisterResponse.SerializeToString,
        ),
        'Start': grpc.unary_unary_rpc_method_handler(
            servicer.Start,
            request_deserializer=natural__join__pb2.Empty.FromString,
            response_serializer=natural__join__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Master', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Master(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Master/Register',
                                             natural__join__pb2.Empty.SerializeToString,
                                             natural__join__pb2.RegisterResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Start(request,
              target,
              options=(),
              channel_credentials=None,
              call_credentials=None,
              insecure=False,
              compression=None,
              wait_for_ready=None,
              timeout=None,
              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Master/Start',
                                             natural__join__pb2.Empty.SerializeToString,
                                             natural__join__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MapperStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Map = channel.unary_unary(
            '/Mapper/Map',
            request_serializer=natural__join__pb2.ProcessRequest.SerializeToString,
            response_deserializer=natural__join__pb2.Empty.FromString,
        )


class MapperServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Map(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Map': grpc.unary_unary_rpc_method_handler(
            servicer.Map,
            request_deserializer=natural__join__pb2.ProcessRequest.FromString,
            response_serializer=natural__join__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Mapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Mapper(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Map(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mapper/Map',
                                             natural__join__pb2.ProcessRequest.SerializeToString,
                                             natural__join__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ReducerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Partition = channel.unary_unary(
            '/Reducer/Partition',
            request_serializer=natural__join__pb2.Empty.SerializeToString,
            response_deserializer=natural__join__pb2.Empty.FromString,
        )
        self.Reduce = channel.unary_unary(
            '/Reducer/Reduce',
            request_serializer=natural__join__pb2.Empty.SerializeToString,
            response_deserializer=natural__join__pb2.Empty.FromString,
        )


class ReducerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Partition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reduce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReducerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Partition': grpc.unary_unary_rpc_method_handler(
            servicer.Partition,
            request_deserializer=natural__join__pb2.Empty.FromString,
            response_serializer=natural__join__pb2.Empty.SerializeToString,
        ),
        'Reduce': grpc.unary_unary_rpc_method_handler(
            servicer.Reduce,
            request_deserializer=natural__join__pb2.Empty.FromString,
            response_serializer=natural__join__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Reducer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Reducer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Partition(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reducer/Partition',
                                             natural__join__pb2.Empty.SerializeToString,
                                             natural__join__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reduce(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Reducer/Reduce',
                                             natural__join__pb2.Empty.SerializeToString,
                                             natural__join__pb2.Empty.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
