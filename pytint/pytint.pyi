from .colors import Colors as Colors
from .svg_tool import ExtractSVG as ExtractSVG, WriteSVG as WriteSVG
from .tint import BatchTint as BatchTint, Tint as Tint

class PyTint:
    def __init__(self, color: str, scheme: str, inverse_scheme: bool = ...) -> None: ...
    def tint_svg(self, svg_in: str, svg_out: str) -> None: ...
    def tint_batch(self, svg_dir: str, out_dir: str) -> None: ...
