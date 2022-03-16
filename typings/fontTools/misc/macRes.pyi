"""
This type stub file was generated by pyright.
"""

from collections.abc import MutableMapping

class ResourceError(Exception):
	...


class ResourceReader(MutableMapping):
	"""Reader for Mac OS resource forks.

	Parses a resource fork and returns resources according to their type.
	If run on OS X, this will open the resource fork in the filesystem.
	Otherwise, it will open the file itself and attempt to read it as
	though it were a resource fork.

	The returned object can be indexed by type and iterated over,
	returning in each case a list of py:class:`Resource` objects
	representing all the resources of a certain type.

	"""
	def __init__(self, fileOrPath) -> None:
		"""Open a file

		Args:
			fileOrPath: Either an object supporting a ``read`` method, an
				``os.PathLike`` object, or a string.
		"""
		...
	
	@staticmethod
	def openResourceFork(path): # -> BytesIO:
		...
	
	@staticmethod
	def openDataFork(path): # -> BytesIO:
		...
	
	def __getitem__(self, resType):
		...
	
	def __delitem__(self, resType): # -> None:
		...
	
	def __setitem__(self, resType, resources): # -> None:
		...
	
	def __len__(self): # -> int:
		...
	
	def __iter__(self): # -> Iterator[Unknown]:
		...
	
	def keys(self): # -> _OrderedDictKeysView[Unknown, Unknown]:
		...
	
	@property
	def types(self): # -> list[Unknown]:
		"""A list of the types of resources in the resource fork."""
		...
	
	def countResources(self, resType): # -> int:
		"""Return the number of resources of a given type."""
		...
	
	def getIndices(self, resType): # -> list[int]:
		"""Returns a list of indices of resources of a given type."""
		...
	
	def getNames(self, resType): # -> list[Unknown | Any]:
		"""Return list of names of all resources of a given type."""
		...
	
	def getIndResource(self, resType, index): # -> None:
		"""Return resource of given type located at an index ranging from 1
		to the number of resources for that type, or None if not found.
		"""
		...
	
	def getNamedResource(self, resType, name): # -> Any | None:
		"""Return the named resource of given type, else return None."""
		...
	
	def close(self): # -> None:
		...
	


class Resource:
	"""Represents a resource stored within a resource fork.

	Attributes:
		type: resource type.
		data: resource data.
		id: ID.
		name: resource name.
		attr: attributes.
	"""
	def __init__(self, resType=..., resData=..., resID=..., resName=..., resAttr=...) -> None:
		...
	
	def decompile(self, refData, reader): # -> None:
		...
	


ResourceForkHeader = ...
ResourceForkHeaderSize = ...
ResourceMapHeader = ...
ResourceMapHeaderSize = ...
ResourceTypeItem = ...
ResourceTypeItemSize = ...
ResourceRefItem = ...
ResourceRefItemSize = ...
