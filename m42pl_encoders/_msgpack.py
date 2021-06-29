import msgpack
import msgpack_numpy as m
m.patch()

from m42pl.encoders import Encoder


class MsgPack(Encoder):
    """Encodes events as MessagePack bytes array.
    """

    _aliases_ = ['msgpack',]

    def _encode(self, data):
        return msgpack.packb(data)

    def _decode(self, data):
        return msgpack.unpackb(data)
