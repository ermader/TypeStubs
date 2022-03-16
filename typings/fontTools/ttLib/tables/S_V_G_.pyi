"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

"""Compiles/decompiles SVG table.

https://docs.microsoft.com/en-us/typography/opentype/spec/svg

The XML format is:

.. code-block:: xml

	<SVG>
		<svgDoc endGlyphID="1" startGlyphID="1">
			<![CDATA[ <complete SVG doc> ]]
		</svgDoc>
	...
		<svgDoc endGlyphID="n" startGlyphID="m">
			<![CDATA[ <complete SVG doc> ]]
		</svgDoc>
	</SVG>
"""
log = ...
SVG_format_0 = ...
SVG_format_0Size = ...
doc_index_entry_format_0 = ...
doc_index_entry_format_0Size = ...
class table_S_V_G_(DefaultTable.DefaultTable):
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont):
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	


class DocumentIndexEntry:
	def __init__(self) -> None:
		...
	
	def __repr__(self): # -> str:
		...
	


