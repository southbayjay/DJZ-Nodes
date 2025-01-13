NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

try:
    from .AspectSize import AspectSize
    NODE_CLASS_MAPPINGS["AspectSize"] = AspectSize
    NODE_DISPLAY_NAME_MAPPINGS["AspectSize"] = "Aspect Size"
except ImportError:
    print("Unable to import AspectSize. This node will not be available.")

try:
    from .AspectSizeV2 import AspectSizeV2
    NODE_CLASS_MAPPINGS["AspectSizeV2"] = AspectSizeV2
    NODE_DISPLAY_NAME_MAPPINGS["AspectSizeV2"] = "Aspect Size V2"
except ImportError:
    print("Unable to import AspectSizeV2. This node will not be available.")

try:
    from .ImageSizeAdjuster import ImageSizeAdjuster
    NODE_CLASS_MAPPINGS["ImageSizeAdjuster"] = ImageSizeAdjuster
    NODE_DISPLAY_NAME_MAPPINGS["ImageSizeAdjuster"] = "Image Size Adjuster"
except ImportError:
    print("Unable to import ImageSizeAdjuster. This node will not be available.")

try:
    from .ImageSizeAdjusterV2 import ImageSizeAdjusterV2
    NODE_CLASS_MAPPINGS["ImageSizeAdjusterV2"] = ImageSizeAdjusterV2
    NODE_DISPLAY_NAME_MAPPINGS["ImageSizeAdjusterV2"] = "Image Size Adjuster V2"
except ImportError:
    print("Unable to import ImageSizeAdjusterV2. This node will not be available.")

try:
    from .ZenkaiPrompt import ZenkaiPrompt
    NODE_CLASS_MAPPINGS["ZenkaiPrompt"] = ZenkaiPrompt
    NODE_DISPLAY_NAME_MAPPINGS["ZenkaiPrompt"] = "Zenkai-Prompt"
except ImportError:
    print("Unable to import ZenkaiPrompt. This node will not be available.")

try:
    from .ZenkaiPromptV2 import ZenkaiPromptV2
    NODE_CLASS_MAPPINGS["ZenkaiPromptV2"] = ZenkaiPromptV2
    NODE_DISPLAY_NAME_MAPPINGS["ZenkaiPromptV2"] = "Zenkai-Prompt V2"
except ImportError:
    print("Unable to import ZenkaiPromptV2. This node will not be available.")

try:
    from .ZenkaiWildcard import ZenkaiWildcard
    NODE_CLASS_MAPPINGS["ZenkaiWildcard"] = ZenkaiWildcard
    NODE_DISPLAY_NAME_MAPPINGS["ZenkaiWildcard"] = "Zenkai-Wildcard"
except ImportError:
    print("Unable to import ZenkaiWildcard. This node will not be available.")

try:
    from .ZenkaiWildcardV2 import ZenkaiWildcardV2
    NODE_CLASS_MAPPINGS["ZenkaiWildcardV2"] = ZenkaiWildcardV2
    NODE_DISPLAY_NAME_MAPPINGS["ZenkaiWildcardV2"] = "Zenkai-Wildcard V2"
except ImportError:
    print("Unable to import ZenkaiWildcardV2. This node will not be available.")

try:
    from .StringWeights import StringWeights
    NODE_CLASS_MAPPINGS["StringWeights"] = StringWeights
    NODE_DISPLAY_NAME_MAPPINGS["StringWeights"] = "String Weights"
except ImportError:
    print("Unable to import StringWeights. This node will not be available.")

try:
    from .PromptCleaner import PromptCleaner
    NODE_CLASS_MAPPINGS["PromptCleaner"] = PromptCleaner
    NODE_DISPLAY_NAME_MAPPINGS["PromptCleaner"] = "Prompt Cleaner"
except ImportError:
    print("Unable to import PromptCleaner. This node will not be available.")

try:
    from .PromptSwap import PromptSwap
    NODE_CLASS_MAPPINGS["PromptSwap"] = PromptSwap
    NODE_DISPLAY_NAME_MAPPINGS["PromptSwap"] = "Prompt Swap"
except ImportError:
    print("Unable to import PromptSwap. This node will not be available.")


