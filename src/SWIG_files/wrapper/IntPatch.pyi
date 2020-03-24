from typing import NewType, Optional

from OCC.Core.IntPatch import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Intf import *
from OCC.Core.Adaptor3d import *
from OCC.Core.math import *
from OCC.Core.Adaptor2d import *
from OCC.Core.gp import *
from OCC.Core.IntSurf import *
from OCC.Core.Geom2d import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.IntAna import *

IntPatch_SearchPnt = NewType('IntPatch_SearchPnt', Intf_InterferencePolygon2d)

class IntPatch_SpecPntType:
	IntPatch_SPntNone: int = ...
	IntPatch_SPntSeamU: int = ...
	IntPatch_SPntSeamV: int = ...
	IntPatch_SPntSeamUV: int = ...
	IntPatch_SPntPoleSeamU: int = ...
	IntPatch_SPntPole: int = ...

class IntPatch_IType:
	IntPatch_Lin: int = ...
	IntPatch_Circle: int = ...
	IntPatch_Ellipse: int = ...
	IntPatch_Parabola: int = ...
	IntPatch_Hyperbola: int = ...
	IntPatch_Analytic: int = ...
	IntPatch_Walking: int = ...
	IntPatch_Restriction: int = ...

class IntPatch_ALineToWLine:
	def __init__(self, theS1: Adaptor3d_HSurface, theS2: Adaptor3d_HSurface, theNbPoints: Optional[int]) -> None: ...
	def MakeWLine(self, aline: IntPatch_ALine, theLines: IntPatch_SequenceOfLine) -> None: ...
	def MakeWLine(self, aline: IntPatch_ALine, paraminf: float, paramsup: float, theLines: IntPatch_SequenceOfLine) -> None: ...
	def SetTol3D(self, aT: float) -> None: ...
	def SetTolOpenDomain(self, aT: float) -> None: ...
	def SetTolTransition(self, aT: float) -> None: ...
	def Tol3D(self) -> float: ...
	def TolOpenDomain(self) -> float: ...
	def TolTransition(self) -> float: ...

class IntPatch_ArcFunction(math_FunctionWithDerivative):
	def __init__(self) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def Derivative(self, X: float, D: float) -> bool: ...
	def GetStateNumber(self) -> int: ...
	def LastComputedPoint(self) -> gp_Pnt: ...
	def NbSamples(self) -> int: ...
	def Quadric(self) -> IntSurf_Quadric: ...
	def Set(self, A: Adaptor2d_HCurve2d) -> None: ...
	def Set(self, S: Adaptor3d_HSurface) -> None: ...
	def SetQuadric(self, Q: IntSurf_Quadric) -> None: ...
	def Surface(self) -> Adaptor3d_HSurface: ...
	def Valpoint(self, Index: int) -> gp_Pnt: ...
	def Value(self, X: float, F: float) -> bool: ...
	def Values(self, X: float, F: float, D: float) -> bool: ...

class IntPatch_CSFunction(math_FunctionSetWithDerivatives):
	def __init__(self, S1: Adaptor3d_HSurface, C: Adaptor2d_HCurve2d, S2: Adaptor3d_HSurface) -> None: ...
	def AuxillarCurve(self) -> Adaptor2d_HCurve2d: ...
	def AuxillarSurface(self) -> Adaptor3d_HSurface: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class IntPatch_CurvIntSurf:
	def __init__(self, U: float, V: float, W: float, F: IntPatch_CSFunction, TolTangency: float, MarginCoef: Optional[float]) -> None: ...
	def __init__(self, F: IntPatch_CSFunction, TolTangency: float) -> None: ...
	def Function(self) -> IntPatch_CSFunction: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def ParameterOnCurve(self) -> float: ...
	def ParameterOnSurface(self, U: float, V: float) -> None: ...
	def Perform(self, U: float, V: float, W: float, Rsnld: math_FunctionSetRoot, u0: float, v0: float, u1: float, v1: float, w0: float, w1: float) -> None: ...
	def Point(self) -> gp_Pnt: ...

