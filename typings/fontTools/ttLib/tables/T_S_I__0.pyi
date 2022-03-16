"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

""" TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT)
tool to store its hinting source data.

TSI0 is the index table containing the lengths and offsets for the glyph
programs and 'extra' programs ('fpgm', 'prep', and 'cvt') that are contained
in the TSI1 table.
"""
tsi0Format = ...
def fixlongs(glyphID, textLength, textOffset): # -> tuple[int, int, Unknown]:
	...

class table_T_S_I__0(DefaultTable.DefaultTable):
	dependencies = ...
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def set(self, indices, extra_indices): # -> None:
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	


