from typing import NewType, Optional

from OCC.Core.SelectBasics import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *


class SelectBasics:
	@staticmethod
	def MaxOwnerPriority(self) -> int: ...
	@staticmethod
	def MinOwnerPriority(self) -> int: ...

class SelectBasics_PickResult:
	def __init__(self) -> None: ...
	def __init__(self, theDepth: float, theDistToCenter: float, theObjPickedPnt: gp_Pnt) -> None: ...
	def Depth(self) -> float: ...
	def DistToGeomCenter(self) -> float: ...
	def HasPickedPoint(self) -> bool: ...
	def Invalidate(self) -> None: ...
	def IsValid(self) -> bool: ...
	@staticmethod
	def Min(self, thePickResult1: SelectBasics_PickResult, thePickResult2: SelectBasics_PickResult) -> SelectBasics_PickResult: ...
	def PickedPoint(self) -> gp_Pnt: ...
	def SetDepth(self, theDepth: float) -> None: ...
	def SetDistToGeomCenter(self, theDistToCenter: float) -> None: ...
	def SetPickedPoint(self, theObjPickedPnt: gp_Pnt) -> None: ...

class SelectBasics_SelectingVolumeManager:
	def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
	def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
	def GetActiveSelectionType(self) -> int: ...
	def GetFarPickedPnt(self) -> gp_Pnt: ...
	def GetMousePosition(self) -> gp_Pnt2d: ...
	def GetNearPickedPnt(self) -> gp_Pnt: ...
	def IsOverlapAllowed(self) -> bool: ...
	def Overlaps(self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePnt: gp_Pnt) -> bool: ...
	def Overlaps(self, theArrayOfPts: TColgp_HArray1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, theArrayOfPts: TColgp_Array1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePt1: gp_Pnt, thePt2: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePt1: gp_Pnt, thePt2: gp_Pnt, thePt3: gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
