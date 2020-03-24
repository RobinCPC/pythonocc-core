from typing import NewType, Optional

from OCC.Core.BRepOffset import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.BRepAlgo import *
from OCC.Core.TopAbs import *
from OCC.Core.GeomAbs import *
from OCC.Core.TCollection import *
from OCC.Core.BRepTools import *
from OCC.Core.TopLoc import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *


class BRepOffset_Error:
	BRepOffset_NoError: int = ...
	BRepOffset_UnknownError: int = ...
	BRepOffset_BadNormalsOnGeometry: int = ...
	BRepOffset_C0Geometry: int = ...
	BRepOffset_NullOffset: int = ...
	BRepOffset_NotConnectedShell: int = ...

class BRepOffsetSimple_Status:
	BRepOffsetSimple_OK: int = ...
	BRepOffsetSimple_NullInputShape: int = ...
	BRepOffsetSimple_ErrorOffsetComputation: int = ...
	BRepOffsetSimple_ErrorWallFaceComputation: int = ...
	BRepOffsetSimple_ErrorInvalidNbShells: int = ...
	BRepOffsetSimple_ErrorNonClosedShell: int = ...

class BRepOffset_Mode:
	BRepOffset_Skin: int = ...
	BRepOffset_Pipe: int = ...
	BRepOffset_RectoVerso: int = ...

class BRepOffset_Type:
	BRepOffset_Concave: int = ...
	BRepOffset_Convex: int = ...
	BRepOffset_Tangent: int = ...
	BRepOffset_FreeBoundary: int = ...
	BRepOffset_Other: int = ...

class BRepOffset_Status:
	BRepOffset_Good: int = ...
	BRepOffset_Reversed: int = ...
	BRepOffset_Degenerated: int = ...
	BRepOffset_Unknown: int = ...

class BRepOffset:
	@staticmethod
	def CollapseSingularities(self, theSurface: Geom_Surface, theFace: TopoDS_Face, thePrecision: float) -> Geom_Surface: ...
	@staticmethod
	def Surface(self, Surface: Geom_Surface, Offset: float, theStatus: BRepOffset_Status, allowC0: Optional[bool]) -> Geom_Surface: ...

