from typing import NewType, Optional

from OCC.Core.BRepApprox import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Approx import *
from OCC.Core.AppParCurves import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.IntSurf import *
from OCC.Core.math import *
from OCC.Core.TColStd import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.IntImp import *
from OCC.Core.gp import *
from OCC.Core.ApproxInt import *
from OCC.Core.TColgp import *


class BRepApprox_Approx:
	def __init__(self) -> None: ...
	def IsDone(self) -> bool: ...
	def NbMultiCurves(self) -> int: ...
	def SetParameters(self, Tol3d: float, Tol2d: float, DegMin: int, DegMax: int, NbIterMax: int, NbPntMax: Optional[int], ApproxWithTangency: Optional[bool], Parametrization: Optional[Approx_ParametrizationType]) -> None: ...
	def TolReached2d(self) -> float: ...
	def TolReached3d(self) -> float: ...
	def Value(self, Index: int) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_ApproxLine(Standard_Transient):
	def __init__(self, CurveXYZ: Geom_BSplineCurve, CurveUV1: Geom2d_BSplineCurve, CurveUV2: Geom2d_BSplineCurve) -> None: ...
	def __init__(self, lin: IntSurf_LineOn2S, theTang: Optional[bool]) -> None: ...
	def NbPnts(self) -> int: ...
	def Point(self, Index: int) -> IntSurf_PntOn2S: ...

class BRepApprox_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NbPol: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiBSpCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def Index(self) -> math_IntegerVector: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def SetFirstLambda(self, l1: float) -> None: ...
	def SetLastLambda(self, l2: float) -> None: ...
	def Value(self, X: math_Vector, F: float) -> bool: ...
	def Values(self, X: math_Vector, F: float, G: math_Vector) -> bool: ...

class BRepApprox_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def ErrorGradient(self, Grad: math_Vector, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	def Perform(self, Parameters: math_Vector) -> None: ...
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class BRepApprox_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_MyBSplGradientOfTheComputeLineOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int, lambda1: float, lambda2: float) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_MyGradientOfTheComputeLineBezierOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiCurve: ...

class BRepApprox_MyGradientbisOfTheComputeLineOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiCurve: ...

class BRepApprox_ParFunctionOfMyGradientOfTheComputeLineBezierOfApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiCurve: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def Value(self, X: math_Vector, F: float) -> bool: ...
	def Values(self, X: math_Vector, F: float, G: math_Vector) -> bool: ...

class BRepApprox_ParFunctionOfMyGradientbisOfTheComputeLineOfApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiCurve: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def Value(self, X: math_Vector, F: float) -> bool: ...
	def Values(self, X: math_Vector, F: float, G: math_Vector) -> bool: ...

class BRepApprox_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def ErrorGradient(self, Grad: math_Vector, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	def Perform(self, Parameters: math_Vector) -> None: ...
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class BRepApprox_ParLeastSquareOfMyGradientbisOfTheComputeLineOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def ErrorGradient(self, Grad: math_Vector, F: float, MaxE3d: float, MaxE2d: float) -> None: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	def Perform(self, Parameters: math_Vector) -> None: ...
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class BRepApprox_ResConstraintOfMyGradientOfTheComputeLineBezierOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, SCurv: AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: AppParCurves_HArray1OfConstraintCouple, Bern: math_Matrix, DerivativeBern: math_Matrix, Tolerance: Optional[float]) -> None: ...
	def ConstraintDerivative(self, SSP: BRepApprox_TheMultiLineOfApprox, Parameters: math_Vector, Deg: int, DA: math_Matrix) -> math_Matrix: ...
	def ConstraintMatrix(self) -> math_Matrix: ...
	def Duale(self) -> math_Vector: ...
	def InverseMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...

class BRepApprox_ResConstraintOfMyGradientbisOfTheComputeLineOfApprox:
	def __init__(self, SSP: BRepApprox_TheMultiLineOfApprox, SCurv: AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: AppParCurves_HArray1OfConstraintCouple, Bern: math_Matrix, DerivativeBern: math_Matrix, Tolerance: Optional[float]) -> None: ...
	def ConstraintDerivative(self, SSP: BRepApprox_TheMultiLineOfApprox, Parameters: math_Vector, Deg: int, DA: math_Matrix) -> math_Matrix: ...
	def ConstraintMatrix(self) -> math_Matrix: ...
	def Duale(self) -> math_Vector: ...
	def InverseMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...

