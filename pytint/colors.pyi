from . import COLORS as COLORS, DEFAULTS as DEFAULTS, INVERSE_SCHEMES as INVERSE_SCHEMES, SCHEMES as SCHEMES

class Colors:
    def __init__(self) -> None: ...
    def get_defaults(self) -> list[str]: ...
    def get_scheme_variants(self) -> list[str]: ...
    def get_colors_list(self) -> list[str]: ...
    def select_scheme(self, scheme: str, inverse: bool = ...) -> tuple[str, str, str]: ...
    def select_color(self, color: str) -> tuple[str, str]: ...