"""
This type stub file was generated by pyright.
"""

sbixStrikeHeaderFormat = ...
sbixGlyphDataOffsetFormat = ...
sbixStrikeHeaderFormatSize = ...
sbixGlyphDataOffsetFormatSize = ...
class Strike:
	def __init__(self, rawdata=..., ppem=..., resolution=...) -> None:
		...
	
	def decompile(self, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> None:
		...
	
	def toXML(self, xmlWriter, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont):
		...
	


