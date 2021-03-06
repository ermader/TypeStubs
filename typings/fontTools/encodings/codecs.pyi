"""
This type stub file was generated by pyright.
"""

import codecs

"""Extend the Python codecs module with a few encodings that are used in OpenType (name table)
but missing from Python.  See https://github.com/fonttools/fonttools/issues/236 for details."""
class ExtendCodec(codecs.Codec):
	def __init__(self, name, base_encoding, mapping) -> None:
		...
	
	def encode(self, input, errors=...): # -> tuple[bytes, int]:
		...
	
	def decode(self, input, errors=...): # -> tuple[Unknown | str, int]:
		...
	
	def error(self, e): # -> tuple[Unknown, int]:
		...
	


_extended_encodings = ...
_cache = ...
def search_function(name): # -> None:
	...

