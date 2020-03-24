from typing import NewType, Optional

from OCC.Core.TopTrans import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *


class TopTrans_CurveTransition:
	def __init__(self) -> None: ...
	def Compare(self, Tole: float, Tang: gp_Dir, Norm: gp_Dir, Curv: float, S: TopAbs_Orientation, Or: TopAbs_Orientation) -> None: ...
	def Reset(self, Tgt: gp_Dir, Norm: gp_Dir, Curv: float) -> None: ...
	def Reset(self, Tgt: gp_Dir) -> None: ...
	def StateAfter(self) -> TopAbs_State: ...
	def StateBefore(self) -> TopAbs_State: ...

class TopTrans_SurfaceTransition:
	def __init__(self) -> None: ...
	def Compare(self, Tole: float, Norm: gp_Dir, MaxD: gp_Dir, MinD: gp_Dir, MaxCurv: float, MinCurv: float, S: TopAbs_Orientation, O: TopAbs_Orientation) -> None: ...
	def Compare(self, Tole: float, Norm: gp_Dir, S: TopAbs_Orientation, O: TopAbs_Orientation) -> None: ...
	@staticmethod
	def GetAfter(self, Tran: TopAbs_Orientation) -> TopAbs_State: ...
	@staticmethod
	def GetBefore(self, Tran: TopAbs_Orientation) -> TopAbs_State: ...
	def Reset(self, Tgt: gp_Dir, Norm: gp_Dir, MaxD: gp_Dir, MinD: gp_Dir, MaxCurv: float, MinCurv: float) -> None: ...
	def Reset(self, Tgt: gp_Dir, Norm: gp_Dir) -> None: ...
	def StateAfter(self) -> TopAbs_State: ...
	def StateBefore(self) -> TopAbs_State: ...