class BRepApprox_TheComputeLineBezierOfApprox:
	def __init__(self, Line: BRepApprox_TheMultiLineOfApprox, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def __init__(self, Line: BRepApprox_TheMultiLineOfApprox, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	def __init__(self, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def ChangeValue(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...
	def Error(self, Index: int, tol3d: float, tol2d: float) -> None: ...
	def Init(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def NbMultiCurves(self) -> int: ...
	def Parameters(self, Index: Optional[int]) -> TColStd_Array1OfReal: ...
	def Parametrization(self) -> Approx_ParametrizationType: ...
	def Perform(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
	def SetConstraints(self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def SplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def Value(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...

class BRepApprox_TheComputeLineOfApprox:
	def __init__(self, Line: BRepApprox_TheMultiLineOfApprox, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def __init__(self, Line: BRepApprox_TheMultiLineOfApprox, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	def __init__(self, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def ChangeValue(self) -> AppParCurves_MultiBSpCurve: ...
	def Error(self, tol3d: float, tol2d: float) -> None: ...
	def Init(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def Interpol(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def Parameters(self) -> TColStd_Array1OfReal: ...
	def Perform(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
	def SetConstraints(self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint) -> None: ...
	def SetContinuity(self, C: int) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
	def SetKnotsAndMultiplicities(self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> None: ...
	def SetParameters(self, ThePar: math_Vector) -> None: ...
	def SetPeriodic(self, thePeriodic: bool) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def Value(self) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfApprox(math_FunctionSetWithDerivatives):
	def __init__(self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface) -> None: ...
	def AuxillarSurface1(self) -> BRepAdaptor_Surface: ...
	def AuxillarSurface2(self) -> BRepAdaptor_Surface: ...
	def ComputeParameters(self, ChoixIso: IntImp_ConstIsoparametric, Param: TColStd_Array1OfReal, UVap: math_Vector, BornInf: math_Vector, BornSup: math_Vector, Tolerance: math_Vector) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction(self) -> gp_Dir: ...
	def DirectionOnS1(self) -> gp_Dir2d: ...
	def DirectionOnS2(self) -> gp_Dir2d: ...
	def IsTangent(self, UVap: math_Vector, Param: TColStd_Array1OfReal, BestChoix: IntImp_ConstIsoparametric) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepApprox_TheImpPrmSvSurfacesOfApprox(ApproxInt_SvSurfaces):
	def __init__(self, Surf1: BRepAdaptor_Surface, Surf2: IntSurf_Quadric) -> None: ...
	def __init__(self, Surf1: IntSurf_Quadric, Surf2: BRepAdaptor_Surface) -> None: ...
	def Compute(self, u1: float, v1: float, u2: float, v2: float, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d) -> bool: ...
	def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
	def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S) -> bool: ...
	def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec) -> bool: ...
	def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...
	def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...

class BRepApprox_TheInt2SOfThePrmPrmSvSurfacesOfApprox:
	def __init__(self, Param: TColStd_Array1OfReal, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface, TolTangency: float) -> None: ...
	def __init__(self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface, TolTangency: float) -> None: ...
	def ChangePoint(self) -> IntSurf_PntOn2S: ...
	def Direction(self) -> gp_Dir: ...
	def DirectionOnS1(self) -> gp_Dir2d: ...
	def DirectionOnS2(self) -> gp_Dir2d: ...
	def Function(self) -> BRepApprox_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfApprox: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsTangent(self) -> bool: ...
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot) -> IntImp_ConstIsoparametric: ...
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot, ChoixIso: IntImp_ConstIsoparametric) -> IntImp_ConstIsoparametric: ...
	def Point(self) -> IntSurf_PntOn2S: ...

class BRepApprox_TheMultiLineOfApprox:
	def __init__(self) -> None: ...
	def __init__(self, line: BRepApprox_ApproxLine, PtrSvSurfaces: None, NbP3d: int, NbP2d: int, ApproxU1V1: bool, ApproxU2V2: bool, xo: float, yo: float, zo: float, u1o: float, v1o: float, u2o: float, v2o: float, P2DOnFirst: bool, IndMin: Optional[int], IndMax: Optional[int]) -> None: ...
	def __init__(self, line: BRepApprox_ApproxLine, NbP3d: int, NbP2d: int, ApproxU1V1: bool, ApproxU2V2: bool, xo: float, yo: float, zo: float, u1o: float, v1o: float, u2o: float, v2o: float, P2DOnFirst: bool, IndMin: Optional[int], IndMax: Optional[int]) -> None: ...
	def Dump(self) -> None: ...
	def FirstPoint(self) -> int: ...
	def LastPoint(self) -> int: ...
	def MakeMLBetween(self, Low: int, High: int, NbPointsToInsert: int) -> BRepApprox_TheMultiLineOfApprox: ...
	def MakeMLOneMorePoint(self, Low: int, High: int, indbad: int, OtherLine: BRepApprox_TheMultiLineOfApprox) -> bool: ...
	def NbP2d(self) -> int: ...
	def NbP3d(self) -> int: ...
	def Tangency(self, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	def Tangency(self, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	def Tangency(self, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	def Value(self, MPointIndex: int, tabPt: TColgp_Array1OfPnt) -> None: ...
	def Value(self, MPointIndex: int, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	def Value(self, MPointIndex: int, tabPt: TColgp_Array1OfPnt, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	def WhatStatus(self) -> Approx_Status: ...

class BRepApprox_TheMultiLineToolOfApprox:
	@staticmethod
	def Curvature(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	@staticmethod
	def Curvature(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@staticmethod
	def Curvature(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@staticmethod
	def Dump(self, ML: BRepApprox_TheMultiLineOfApprox) -> None: ...
	@staticmethod
	def FirstPoint(self, ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
	@staticmethod
	def LastPoint(self, ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
	@staticmethod
	def MakeMLBetween(self, ML: BRepApprox_TheMultiLineOfApprox, I1: int, I2: int, NbPMin: int) -> BRepApprox_TheMultiLineOfApprox: ...
	@staticmethod
	def MakeMLOneMorePoint(self, ML: BRepApprox_TheMultiLineOfApprox, I1: int, I2: int, indbad: int, OtherLine: BRepApprox_TheMultiLineOfApprox) -> bool: ...
	@staticmethod
	def NbP2d(self, ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
	@staticmethod
	def NbP3d(self, ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
	@staticmethod
	def Tangency(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	@staticmethod
	def Tangency(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@staticmethod
	def Tangency(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@staticmethod
	def Value(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabPt: TColgp_Array1OfPnt) -> None: ...
	@staticmethod
	def Value(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	@staticmethod
	def Value(self, ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabPt: TColgp_Array1OfPnt, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	@staticmethod
	def WhatStatus(self, ML: BRepApprox_TheMultiLineOfApprox, I1: int, I2: int) -> Approx_Status: ...

class BRepApprox_ThePrmPrmSvSurfacesOfApprox(ApproxInt_SvSurfaces):
	def __init__(self, Surf1: BRepAdaptor_Surface, Surf2: BRepAdaptor_Surface) -> None: ...
	def Compute(self, u1: float, v1: float, u2: float, v2: float, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d) -> bool: ...
	def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
	def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S) -> bool: ...
	def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec) -> bool: ...
	def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...
	def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...

class BRepApprox_TheZerImpFuncOfTheImpPrmSvSurfacesOfApprox(math_FunctionSetWithDerivatives):
	def __init__(self) -> None: ...
	def __init__(self, PS: BRepAdaptor_Surface, IS: IntSurf_Quadric) -> None: ...
	def __init__(self, IS: IntSurf_Quadric) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction2d(self) -> gp_Dir2d: ...
	def Direction3d(self) -> gp_Vec: ...
	def ISurface(self) -> IntSurf_Quadric: ...
	def IsTangent(self) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def PSurface(self) -> BRepAdaptor_Surface: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Set(self, PS: BRepAdaptor_Surface) -> None: ...
	def Set(self, Tolerance: float) -> None: ...
	def SetImplicitSurface(self, IS: IntSurf_Quadric) -> None: ...
	def Tolerance(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...
