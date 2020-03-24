from typing import NewType, Optional

from OCC.Core.IntCurveSurface import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.math import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Intf import *
from OCC.Core.Bnd import *
from OCC.Core.IntSurf import *


class IntCurveSurface_TransitionOnCurve:
	IntCurveSurface_Tangent: int = ...
	IntCurveSurface_In: int = ...
	IntCurveSurface_Out: int = ...

class IntCurveSurface_Intersection:
	def Dump(self) -> None: ...
	def IsDone(self) -> bool: ...
	def IsParallel(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def NbSegments(self) -> int: ...
	def Point(self, Index: int) -> IntCurveSurface_IntersectionPoint: ...
	def Segment(self, Index: int) -> IntCurveSurface_IntersectionSegment: ...

class IntCurveSurface_IntersectionPoint:
	def __init__(self) -> None: ...
	def __init__(self, P: gp_Pnt, USurf: float, VSurf: float, UCurv: float, TrCurv: IntCurveSurface_TransitionOnCurve) -> None: ...
	def Dump(self) -> None: ...
	def Pnt(self) -> gp_Pnt: ...
	def SetValues(self, P: gp_Pnt, USurf: float, VSurf: float, UCurv: float, TrCurv: IntCurveSurface_TransitionOnCurve) -> None: ...
	def Transition(self) -> IntCurveSurface_TransitionOnCurve: ...
	def U(self) -> float: ...
	def V(self) -> float: ...
	def Values(self, P: gp_Pnt, USurf: float, VSurf: float, UCurv: float, TrCurv: IntCurveSurface_TransitionOnCurve) -> None: ...
	def W(self) -> float: ...

class IntCurveSurface_IntersectionSegment:
	def __init__(self) -> None: ...
	def __init__(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...
	def Dump(self) -> None: ...
	def FirstPoint(self, P1: IntCurveSurface_IntersectionPoint) -> None: ...
	def FirstPoint(self) -> IntCurveSurface_IntersectionPoint: ...
	def SecondPoint(self, P2: IntCurveSurface_IntersectionPoint) -> None: ...
	def SecondPoint(self) -> IntCurveSurface_IntersectionPoint: ...
	def SetValues(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...
	def Values(self, P1: IntCurveSurface_IntersectionPoint, P2: IntCurveSurface_IntersectionPoint) -> None: ...

class IntCurveSurface_TheCSFunctionOfHInter(math_FunctionSetWithDerivatives):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def AuxillarCurve(self) -> Adaptor3d_HCurve: ...
	def AuxillarSurface(self) -> Adaptor3d_HSurface: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class IntCurveSurface_TheExactHInter:
	def __init__(self, U: float, V: float, W: float, F: IntCurveSurface_TheCSFunctionOfHInter, TolTangency: float, MarginCoef: Optional[float]) -> None: ...
	def __init__(self, F: IntCurveSurface_TheCSFunctionOfHInter, TolTangency: float) -> None: ...
	def Function(self) -> IntCurveSurface_TheCSFunctionOfHInter: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def ParameterOnCurve(self) -> float: ...
	def ParameterOnSurface(self, U: float, V: float) -> None: ...
	def Perform(self, U: float, V: float, W: float, Rsnld: math_FunctionSetRoot, u0: float, v0: float, u1: float, v1: float, w0: float, w1: float) -> None: ...
	def Point(self) -> gp_Pnt: ...

class IntCurveSurface_TheHCurveTool:
	@staticmethod
	def BSpline(self, C: Adaptor3d_HCurve) -> Geom_BSplineCurve: ...
	@staticmethod
	def Bezier(self, C: Adaptor3d_HCurve) -> Geom_BezierCurve: ...
	@staticmethod
	def Circle(self, C: Adaptor3d_HCurve) -> gp_Circ: ...
	@staticmethod
	def Continuity(self, C: Adaptor3d_HCurve) -> GeomAbs_Shape: ...
	@staticmethod
	def D0(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt) -> None: ...
	@staticmethod
	def D1(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	@staticmethod
	def D2(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@staticmethod
	def D3(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	@staticmethod
	def DN(self, C: Adaptor3d_HCurve, U: float, N: int) -> gp_Vec: ...
	@staticmethod
	def Ellipse(self, C: Adaptor3d_HCurve) -> gp_Elips: ...
	@staticmethod
	def FirstParameter(self, C: Adaptor3d_HCurve) -> float: ...
	@staticmethod
	def GetType(self, C: Adaptor3d_HCurve) -> GeomAbs_CurveType: ...
	@staticmethod
	def Hyperbola(self, C: Adaptor3d_HCurve) -> gp_Hypr: ...
	@staticmethod
	def Intervals(self, C: Adaptor3d_HCurve, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	@staticmethod
	def IsClosed(self, C: Adaptor3d_HCurve) -> bool: ...
	@staticmethod
	def IsPeriodic(self, C: Adaptor3d_HCurve) -> bool: ...
	@staticmethod
	def LastParameter(self, C: Adaptor3d_HCurve) -> float: ...
	@staticmethod
	def Line(self, C: Adaptor3d_HCurve) -> gp_Lin: ...
	@staticmethod
	def NbIntervals(self, C: Adaptor3d_HCurve, S: GeomAbs_Shape) -> int: ...
	@staticmethod
	def NbSamples(self, C: Adaptor3d_HCurve, U0: float, U1: float) -> int: ...
	@staticmethod
	def Parabola(self, C: Adaptor3d_HCurve) -> gp_Parab: ...
	@staticmethod
	def Period(self, C: Adaptor3d_HCurve) -> float: ...
	@staticmethod
	def Resolution(self, C: Adaptor3d_HCurve, R3d: float) -> float: ...
	@staticmethod
	def SamplePars(self, C: Adaptor3d_HCurve, U0: float, U1: float, Defl: float, NbMin: int, Pars: TColStd_HArray1OfReal) -> None: ...
	@staticmethod
	def Value(self, C: Adaptor3d_HCurve, U: float) -> gp_Pnt: ...

class IntCurveSurface_TheInterferenceOfHInter(Intf_Interference):
	def __init__(self) -> None: ...
	def __init__(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def __init__(self, theLin: gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def __init__(self, theLins: Intf_Array1OfLin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def __init__(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def __init__(self, theLin: gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def __init__(self, theLins: Intf_Array1OfLin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def Interference(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def Interference(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def Perform(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def Perform(self, theLin: gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def Perform(self, theLins: Intf_Array1OfLin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def Perform(self, thePolyg: IntCurveSurface_ThePolygonOfHInter, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def Perform(self, theLin: gp_Lin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...
	def Perform(self, theLins: Intf_Array1OfLin, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, theBoundSB: Bnd_BoundSortBox) -> None: ...

class IntCurveSurface_ThePolygonOfHInter:
	def __init__(self, Curve: Adaptor3d_HCurve, NbPnt: int) -> None: ...
	def __init__(self, Curve: Adaptor3d_HCurve, U1: float, U2: float, NbPnt: int) -> None: ...
	def __init__(self, Curve: Adaptor3d_HCurve, Upars: TColStd_Array1OfReal) -> None: ...
	def ApproxParamOnCurve(self, Index: int, ParamOnLine: float) -> float: ...
	def BeginOfSeg(self, Index: int) -> gp_Pnt: ...
	def Bounding(self) -> Bnd_Box: ...
	def Closed(self, clos: bool) -> None: ...
	def Closed(self) -> bool: ...
	def DeflectionOverEstimation(self) -> float: ...
	def Dump(self) -> None: ...
	def EndOfSeg(self, Index: int) -> gp_Pnt: ...
	def InfParameter(self) -> float: ...
	def NbSegments(self) -> int: ...
	def SetDeflectionOverEstimation(self, x: float) -> None: ...
	def SupParameter(self) -> float: ...

class IntCurveSurface_ThePolygonToolOfHInter:
	@staticmethod
	def BeginOfSeg(self, thePolygon: IntCurveSurface_ThePolygonOfHInter, Index: int) -> gp_Pnt: ...
	@staticmethod
	def Bounding(self, thePolygon: IntCurveSurface_ThePolygonOfHInter) -> Bnd_Box: ...
	@staticmethod
	def Closed(self, thePolygon: IntCurveSurface_ThePolygonOfHInter) -> bool: ...
	@staticmethod
	def DeflectionOverEstimation(self, thePolygon: IntCurveSurface_ThePolygonOfHInter) -> float: ...
	@staticmethod
	def Dump(self, thePolygon: IntCurveSurface_ThePolygonOfHInter) -> None: ...
	@staticmethod
	def EndOfSeg(self, thePolygon: IntCurveSurface_ThePolygonOfHInter, Index: int) -> gp_Pnt: ...
	@staticmethod
	def NbSegments(self, thePolygon: IntCurveSurface_ThePolygonOfHInter) -> int: ...

class IntCurveSurface_ThePolyhedronToolOfHInter:
	@staticmethod
	def Bounding(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> Bnd_Box: ...
	@staticmethod
	def ComponentsBounding(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> Bnd_HArray1OfBox: ...
	@staticmethod
	def DeflectionOverEstimation(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> float: ...
	@staticmethod
	def Dump(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	@staticmethod
	def GetBorderDeflection(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> float: ...
	@staticmethod
	def IsOnBound(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index1: int, Index2: int) -> bool: ...
	@staticmethod
	def NbTriangles(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter) -> int: ...
	@staticmethod
	def Point(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index: int) -> gp_Pnt: ...
	@staticmethod
	def TriConnex(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Triang: int, Pivot: int, Pedge: int, TriCon: int, OtherP: int) -> int: ...
	@staticmethod
	def Triangle(self, thePolyh: IntCurveSurface_ThePolyhedronOfHInter, Index: int, P1: int, P2: int, P3: int) -> None: ...

class IntCurveSurface_TheQuadCurvExactHInter:
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Intervals(self, Index: int, U1: float, U2: float) -> None: ...
	def IsDone(self) -> bool: ...
	def NbIntervals(self) -> int: ...
	def NbRoots(self) -> int: ...
	def Root(self, Index: int) -> float: ...

class IntCurveSurface_TheQuadCurvFuncOfTheQuadCurvExactHInter(math_FunctionWithDerivative):
	def __init__(self, Q: IntSurf_Quadric, C: Adaptor3d_HCurve) -> None: ...
	def Derivative(self, Param: float, D: float) -> bool: ...
	def Value(self, Param: float, F: float) -> bool: ...
	def Values(self, Param: float, F: float, D: float) -> bool: ...

class IntCurveSurface_HInter(IntCurveSurface_Intersection):
	def __init__(self) -> None: ...
	def Perform(self, Curve: Adaptor3d_HCurve, Surface: Adaptor3d_HSurface) -> None: ...
	def Perform(self, Curve: Adaptor3d_HCurve, Polygon: IntCurveSurface_ThePolygonOfHInter, Surface: Adaptor3d_HSurface) -> None: ...
	def Perform(self, Curve: Adaptor3d_HCurve, ThePolygon: IntCurveSurface_ThePolygonOfHInter, Surface: Adaptor3d_HSurface, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
	def Perform(self, Curve: Adaptor3d_HCurve, ThePolygon: IntCurveSurface_ThePolygonOfHInter, Surface: Adaptor3d_HSurface, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter, BndBSB: Bnd_BoundSortBox) -> None: ...
	def Perform(self, Curve: Adaptor3d_HCurve, Surface: Adaptor3d_HSurface, Polyhedron: IntCurveSurface_ThePolyhedronOfHInter) -> None: ...
