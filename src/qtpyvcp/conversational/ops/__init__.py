"""Compatibility shims for legacy ``qtpyvcp.conversational.ops`` imports."""

from qtpyvcp.ops.base_op import BaseGenerator
from qtpyvcp.ops.drill_ops import DrillOps
from qtpyvcp.ops.face_ops import FaceOps
from qtpyvcp.ops.gcode_file import GCodeFile

__all__ = [
    "BaseGenerator",
    "DrillOps",
    "FaceOps",
    "GCodeFile",
]
