from typing import NewType, Optional

from OCC.Core.HLRAlgo import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopAbs import *
from OCC.Core.TColStd import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *


class HLRAlgo_PolyMask:
	HLRAlgo_PolyMask_EMskOutLin1: int = ...
	HLRAlgo_PolyMask_EMskOutLin2: int = ...
	HLRAlgo_PolyMask_EMskOutLin3: int = ...
	HLRAlgo_PolyMask_EMskGrALin1: int = ...
	HLRAlgo_PolyMask_EMskGrALin2: int = ...
	HLRAlgo_PolyMask_EMskGrALin3: int = ...
	HLRAlgo_PolyMask_FMskBack: int = ...
	HLRAlgo_PolyMask_FMskSide: int = ...
	HLRAlgo_PolyMask_FMskHiding: int = ...
	HLRAlgo_PolyMask_FMskFlat: int = ...
	HLRAlgo_PolyMask_FMskOnOutL: int = ...
	HLRAlgo_PolyMask_FMskOrBack: int = ...
	HLRAlgo_PolyMask_FMskFrBack: int = ...

class HLRAlgo:
	@staticmethod
	def EnlargeMinMax(self, tol: float, Min[16]: float, Max[16]: float) -> None: ...
	@staticmethod
	def InitMinMax(self, Big: float, Min[16]: float, Max[16]: float) -> None: ...
	@staticmethod
	def UpdateMinMax(self, x: float, y: float, z: float, Min[16]: float, Max[16]: float) -> None: ...

class HLRAlgo_BiPoint:
	def __init__(self) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, flag: int) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, flag: int) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, i2: int, i2p1: int, i2p2: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> None: ...
	def __init__(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float, XT1: float, YT1: float, ZT1: float, XT2: float, YT2: float, ZT2: float, Index: int, i1: int, i1p1: int, i1p2: int, i2: int, i2p1: int, i2p2: int, flag: int) -> None: ...
	def Hidden(self) -> bool: ...
	def Hidden(self, B: bool) -> None: ...
	def IntLine(self) -> bool: ...
	def IntLine(self, B: bool) -> None: ...
	def OutLine(self) -> bool: ...
	def OutLine(self, B: bool) -> None: ...
	def Rg1Line(self) -> bool: ...
	def Rg1Line(self, B: bool) -> None: ...
	def RgNLine(self) -> bool: ...
	def RgNLine(self, B: bool) -> None: ...

class HLRAlgo_Coincidence:
	def __init__(self) -> None: ...
	def Set2D(self, FE: int, Param: float) -> None: ...
	def SetState3D(self, stbef: TopAbs_State, staft: TopAbs_State) -> None: ...
	def State3D(self, stbef: TopAbs_State, staft: TopAbs_State) -> None: ...
	def Value2D(self, FE: int, Param: float) -> None: ...

class HLRAlgo_EdgeIterator:
	def __init__(self) -> None: ...
	def Hidden(self, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal) -> None: ...
	def InitHidden(self, status: HLRAlgo_EdgeStatus) -> None: ...
	def InitVisible(self, status: HLRAlgo_EdgeStatus) -> None: ...
	def MoreHidden(self) -> bool: ...
	def MoreVisible(self) -> bool: ...
	def NextHidden(self) -> None: ...
	def NextVisible(self) -> None: ...
	def Visible(self, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal) -> None: ...

class HLRAlgo_EdgeStatus:
	def __init__(self) -> None: ...
	def __init__(self, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal) -> None: ...
	def AllHidden(self) -> bool: ...
	def AllHidden(self, B: bool) -> None: ...
	def AllVisible(self) -> bool: ...
	def AllVisible(self, B: bool) -> None: ...
	def Bounds(self, theStart: float, theTolStart: Standard_ShortReal, theEnd: float, theTolEnd: Standard_ShortReal) -> None: ...
	def Hide(self, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal, OnFace: bool, OnBoundary: bool) -> None: ...
	def HideAll(self) -> None: ...
	def Initialize(self, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal) -> None: ...
	def NbVisiblePart(self) -> int: ...
	def ShowAll(self) -> None: ...
	def VisiblePart(self, Index: int, Start: float, TolStart: Standard_ShortReal, End: float, TolEnd: Standard_ShortReal) -> None: ...