class IntPatch_HCurve2dTool:
	@staticmethod
	def BSpline(self, C: Adaptor2d_HCurve2d) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def Bezier(self, C: Adaptor2d_HCurve2d) -> Geom2d_BezierCurve: ...
	@staticmethod
	def Circle(self, C: Adaptor2d_HCurve2d) -> gp_Circ2d: ...
	@staticmethod
	def Continuity(self, C: Adaptor2d_HCurve2d) -> GeomAbs_Shape: ...
	@staticmethod
	def D0(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d) -> None: ...
	@staticmethod
	def D1(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	@staticmethod
	def D2(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	@staticmethod
	def D3(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	@staticmethod
	def DN(self, C: Adaptor2d_HCurve2d, U: float, N: int) -> gp_Vec2d: ...
	@staticmethod
	def Ellipse(self, C: Adaptor2d_HCurve2d) -> gp_Elips2d: ...
	@staticmethod
	def FirstParameter(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def GetType(self, C: Adaptor2d_HCurve2d) -> GeomAbs_CurveType: ...
	@staticmethod
	def Hyperbola(self, C: Adaptor2d_HCurve2d) -> gp_Hypr2d: ...
	@staticmethod
	def Intervals(self, C: Adaptor2d_HCurve2d, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	@staticmethod
	def IsClosed(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def IsPeriodic(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def LastParameter(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Line(self, C: Adaptor2d_HCurve2d) -> gp_Lin2d: ...
	@staticmethod
	def NbIntervals(self, C: Adaptor2d_HCurve2d, S: GeomAbs_Shape) -> int: ...
	@staticmethod
	def NbSamples(self, C: Adaptor2d_HCurve2d, U0: float, U1: float) -> int: ...
	@staticmethod
	def Parabola(self, C: Adaptor2d_HCurve2d) -> gp_Parab2d: ...
	@staticmethod
	def Period(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Resolution(self, C: Adaptor2d_HCurve2d, R3d: float) -> float: ...
	@staticmethod
	def Value(self, C: Adaptor2d_HCurve2d, U: float) -> gp_Pnt2d: ...

class IntPatch_HInterTool:
	def __init__(self) -> None: ...
	@staticmethod
	def Bounds(self, C: Adaptor2d_HCurve2d, Ufirst: float, Ulast: float) -> None: ...
	@staticmethod
	def HasBeenSeen(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def HasFirstPoint(self, C: Adaptor2d_HCurve2d, Index: int, IndFirst: int) -> bool: ...
	@staticmethod
	def HasLastPoint(self, C: Adaptor2d_HCurve2d, Index: int, IndLast: int) -> bool: ...
	@staticmethod
	def IsAllSolution(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def IsVertex(self, C: Adaptor2d_HCurve2d, Index: int) -> bool: ...
	@staticmethod
	def NbPoints(self, C: Adaptor2d_HCurve2d) -> int: ...
	def NbSamplePoints(self, S: Adaptor3d_HSurface) -> int: ...
	@staticmethod
	def NbSamplesOnArc(self, A: Adaptor2d_HCurve2d) -> int: ...
	@staticmethod
	def NbSamplesU(self, S: Adaptor3d_HSurface, u1: float, u2: float) -> int: ...
	@staticmethod
	def NbSamplesV(self, S: Adaptor3d_HSurface, v1: float, v2: float) -> int: ...
	@staticmethod
	def NbSegments(self, C: Adaptor2d_HCurve2d) -> int: ...
	@staticmethod
	def Parameter(self, V: Adaptor3d_HVertex, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Project(self, C: Adaptor2d_HCurve2d, P: gp_Pnt2d, Paramproj: float, Ptproj: gp_Pnt2d) -> bool: ...
	def SamplePoint(self, S: Adaptor3d_HSurface, Index: int, U: float, V: float) -> None: ...
	@staticmethod
	def SingularOnUMax(self, S: Adaptor3d_HSurface) -> bool: ...
	@staticmethod
	def SingularOnUMin(self, S: Adaptor3d_HSurface) -> bool: ...
	@staticmethod
	def SingularOnVMax(self, S: Adaptor3d_HSurface) -> bool: ...
	@staticmethod
	def SingularOnVMin(self, S: Adaptor3d_HSurface) -> bool: ...
	@staticmethod
	def Tolerance(self, V: Adaptor3d_HVertex, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Value(self, C: Adaptor2d_HCurve2d, Index: int, Pt: gp_Pnt, Tol: float, U: float) -> None: ...
	@staticmethod
	def Vertex(self, C: Adaptor2d_HCurve2d, Index: int, V: Adaptor3d_HVertex) -> None: ...

class IntPatch_ImpImpIntersection:
	def __init__(self) -> None: ...
	def __init__(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, theIsReqToKeepRLine: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Line(self, Index: int) -> IntPatch_Line: ...
	def NbLines(self) -> int: ...
	def NbPnts(self) -> int: ...
	def OppositeFaces(self) -> bool: ...
	def Perform(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, theIsReqToKeepRLine: Optional[bool]) -> None: ...
	def Point(self, Index: int) -> IntPatch_Point: ...
	def TangentFaces(self) -> bool: ...

class IntPatch_ImpPrmIntersection:
	def __init__(self) -> None: ...
	def __init__(self, Surf1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, Surf2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, Fleche: float, Pas: float) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Line(self, Index: int) -> IntPatch_Line: ...
	def NbLines(self) -> int: ...
	def NbPnts(self) -> int: ...
	def Perform(self, Surf1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, Surf2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, Fleche: float, Pas: float) -> None: ...
	def Point(self, Index: int) -> IntPatch_Point: ...
	def SetStartPoint(self, U: float, V: float) -> None: ...

class IntPatch_InterferencePolyhedron(Intf_Interference):
	def __init__(self) -> None: ...
	def __init__(self, Obje1: IntPatch_Polyhedron, Obje2: IntPatch_Polyhedron) -> None: ...
	def __init__(self, Obje: IntPatch_Polyhedron) -> None: ...
	def Perform(self, Obje1: IntPatch_Polyhedron, Obje2: IntPatch_Polyhedron) -> None: ...
	def Perform(self, Obje: IntPatch_Polyhedron) -> None: ...

class IntPatch_Intersection:
	def __init__(self) -> None: ...
	def __init__(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float) -> None: ...
	def __init__(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, TolArc: float, TolTang: float) -> None: ...
	def Dump(self, Mode: int, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Line(self, Index: int) -> IntPatch_Line: ...
	def NbLines(self) -> int: ...
	def NbPnts(self) -> int: ...
	def OppositeFaces(self) -> bool: ...
	def Perform(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, isGeomInt: Optional[bool], theIsReqToKeepRLine: Optional[bool], theIsReqToPostWLProc: Optional[bool]) -> None: ...
	def Perform(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, TolArc: float, TolTang: float, LOfPnts: IntSurf_ListOfPntOn2S, isGeomInt: Optional[bool], theIsReqToKeepRLine: Optional[bool], theIsReqToPostWLProc: Optional[bool]) -> None: ...
	def Perform(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, U1: float, V1: float, U2: float, V2: float, TolArc: float, TolTang: float) -> None: ...
	def Perform(self, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, TolArc: float, TolTang: float) -> None: ...
	def Point(self, Index: int) -> IntPatch_Point: ...
	def SequenceOfLine(self) -> IntPatch_SequenceOfLine: ...
	def SetTolerances(self, TolArc: float, TolTang: float, UVMaxStep: float, Fleche: float) -> None: ...
	def TangentFaces(self) -> bool: ...

class IntPatch_Line(Standard_Transient):
	def ArcType(self) -> IntPatch_IType: ...
	def IsTangent(self) -> bool: ...
	def IsUIsoOnS1(self) -> bool: ...
	def IsUIsoOnS2(self) -> bool: ...
	def IsVIsoOnS1(self) -> bool: ...
	def IsVIsoOnS2(self) -> bool: ...
	def SetValue(self, Uiso1: bool, Viso1: bool, Uiso2: bool, Viso2: bool) -> None: ...
	def SituationS1(self) -> IntSurf_Situation: ...
	def SituationS2(self) -> IntSurf_Situation: ...
	def TransitionOnS1(self) -> IntSurf_TypeTrans: ...
	def TransitionOnS2(self) -> IntSurf_TypeTrans: ...

class IntPatch_LineConstructor:
	def __init__(self, mode: int) -> None: ...
	def Line(self, index: int) -> IntPatch_Line: ...
	def NbLines(self) -> int: ...
	def Perform(self, SL: IntPatch_SequenceOfLine, L: IntPatch_Line, S1: Adaptor3d_HSurface, D1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, D2: Adaptor3d_TopolTool, Tol: float) -> None: ...

class IntPatch_Point:
	def __init__(self) -> None: ...
	def ArcOnS1(self) -> Adaptor2d_HCurve2d: ...
	def ArcOnS2(self) -> Adaptor2d_HCurve2d: ...
	def Dump(self) -> None: ...
	def IsMultiple(self) -> bool: ...
	def IsOnDomS1(self) -> bool: ...
	def IsOnDomS2(self) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def IsVertexOnS1(self) -> bool: ...
	def IsVertexOnS2(self) -> bool: ...
	def ParameterOnArc1(self) -> float: ...
	def ParameterOnArc2(self) -> float: ...
	def ParameterOnLine(self) -> float: ...
	def Parameters(self, U1: float, V1: float, U2: float, V2: float) -> None: ...
	def ParametersOnS1(self, U1: float, V1: float) -> None: ...
	def ParametersOnS2(self, U2: float, V2: float) -> None: ...
	def PntOn2S(self) -> IntSurf_PntOn2S: ...
	def ReverseTransition(self) -> None: ...
	def SetArc(self, OnFirst: bool, A: Adaptor2d_HCurve2d, Param: float, TLine: IntSurf_Transition, TArc: IntSurf_Transition) -> None: ...
	def SetMultiple(self, IsMult: bool) -> None: ...
	def SetParameter(self, Para: float) -> None: ...
	def SetParameters(self, U1: float, V1: float, U2: float, V2: float) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...
	def SetValue(self, Pt: gp_Pnt, Tol: float, Tangent: bool) -> None: ...
	def SetValue(self, Pt: gp_Pnt) -> None: ...
	def SetValue(self, thePOn2S: IntSurf_PntOn2S) -> None: ...
	def SetVertex(self, OnFirst: bool, V: Adaptor3d_HVertex) -> None: ...
	def Tolerance(self) -> float: ...
	def TransitionLineArc1(self) -> IntSurf_Transition: ...
	def TransitionLineArc2(self) -> IntSurf_Transition: ...
	def TransitionOnS1(self) -> IntSurf_Transition: ...
	def TransitionOnS2(self) -> IntSurf_Transition: ...
	def Value(self) -> gp_Pnt: ...
	def VertexOnS1(self) -> Adaptor3d_HVertex: ...
	def VertexOnS2(self) -> Adaptor3d_HVertex: ...

class IntPatch_Polygo(Intf_Polygon2d):
	def DeflectionOverEstimation(self) -> float: ...
	def Dump(self) -> None: ...
	def Error(self) -> float: ...
	def NbPoints(self) -> int: ...
	def NbSegments(self) -> int: ...
	def Point(self, Index: int) -> gp_Pnt2d: ...
	def Segment(self, theIndex: int, theBegin: gp_Pnt2d, theEnd: gp_Pnt2d) -> None: ...

class IntPatch_PolyhedronTool:
	@staticmethod
	def Bounding(self, thePolyh: IntPatch_Polyhedron) -> Bnd_Box: ...
	@staticmethod
	def ComponentsBounding(self, thePolyh: IntPatch_Polyhedron) -> Bnd_HArray1OfBox: ...
	@staticmethod
	def DeflectionOverEstimation(self, thePolyh: IntPatch_Polyhedron) -> float: ...
	@staticmethod
	def NbTriangles(self, thePolyh: IntPatch_Polyhedron) -> int: ...
	@staticmethod
	def Point(self, thePolyh: IntPatch_Polyhedron, Index: int) -> gp_Pnt: ...
	@staticmethod
	def TriConnex(self, thePolyh: IntPatch_Polyhedron, Triang: int, Pivot: int, Pedge: int, TriCon: int, OtherP: int) -> int: ...
	@staticmethod
	def Triangle(self, thePolyh: IntPatch_Polyhedron, Index: int, P1: int, P2: int, P3: int) -> None: ...

class IntPatch_PrmPrmIntersection:
	def __init__(self) -> None: ...
	def CodeReject(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float) -> int: ...
	def DansGrille(self, t: int) -> int: ...
	def GrilleInteger(self, ix: int, iy: int, iz: int) -> int: ...
	def IntegerGrille(self, t: int, ix: int, iy: int, iz: int) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Line(self, Index: int) -> IntPatch_Line: ...
	def NbLines(self) -> int: ...
	def NbPointsGrille(self) -> int: ...
	def NewLine(self, Caro1: Adaptor3d_HSurface, Caro2: Adaptor3d_HSurface, IndexLine: int, LowPoint: int, HighPoint: int, NbPoints: int) -> IntPatch_Line: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Polyhedron1: IntPatch_Polyhedron, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Polyhedron2: IntPatch_Polyhedron, Domain2: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Polyhedron1: IntPatch_Polyhedron, Domain1: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Domain2: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float, ClearFlag: Optional[bool]) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Domain2: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float, ListOfPnts: IntSurf_ListOfPntOn2S) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Domain2: Adaptor3d_TopolTool, U1: float, V1: float, U2: float, V2: float, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Polyhedron2: IntPatch_Polyhedron, Domain2: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def Perform(self, Caro1: Adaptor3d_HSurface, Polyhedron1: IntPatch_Polyhedron, Domain1: Adaptor3d_TopolTool, Caro2: Adaptor3d_HSurface, Domain2: Adaptor3d_TopolTool, TolTangency: float, Epsilon: float, Deflection: float, Increment: float) -> None: ...
	def PointDepart(self, LineOn2S: IntSurf_LineOn2S, S1: Adaptor3d_HSurface, SU1: int, SV1: int, S2: Adaptor3d_HSurface, SU2: int, SV2: int) -> None: ...
	def Remplit(self, a: int, b: int, c: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...
	def RemplitLin(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...
	def RemplitTri(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, x3: int, y3: int, z3: int, Map: IntPatch_PrmPrmIntersection_T3Bits) -> None: ...

class IntPatch_PrmPrmIntersection_T3Bits:
	def __init__(self, size: int) -> None: ...
	def Add(self, t: int) -> None: ...
	def And(self, Oth: IntPatch_PrmPrmIntersection_T3Bits, indiceprecedent: int) -> int: ...
	def Destroy(self) -> None: ...
	def Raz(self, t: int) -> None: ...
	def ResetAnd(self) -> None: ...
	def Val(self, t: int) -> int: ...

class IntPatch_RstInt:
	@staticmethod
	def PutVertexOnLine(self, L: IntPatch_Line, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, OtherSurf: Adaptor3d_HSurface, OnFirst: bool, Tol: float) -> None: ...

class IntPatch_SpecialPoints:
	@staticmethod
	def AddCrossUVIsoPoint(self, theQSurf: Adaptor3d_HSurface, thePSurf: Adaptor3d_HSurface, theRefPt: IntSurf_PntOn2S, theTol3d: float, theAddedPoint: IntSurf_PntOn2S, theIsReversed: Optional[bool]) -> bool: ...
	@staticmethod
	def AddPointOnUorVIso(self, theQSurf: Adaptor3d_HSurface, thePSurf: Adaptor3d_HSurface, theRefPt: IntSurf_PntOn2S, theIsU: bool, theIsoParameter: float, theToler: math_Vector, theInitPoint: math_Vector, theInfBound: math_Vector, theSupBound: math_Vector, theAddedPoint: IntSurf_PntOn2S, theIsReversed: Optional[bool]) -> bool: ...
	@staticmethod
	def AddSingularPole(self, theQSurf: Adaptor3d_HSurface, thePSurf: Adaptor3d_HSurface, thePtIso: IntSurf_PntOn2S, theVertex: IntPatch_Point, theAddedPoint: IntSurf_PntOn2S, theIsReversed: Optional[bool], theIsReqRefCheck: Optional[bool]) -> bool: ...
	@staticmethod
	def AdjustPointAndVertex(self, theRefPoint: IntSurf_PntOn2S, theArrPeriods[4]: float, theNewPoint: IntSurf_PntOn2S, theVertex: Optional[IntPatch_Point]) -> None: ...
	@staticmethod
	def ContinueAfterSpecialPoint(self, theQSurf: Adaptor3d_HSurface, thePSurf: Adaptor3d_HSurface, theRefPt: IntSurf_PntOn2S, theSPType: IntPatch_SpecPntType, theTol2D: float, theNewPoint: IntSurf_PntOn2S, theIsReversed: Optional[bool]) -> bool: ...

class IntPatch_TheIWLineOfTheIWalking(Standard_Transient):
	def __init__(self, theAllocator: Optional[IntSurf_Allocator]) -> None: ...
	def AddIndexPassing(self, Index: int) -> None: ...
	def AddPoint(self, P: IntSurf_PntOn2S) -> None: ...
	def AddStatusFirst(self, Closed: bool, HasFirst: bool) -> None: ...
	def AddStatusFirst(self, Closed: bool, HasLast: bool, Index: int, P: IntSurf_PathPoint) -> None: ...
	def AddStatusFirstLast(self, Closed: bool, HasFirst: bool, HasLast: bool) -> None: ...
	def AddStatusLast(self, HasLast: bool) -> None: ...
	def AddStatusLast(self, HasLast: bool, Index: int, P: IntSurf_PathPoint) -> None: ...
	def Cut(self, Index: int) -> None: ...
	def FirstPoint(self) -> IntSurf_PathPoint: ...
	def FirstPointIndex(self) -> int: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsTangentAtBegining(self) -> bool: ...
	def IsTangentAtEnd(self) -> bool: ...
	def LastPoint(self) -> IntSurf_PathPoint: ...
	def LastPointIndex(self) -> int: ...
	def Line(self) -> IntSurf_LineOn2S: ...
	def NbPassingPoint(self) -> int: ...
	def NbPoints(self) -> int: ...
	def PassingPoint(self, Index: int, IndexLine: int, IndexPnts: int) -> None: ...
	def Reverse(self) -> None: ...
	def SetTangencyAtBegining(self, IsTangent: bool) -> None: ...
	def SetTangencyAtEnd(self, IsTangent: bool) -> None: ...
	def SetTangentVector(self, V: gp_Vec, Index: int) -> None: ...
	def TangentVector(self, Index: int) -> gp_Vec: ...
	def Value(self, Index: int) -> IntSurf_PntOn2S: ...

class IntPatch_TheIWalking:
	def __init__(self, Epsilon: float, Deflection: float, Step: float, theToFillHoles: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbLines(self) -> int: ...
	def NbSinglePnts(self) -> int: ...
	def Perform(self, Pnts1: IntSurf_SequenceOfPathPoint, Pnts2: IntSurf_SequenceOfInteriorPoint, Func: IntPatch_TheSurfFunction, S: Adaptor3d_HSurface, Reversed: Optional[bool]) -> None: ...
	def Perform(self, Pnts1: IntSurf_SequenceOfPathPoint, Func: IntPatch_TheSurfFunction, S: Adaptor3d_HSurface, Reversed: Optional[bool]) -> None: ...
	def SetTolerance(self, Epsilon: float, Deflection: float, Step: float) -> None: ...
	def SinglePnt(self, Index: int) -> IntSurf_PathPoint: ...
	def Value(self, Index: int) -> IntPatch_TheIWLineOfTheIWalking: ...

class IntPatch_ThePathPointOfTheSOnBounds:
	def __init__(self) -> None: ...
	def __init__(self, P: gp_Pnt, Tol: float, V: Adaptor3d_HVertex, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def __init__(self, P: gp_Pnt, Tol: float, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def IsNew(self) -> bool: ...
	def Parameter(self) -> float: ...
	def SetValue(self, P: gp_Pnt, Tol: float, V: Adaptor3d_HVertex, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def SetValue(self, P: gp_Pnt, Tol: float, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def Tolerance(self) -> float: ...
	def Value(self) -> gp_Pnt: ...
	def Vertex(self) -> Adaptor3d_HVertex: ...

class IntPatch_TheSOnBounds:
	def __init__(self) -> None: ...
	def AllArcSolution(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def NbSegments(self) -> int: ...
	def Perform(self, F: IntPatch_ArcFunction, Domain: Adaptor3d_TopolTool, TolBoundary: float, TolTangency: float, RecheckOnRegularity: Optional[bool]) -> None: ...
	def Point(self, Index: int) -> IntPatch_ThePathPointOfTheSOnBounds: ...
	def Segment(self, Index: int) -> IntPatch_TheSegmentOfTheSOnBounds: ...

class IntPatch_TheSearchInside:
	def __init__(self) -> None: ...
	def __init__(self, F: IntPatch_TheSurfFunction, Surf: Adaptor3d_HSurface, T: Adaptor3d_TopolTool, Epsilon: float) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Perform(self, F: IntPatch_TheSurfFunction, Surf: Adaptor3d_HSurface, T: Adaptor3d_TopolTool, Epsilon: float) -> None: ...
	def Perform(self, F: IntPatch_TheSurfFunction, Surf: Adaptor3d_HSurface, UStart: float, VStart: float) -> None: ...
	def Value(self, Index: int) -> IntSurf_InteriorPoint: ...

class IntPatch_TheSegmentOfTheSOnBounds:
	def __init__(self) -> None: ...
	def Curve(self) -> Adaptor2d_HCurve2d: ...
	def FirstPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def LastPoint(self) -> IntPatch_ThePathPointOfTheSOnBounds: ...
	def SetLimitPoint(self, V: IntPatch_ThePathPointOfTheSOnBounds, First: bool) -> None: ...
	def SetValue(self, A: Adaptor2d_HCurve2d) -> None: ...

class IntPatch_TheSurfFunction(math_FunctionSetWithDerivatives):
	def __init__(self) -> None: ...
	def __init__(self, PS: Adaptor3d_HSurface, IS: IntSurf_Quadric) -> None: ...
	def __init__(self, IS: IntSurf_Quadric) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction2d(self) -> gp_Dir2d: ...
	def Direction3d(self) -> gp_Vec: ...
	def ISurface(self) -> IntSurf_Quadric: ...
	def IsTangent(self) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def PSurface(self) -> Adaptor3d_HSurface: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Set(self, PS: Adaptor3d_HSurface) -> None: ...
	def Set(self, Tolerance: float) -> None: ...
	def SetImplicitSurface(self, IS: IntSurf_Quadric) -> None: ...
	def Tolerance(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class IntPatch_WLineTool:
	@staticmethod
	def ComputePurgedWLine(self, theWLine: IntPatch_WLine, theS1: Adaptor3d_HSurface, theS2: Adaptor3d_HSurface, theDom1: Adaptor3d_TopolTool, theDom2: Adaptor3d_TopolTool) -> IntPatch_WLine: ...
	@staticmethod
	def JoinWLines(self, theSlin: IntPatch_SequenceOfLine, theSPnt: IntPatch_SequenceOfPoint, theS1: Adaptor3d_HSurface, theS2: Adaptor3d_HSurface, theTol3D: float) -> None: ...

class IntPatch_ALine(IntPatch_Line):
	def __init__(self, C: IntAna_Curve, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, C: IntAna_Curve, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, C: IntAna_Curve, Tang: bool) -> None: ...
	def AddVertex(self, Pnt: IntPatch_Point) -> None: ...
	def ChangeVertex(self, theIndex: int) -> IntPatch_Point: ...
	def ComputeVertexParameters(self, Tol: float) -> None: ...
	def Curve(self) -> IntAna_Curve: ...
	def D1(self, U: float, P: gp_Pnt, Du: gp_Vec) -> bool: ...
	def FindParameter(self, P: gp_Pnt, theParams: TColStd_ListOfReal) -> None: ...
	def FirstParameter(self, IsIncluded: bool) -> float: ...
	def FirstPoint(self) -> IntPatch_Point: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def LastParameter(self, IsIncluded: bool) -> float: ...
	def LastPoint(self) -> IntPatch_Point: ...
	def NbVertex(self) -> int: ...
	def Replace(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def SetFirstPoint(self, IndFirst: int) -> None: ...
	def SetLastPoint(self, IndLast: int) -> None: ...
	def Value(self, U: float) -> gp_Pnt: ...
	def Vertex(self, Index: int) -> IntPatch_Point: ...

class IntPatch_GLine(IntPatch_Line):
	def __init__(self, L: gp_Lin, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, L: gp_Lin, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, L: gp_Lin, Tang: bool) -> None: ...
	def __init__(self, C: gp_Circ, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, C: gp_Circ, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, C: gp_Circ, Tang: bool) -> None: ...
	def __init__(self, E: gp_Elips, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, E: gp_Elips, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, E: gp_Elips, Tang: bool) -> None: ...
	def __init__(self, P: gp_Parab, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, P: gp_Parab, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, P: gp_Parab, Tang: bool) -> None: ...
	def __init__(self, H: gp_Hypr, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, H: gp_Hypr, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, H: gp_Hypr, Tang: bool) -> None: ...
	def AddVertex(self, Pnt: IntPatch_Point) -> None: ...
	def Circle(self) -> gp_Circ: ...
	def ComputeVertexParameters(self, Tol: float) -> None: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstPoint(self) -> IntPatch_Point: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def LastPoint(self) -> IntPatch_Point: ...
	def Line(self) -> gp_Lin: ...
	def NbVertex(self) -> int: ...
	def Parabola(self) -> gp_Parab: ...
	def Replace(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def SetFirstPoint(self, IndFirst: int) -> None: ...
	def SetLastPoint(self, IndLast: int) -> None: ...
	def Vertex(self, Index: int) -> IntPatch_Point: ...

class IntPatch_PointLine(IntPatch_Line):
	def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: Optional[bool]) -> None: ...
	def ChangeVertex(self, Index: int) -> IntPatch_Point: ...
	def ClearVertexes(self) -> None: ...
	@staticmethod
	def CurvatureRadiusOfIntersLine(self, theS1: Adaptor3d_HSurface, theS2: Adaptor3d_HSurface, theUVPoint: IntSurf_PntOn2S) -> float: ...
	def Curve(self) -> IntSurf_LineOn2S: ...
	def IsOutBox(self, P: gp_Pnt) -> bool: ...
	def IsOutSurf1Box(self, P1: gp_Pnt2d) -> bool: ...
	def IsOutSurf2Box(self, P2: gp_Pnt2d) -> bool: ...
	def NbPnts(self) -> int: ...
	def NbVertex(self) -> int: ...
	def Point(self, Index: int) -> IntSurf_PntOn2S: ...
	def RemoveVertex(self, theIndex: int) -> None: ...
	def Vertex(self, Index: int) -> IntPatch_Point: ...

class IntPatch_PolyArc(IntPatch_Polygo):
	def __init__(self, A: Adaptor2d_HCurve2d, NbSample: int, Pfirst: float, Plast: float, BoxOtherPolygon: Bnd_Box2d) -> None: ...
	def Closed(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def Parameter(self, Index: int) -> float: ...
	def Point(self, Index: int) -> gp_Pnt2d: ...
	def SetOffset(self, OffsetX: float, OffsetY: float) -> None: ...

class IntPatch_PolyLine(IntPatch_Polygo):
	def __init__(self) -> None: ...
	def __init__(self, InitDefle: float) -> None: ...
	def NbPoints(self) -> int: ...
	def Point(self, Index: int) -> gp_Pnt2d: ...
	def ResetError(self) -> None: ...
	def SetRLine(self, OnFirst: bool, Line: IntPatch_RLine) -> None: ...
	def SetWLine(self, OnFirst: bool, Line: IntPatch_WLine) -> None: ...

class IntPatch_RLine(IntPatch_PointLine):
	def __init__(self, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, Tang: bool) -> None: ...
	def Add(self, L: IntSurf_LineOn2S) -> None: ...
	def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: Optional[bool]) -> None: ...
	def ArcOnS1(self) -> Adaptor2d_HCurve2d: ...
	def ArcOnS2(self) -> Adaptor2d_HCurve2d: ...
	def ChangeVertex(self, Index: int) -> IntPatch_Point: ...
	def ClearVertexes(self) -> None: ...
	def ComputeVertexParameters(self, Tol: float) -> None: ...
	def Curve(self) -> IntSurf_LineOn2S: ...
	def Dump(self, theMode: int) -> None: ...
	def FirstPoint(self) -> IntPatch_Point: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def HasPolygon(self) -> bool: ...
	def IsArcOnS1(self) -> bool: ...
	def IsArcOnS2(self) -> bool: ...
	def IsOutBox(self, theP: gp_Pnt) -> bool: ...
	def IsOutSurf1Box(self, theP: gp_Pnt2d) -> bool: ...
	def IsOutSurf2Box(self, theP: gp_Pnt2d) -> bool: ...
	def LastPoint(self) -> IntPatch_Point: ...
	def NbPnts(self) -> int: ...
	def NbVertex(self) -> int: ...
	def ParamOnS1(self, p1: float, p2: float) -> None: ...
	def ParamOnS2(self, p1: float, p2: float) -> None: ...
	def Point(self, Index: int) -> IntSurf_PntOn2S: ...
	def RemoveVertex(self, theIndex: int) -> None: ...
	def Replace(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def SetArcOnS1(self, A: Adaptor2d_HCurve2d) -> None: ...
	def SetArcOnS2(self, A: Adaptor2d_HCurve2d) -> None: ...
	def SetCurve(self, theNewCurve: IntSurf_LineOn2S) -> None: ...
	def SetFirstPoint(self, IndFirst: int) -> None: ...
	def SetLastPoint(self, IndLast: int) -> None: ...
	def SetPoint(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def Vertex(self, Index: int) -> IntPatch_Point: ...

class IntPatch_WLine(IntPatch_PointLine):
	def __init__(self, Line: IntSurf_LineOn2S, Tang: bool, Trans1: IntSurf_TypeTrans, Trans2: IntSurf_TypeTrans) -> None: ...
	def __init__(self, Line: IntSurf_LineOn2S, Tang: bool, Situ1: IntSurf_Situation, Situ2: IntSurf_Situation) -> None: ...
	def __init__(self, Line: IntSurf_LineOn2S, Tang: bool) -> None: ...
	def AddVertex(self, Pnt: IntPatch_Point, theIsPrepend: Optional[bool]) -> None: ...
	def ChangeVertex(self, Index: int) -> IntPatch_Point: ...
	def ClearVertexes(self) -> None: ...
	def ComputeVertexParameters(self, Tol: float) -> None: ...
	def Curve(self) -> IntSurf_LineOn2S: ...
	def Dump(self, theMode: int) -> None: ...
	def EnablePurging(self, theIsEnabled: bool) -> None: ...
	def FirstPoint(self) -> IntPatch_Point: ...
	def FirstPoint(self, Indfirst: int) -> IntPatch_Point: ...
	def GetArcOnS1(self) -> Adaptor2d_HCurve2d: ...
	def GetArcOnS2(self) -> Adaptor2d_HCurve2d: ...
	def GetCreatingWay(self) -> False: ...
	def HasArcOnS1(self) -> bool: ...
	def HasArcOnS2(self) -> bool: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def InsertVertexBefore(self, theIndex: int, thePnt: IntPatch_Point) -> None: ...
	def IsOutBox(self, theP: gp_Pnt) -> bool: ...
	def IsOutSurf1Box(self, theP: gp_Pnt2d) -> bool: ...
	def IsOutSurf2Box(self, theP: gp_Pnt2d) -> bool: ...
	def IsPurgingAllowed(self) -> bool: ...
	def LastPoint(self) -> IntPatch_Point: ...
	def LastPoint(self, Indlast: int) -> IntPatch_Point: ...
	def NbPnts(self) -> int: ...
	def NbVertex(self) -> int: ...
	def Point(self, Index: int) -> IntSurf_PntOn2S: ...
	def RemoveVertex(self, theIndex: int) -> None: ...
	def Replace(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def SetArcOnS1(self, A: Adaptor2d_HCurve2d) -> None: ...
	def SetArcOnS2(self, A: Adaptor2d_HCurve2d) -> None: ...
	def SetCreatingWayInfo(self, theAlgo: IntPatch_WLType) -> None: ...
	def SetFirstPoint(self, IndFirst: int) -> None: ...
	def SetLastPoint(self, IndLast: int) -> None: ...
	def SetPeriod(self, pu1: float, pv1: float, pu2: float, pv2: float) -> None: ...
	def SetPoint(self, Index: int, Pnt: IntPatch_Point) -> None: ...
	def U1Period(self) -> float: ...
	def U2Period(self) -> float: ...
	def V1Period(self) -> float: ...
	def V2Period(self) -> float: ...
	def Vertex(self, Index: int) -> IntPatch_Point: ...
