from typing import NewType, Optional

from OCC.Core.LProp import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.GeomAbs import *


class LProp_Status:
	LProp_Undecided: int = ...
	LProp_Undefined: int = ...
	LProp_Defined: int = ...
	LProp_Computed: int = ...

class LProp_CIType:
	LProp_Inflection: int = ...
	LProp_MinCur: int = ...
	LProp_MaxCur: int = ...

class LProp_AnalyticCurInf:
	def __init__(self) -> None: ...
	def Perform(self, T: GeomAbs_CurveType, UFirst: float, ULast: float, Result: LProp_CurAndInf) -> None: ...

class LProp_CurAndInf:
	def __init__(self) -> None: ...
	def AddExtCur(self, Param: float, IsMin: bool) -> None: ...
	def AddInflection(self, Param: float) -> None: ...
	def Clear(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, N: int) -> float: ...
	def Type(self, N: int) -> LProp_CIType: ...
