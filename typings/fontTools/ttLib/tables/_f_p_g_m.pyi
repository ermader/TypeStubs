"""
This type stub file was generated by pyright.
"""

from . import DefaultTable

class table__f_p_g_m(DefaultTable.DefaultTable):
	def decompile(self, data, ttFont): # -> None:
		...
	
	def compile(self, ttFont): # -> bytes:
		...
	
	def toXML(self, writer, ttFont): # -> None:
		...
	
	def fromXML(self, name, attrs, content, ttFont): # -> None:
		...
	
	def __bool__(self): # -> bool:
		"""
		>>> fpgm = table__f_p_g_m()
		>>> bool(fpgm)
		False
		>>> p = ttProgram.Program()
		>>> fpgm.program = p
		>>> bool(fpgm)
		False
		>>> bc = bytearray([0])
		>>> p.fromBytecode(bc)
		>>> bool(fpgm)
		True
		>>> p.bytecode.pop()
		0
		>>> bool(fpgm)
		False
		"""
		...
	
	__nonzero__ = ...


if __name__ == "__main__":
	...