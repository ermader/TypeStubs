"""
This type stub file was generated by pyright.
"""

import enum
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, TypeVar, Union
from fontTools.ttLib.tables import C_O_L_R_, C_P_A_L_, _n_a_m_e, otTables as ot

"""
colorLib.builder: Build COLR/CPAL tables from scratch

"""
T = TypeVar("T")
_Kwargs = Mapping[str, Any]
_PaintInput = Union[int, _Kwargs, ot.Paint, Tuple[str, "_PaintInput"]]
_PaintInputList = Sequence[_PaintInput]
_ColorGlyphsDict = Dict[str, Union[_PaintInputList, _PaintInput]]
_ColorGlyphsV0Dict = Dict[str, Sequence[Tuple[str, int]]]
_ClipBoxInput = Union[Tuple[int, int, int, int, int], Tuple[int, int, int, int], ot.ClipBox],
MAX_PAINT_COLR_LAYER_COUNT = ...
_DEFAULT_ALPHA = ...
_MAX_REUSE_LEN = ...
def populateCOLRv0(table: ot.COLR, colorGlyphsV0: _ColorGlyphsV0Dict, glyphMap: Optional[Mapping[str, int]] = ...): # -> None:
    """Build v0 color layers and add to existing COLR table.

    Args:
        table: a raw ``otTables.COLR()`` object (not ttLib's ``table_C_O_L_R_``).
        colorGlyphsV0: map of base glyph names to lists of (layer glyph names,
            color palette index) tuples. Can be empty.
        glyphMap: a map from glyph names to glyph indices, as returned from
            ``TTFont.getReverseGlyphMap()``, to optionally sort base records by GID.
    """
    ...

def buildCOLR(colorGlyphs: _ColorGlyphsDict, version: Optional[int] = ..., glyphMap: Optional[Mapping[str, int]] = ..., varStore: Optional[ot.VarStore] = ..., varIndexMap: Optional[ot.DeltaSetIndexMap] = ..., clipBoxes: Optional[Dict[str, _ClipBoxInput]] = ...) -> C_O_L_R_.table_C_O_L_R_:
    """Build COLR table from color layers mapping.

    Args:

        colorGlyphs: map of base glyph name to, either list of (layer glyph name,
            color palette index) tuples for COLRv0; or a single ``Paint`` (dict) or
            list of ``Paint`` for COLRv1.
        version: the version of COLR table. If None, the version is determined
            by the presence of COLRv1 paints or variation data (varStore), which
            require version 1; otherwise, if all base glyphs use only simple color
            layers, version 0 is used.
        glyphMap: a map from glyph names to glyph indices, as returned from
            TTFont.getReverseGlyphMap(), to optionally sort base records by GID.
        varStore: Optional ItemVarationStore for deltas associated with v1 layer.
        varIndexMap: Optional DeltaSetIndexMap for deltas associated with v1 layer.
        clipBoxes: Optional map of base glyph name to clip box 4- or 5-tuples:
            (xMin, yMin, xMax, yMax) or (xMin, yMin, xMax, yMax, varIndexBase).

    Returns:
        A new COLR table.
    """
    ...

def buildClipList(clipBoxes: Dict[str, _ClipBoxInput]) -> ot.ClipList:
    ...

def buildClipBox(clipBox: _ClipBoxInput) -> ot.ClipBox:
    ...

class ColorPaletteType(enum.IntFlag):
    USABLE_WITH_LIGHT_BACKGROUND = ...
    USABLE_WITH_DARK_BACKGROUND = ...


_OptionalLocalizedString = Union[None, str, Dict[str, str]]
def buildPaletteLabels(labels: Iterable[_OptionalLocalizedString], nameTable: _n_a_m_e.table__n_a_m_e) -> List[Optional[int]]:
    ...

def buildCPAL(palettes: Sequence[Sequence[Tuple[float, float, float, float]]], paletteTypes: Optional[Sequence[ColorPaletteType]] = ..., paletteLabels: Optional[Sequence[_OptionalLocalizedString]] = ..., paletteEntryLabels: Optional[Sequence[_OptionalLocalizedString]] = ..., nameTable: Optional[_n_a_m_e.table__n_a_m_e] = ...) -> C_P_A_L_.table_C_P_A_L_:
    """Build CPAL table from list of color palettes.

    Args:
        palettes: list of lists of colors encoded as tuples of (R, G, B, A) floats
            in the range [0..1].
        paletteTypes: optional list of ColorPaletteType, one for each palette.
        paletteLabels: optional list of palette labels. Each lable can be either:
            None (no label), a string (for for default English labels), or a
            localized string (as a dict keyed with BCP47 language codes).
        paletteEntryLabels: optional list of palette entry labels, one for each
            palette entry (see paletteLabels).
        nameTable: optional name table where to store palette and palette entry
            labels. Required if either paletteLabels or paletteEntryLabels is set.

    Return:
        A new CPAL v0 or v1 table, if custom palette types or labels are specified.
    """
    ...

class LayerListBuilder:
    layers: List[ot.Paint]
    reusePool: Mapping[Tuple[Any, ...], int]
    tuples: Mapping[int, Tuple[Any, ...]]
    keepAlive: List[ot.Paint]
    def __init__(self) -> None:
        ...
    
    def buildPaint(self, paint: _PaintInput) -> ot.Paint:
        ...
    
    def build(self) -> Optional[ot.LayerList]:
        ...
    


def buildBaseGlyphPaintRecord(baseGlyph: str, layerBuilder: LayerListBuilder, paint: _PaintInput) -> ot.BaseGlyphList:
    ...

def buildColrV1(colorGlyphs: _ColorGlyphsDict, glyphMap: Optional[Mapping[str, int]] = ...) -> Tuple[Optional[ot.LayerList], ot.BaseGlyphList]:
    ...