class BRepOffset_Analyse:
	def __init__(self) -> None: ...
	def __init__(self, S: TopoDS_Shape, Angle: float) -> None: ...
	def AddFaces(self, Face: TopoDS_Face, Co: TopoDS_Compound, Map: TopTools_MapOfShape, Type: BRepOffset_Type) -> None: ...
	def AddFaces(self, Face: TopoDS_Face, Co: TopoDS_Compound, Map: TopTools_MapOfShape, Type1: BRepOffset_Type, Type2: BRepOffset_Type) -> None: ...
	def Ancestors(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Clear(self) -> None: ...
	def Edges(self, V: TopoDS_Vertex, T: BRepOffset_Type, L: TopTools_ListOfShape) -> None: ...
	def Edges(self, F: TopoDS_Face, T: BRepOffset_Type, L: TopTools_ListOfShape) -> None: ...
	def Explode(self, L: TopTools_ListOfShape, Type: BRepOffset_Type) -> None: ...
	def Explode(self, L: TopTools_ListOfShape, Type1: BRepOffset_Type, Type2: BRepOffset_Type) -> None: ...
	def HasAncestor(self, S: TopoDS_Shape) -> bool: ...
	def IsDone(self) -> bool: ...
	def Perform(self, S: TopoDS_Shape, Angle: float) -> None: ...
	def TangentEdges(self, Edge: TopoDS_Edge, Vertex: TopoDS_Vertex, Edges: TopTools_ListOfShape) -> None: ...
	def Type(self, E: TopoDS_Edge) -> BRepOffset_ListOfInterval: ...

class BRepOffset_Inter2d:
	@staticmethod
	def Compute(self, AsDes: BRepAlgo_AsDes, F: TopoDS_Face, NewEdges: TopTools_IndexedMapOfShape, Tol: float, theDMVV: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def ConnexIntByInt(self, FI: TopoDS_Face, OFI: BRepOffset_Offset, MES: TopTools_DataMapOfShapeShape, Build: TopTools_DataMapOfShapeShape, AsDes2d: BRepAlgo_AsDes, Offset: float, Tol: float, FacesWithVerts: TopTools_IndexedMapOfShape, theDMVV: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def ConnexIntByIntInVert(self, FI: TopoDS_Face, OFI: BRepOffset_Offset, MES: TopTools_DataMapOfShapeShape, Build: TopTools_DataMapOfShapeShape, AsDes: BRepAlgo_AsDes, AsDes2d: BRepAlgo_AsDes, Tol: float, theDMVV: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def ExtentEdge(self, E: TopoDS_Edge, NE: TopoDS_Edge, theOffset: float) -> None: ...
	@staticmethod
	def FuseVertices(self, theDMVV: TopTools_IndexedDataMapOfShapeListOfShape, theAsDes: BRepAlgo_AsDes) -> None: ...

class BRepOffset_Inter3d:
	def __init__(self, AsDes: BRepAlgo_AsDes, Side: TopAbs_State, Tol: float) -> None: ...
	def AddCommonEdges(self, SetOfFaces: TopTools_ListOfShape) -> None: ...
	def AsDes(self) -> BRepAlgo_AsDes: ...
	def CompletInt(self, SetOfFaces: TopTools_ListOfShape, InitOffsetFace: BRepAlgo_Image) -> None: ...
	def ConnexIntByArc(self, SetOfFaces: TopTools_ListOfShape, ShapeInit: TopoDS_Shape, Analyse: BRepOffset_Analyse, InitOffsetFace: BRepAlgo_Image) -> None: ...
	def ConnexIntByInt(self, SI: TopoDS_Shape, MapSF: BRepOffset_DataMapOfShapeOffset, A: BRepOffset_Analyse, MES: TopTools_DataMapOfShapeShape, Build: TopTools_DataMapOfShapeShape, Failed: TopTools_ListOfShape, bIsPlanar: Optional[bool]) -> None: ...
	def ContextIntByArc(self, ContextFaces: TopTools_IndexedMapOfShape, ExtentContext: bool, Analyse: BRepOffset_Analyse, InitOffsetFace: BRepAlgo_Image, InitOffsetEdge: BRepAlgo_Image) -> None: ...
	def ContextIntByInt(self, ContextFaces: TopTools_IndexedMapOfShape, ExtentContext: bool, MapSF: BRepOffset_DataMapOfShapeOffset, A: BRepOffset_Analyse, MES: TopTools_DataMapOfShapeShape, Build: TopTools_DataMapOfShapeShape, Failed: TopTools_ListOfShape, bIsPlanar: Optional[bool]) -> None: ...
	def FaceInter(self, F1: TopoDS_Face, F2: TopoDS_Face, InitOffsetFace: BRepAlgo_Image) -> None: ...
	def IsDone(self, F1: TopoDS_Face, F2: TopoDS_Face) -> bool: ...
	def NewEdges(self) -> TopTools_IndexedMapOfShape: ...
	def SetDone(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def TouchedFaces(self) -> TopTools_IndexedMapOfShape: ...

class BRepOffset_Interval:
	def __init__(self) -> None: ...
	def __init__(self, U1: float, U2: float, Type: BRepOffset_Type) -> None: ...
	def First(self, U: float) -> None: ...
	def First(self) -> float: ...
	def Last(self, U: float) -> None: ...
	def Last(self) -> float: ...
	def Type(self, T: BRepOffset_Type) -> None: ...
	def Type(self) -> BRepOffset_Type: ...

class BRepOffset_MakeLoops:
	def __init__(self) -> None: ...
	def Build(self, LF: TopTools_ListOfShape, AsDes: BRepAlgo_AsDes, Image: BRepAlgo_Image) -> None: ...
	def BuildFaces(self, LF: TopTools_ListOfShape, AsDes: BRepAlgo_AsDes, Image: BRepAlgo_Image) -> None: ...
	def BuildOnContext(self, LContext: TopTools_ListOfShape, Analyse: BRepOffset_Analyse, AsDes: BRepAlgo_AsDes, Image: BRepAlgo_Image, InSide: bool) -> None: ...

class BRepOffset_MakeOffset:
	def __init__(self) -> None: ...
	def __init__(self, S: TopoDS_Shape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], Thickening: Optional[bool], RemoveIntEdges: Optional[bool]) -> None: ...
	def AddFace(self, F: TopoDS_Face) -> None: ...
	def CheckInputData(self) -> bool: ...
	def Clear(self) -> None: ...
	def ClosingFaces(self) -> TopTools_IndexedMapOfShape: ...
	def Error(self) -> BRepOffset_Error: ...
	def GetBadShape(self) -> TopoDS_Shape: ...
	def GetJoinType(self) -> GeomAbs_JoinType: ...
	def Initialize(self, S: TopoDS_Shape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], Thickening: Optional[bool], RemoveIntEdges: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def MakeOffsetShape(self) -> None: ...
	def MakeThickSolid(self) -> None: ...
	def OffsetEdgesFromShapes(self) -> BRepAlgo_Image: ...
	def OffsetFacesFromShapes(self) -> BRepAlgo_Image: ...
	def SetOffsetOnFace(self, F: TopoDS_Face, Off: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class BRepOffset_MakeSimpleOffset:
	def __init__(self) -> None: ...
	def __init__(self, theInputShape: TopoDS_Shape, theOffsetValue: float) -> None: ...
	def Generated(self, theShape: TopoDS_Shape) -> TopoDS_Shape: ...
	def GetBuildSolidFlag(self) -> bool: ...
	def GetError(self) -> False: ...
	def GetErrorMessage(self) -> TCollection_AsciiString: ...
	def GetOffsetValue(self) -> float: ...
	def GetResultShape(self) -> TopoDS_Shape: ...
	def GetTolerance(self) -> float: ...
	def Initialize(self, theInputShape: TopoDS_Shape, theOffsetValue: float) -> None: ...
	def IsDone(self) -> bool: ...
	def Modified(self, theShape: TopoDS_Shape) -> TopoDS_Shape: ...
	def Perform(self) -> None: ...
	def SetBuildSolidFlag(self, theBuildFlag: bool) -> None: ...
	def SetOffsetValue(self, theOffsetValue: float) -> None: ...
	def SetTolerance(self, theValue: float) -> None: ...

class BRepOffset_Offset:
	def __init__(self) -> None: ...
	def __init__(self, Face: TopoDS_Face, Offset: float, OffsetOutside: Optional[bool], JoinType: Optional[GeomAbs_JoinType]) -> None: ...
	def __init__(self, Face: TopoDS_Face, Offset: float, Created: TopTools_DataMapOfShapeShape, OffsetOutside: Optional[bool], JoinType: Optional[GeomAbs_JoinType]) -> None: ...
	def __init__(self, Path: TopoDS_Edge, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Offset: float, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def __init__(self, Path: TopoDS_Edge, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Offset: float, FirstEdge: TopoDS_Edge, LastEdge: TopoDS_Edge, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def __init__(self, Vertex: TopoDS_Vertex, LEdge: TopTools_ListOfShape, Offset: float, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def Generated(self, Shape: TopoDS_Shape) -> TopoDS_Shape: ...
	def Init(self, Face: TopoDS_Face, Offset: float, OffsetOutside: Optional[bool], JoinType: Optional[GeomAbs_JoinType]) -> None: ...
	def Init(self, Face: TopoDS_Face, Offset: float, Created: TopTools_DataMapOfShapeShape, OffsetOutside: Optional[bool], JoinType: Optional[GeomAbs_JoinType]) -> None: ...
	def Init(self, Path: TopoDS_Edge, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Offset: float, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def Init(self, Path: TopoDS_Edge, Edge1: TopoDS_Edge, Edge2: TopoDS_Edge, Offset: float, FirstEdge: TopoDS_Edge, LastEdge: TopoDS_Edge, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def Init(self, Vertex: TopoDS_Vertex, LEdge: TopTools_ListOfShape, Offset: float, Polynomial: Optional[bool], Tol: Optional[float], Conti: Optional[GeomAbs_Shape]) -> None: ...
	def Init(self, Edge: TopoDS_Edge, Offset: float) -> None: ...
	def InitialShape(self) -> TopoDS_Shape: ...
	def Status(self) -> BRepOffset_Status: ...

class BRepOffset_SimpleOffset(BRepTools_Modification):
	def __init__(self, theInputShape: TopoDS_Shape, theOffsetValue: float, theTolerance: float) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location, Tol: float) -> bool: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve, Tol: float) -> bool: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge, P: float, Tol: float) -> bool: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt, Tol: float) -> bool: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location, Tol: float, RevWires: bool, RevFace: bool) -> bool: ...

class BRepOffset_Tool:
	@staticmethod
	def BuildNeighbour(self, W: TopoDS_Wire, F: TopoDS_Face, NOnV1: TopTools_DataMapOfShapeShape, NOnV2: TopTools_DataMapOfShapeShape) -> None: ...
	@staticmethod
	def CheckBounds(self, F: TopoDS_Face, Analyse: BRepOffset_Analyse, enlargeU: bool, enlargeVfirst: bool, enlargeVlast: bool) -> None: ...
	@staticmethod
	def CheckPlanesNormals(self, theFace1: TopoDS_Face, theFace2: TopoDS_Face, theTolAng: Optional[float]) -> bool: ...
	@staticmethod
	def CorrectOrientation(self, SI: TopoDS_Shape, NewEdges: TopTools_IndexedMapOfShape, AsDes: BRepAlgo_AsDes, InitOffset: BRepAlgo_Image, Offset: float) -> None: ...
	@staticmethod
	def Deboucle3D(self, S: TopoDS_Shape, Boundary: TopTools_MapOfShape) -> TopoDS_Shape: ...
	@staticmethod
	def EdgeVertices(self, E: TopoDS_Edge, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@staticmethod
	def EnLargeFace(self, F: TopoDS_Face, NF: TopoDS_Face, ChangeGeom: bool, UpDatePCurve: Optional[bool], enlargeU: Optional[bool], enlargeVfirst: Optional[bool], enlargeVlast: Optional[bool], theExtensionMode: Optional[int], theLenBeforeUfirst: Optional[float], theLenAfterUlast: Optional[float], theLenBeforeVfirst: Optional[float], theLenAfterVlast: Optional[float]) -> bool: ...
	@staticmethod
	def ExtentFace(self, F: TopoDS_Face, ConstShapes: TopTools_DataMapOfShapeShape, ToBuild: TopTools_DataMapOfShapeShape, Side: TopAbs_State, TolConf: float, NF: TopoDS_Face) -> None: ...
	@staticmethod
	def FindCommonShapes(self, theF1: TopoDS_Face, theF2: TopoDS_Face, theLE: TopTools_ListOfShape, theLV: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def FindCommonShapes(self, theS1: TopoDS_Shape, theS2: TopoDS_Shape, theType: TopAbs_ShapeEnum, theLSC: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def Gabarit(self, aCurve: Geom_Curve) -> float: ...
	@staticmethod
	def Inter2d(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, LV: TopTools_ListOfShape, Tol: float) -> None: ...
	@staticmethod
	def Inter3D(self, F1: TopoDS_Face, F2: TopoDS_Face, LInt1: TopTools_ListOfShape, LInt2: TopTools_ListOfShape, Side: TopAbs_State, RefEdge: TopoDS_Edge, IsRefEdgeDefined: Optional[bool]) -> None: ...
	@staticmethod
	def InterOrExtent(self, F1: TopoDS_Face, F2: TopoDS_Face, LInt1: TopTools_ListOfShape, LInt2: TopTools_ListOfShape, Side: TopAbs_State) -> None: ...
	@staticmethod
	def MapVertexEdges(self, S: TopoDS_Shape, MVE: TopTools_DataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def OriEdgeInFace(self, E: TopoDS_Edge, F: TopoDS_Face) -> TopAbs_Orientation: ...
	@staticmethod
	def OrientSection(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, O1: TopAbs_Orientation, O2: TopAbs_Orientation) -> None: ...
	@staticmethod
	def PipeInter(self, F1: TopoDS_Face, F2: TopoDS_Face, LInt1: TopTools_ListOfShape, LInt2: TopTools_ListOfShape, Side: TopAbs_State) -> None: ...
	@staticmethod
	def TryProject(self, F1: TopoDS_Face, F2: TopoDS_Face, Edges: TopTools_ListOfShape, LInt1: TopTools_ListOfShape, LInt2: TopTools_ListOfShape, Side: TopAbs_State, TolConf: float) -> bool: ...