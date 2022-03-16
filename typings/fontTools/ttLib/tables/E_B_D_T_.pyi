"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

log = ...
ebdtTableVersionFormat = ...
ebdtComponentFormat = ...
class table_E_B_D_T_(DefaultTable.DefaultTable):
	locatorName = ...
	def getImageFormatClass(self, imageFormat): # -> Type[ebdt_bitmap_format_1] | Type[ebdt_bitmap_format_2] | Type[ebdt_bitmap_format_5] | Type[ebdt_bitmap_format_6] | Type[ebdt_bitmap_format_7] | Type[ebdt_bitmap_format_8] | Type[ebdt_bitmap_format_9]:
		...
	
	def decompile(self, data, ttFont):
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont):
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class EbdtComponent:
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


_bitmapGlyphSubclassPrefix = ...
class BitmapGlyph:
	fileExtension = ...
	xmlDataFunctions = ...
	def __init__(self, data, ttFont) -> None:
		...
	
	def __getattr__(self, attr): # -> Any:
		...
	
	def getFormat(self): # -> Any:
		...
	
	def toXML(self, strikeIndex, glyphName, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	
	def writeMetrics(self, writer, ttFont): # -> None:
		...
	
	def readMetrics(self, name, attrs, content, ttFont): # -> None:
		...
	
	def writeData(self, strikeIndex, glyphName, writer, ttFont): # -> None:
		...
	
	def readData(self, name, attrs, content, ttFont): # -> None:
		...
	


BitmapPlusBigMetricsMixin = ...
BitmapPlusSmallMetricsMixin = ...
class BitAlignedBitmapMixin:
	def getRow(self, row, bitDepth=..., metrics=..., reverseBytes=...):
		...
	
	def setRows(self, dataRows, bitDepth=..., metrics=..., reverseBytes=...):
		...
	


class ByteAlignedBitmapMixin:
	def getRow(self, row, bitDepth=..., metrics=..., reverseBytes=...): # -> bytes:
		...
	
	def setRows(self, dataRows, bitDepth=..., metrics=..., reverseBytes=...): # -> None:
		...
	


class ebdt_bitmap_format_1(ByteAlignedBitmapMixin, BitmapPlusSmallMetricsMixin, BitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont):
		...
	


class ebdt_bitmap_format_2(BitAlignedBitmapMixin, BitmapPlusSmallMetricsMixin, BitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont):
		...
	


class ebdt_bitmap_format_5(BitAlignedBitmapMixin, BitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont):
		...
	


class ebdt_bitmap_format_6(ByteAlignedBitmapMixin, BitmapPlusBigMetricsMixin, BitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont):
		...
	


class ebdt_bitmap_format_7(BitAlignedBitmapMixin, BitmapPlusBigMetricsMixin, BitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont):
		...
	


class ComponentBitmapGlyph(BitmapGlyph):
	def toXML(self, strikeIndex, glyphName, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont):
		...
	


class ebdt_bitmap_format_8(BitmapPlusSmallMetricsMixin, ComponentBitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	


class ebdt_bitmap_format_9(BitmapPlusBigMetricsMixin, ComponentBitmapGlyph):
	def decompile(self): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	


ebdt_bitmap_classes = ...