class HLRAlgo_EdgesBlock(Standard_Transient):
	def __init__(self, NbEdges: int) -> None: ...
	def Double(self, I: int) -> bool: ...
	def Double(self, I: int, B: bool) -> None: ...
	def Edge(self, I: int, EI: int) -> None: ...
	def Edge(self, I: int) -> int: ...
	def Internal(self, I: int) -> bool: ...
	def Internal(self, I: int, B: bool) -> None: ...
	def IsoLine(self, I: int) -> bool: ...
	def IsoLine(self, I: int, B: bool) -> None: ...
	def MinMax(self) -> False: ...
	def NbEdges(self) -> int: ...
	def Orientation(self, I: int, Or: TopAbs_Orientation) -> None: ...
	def Orientation(self, I: int) -> TopAbs_Orientation: ...
	def OutLine(self, I: int) -> bool: ...
	def OutLine(self, I: int, B: bool) -> None: ...

class HLRAlgo_Interference:
	def __init__(self) -> None: ...
	def __init__(self, Inters: HLRAlgo_Intersection, Bound: HLRAlgo_Coincidence, Orient: TopAbs_Orientation, Trans: TopAbs_Orientation, BTrans: TopAbs_Orientation) -> None: ...
	def Boundary(self, B: HLRAlgo_Coincidence) -> None: ...
	def Boundary(self) -> HLRAlgo_Coincidence: ...
	def BoundaryTransition(self, BTr: TopAbs_Orientation) -> None: ...
	def BoundaryTransition(self) -> TopAbs_Orientation: ...
	def ChangeBoundary(self) -> HLRAlgo_Coincidence: ...
	def ChangeIntersection(self) -> HLRAlgo_Intersection: ...
	def Intersection(self, I: HLRAlgo_Intersection) -> None: ...
	def Intersection(self) -> HLRAlgo_Intersection: ...
	def Orientation(self, O: TopAbs_Orientation) -> None: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def Transition(self, Tr: TopAbs_Orientation) -> None: ...
	def Transition(self) -> TopAbs_Orientation: ...

class HLRAlgo_Intersection:
	def __init__(self) -> None: ...
	def __init__(self, Ori: TopAbs_Orientation, Lev: int, SegInd: int, Ind: int, P: float, Tol: Standard_ShortReal, S: TopAbs_State) -> None: ...
	def Index(self, Ind: int) -> None: ...
	def Index(self) -> int: ...
	def Level(self, Lev: int) -> None: ...
	def Level(self) -> int: ...
	def Orientation(self, Ori: TopAbs_Orientation) -> None: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def Parameter(self, P: float) -> None: ...
	def Parameter(self) -> float: ...
	def SegIndex(self, SegInd: int) -> None: ...
	def SegIndex(self) -> int: ...
	def State(self, S: TopAbs_State) -> None: ...
	def State(self) -> TopAbs_State: ...
	def Tolerance(self, T: Standard_ShortReal) -> None: ...
	def Tolerance(self) -> Standard_ShortReal: ...

