# M42PL - Data encoders and decoders

M42PL encoders provides support for events _casting_ from and to foreign
data formats such as `JSON`, `MessagePack`, `BSON`, etc.

## Installation

```shell
git clone https://github.com/jpclipffel/m42pl-encoders
pip install m42pl-encoders
```

## Encoders list

| Aliases   | Module        | Description                                     |
|-----------|---------------|-------------------------------------------------|
| `json`    | `_json.py`    | Encodes to and decodes from JSON strings        |
| `msgpack` | `_msgpack.py` | Encodes to and decodes from MsgPack bytes array |
