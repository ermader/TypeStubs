"""
This type stub file was generated by pyright.
"""

"""fontTools.misc.encodingTools.py -- tools for working with OpenType encodings.
"""
_encodingMap = ...
def getEncoding(platformID, platEncID, langID, default=...): # -> str:
	"""Returns the Python encoding name for OpenType platformID/encodingID/langID
	triplet.  If encoding for these values is not known, by default None is
	returned.  That can be overriden by passing a value to the default argument.
	"""
	...