try:
    from .StringPainter import StringPainter
    NODE_CLASS_MAPPINGS["StringPainter"] = StringPainter
    NODE_DISPLAY_NAME_MAPPINGS["StringPainter"] = "String Painter"
except ImportError:
    print("Unable to import StringPainter. This node will not be available.")

try:
    from .StringPainterV2 import StringPainterV2
    NODE_CLASS_MAPPINGS["StringPainterV2"] = StringPainterV2
    NODE_DISPLAY_NAME_MAPPINGS["StringPainterV2"] = "String Painter V2"
except ImportError:
    print("Unable to import StringPainterV2. This node will not be available.")

try:
    from .FFXFADEORAMA import FFXFADEORAMA
    NODE_CLASS_MAPPINGS["FFXFADEORAMA"] = FFXFADEORAMA
    NODE_DISPLAY_NAME_MAPPINGS["FFXFADEORAMA"] = "FFX Fade-O-Rama"
except ImportError:
    print("Unable to import FFXFADEORAMA. This node will not be available.")

try:
    from .ProjectFilePathNode import ProjectFilePathNode
    NODE_CLASS_MAPPINGS["ProjectFilePathNode"] = ProjectFilePathNode
    NODE_DISPLAY_NAME_MAPPINGS["ProjectFilePathNode"] = "Project File Path Generator"
except ImportError:
    print("Unable to import ProjectFilePathNode. This node will not be available.")

try:
    from .CaptionsToPromptList import CaptionsToPromptList
    NODE_CLASS_MAPPINGS["CaptionsToPromptList"] = CaptionsToPromptList
    NODE_DISPLAY_NAME_MAPPINGS["CaptionsToPromptList"] = "Captions To Prompt List"
except ImportError:
    print("Unable to import CaptionsToPromptList. This node will not be available.")

try:
    from .ImageSizeAdjusterV3 import ImageSizeAdjusterV3
    NODE_CLASS_MAPPINGS["ImageSizeAdjusterV3"] = ImageSizeAdjusterV3
    NODE_DISPLAY_NAME_MAPPINGS["ImageSizeAdjusterV3"] = "Image Size Adjuster V3"
except ImportError:
    print("Unable to import ImageSizeAdjusterV3. This node will not be available.")

try:
    from .DJZLoadLatent import DJZLoadLatent
    NODE_CLASS_MAPPINGS["DJZ-LoadLatent"] = DJZLoadLatent
    NODE_DISPLAY_NAME_MAPPINGS["DJZ-LoadLatent"] = "DJZ Load Latent"
except ImportError:
    print("Unable to import DJZ-LoadLatent. This node will not be available.")

try:
    from .DJZLoadLatentV2 import DJZLoadLatentV2
    NODE_CLASS_MAPPINGS["DJZ-LoadLatentV2"] = DJZLoadLatentV2
    NODE_DISPLAY_NAME_MAPPINGS["DJZ-LoadLatentV2"] = "DJZ Load Latent V2"
except ImportError:
    print("Unable to import DJZ-LoadLatentV2. This node will not be available.")

try:
    from .SaveText import SaveText
    NODE_CLASS_MAPPINGS["SaveText"] = SaveText
    NODE_DISPLAY_NAME_MAPPINGS["SaveText"] = "Save Text"
except ImportError:
    print("Unable to import SaveText. This node will not be available.")

try:
    from .LoadVideoBatchFrame import LoadVideoBatchFrame
    NODE_CLASS_MAPPINGS["LoadVideoBatchFrame"] = LoadVideoBatchFrame
    NODE_DISPLAY_NAME_MAPPINGS["LoadVideoBatchFrame"] = "Load Video Batch Frame"
except ImportError:
    print("Unable to import LoadVideoBatchFrame. This node will not be available.")

try:
    from .BatchOffset import BatchOffset
    NODE_CLASS_MAPPINGS["BatchOffset"] = BatchOffset
    NODE_DISPLAY_NAME_MAPPINGS["BatchOffset"] = "Batch Offset"
except ImportError:
    print("Unable to import BatchOffset. This node will not be available.")
    
