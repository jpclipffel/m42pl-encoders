import msgpack

# Some MPL modules (like m42pl-cv) yields NumPy arrays, which are not
# supported out of the box by msgpack.
try:
    import msgpack_numpy as m
    m.patch()
except ImportError:
    pass

from m42pl.encoders import Encoder


class MsgPack(Encoder):
    """Encodes events as MessagePack bytes array.
    """

    _aliases_ = ['msgpack',]
    _about_ = 'Support for MsgPack binary format'

    def _encode(self, data):
        return msgpack.packb(data)

    def _decode(self, data):
        return msgpack.unpackb(data)
