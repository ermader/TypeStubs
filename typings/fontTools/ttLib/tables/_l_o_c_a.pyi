"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

log = ...
class table__l_o_c_a(DefaultTable.DefaultTable):
	dependencies = ...
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont):
		...
	
	def set(self, locations): # -> None:
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def __getitem__(self, index): # -> int:
		...
	
	def __len__(self): # -> int:
		...
	


