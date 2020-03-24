from typing import NewType, Optional

from OCC.Core.TopoDSToStep import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Transfer import *
from OCC.Core.TopoDS import *
from OCC.Core.TCollection import *
from OCC.Core.MoniTool import *
from OCC.Core.StepShape import *
from OCC.Core.TColStd import *


class TopoDSToStep_MakeEdgeError:
	TopoDSToStep_EdgeDone: int = ...
	TopoDSToStep_NonManifoldEdge: int = ...
	TopoDSToStep_EdgeOther: int = ...

class TopoDSToStep_BuilderError:
	TopoDSToStep_BuilderDone: int = ...
	TopoDSToStep_NoFaceMapped: int = ...
	TopoDSToStep_BuilderOther: int = ...

class TopoDSToStep_MakeVertexError:
	TopoDSToStep_VertexDone: int = ...
	TopoDSToStep_VertexOther: int = ...

class TopoDSToStep_MakeWireError:
	TopoDSToStep_WireDone: int = ...
	TopoDSToStep_NonManifoldWire: int = ...
	TopoDSToStep_WireOther: int = ...

class TopoDSToStep_MakeFaceError:
	TopoDSToStep_FaceDone: int = ...
	TopoDSToStep_InfiniteFace: int = ...
	TopoDSToStep_NonManifoldFace: int = ...
	TopoDSToStep_NoWireMapped: int = ...
	TopoDSToStep_FaceOther: int = ...

class TopoDSToStep_FacetedError:
	TopoDSToStep_FacetedDone: int = ...
	TopoDSToStep_SurfaceNotPlane: int = ...
	TopoDSToStep_PCurveNotLinear: int = ...

class TopoDSToStep:
	@staticmethod
	def AddResult(self, FP: Transfer_FinderProcess, Shape: TopoDS_Shape, entity: Standard_Transient) -> None: ...
	@staticmethod
	def AddResult(self, FP: Transfer_FinderProcess, Tool: TopoDSToStep_Tool) -> None: ...
	@staticmethod
	def DecodeBuilderError(self, E: TopoDSToStep_BuilderError) -> TCollection_HAsciiString: ...
	@staticmethod
	def DecodeEdgeError(self, E: TopoDSToStep_MakeEdgeError) -> TCollection_HAsciiString: ...
	@staticmethod
	def DecodeFaceError(self, E: TopoDSToStep_MakeFaceError) -> TCollection_HAsciiString: ...
	@staticmethod
	def DecodeVertexError(self, E: TopoDSToStep_MakeVertexError) -> TCollection_HAsciiString: ...
	@staticmethod
	def DecodeWireError(self, E: TopoDSToStep_MakeWireError) -> TCollection_HAsciiString: ...

class TopoDSToStep_FacetedTool:
	@staticmethod
	def CheckTopoDSShape(self, SH: TopoDS_Shape) -> TopoDSToStep_FacetedError: ...

class TopoDSToStep_Root:
	def IsDone(self) -> bool: ...

class TopoDSToStep_Tool:
	def __init__(self) -> None: ...
	def __init__(self, M: MoniTool_DataMapOfShapeTransient, FacetedContext: bool) -> None: ...
	def Bind(self, S: TopoDS_Shape, T: StepShape_TopologicalRepresentationItem) -> None: ...
	def CurrentEdge(self) -> TopoDS_Edge: ...
	def CurrentFace(self) -> TopoDS_Face: ...
	def CurrentShell(self) -> TopoDS_Shell: ...
	def CurrentVertex(self) -> TopoDS_Vertex: ...
	def CurrentWire(self) -> TopoDS_Wire: ...
	def Faceted(self) -> bool: ...
	def Find(self, S: TopoDS_Shape) -> StepShape_TopologicalRepresentationItem: ...
	def Init(self, M: MoniTool_DataMapOfShapeTransient, FacetedContext: bool) -> None: ...
	def IsBound(self, S: TopoDS_Shape) -> bool: ...
	def Lowest3DTolerance(self) -> float: ...
	def Map(self) -> MoniTool_DataMapOfShapeTransient: ...
	def PCurveMode(self) -> int: ...
	def SetCurrentEdge(self, E: TopoDS_Edge) -> None: ...
	def SetCurrentFace(self, F: TopoDS_Face) -> None: ...
	def SetCurrentShell(self, S: TopoDS_Shell) -> None: ...
	def SetCurrentVertex(self, V: TopoDS_Vertex) -> None: ...
	def SetCurrentWire(self, W: TopoDS_Wire) -> None: ...
	def SetSurfaceReversed(self, B: bool) -> None: ...
	def SurfaceReversed(self) -> bool: ...

class TopoDSToStep_Builder(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_BuilderError: ...
	def Init(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeBrepWithVoids(TopoDSToStep_Root):
	def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_BrepWithVoids: ...

class TopoDSToStep_MakeFacetedBrep(TopoDSToStep_Root):
	def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess) -> None: ...
	def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_FacetedBrep: ...

class TopoDSToStep_MakeFacetedBrepAndBrepWithVoids(TopoDSToStep_Root):
	def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_FacetedBrepAndBrepWithVoids: ...

class TopoDSToStep_MakeGeometricCurveSet(TopoDSToStep_Root):
	def __init__(self, SH: TopoDS_Shape, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_GeometricCurveSet: ...

class TopoDSToStep_MakeManifoldSolidBrep(TopoDSToStep_Root):
	def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess) -> None: ...
	def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_ManifoldSolidBrep: ...

class TopoDSToStep_MakeShellBasedSurfaceModel(TopoDSToStep_Root):
	def __init__(self, F: TopoDS_Face, FP: Transfer_FinderProcess) -> None: ...
	def __init__(self, S: TopoDS_Shell, FP: Transfer_FinderProcess) -> None: ...
	def __init__(self, S: TopoDS_Solid, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_ShellBasedSurfaceModel: ...

class TopoDSToStep_MakeStepEdge(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, E: TopoDS_Edge, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_MakeEdgeError: ...
	def Init(self, E: TopoDS_Edge, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepFace(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, F: TopoDS_Face, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_MakeFaceError: ...
	def Init(self, F: TopoDS_Face, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepVertex(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, V: TopoDS_Vertex, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_MakeVertexError: ...
	def Init(self, V: TopoDS_Vertex, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_MakeStepWire(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, W: TopoDS_Wire, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_MakeWireError: ...
	def Init(self, W: TopoDS_Wire, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> StepShape_TopologicalRepresentationItem: ...

class TopoDSToStep_WireframeBuilder(TopoDSToStep_Root):
	def __init__(self) -> None: ...
	def __init__(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Error(self) -> TopoDSToStep_BuilderError: ...
	def GetTrimmedCurveFromEdge(self, E: TopoDS_Edge, F: TopoDS_Face, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient) -> bool: ...
	def GetTrimmedCurveFromFace(self, F: TopoDS_Face, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient) -> bool: ...
	def GetTrimmedCurveFromShape(self, S: TopoDS_Shape, M: MoniTool_DataMapOfShapeTransient, L: TColStd_HSequenceOfTransient) -> bool: ...
	def Init(self, S: TopoDS_Shape, T: TopoDSToStep_Tool, FP: Transfer_FinderProcess) -> None: ...
	def Value(self) -> TColStd_HSequenceOfTransient: ...