try:
    from .DjzDatamosh import DJZDatamosh
    NODE_CLASS_MAPPINGS["DJZDatamosh"] = DJZDatamosh
    NODE_DISPLAY_NAME_MAPPINGS["DJZDatamosh"] = "DJZ Datamosh"
except ImportError:
    print("Unable to import DJZDatamosh. This node will not be available.")
    
try:
    from .DJZDatamoshV2 import DJZDatamoshV2
    NODE_CLASS_MAPPINGS["DJZDatamoshV2"] = DJZDatamoshV2
    NODE_DISPLAY_NAME_MAPPINGS["DJZDatamoshV2"] = "DJZ Datamosh V2"
except ImportError:
    print("Unable to import DJZDatamoshV2. This node will not be available.")

try:
    from .DjzDatamoshV3 import DjzDatamoshV3
    NODE_CLASS_MAPPINGS["DjzDatamoshV3"] = DjzDatamoshV3
    NODE_DISPLAY_NAME_MAPPINGS["DjzDatamoshV3"] = "Djz Datamosh V3"
except ImportError:
    print("Unable to import DjzDatamoshV3. This node will not be available.")

try:
    from .DjzDatamoshV4 import DjzDatamoshV4
    NODE_CLASS_MAPPINGS["DjzDatamoshV4"] = DjzDatamoshV4
    NODE_DISPLAY_NAME_MAPPINGS["DjzDatamoshV4"] = "Djz Datamosh V4 (Style Transfer)"
except ImportError:
    print("Unable to import DjzDatamoshV4. This node will not be available.")

try:
    from .DjzDatamoshV5 import DjzDatamoshV5
    NODE_CLASS_MAPPINGS["DjzDatamoshV5"] = DjzDatamoshV5
    NODE_DISPLAY_NAME_MAPPINGS["DjzDatamoshV5"] = "Djz Datamosh V5 (Size Range)"
except ImportError:
    print("Unable to import DjzDatamoshV5. This node will not be available.")

try:
    from .DjzDatamoshV6 import DjzDatamoshV6
    NODE_CLASS_MAPPINGS["DjzDatamoshV6"] = DjzDatamoshV6
    NODE_DISPLAY_NAME_MAPPINGS["DjzDatamoshV6"] = "Djz Datamosh V6 (Pixel Sorting)"
except ImportError:
    print("Unable to import DjzDatamoshV6. This node will not be available.")

try:
    from .DjzDatamoshV7 import DjzDatamoshV7
    NODE_CLASS_MAPPINGS["DjzDatamoshV7"] = DjzDatamoshV7
    NODE_DISPLAY_NAME_MAPPINGS["DjzDatamoshV7"] = "Djz Pixel Sort V7 Advanced"
except ImportError:
    print("Unable to import DjzDatamoshV7. This node will not be available.")

try:
    from .BatchThief import BatchThief
    NODE_CLASS_MAPPINGS["BatchThief"] = BatchThief
    NODE_DISPLAY_NAME_MAPPINGS["BatchThief"] = "Batch Thief"
except ImportError:
    print("Unable to import BatchThief. This node will not be available.")

try:
    from .BatchRangeSwap import BatchRangeSwap
    NODE_CLASS_MAPPINGS["BatchRangeSwap"] = BatchRangeSwap
    NODE_DISPLAY_NAME_MAPPINGS["BatchRangeSwap"] = "Batch Range Swap"
except ImportError:
    print("Unable to import BatchRangeSwap. This node will not be available.")

try:
    from .LoadVideoDirectory import LoadVideoDirectory
    NODE_CLASS_MAPPINGS["LoadVideoDirectory"] = LoadVideoDirectory
    NODE_DISPLAY_NAME_MAPPINGS["LoadVideoDirectory"] = "Load Video Directory"
except ImportError:
    print("Unable to import LoadVideoDirectory. This node will not be available.")

try:
    from .BatchRangeInsert import BatchRangeInsert
    NODE_CLASS_MAPPINGS["BatchRangeInsert"] = BatchRangeInsert
    NODE_DISPLAY_NAME_MAPPINGS["BatchRangeInsert"] = "Batch Range Insert"
except ImportError:
    print("Unable to import BatchRangeInsert. This node will not be available.")

