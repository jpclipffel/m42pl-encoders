from m42pl.encoders import Encoder


class Raw(Encoder):
    """Encode data as a string.

    One should probably **not** use this encoder, as it relies
    only on Python's `str` type (and thus on `__str__` and `__repr__`).

    TODO: Remove this encoder ?
    """

    _aliases_ = ['raw',]

    def _encode(self, data):
        return str(data)
