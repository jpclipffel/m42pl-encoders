import json
from functools import partial
# pylint: disable=no-name-in-module
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from m42pl.encoders import Encoder


class Json(Encoder):
    """Encodes data as JSON string.
    """

    _aliases_ = ['json',]

    class _Encoder(json.JSONEncoder):
        """JSON encoder for :class:`Event`.
        """

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
        def default(self, o):
            if isinstance(o, (set, tuple)):
                return list(o)
            return {
                'type': str(type(o)),
                'repr': str(repr(o)),
                'info': 'Data type not suitable for "json" formatter'
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._encoder = partial(
            json.dumps,
            *args, 
            **{
                **kwargs,
                **{'cls': self._Encoder}
            }
        )
        self._decoder = json.loads

    def _encode(self, data):
        return self._encoder(data)

    def _decode(self, data):
        return self._decoder(data)


class HJson(Json):
    """Encodes data as highlighted JSON string.
    """

    _aliases_ = ['hjson',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lexer = JsonLexer()
        self.formatter = TerminalFormatter()

    def _encode(self, data):
        return highlight(
            super()._encode(data),
            self.lexer,
            self.formatter
        )
