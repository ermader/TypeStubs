"""
This type stub file was generated by pyright.
"""

import typing
from io import BufferedReader, BufferedWriter
import logging

log: logging.Logger = ...

class TTFont:
    """Represents a TrueType font.

    The object manages file input and output, and offers a convenient way of
    accessing tables. Tables will be only decompiled when necessary, ie. when
    they're actually accessed. This means that simple operations can be extremely fast.

    Example usage::

            >> from fontTools import ttLib
            >> tt = ttLib.TTFont("afont.ttf") # Load an existing font file
            >> tt['maxp'].numGlyphs
            242
            >> tt['OS/2'].achVendID
            'B&H\000'
            >> tt['head'].unitsPerEm
            2048

    For details of the objects returned when accessing each table, see :ref:`tables`.
    To add a table to the font, use the :py:func:`newTable` function::

            >> os2 = newTable("OS/2")
            >> os2.version = 4
            >> # set other attributes
            >> font["OS/2"] = os2

    TrueType fonts can also be serialized to and from XML format (see also the
    :ref:`ttx` binary)::

            >> tt.saveXML("afont.ttx")
            Dumping 'LTSH' table...
            Dumping 'OS/2' table...
            [...]

            >> tt2 = ttLib.TTFont() # Create a new font object
            >> tt2.importXML("afont.ttx")
            >> tt2['maxp'].numGlyphs
            242

    The TTFont object may be used as a context manager; this will cause the file
    reader to be closed after the context ``with`` block is exited::

            with TTFont(filename) as f:
                    # Do stuff

    Args:
            file: When reading a font from disk, either a pathname pointing to a file,
                    or a readable file object.
            res_name_or_index: If running on a Macintosh, either a sfnt resource name or
                    an sfnt resource index number. If the index number is zero, TTLib will
                    autodetect whether the file is a flat file or a suitcase. (If it is a suitcase,
                    only the first 'sfnt' resource will be read.)
            sfntVersion (str): When constructing a font object from scratch, sets the four-byte
                    sfnt magic number to be used. Defaults to ``\0\1\0\0`` (TrueType). To create
                    an OpenType file, use ``OTTO``.
            flavor (str): Set this to ``woff`` when creating a WOFF file or ``woff2`` for a WOFF2
                    file.
            checkChecksums (int): How checksum data should be treated. Default is 0
                    (no checking). Set to 1 to check and warn on wrong checksums; set to 2 to
                    raise an exception if any wrong checksums are found.
            recalcBBoxes (bool): If true (the default), recalculates ``glyf``, ``CFF ``,
                    ``head`` bounding box values and ``hhea``/``vhea`` min/max values on save.
                    Also compiles the glyphs on importing, which saves memory consumption and
                    time.
            ignoreDecompileErrors (bool): If true, exceptions raised during table decompilation
                    will be ignored, and the binary data will be returned for those tables instead.
            recalcTimestamp (bool): If true (the default), sets the ``modified`` timestamp in
                    the ``head`` table on save.
            fontNumber (int): The index of the font in a TrueType Collection file.
            lazy (bool): If lazy is set to True, many data structures are loaded lazily, upon
                    access only. If it is set to False, many data structures are loaded immediately.
                    The default is ``lazy=None`` which is somewhere in between.
    """

    def __init__(
        self,
        file: typing.Optional[typing.Union[BufferedReader, str]] = ...,
        res_name_or_index: typing.Optional[typing.Union[str, int]] = ...,
        sfntVersion: str = ...,
        flavor: typing.Optional[str] = ...,
        checkChecksums: int = ...,
        verbose: typing.Optional[bool] = ...,
        recalcBBoxes: bool = ...,
        allowVID: bool = ...,
        ignoreDecompileErrors: bool = ...,
        recalcTimestamp: bool = ...,
        fontNumber: int = ...,
        lazy: typing.Optional[bool] = ...,
        quiet: typing.Optional[bool] = ...,
        _tableCache: typing.Optional[dict[str, typing.Any]] = ...,
    ) -> None: ...
    def __enter__(self) -> TTFont: ...
    def __exit__(
        self, type: typing.Any, value: typing.Any, traceback: typing.Any
    ) -> None: ...
    def close(self) -> None:
        """If we still have a reader object, close it."""
        ...
    def save(
        self, file: typing.Union[BufferedWriter, str], reorderTables: bool = ...
    ) -> None:
        """Save the font to disk.

        Args:
                file: Similarly to the constructor, can be either a pathname or a writable
                        file object.
                reorderTables (Option[bool]): If true (the default), reorder the tables,
                        sorting them by tag (recommended by the OpenType specification). If
                        false, retain the original font order. If None, reorder by table
                        dependency (fastest).
        """
        ...
    def saveXML(
        self,
        fileOrPath: typing.Union[BufferedWriter, str],
        newlinestr: str = ...,
        **kwargs: dict[str, typing.Any]
    ) -> None:
        """Export the font as TTX (an XML-based text file), or as a series of text
        files when splitTables is true. In the latter case, the 'fileOrPath'
        argument should be a path to a directory.
        The 'tables' argument must either be false (dump all tables) or a
        list of tables to dump. The 'skipTables' argument may be a list of tables
        to skip, but only when the 'tables' argument is false.
        """
        ...
    def importXML(
        self,
        fileOrPath: typing.Union[BufferedReader, str],
        quiet: typing.Optional[bool] = ...,
    ) -> None:
        """Import a TTX file (an XML-based text format), so as to recreate
        a font object.
        """
        ...
    def isLoaded(self, tag: str) -> bool:
        """Return true if the table identified by ``tag`` has been
        decompiled and loaded into memory."""
        ...
    def has_key(self, tag: str) -> bool:
        """Test if the table identified by ``tag`` is present in the font.

        As well as this method, ``tag in font`` can also be used to determine the
        presence of the table."""
        ...
    __contains__: typing.Callable[[TTFont, str], bool] = ...
    def keys(self) -> list[str]:
        """Returns the list of tables in the font, along with the ``GlyphOrder`` pseudo-table."""
        ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag: str) -> typing.Any: ...
    def __setitem__(self, tag: str, table: typing.Any) -> None: ...
    def __delitem__(self, tag: str) -> None: ...
    def get(
        self, tag: str, default: typing.Optional[typing.Any] = ...
    ) -> typing.Any:  # -> GlyphOrder | Any | DefaultTable:
        """Returns the table if it exists or (optionally) a default if it doesn't."""
        ...
    def setGlyphOrder(self, glyphOrder: list[str]) -> None:
        """Set the glyph order

        Args:
                glyphOrder ([str]): List of glyph names in order.
        """
        ...
    def getGlyphOrder(self) -> list[str]:
        """Returns a list of glyph names ordered by their position in the font."""
        ...
    def getGlyphNames(self) -> list[str]:
        """Get a list of glyph names, sorted alphabetically."""
        ...
    def getGlyphNames2(self) -> list[str]:
        """Get a list of glyph names, sorted alphabetically,
        but not case sensitive.
        """
        ...
    def getGlyphName(self, glyphID: int) -> str:
        """Returns the name for the glyph with the given ID.

        If no name is available, synthesises one with the form ``glyphXXXXX``` where
        ```XXXXX`` is the zero-padded glyph ID.
        """
        ...
    def getGlyphNameMany(self, lst: list[int]) -> list[str]:
        """Converts a list of glyph IDs into a list of glyph names."""
        ...
    def getGlyphID(self, glyphName: str) -> int:
        """Returns the ID of the glyph with the given name."""
        ...
    def getGlyphIDMany(self, lst: list[str]) -> list[int]:
        """Converts a list of glyph names into a list of glyph IDs."""
        ...
    def getReverseGlyphMap(self, rebuild: bool = ...) -> dict[str, int]:
        """Returns a mapping of glyph names to glyph IDs."""
        ...
    def getTableData(self, tag: bytes) -> typing.Any:
        """Returns the binary representation of a table.

        If the table is currently loaded and in memory, the data is compiled to
        binary and returned; if it is not currently loaded, the binary data is
        read from the font file and returned.
        """
        ...
    def getGlyphSet(self, preferCFF: bool = ...) -> dict[str, typing.Any]:
        """Return a generic GlyphSet, which is a dict-like object
        mapping glyph names to glyph objects. The returned glyph objects
        have a .draw() method that supports the Pen protocol, and will
        have an attribute named 'width'.

        If the font is CFF-based, the outlines will be taken from the 'CFF ' or
        'CFF2' tables. Otherwise the outlines will be taken from the 'glyf' table.
        If the font contains both a 'CFF '/'CFF2' and a 'glyf' table, you can use
        the 'preferCFF' argument to specify which one should be taken. If the
        font contains both a 'CFF ' and a 'CFF2' table, the latter is taken.
        """
        ...
    def getBestCmap(
        self, cmapPreferences: tuple[tuple[int, int], ...] = ...
    ) -> dict[int, str]:
        """Return the 'best' unicode cmap dictionary available in the font,
        or None, if no unicode cmap subtable is available.

        By default it will search for the following (platformID, platEncID)
        pairs::

                (3, 10),
                (0, 6),
                (0, 4),
                (3, 1),
                (0, 3),
                (0, 2),
                (0, 1),
                (0, 0)

        This can be customized via the ``cmapPreferences`` argument.
        """
        ...