class HLRAlgo_PolyAlgo(Standard_Transient):
	def __init__(self) -> None: ...
	def Clear(self) -> None: ...
	def Hide(self, status: HLRAlgo_EdgeStatus, Index: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> False: ...
	def Init(self, HShell: TColStd_HArray1OfTransient) -> None: ...
	def InitHide(self) -> None: ...
	def InitShow(self) -> None: ...
	def MoreHide(self) -> bool: ...
	def MoreShow(self) -> bool: ...
	def NextHide(self) -> None: ...
	def NextShow(self) -> None: ...
	def PolyShell(self) -> TColStd_Array1OfTransient: ...
	def Show(self, Index: int, reg1: bool, regn: bool, outl: bool, intl: bool) -> False: ...
	def Update(self) -> None: ...

class HLRAlgo_PolyData(Standard_Transient):
	def __init__(self) -> None: ...
	def FaceIndex(self, I: int) -> None: ...
	def FaceIndex(self) -> int: ...
	def HNodes(self, HNodes: TColgp_HArray1OfXYZ) -> None: ...
	def HPHDat(self, HPHDat: HLRAlgo_HArray1OfPHDat) -> None: ...
	def HTData(self, HTData: HLRAlgo_HArray1OfTData) -> None: ...
	def Hiding(self) -> bool: ...
	def Nodes(self) -> TColgp_Array1OfXYZ: ...
	def PHDat(self) -> HLRAlgo_Array1OfPHDat: ...
	def TData(self) -> HLRAlgo_Array1OfTData: ...

class HLRAlgo_PolyInternalData(Standard_Transient):
	def __init__(self, nbNod: int, nbTri: int) -> None: ...
	def DecPINod(self) -> None: ...
	def DecPISeg(self) -> None: ...
	def DecTData(self) -> None: ...
	def Dump(self) -> None: ...
	def IncPINod(self, PINod1: HLRAlgo_Array1OfPINod, PINod2: HLRAlgo_Array1OfPINod) -> None: ...
	def IncPISeg(self, PISeg1: HLRAlgo_Array1OfPISeg, PISeg2: HLRAlgo_Array1OfPISeg) -> None: ...
	def IncTData(self, TData1: HLRAlgo_Array1OfTData, TData2: HLRAlgo_Array1OfTData) -> None: ...
	def IntOutL(self) -> bool: ...
	def IntOutL(self, B: bool) -> None: ...
	def NbPINod(self) -> int: ...
	def NbPISeg(self) -> int: ...
	def NbTData(self) -> int: ...
	def PINod(self) -> HLRAlgo_Array1OfPINod: ...
	def PISeg(self) -> HLRAlgo_Array1OfPISeg: ...
	def Planar(self) -> bool: ...
	def Planar(self, B: bool) -> None: ...
	def TData(self) -> HLRAlgo_Array1OfTData: ...
	def UpdateLinks(self, TData: HLRAlgo_Array1OfTData, PISeg: HLRAlgo_Array1OfPISeg, PINod: HLRAlgo_Array1OfPINod) -> None: ...
	def UpdateLinks(self, ip1: int, ip2: int, ip3: int, TData1: HLRAlgo_Array1OfTData, TData2: HLRAlgo_Array1OfTData, PISeg1: HLRAlgo_Array1OfPISeg, PISeg2: HLRAlgo_Array1OfPISeg, PINod1: HLRAlgo_Array1OfPINod, PINod2: HLRAlgo_Array1OfPINod) -> None: ...

class HLRAlgo_PolyInternalNode(Standard_Transient):
	def __init__(self) -> None: ...

class HLRAlgo_PolyShellData(Standard_Transient):
	def __init__(self, nbFace: int) -> None: ...
	def Edges(self) -> HLRAlgo_ListOfBPoint: ...
	def Hiding(self) -> bool: ...
	def HidingPolyData(self) -> TColStd_Array1OfTransient: ...
	def PolyData(self) -> TColStd_Array1OfTransient: ...
	def UpdateHiding(self, nbHiding: int) -> None: ...

class HLRAlgo_Projector:
	def __init__(self) -> None: ...
	def __init__(self, CS: gp_Ax2) -> None: ...
	def __init__(self, CS: gp_Ax2, Focus: float) -> None: ...
	def __init__(self, T: gp_Trsf, Persp: bool, Focus: float) -> None: ...
	def __init__(self, T: gp_Trsf, Persp: bool, Focus: float, v1: gp_Vec2d, v2: gp_Vec2d, v3: gp_Vec2d) -> None: ...
	def Directions(self, D1: gp_Vec2d, D2: gp_Vec2d, D3: gp_Vec2d) -> None: ...
	def Focus(self) -> float: ...
	def FullTransformation(self) -> gp_Trsf: ...
	def InvertedTransformation(self) -> gp_Trsf: ...
	def Perspective(self) -> bool: ...
	def Project(self, P: gp_Pnt, Pout: gp_Pnt2d) -> None: ...
	def Project(self, P: gp_Pnt, X: float, Y: float, Z: float) -> None: ...
	def Project(self, P: gp_Pnt, D1: gp_Vec, Pout: gp_Pnt2d, D1out: gp_Vec2d) -> None: ...
	def Scaled(self, On: Optional[bool]) -> None: ...
	def Set(self, T: gp_Trsf, Persp: bool, Focus: float) -> None: ...
	def Shoot(self, X: float, Y: float) -> gp_Lin: ...
	def Transform(self, D: gp_Vec) -> None: ...
	def Transform(self, Pnt: gp_Pnt) -> None: ...
	def Transformation(self) -> gp_Trsf: ...

class HLRAlgo_WiresBlock(Standard_Transient):
	def __init__(self, NbWires: int) -> None: ...
	def MinMax(self) -> False: ...
	def NbWires(self) -> int: ...
	def Set(self, I: int, W: HLRAlgo_EdgesBlock) -> None: ...
	def Wire(self, I: int) -> HLRAlgo_EdgesBlock: ...