try:
    from .SequentialNumberGenerator import SequentialNumberGenerator
    NODE_CLASS_MAPPINGS["SequentialNumberGenerator"] = SequentialNumberGenerator
    NODE_DISPLAY_NAME_MAPPINGS["SequentialNumberGenerator"] = "Sequential Number Generator"
except ImportError:
    print("Unable to import SequentialNumberGenerator. This node will not be available.")

try:
    from .DinskyPlus import DinskyPlus
    NODE_CLASS_MAPPINGS["DinskyPlus"] = DinskyPlus
    NODE_DISPLAY_NAME_MAPPINGS["DinskyPlus"] = "Dinsky Plus Generator"
except ImportError:
    print("Unable to import DinskyPlus. This node will not be available.")

try:
    from .DinskyPlusV2 import DinskyPlusV2
    NODE_CLASS_MAPPINGS["DinskyPlusV2"] = DinskyPlusV2
    NODE_DISPLAY_NAME_MAPPINGS["DinskyPlusV2"] = "Dinsky Plus Generator V2"
except ImportError:
    print("Unable to import DinskyPlusV2. This node will not be available.")

try:
    from .TrianglesPlus import TrianglesPlus
    NODE_CLASS_MAPPINGS["TrianglesPlus"] = TrianglesPlus
    NODE_DISPLAY_NAME_MAPPINGS["TrianglesPlus"] = "Triangles Plus Generator"
except ImportError:
    print("Unable to import TrianglesPlus. This node will not be available.")

try:
    from .TrianglesPlusV2 import TrianglesPlusV2
    NODE_CLASS_MAPPINGS["TrianglesPlusV2"] = TrianglesPlusV2
    NODE_DISPLAY_NAME_MAPPINGS["TrianglesPlusV2"] = "Triangles Plus Generator V2"
except ImportError:
    print("Unable to import TrianglesPlusV2. This node will not be available.")

try:
    from .ParametricMeshGen import ParametricMeshGen
    NODE_CLASS_MAPPINGS["ParametricMeshGen"] = ParametricMeshGen
    NODE_DISPLAY_NAME_MAPPINGS["ParametricMeshGen"] = "Parametric Mesh Generator"
except ImportError:
    print("Unable to import ParametricMeshGen. This node will not be available.")

try:
    from .ParametricMeshGenV2 import ParametricMeshGenV2
    NODE_CLASS_MAPPINGS["ParametricMeshGenV2"] = ParametricMeshGenV2
    NODE_DISPLAY_NAME_MAPPINGS["ParametricMeshGenV2"] = "Parametric Mesh Generator V2"
except ImportError:
    print("Unable to import ParametricMeshGenV2. This node will not be available.")


try:
    from .FractalGenerator import FractalGenerator
    NODE_CLASS_MAPPINGS["FractalGenerator"] = FractalGenerator
    NODE_DISPLAY_NAME_MAPPINGS["FractalGenerator"] = "Fractal Art Generator"
except ImportError:
    print("Unable to import FractalGenerator. This node will not be available.")

try:
    from .FractalGeneratorV2 import FractalGeneratorV2
    NODE_CLASS_MAPPINGS["FractalGeneratorV2"] = FractalGeneratorV2
    NODE_DISPLAY_NAME_MAPPINGS["FractalGeneratorV2"] = "Fractal Art Generator V2"
except ImportError:
    print("Unable to import FractalGeneratorV2. This node will not be available.")

try:
    from .FractalGeneratorV3 import FractalGeneratorV3
    NODE_CLASS_MAPPINGS["FractalGeneratorV3"] = FractalGeneratorV3
    NODE_DISPLAY_NAME_MAPPINGS["FractalGeneratorV3"] = "Fractal Gen Cuda"
except ImportError:
    print("Unable to import FractalGeneratorV3. This node will not be available.")

try:
    from .DatasetWordcloud import DatasetWordcloud
    NODE_CLASS_MAPPINGS["DatasetWordcloud"] = DatasetWordcloud
    NODE_DISPLAY_NAME_MAPPINGS["DatasetWordcloud"] = "Dataset Wordcloud"
except ImportError:
    print("Unable to import DatasetWordcloud. This node will not be available.")