class _TTGlyphSet:
    """Generic dict-like GlyphSet class that pulls metrics from hmtx and
    glyph shape from TrueType or CFF.
    """

    def __init__(
        self,
        ttFont: TTFont,
        glyphs: dict[str, _TTGlyph],
        glyphType: typing.Union[_TTGlyphCFF, _TTGlyphGlyf],
    ) -> None:
        """Construct a new glyphset.

        Args:
                font (TTFont): The font object (used to get metrics).
                glyphs (dict): A dictionary mapping glyph names to ``_TTGlyph`` objects.
                glyphType (class): Either ``_TTGlyphCFF`` or ``_TTGlyphGlyf``.
        """
        ...
    def keys(self) -> list[str]: ...
    def has_key(self, glyphName: str) -> bool: ...
    def __contains__(self, glyphName: str) -> bool: ...
    def __getitem__(self, glyphName: str) -> _TTGlyph: ...
    def __len__(self) -> int: ...
    def get(
        self, glyphName: str, default: typing.Optional[_TTGlyph] = ...
    ) -> _TTGlyph: ...

class _TTGlyph:
    """Wrapper for a TrueType glyph that supports the Pen protocol, meaning
    that it has .draw() and .drawPoints() methods that take a pen object as
    their only argument. Additionally there are 'width' and 'lsb' attributes,
    read from the 'hmtx' table.

    If the font contains a 'vmtx' table, there will also be 'height' and 'tsb'
    attributes.
    """

    def __init__(
        self,
        glyphset: _TTGlyphSet,
        glyph: typing.Any,
        horizontalMetrics: tuple[int, int],
        verticalMetrics: typing.Optional[tuple[int, int]] = ...,
    ) -> None:
        """Construct a new _TTGlyph.

        Args:
                glyphset (_TTGlyphSet): A glyphset object used to resolve components.
                glyph (ttLib.tables._g_l_y_f.Glyph): The glyph object.
                horizontalMetrics (int, int): The glyph's width and left sidebearing.
        """
        ...
    def draw(self, pen: typing.Any) -> None:
        """Draw the glyph onto ``pen``. See fontTools.pens.basePen for details
        how that works.
        """
        ...
    def drawPoints(self, pen: typing.Any) -> None: ...

