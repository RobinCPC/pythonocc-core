from typing import NewType, Optional

from OCC.Core.TopCnx import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *


class TopCnx_EdgeFaceTransition:
	def __init__(self) -> None: ...
	def AddInterference(self, Tole: float, Tang: gp_Dir, Norm: gp_Dir, Curv: float, Or: TopAbs_Orientation, Tr: TopAbs_Orientation, BTr: TopAbs_Orientation) -> None: ...
	def BoundaryTransition(self) -> TopAbs_Orientation: ...
	def Reset(self, Tgt: gp_Dir, Norm: gp_Dir, Curv: float) -> None: ...
	def Reset(self, Tgt: gp_Dir) -> None: ...
	def Transition(self) -> TopAbs_Orientation: ...
