"""Shim module for ``qtpyvcp.conversational.ops.face_ops``.

The original conversational namespace exposed the operations modules from
``qtpyvcp.ops``. This shim re-exports the current implementation to
preserve compatibility with downstream consumers.
"""

from qtpyvcp.ops.face_ops import *  # noqa: F401,F403
