"""
This type stub file was generated by pyright.
"""

from . import DefaultTable
from fontTools.misc.loggingTools import LogMixin

""" TSI{0,1,2,3,5} are private tables used by Microsoft Visual TrueType (VTT)
tool to store its hinting source data.

TSI1 contains the text of the glyph programs in the form of low-level assembly
code, as well as the 'extra' programs 'fpgm', 'ppgm' (i.e. 'prep'), and 'cvt'.
"""
class table_T_S_I__1(LogMixin, DefaultTable.DefaultTable):
	extras = ...
	indextable = ...
	def decompile(self, data, ttFont):
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


