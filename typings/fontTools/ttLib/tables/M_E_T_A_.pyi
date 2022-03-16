"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

METAHeaderFormat = ...
METAGlyphRecordFormat = ...
METAStringRecordFormat = ...
METALabelDict = ...
def getLabelString(labelID): # -> str:
	...

class table_M_E_T_A_(DefaultTable.DefaultTable):
	dependencies = ...
	def decompile(self, data, ttFont):
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class GlyphRecord:
	def __init__(self) -> None:
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	
	def compile(self, parentTable): # -> bytes:
		...
	
	def __repr__(self): # -> str:
		...
	


def mapXMLToUTF8(string): # -> bytes:
	...

def mapUTF8toXML(string): # -> str:
	...

class StringRecord:
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	
	def compile(self, parentTable): # -> bytes:
		...
	
	def __repr__(self):
		...
	

