from typing import NewType, Optional

from OCC.Core.RWGltf import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class RWGltf_GltfPrimitiveMode:
	RWGltf_GltfPrimitiveMode_UNKNOWN: int = ...
	RWGltf_GltfPrimitiveMode_Points: int = ...
	RWGltf_GltfPrimitiveMode_Lines: int = ...
	RWGltf_GltfPrimitiveMode_LineLoop: int = ...
	RWGltf_GltfPrimitiveMode_LineStrip: int = ...
	RWGltf_GltfPrimitiveMode_Triangles: int = ...
	RWGltf_GltfPrimitiveMode_TriangleStrip: int = ...
	RWGltf_GltfPrimitiveMode_TriangleFan: int = ...

class RWGltf_GltfBufferViewTarget:
	RWGltf_GltfBufferViewTarget_UNKNOWN: int = ...
	RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: int = ...
	RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: int = ...

class RWGltf_GltfArrayType:
	RWGltf_GltfArrayType_UNKNOWN: int = ...
	RWGltf_GltfArrayType_Indices: int = ...
	RWGltf_GltfArrayType_Position: int = ...
	RWGltf_GltfArrayType_Normal: int = ...
	RWGltf_GltfArrayType_Color: int = ...
	RWGltf_GltfArrayType_TCoord0: int = ...
	RWGltf_GltfArrayType_TCoord1: int = ...
	RWGltf_GltfArrayType_Joint: int = ...
	RWGltf_GltfArrayType_Weight: int = ...

class RWGltf_GltfRootElement:
	RWGltf_GltfRootElement_Asset: int = ...
	RWGltf_GltfRootElement_Scenes: int = ...
	RWGltf_GltfRootElement_Scene: int = ...
	RWGltf_GltfRootElement_Nodes: int = ...
	RWGltf_GltfRootElement_Meshes: int = ...
	RWGltf_GltfRootElement_Accessors: int = ...
	RWGltf_GltfRootElement_BufferViews: int = ...
	RWGltf_GltfRootElement_Buffers: int = ...
	RWGltf_GltfRootElement_NB_MANDATORY: int = ...
	RWGltf_GltfRootElement_Animations: int = ...
	RWGltf_GltfRootElement_Materials: int = ...
	RWGltf_GltfRootElement_Programs: int = ...
	RWGltf_GltfRootElement_Samplers: int = ...
	RWGltf_GltfRootElement_Shaders: int = ...
	RWGltf_GltfRootElement_Skins: int = ...
	RWGltf_GltfRootElement_Techniques: int = ...
	RWGltf_GltfRootElement_Textures: int = ...
	RWGltf_GltfRootElement_Images: int = ...
	RWGltf_GltfRootElement_ExtensionsUsed: int = ...
	RWGltf_GltfRootElement_ExtensionsRequired: int = ...
	RWGltf_GltfRootElement_NB: int = ...

class RWGltf_GltfAccessorCompType:
	RWGltf_GltfAccessorCompType_UNKNOWN: int = ...
	RWGltf_GltfAccessorCompType_Int8: int = ...
	RWGltf_GltfAccessorCompType_UInt8: int = ...
	RWGltf_GltfAccessorCompType_Int16: int = ...
	RWGltf_GltfAccessorCompType_UInt16: int = ...
	RWGltf_GltfAccessorCompType_UInt32: int = ...
	RWGltf_GltfAccessorCompType_Float32: int = ...

class RWGltf_GltfAccessorLayout:
	RWGltf_GltfAccessorLayout_UNKNOWN: int = ...
	RWGltf_GltfAccessorLayout_Scalar: int = ...
	RWGltf_GltfAccessorLayout_Vec2: int = ...
	RWGltf_GltfAccessorLayout_Vec3: int = ...
	RWGltf_GltfAccessorLayout_Vec4: int = ...
	RWGltf_GltfAccessorLayout_Mat2: int = ...
	RWGltf_GltfAccessorLayout_Mat3: int = ...
	RWGltf_GltfAccessorLayout_Mat4: int = ...

class RWGltf_GltfAccessor:
	def __init__(self) -> None: ...

class RWGltf_GltfBufferView:
	def __init__(self) -> None: ...

class RWGltf_GltfFace:
	pass

class RWGltf_GltfPrimArrayData:
	def __init__(self) -> None: ...
	def __init__(self, theType: RWGltf_GltfArrayType) -> None: ...

class RWGltf_MaterialCommon(Standard_Transient):
	def __init__(self) -> None: ...

class RWGltf_MaterialMetallicRoughness(Standard_Transient):
	def __init__(self) -> None: ...