try:
    from .LoadTextDirectory import LoadTextDirectory
    NODE_CLASS_MAPPINGS["LoadTextDirectory"] = LoadTextDirectory
    NODE_DISPLAY_NAME_MAPPINGS["LoadTextDirectory"] = "Load Text Directory"
except ImportError:
    print("Unable to import LoadTextDirectory. This node will not be available.")

try:
    from .PromptInject import PromptInject
    NODE_CLASS_MAPPINGS["PromptInject"] = PromptInject
    NODE_DISPLAY_NAME_MAPPINGS["PromptInject"] = "Prompt Inject"
except ImportError:
    print("Unable to import PromptInject. This node will not be available.")

try:
    from .VHS_Effect_v1 import VHS_Effect_v1
    NODE_CLASS_MAPPINGS["VHS_Effect_v1"] = VHS_Effect_v1
    NODE_DISPLAY_NAME_MAPPINGS["VHS_Effect_v1"] = "VHS Effect v1"
except ImportError:
    print("Unable to import VHS_Effect_v1. This node will not be available.")

try:
    from .VHS_Effect_v2 import VHS_Effect_v2
    NODE_CLASS_MAPPINGS["VHS_Effect_v2"] = VHS_Effect_v2
    NODE_DISPLAY_NAME_MAPPINGS["VHS_Effect_v2"] = "VHS Effect v2"
except ImportError:
    print("Unable to import VHS_Effect_v2. This node will not be available.")

try:
    from .AnamorphicEffect import AnamorphicEffect
    NODE_CLASS_MAPPINGS["AnamorphicEffect"] = AnamorphicEffect
    NODE_DISPLAY_NAME_MAPPINGS["AnamorphicEffect"] = "Anamorphic Lens Effect"
except ImportError:
    print("Unable to import AnamorphicEffect. This node will not be available.")

try:
    from .Technicolor3Strip_v1 import Technicolor3Strip_v1
    NODE_CLASS_MAPPINGS["Technicolor3Strip_v1"] = Technicolor3Strip_v1
    NODE_DISPLAY_NAME_MAPPINGS["Technicolor3Strip_v1"] = "Technicolor 3-Strip v1"
except ImportError:
    print("Unable to import Technicolor3Strip_v1. This node will not be available.")

try:
    from .Technicolor3Strip_v2 import Technicolor3Strip_v2
    NODE_CLASS_MAPPINGS["Technicolor3Strip_v2"] = Technicolor3Strip_v2
    NODE_DISPLAY_NAME_MAPPINGS["Technicolor3Strip_v2"] = "Technicolor 3-Strip v2"
except ImportError:
    print("Unable to import Technicolor3Strip_v2. This node will not be available.")

try:
    from .PanavisionLensV1 import PanavisionLensV1
    NODE_CLASS_MAPPINGS["PanavisionLensV1"] = PanavisionLensV1
    NODE_DISPLAY_NAME_MAPPINGS["PanavisionLensV1"] = "Panavision Lens Effect V1"
except ImportError:
    print("Unable to import PanavisionLensV1. This node will not be available.")

try:
    from .PanavisionLensV2 import PanavisionLensV2
    NODE_CLASS_MAPPINGS["PanavisionLensV2"] = PanavisionLensV2
    NODE_DISPLAY_NAME_MAPPINGS["PanavisionLensV2"] = "Panavision Lens Effect V2"
except ImportError:
    print("Unable to import PanavisionLensV2. This node will not be available.")

try:
    from .KinescopeEffectV1 import KinescopeEffectV1
    NODE_CLASS_MAPPINGS["KinescopeEffectV1"] = KinescopeEffectV1
    NODE_DISPLAY_NAME_MAPPINGS["KinescopeEffectV1"] = "Kinescope Effect V1"
except ImportError:
    print("Unable to import KinescopeEffectV1. This node will not be available.")

try:
    from .VideoInterlaced import VideoInterlaced
    NODE_CLASS_MAPPINGS["VideoInterlaced"] = VideoInterlaced
    NODE_DISPLAY_NAME_MAPPINGS["VideoInterlaced"] = "Video Interlaced Upscaler"
