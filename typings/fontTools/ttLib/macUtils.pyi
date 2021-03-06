"""
This type stub file was generated by pyright.
"""

from io import BytesIO

"""ttLib.macUtils.py -- Various Mac-specific stuff."""
def getSFNTResIndices(path): # -> list[int]:
	"""Determine whether a file has a 'sfnt' resource fork or not."""
	...

def openTTFonts(path): # -> list[Unknown]:
	"""Given a pathname, return a list of TTFont objects. In the case
	of a flat TTF/OTF file, the list will contain just one font object;
	but in the case of a Mac font suitcase it will contain as many
	font objects as there are sfnt resources in the file.
	"""
	...

class SFNTResourceReader(BytesIO):
	"""Simple read-only file wrapper for 'sfnt' resources."""
	def __init__(self, path, res_name_or_index) -> None:
		...
	


