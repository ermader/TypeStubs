"""
This type stub file was generated by pyright.
"""

from . import DefaultTable
from collections import namedtuple

class table_C_P_A_L_(DefaultTable.DefaultTable):
	NO_NAME_ID = ...
	DEFAULT_PALETTE_TYPE = ...
	def __init__(self, tag=...) -> None:
		...
	
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def toXML(self, writer, ttFont):
		...
	
	def fromXML(self, name, attrs, content, ttFont):
		...
	


class Color(namedtuple("Color", "blue green red alpha")):
	def hex(self): # -> str:
		...
	
	def __repr__(self): # -> str:
		...
	
	def toXML(self, writer, ttFont, index=...): # -> None:
		...
	
	@classmethod
	def fromHex(cls, value): # -> Self@Color:
		...
	
	@classmethod
	def fromRGBA(cls, red, green, blue, alpha): # -> Self@Color:
		...
	


