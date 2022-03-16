"""
This type stub file was generated by pyright.
"""

"""\
Provides the Color class, which represents an RGB color.
"""
class Color:
    """\
    The Color object represents an RGB color with integer red, green, and blue values
    between 0 and 255.
    """
    def __init__(self, red: int, green: int, blue: int) -> None:
        """\
        Create a Color object with the given RGB values.
        """
        ...
    
    def __eq__(self, other: Color) -> bool:
        """\
        Check whether this object and other have the same RGB values.
        """
        ...
    
    def __repr__(self) -> str:
        ...
    
    def asHex(self) -> str:
        """\
        Return the 6-digit hexadecimal RGB values, prefixed with “#”,
        for the color of this object.
        """
        ...
    
    _keywords: dict[str, tuple[int, int, int]] = ...
    @classmethod
    def forCSS(cls, color: str) -> Color:
        """\
        Return a new Color object for the given CSS color value.
        Raise ValueError if the given string is not in a supported CSS
        color value notation, or is not a valid value.
        """
        ...
    