except ImportError:
    print("Unable to import VideoInterlaced. This node will not be available.")

try:
    from .StringChaos import StringChaos
    NODE_CLASS_MAPPINGS["StringChaos"] = StringChaos
    NODE_DISPLAY_NAME_MAPPINGS["StringChaos"] = "String Chaos Modes"
except ImportError:
    print("Unable to import StringChaos. This node will not be available.")

try:
    from .CombineAudio import CombineAudio
    NODE_CLASS_MAPPINGS["CombineAudio"] = CombineAudio
    NODE_DISPLAY_NAME_MAPPINGS["CombineAudio"] = "Combine Audio Tracks"
except ImportError:
    print("Unable to import CombineAudio. This node will not be available.")

try:
    from .BlackBarsV1 import BlackBarsV1
    NODE_CLASS_MAPPINGS["BlackBarsV1"] = BlackBarsV1
    NODE_DISPLAY_NAME_MAPPINGS["BlackBarsV1"] = "Black Bars V1"
except ImportError:
    print("Unable to import BlackBarsV1. This node will not be available.")

try:
    from .BlackBarsV2 import BlackBarsV2
    NODE_CLASS_MAPPINGS["BlackBarsV2"] = BlackBarsV2
    NODE_DISPLAY_NAME_MAPPINGS["BlackBarsV2"] = "Black Bars V2"
except ImportError:
    print("Unable to import BlackBarsV2. This node will not be available.")

try:
    from .VideoInterlacedV2 import VideoInterlacedV2
    NODE_CLASS_MAPPINGS["VideoInterlacedV2"] = VideoInterlacedV2
    NODE_DISPLAY_NAME_MAPPINGS["VideoInterlacedV2"] = "Video Interlaced Upscaler V2"
except ImportError:
    print("Unable to import VideoInterlacedV2. This node will not be available.")

try:
    from .VHS_Effect_V3 import VHS_Effect_V3
    NODE_CLASS_MAPPINGS["VHS_Effect_V3"] = VHS_Effect_V3
    NODE_DISPLAY_NAME_MAPPINGS["VHS_Effect_V3"] = "VHS Effect V3"
except ImportError:
    print("Unable to import VHS_Effect_V3. This node will not be available.")

try:
    from .RetroVideoText import RetroVideoText
    NODE_CLASS_MAPPINGS["RetroVideoText"] = RetroVideoText
    NODE_DISPLAY_NAME_MAPPINGS["RetroVideoText"] = "Retro Video Text"
except ImportError:
    print("Unable to import RetroVideoText. This node will not be available.")

try:
    from .NonSquarePixelsV1 import NonSquarePixelsV1
    NODE_CLASS_MAPPINGS["NonSquarePixelsV1"] = NonSquarePixelsV1
    NODE_DISPLAY_NAME_MAPPINGS["NonSquarePixelsV1"] = "Non-Square Pixels V1"
except ImportError:
    print("Unable to import NonSquarePixelsV1. This node will not be available.")

try:
    from .BlackBarsV3 import BlackBarsV3
    NODE_CLASS_MAPPINGS["BlackBarsV3"] = BlackBarsV3
    NODE_DISPLAY_NAME_MAPPINGS["BlackBarsV3"] = "Black Bars V3"
except ImportError:
    print("Unable to import BlackBarsV3. This node will not be available.")

try:
    from .VideoInterlaceGANV3 import VideoInterlaceGANV3
    NODE_CLASS_MAPPINGS["VideoInterlaceGANV3"] = VideoInterlaceGANV3
    NODE_DISPLAY_NAME_MAPPINGS["VideoInterlaceGANV3"] = "GAN Video Interlaced Upscaler V3"
except ImportError:
    print("Unable to import VideoInterlaceGANV3. This node will not be available.")


try:
    from .VideoInterlaceFastV4 import VideoInterlaceFastV4
    NODE_CLASS_MAPPINGS["VideoInterlaceFastV4"] = VideoInterlaceFastV4
    NODE_DISPLAY_NAME_MAPPINGS["VideoInterlaceFastV4"] = "Fast Video Interlaced Upscaler V4"
except ImportError:
    print("Unable to import VideoInterlaceFastV4. This node will not be available.")


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