class _TTGlyphCFF(_TTGlyph): ...

class _TTGlyphGlyf(_TTGlyph):
    def draw(self, pen: typing.Any) -> None:
        """Draw the glyph onto Pen. See fontTools.pens.basePen for details
        how that works.
        """
        ...
    def drawPoints(self, pen: typing.Any) -> None:
        """Draw the glyph onto PointPen. See fontTools.pens.pointPen
        for details how that works.
        """
        ...

class GlyphOrder:
    """A pseudo table. The glyph order isn't in the font as a separate
    table, but it's nice to present it as such in the TTX format.
    """

    def __init__(self, tag: typing.Any = ...) -> None: ...
    def toXML(self, writer: typing.Any, ttFont: TTFont) -> None: ...
    def fromXML(
        self,
        name: str,
        attrs: dict[str, typing.Any],
        content: typing.Any,
        ttFont: TTFont,
    ) -> None: ...

def getTableModule(tag: str) -> typing.Optional[typing.Any]:
    """Fetch the packer/unpacker module for a table.
    Return None when no module is found.
    """
    ...

_customTableRegistry: dict[str, tuple[str, str]] = ...

def registerCustomTableClass(
    tag: str, moduleName: str, className: typing.Optional[str] = ...
) -> None:
    """Register a custom packer/unpacker class for a table.

    The 'moduleName' must be an importable module. If no 'className'
    is given, it is derived from the tag, for example it will be
    ``table_C_U_S_T_`` for a 'CUST' tag.

    The registered table class should be a subclass of
    :py:class:`fontTools.ttLib.tables.DefaultTable.DefaultTable`
    """
    ...

