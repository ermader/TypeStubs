"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

log = ...
postFormat = ...
postFormatSize = ...
class table__p_o_s_t(DefaultTable.DefaultTable):
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def getGlyphOrder(self): # -> list[str] | None:
		"""This function will get called by a ttLib.TTFont instance.
		Do not call this function yourself, use TTFont().getGlyphOrder()
		or its relatives instead!
		"""
		...
	
	def decode_format_1_0(self, data, ttFont): # -> None:
		...
	
	def decode_format_2_0(self, data, ttFont):
		...
	
	def build_psNameMapping(self, ttFont):
		...
	
	def decode_format_3_0(self, data, ttFont): # -> None:
		...
	
	def decode_format_4_0(self, data, ttFont): # -> None:
		...
	
	def encode_format_2_0(self, ttFont):
		...
	
	def encode_format_4_0(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont):
		...
	


def unpackPStrings(data, n): # -> list[Unknown]:
	...

def packPStrings(strings): # -> bytes:
	...
