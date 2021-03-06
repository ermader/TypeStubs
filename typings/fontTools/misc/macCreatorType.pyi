"""
This type stub file was generated by pyright.
"""

def getMacCreatorAndType(path): # -> tuple[Tag, Tag] | tuple[None, None]:
	"""Returns file creator and file type codes for a path.

	Args:
		path (str): A file path.

	Returns:
		A tuple of two :py:class:`fontTools.textTools.Tag` objects, the first
		representing the file creator and the second representing the
		file type.
	"""
	...

def setMacCreatorAndType(path, fileCreator, fileType): # -> None:
	"""Set file creator and file type codes for a path.

	Note that if the ``xattr`` module is not installed, no action is
	taken but no error is raised.

	Args:
		path (str): A file path.
		fileCreator: A four-character file creator tag.
		fileType: A four-character file type tag.

	"""
	...