def unregisterCustomTableClass(tag: str) -> None:
    """Unregister the custom packer/unpacker class for a table."""
    ...

def getCustomTableClass(tag: str) -> typing.Optional[typing.Any]:
    """Return the custom table class for tag, if one has been registered
    with 'registerCustomTableClass()'. Else return None.
    """
    ...

def getTableClass(tag: str) -> typing.Any:
    """Fetch the packer/unpacker class for a table."""
    ...

def getClassTag(klass: typing.Any) -> str:
    """Fetch the table tag for a class object."""
    ...

def newTable(tag: str) -> typing.Any:
    """Return a new instance of a table."""
    ...

def tagToIdentifier(tag: str) -> str:
    """Convert a table tag to a valid (but UGLY) python identifier,
    as well as a filename that's guaranteed to be unique even on a
    caseless file system. Each character is mapped to two characters.
    Lowercase letters get an underscore before the letter, uppercase
    letters get an underscore after the letter. Trailing spaces are
    trimmed. Illegal characters are escaped as two hex bytes. If the
    result starts with a number (as the result of a hex escape), an
    extra underscore is prepended. Examples::

            >>> tagToIdentifier('glyf')
            '_g_l_y_f'
            >>> tagToIdentifier('cvt ')
            '_c_v_t'
            >>> tagToIdentifier('OS/2')
            'O_S_2f_2'
    """
    ...

def identifierToTag(ident: str) -> str:
    """the opposite of tagToIdentifier()"""
    ...

def tagToXML(tag: str) -> str:
    """Similarly to tagToIdentifier(), this converts a TT tag
    to a valid XML element name. Since XML element names are
    case sensitive, this is a fairly simple/readable translation.
    """
    ...

def xmlToTag(tag: str) -> str:
    """The opposite of tagToXML()"""
    ...

TTFTableOrder: list[str] = ...
OTFTableOrder: list[str] = ...

def sortedTagList(
    tagList: list[str], tableOrder: typing.Optional[list[str]] = ...
) -> list[str]:
    """Return a sorted copy of tagList, sorted according to the OpenType
    specification, or according to a custom tableOrder. If given and not
    None, tableOrder needs to be a list of tag names.
    """
    ...

def reorderFontTables(
    inFile: BufferedReader,
    outFile: BufferedWriter,
    tableOrder: typing.Optional[list[str]] = ...,
    checkChecksums: bool = ...,
) -> None:
    """Rewrite a font file, ordering the tables as recommended by the
    OpenType specification 1.4.
    """
    ...

def maxPowerOfTwo(x: int) -> int:
    """Return the highest exponent of two, so that
    (2 ** exponent) <= x.  Return 0 if x is 0.
    """
    ...

def getSearchRange(n: int, itemSize: int = ...) -> tuple[int, int, int]:
    """Calculate searchRange, entrySelector, rangeShift."""
    ...
