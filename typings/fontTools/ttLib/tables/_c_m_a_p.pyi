"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

log = ...
class table__c_m_a_p(DefaultTable.DefaultTable):
	"""Character to Glyph Index Mapping Table

	This class represents the `cmap <https://docs.microsoft.com/en-us/typography/opentype/spec/cmap>`_
	table, which maps between input characters (in Unicode or other system encodings)
	and glyphs within the font. The ``cmap`` table contains one or more subtables
	which determine the mapping of of characters to glyphs across different platforms
	and encoding systems.

	``table__c_m_a_p`` objects expose an accessor ``.tables`` which provides access
	to the subtables, although it is normally easier to retrieve individual subtables
	through the utility methods described below. To add new subtables to a font,
	first determine the subtable format (if in doubt use format 4 for glyphs within
	the BMP, format 12 for glyphs outside the BMP, and format 14 for Unicode Variation
	Sequences) construct subtable objects with ``CmapSubtable.newSubtable(format)``,
	and append them to the ``.tables`` list.

	Within a subtable, the mapping of characters to glyphs is provided by the ``.cmap``
	attribute.

	Example::

		cmap4_0_3 = CmapSubtable.newSubtable(4)
		cmap4_0_3.platformID = 0
		cmap4_0_3.platEncID = 3
		cmap4_0_3.language = 0
		cmap4_0_3.cmap = { 0xC1: "Aacute" }

		cmap = newTable("cmap")
		cmap.tableVersion = 0
		cmap.tables = [cmap4_0_3]
	"""
	def getcmap(self, platformID, platEncID): # -> None:
		"""Returns the first subtable which matches the given platform and encoding.

		Args:
			platformID (int): The platform ID. Use 0 for Unicode, 1 for Macintosh
				(deprecated for new fonts), 2 for ISO (deprecated) and 3 for Windows.
			encodingID (int): Encoding ID. Interpretation depends on the platform ID.
				See the OpenType specification for details.

		Returns:
			An object which is a subclass of :py:class:`CmapSubtable` if a matching
			subtable is found within the font, or ``None`` otherwise.
		"""
		...
	
	def getBestCmap(self, cmapPreferences=...): # -> None:
		"""Returns the 'best' Unicode cmap dictionary available in the font
		or ``None``, if no Unicode cmap subtable is available.

		By default it will search for the following (platformID, platEncID)
		pairs in order::

				(3, 10), # Windows Unicode full repertoire
				(0, 6),  # Unicode full repertoire (format 13 subtable)
				(0, 4),  # Unicode 2.0 full repertoire
				(3, 1),  # Windows Unicode BMP
				(0, 3),  # Unicode 2.0 BMP
				(0, 2),  # Unicode ISO/IEC 10646
				(0, 1),  # Unicode 1.1
				(0, 0)   # Unicode 1.0

		This order can be customized via the ``cmapPreferences`` argument.
		"""
		...
	
	def buildReversed(self): # -> dict[Unknown, Unknown]:
		"""Builds a reverse mapping dictionary

		Iterates over all Unicode cmap tables and returns a dictionary mapping
		glyphs to sets of codepoints, such as::

			{
				'one': {0x31}
				'A': {0x41,0x391}
			}

		The values are sets of Unicode codepoints because
		some fonts map different codepoints to the same glyph.
		For example, ``U+0041 LATIN CAPITAL LETTER A`` and ``U+0391
		GREEK CAPITAL LETTER ALPHA`` are sometimes the same glyph.
		"""
		...
	
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class CmapSubtable:
	"""Base class for all cmap subtable formats.

	Subclasses which handle the individual subtable formats are named
	``cmap_format_0``, ``cmap_format_2`` etc. Use :py:meth:`getSubtableClass`
	to retrieve the concrete subclass, or :py:meth:`newSubtable` to get a
	new subtable object for a given format.

	The object exposes a ``.cmap`` attribute, which contains a dictionary mapping
	character codepoints to glyph names.
	"""
	@staticmethod
	def getSubtableClass(format): # -> Type[cmap_format_0] | Type[cmap_format_2] | Type[cmap_format_4] | Type[cmap_format_6] | Type[cmap_format_12] | Type[cmap_format_13] | Type[cmap_format_14] | Type[cmap_format_unknown]:
		"""Return the subtable class for a format."""
		...
	
	@staticmethod
	def newSubtable(format): # -> cmap_format_0 | cmap_format_2 | cmap_format_4 | cmap_format_6 | cmap_format_12 | cmap_format_13 | cmap_format_14 | cmap_format_unknown:
		"""Return a new instance of a subtable for the given format
		."""
		...
	
	def __init__(self, format) -> None:
		...
	
	def __getattr__(self, attr): # -> Any:
		...
	
	def decompileHeader(self, data, ttFont): # -> None:
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def getEncoding(self, default=...): # -> str:
		"""Returns the Python encoding name for this cmap subtable based on its platformID,
		platEncID, and language.  If encoding for these values is not known, by default
		``None`` is returned.  That can be overridden by passing a value to the ``default``
		argument.

		Note that if you want to choose a "preferred" cmap subtable, most of the time
		``self.isUnicode()`` is what you want as that one only returns true for the modern,
		commonly used, Unicode-compatible triplets, not the legacy ones.
		"""
		...
	
	def isUnicode(self): # -> bool:
		"""Returns true if the characters are interpreted as Unicode codepoints."""
		...
	
	def isSymbol(self): # -> bool:
		"""Returns true if the subtable is for the Symbol encoding (3,0)"""
		...
	
	def __lt__(self, other) -> bool:
		...
	


class cmap_format_0(CmapSubtable):
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


subHeaderFormat = ...
class SubHeader:
	def __init__(self) -> None:
		...
	


class cmap_format_2(CmapSubtable):
	def setIDDelta(self, subHeader):
		...
	
	def decompile(self, data, ttFont):
		...
	
	def compile(self, ttFont):
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


cmap_format_4_format = ...
def splitRange(startCode, endCode, cmap):
	...

class cmap_format_4(CmapSubtable):
	def decompile(self, data, ttFont):
		...
	
	def compile(self, ttFont):
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class cmap_format_6(CmapSubtable):
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class cmap_format_12_or_13(CmapSubtable):
	def __init__(self, format) -> None:
		...
	
	def decompileHeader(self, data, ttFont): # -> None:
		...
	
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class cmap_format_12(cmap_format_12_or_13):
	_format_step = ...
	def __init__(self, format=...) -> None:
		...
	


class cmap_format_13(cmap_format_12_or_13):
	_format_step = ...
	def __init__(self, format=...) -> None:
		...
	


def cvtToUVS(threeByteString): # -> Any:
	...

def cvtFromUVS(val): # -> bytes:
	...

class cmap_format_14(CmapSubtable):
	def decompileHeader(self, data, ttFont): # -> None:
		...
	
	def decompile(self, data, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont):
		...
	
	def compile(self, ttFont):
		...
	


class cmap_format_unknown(CmapSubtable):
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	
	def decompileHeader(self, data, ttFont): # -> None:
		...
	
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes | None:
		...
	


cmap_classes = ...
