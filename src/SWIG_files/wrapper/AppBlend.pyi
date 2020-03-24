from typing import NewType, Optional

from OCC.Core.AppBlend import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *


class AppBlend_Approx:
	def Curve2d(self, Index: int, TPoles: TColgp_Array1OfPnt2d, TKnots: TColStd_Array1OfReal, TMults: TColStd_Array1OfInteger) -> None: ...
	def Curve2dPoles(self, Index: int) -> TColgp_Array1OfPnt2d: ...
	def Curves2dDegree(self) -> int: ...
	def Curves2dKnots(self) -> TColStd_Array1OfReal: ...
	def Curves2dMults(self) -> TColStd_Array1OfInteger: ...
	def Curves2dShape(self, Degree: int, NbPoles: int, NbKnots: int) -> None: ...
	def IsDone(self) -> bool: ...
	def NbCurves2d(self) -> int: ...
	def SurfPoles(self) -> TColgp_Array2OfPnt: ...
	def SurfShape(self, UDegree: int, VDegree: int, NbUPoles: int, NbVPoles: int, NbUKnots: int, NbVKnots: int) -> None: ...
	def SurfUKnots(self) -> TColStd_Array1OfReal: ...
	def SurfUMults(self) -> TColStd_Array1OfInteger: ...
	def SurfVKnots(self) -> TColStd_Array1OfReal: ...
	def SurfVMults(self) -> TColStd_Array1OfInteger: ...
	def SurfWeights(self) -> TColStd_Array2OfReal: ...
	def Surface(self, TPoles: TColgp_Array2OfPnt, TWeights: TColStd_Array2OfReal, TUKnots: TColStd_Array1OfReal, TVKnots: TColStd_Array1OfReal, TUMults: TColStd_Array1OfInteger, TVMults: TColStd_Array1OfInteger) -> None: ...
	def TolCurveOnSurf(self, Index: int) -> float: ...
	def TolReached(self, Tol3d: float, Tol2d: float) -> None: ...
	def UDegree(self) -> int: ...
	def VDegree(self) -> int: ...