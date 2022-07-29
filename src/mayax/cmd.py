"""Wrap `maya.cmds` to accept and return instances of `Node`."""

# AUTO-GENERATED. Use `bin/gencmd` to update.
# pylint: disable=redefined-builtin,too-many-lines,too-complex,too-many-branches

from maya import cmds

from .node import Node, MayaNodeError
from .attribute import Attribute, MayaAttributeError
from .strtype import STR_TYPE


def _wrapCommand(cmdFn, args, kwargs):
    args = [
        value.uniqueName if isinstance(value, Node)
        else value.fullName if isinstance(value, Attribute)
        else value
        for value in args
    ]

    for k in kwargs:
        if isinstance(kwargs[k], Node):
            kwargs[k] = kwargs[k].uniqueName
        elif isinstance(kwargs[k], list):
            kwargs[k] = [
                value.uniqueName if isinstance(value, Node) else value
                for value in kwargs[k]
            ]

    result = cmdFn(*args, **kwargs)

    if isinstance(result, STR_TYPE):
        try:
            if result.find('.') != -1:
                result = Attribute(result)
            else:
                result = Node(result)
        except (MayaNodeError, MayaAttributeError):
            pass
    elif isinstance(result, list):
        for i, value in enumerate(result):
            if not isinstance(value, STR_TYPE):
                continue

            try:
                if value.find('.') != -1:
                    result[i] = Attribute(value)
                else:
                    result[i] = Node(value)
            except (MayaNodeError, MayaAttributeError):
                pass

    return result


def aaf2fcp(*args, **kwargs):  # noqa
    """This command is used to convert an aff file to a Final Cut Pro (fcp) xml file The
    conversion process can take several seconds to complete and the command is meant to be
    run asynchronously.

    aaf2fcp([deleteFile=boolean], [dstPath=string], [getFileName=int], [progress=int],
    [srcFile=string], [terminate=int], [waitCompletion=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/aaf2fcp.html
    """
    return _wrapCommand(cmds.aaf2fcp, args, kwargs)


def about(*args, **kwargs):  # noqa
    """This command displays version information about the application if it is executed without
    flags.

    about([apiVersion=boolean], [application=boolean], [batch=boolean],
    [buildDirectory=boolean], [buildVariant=boolean], [codeset=boolean],
    [compositingManager=boolean], [connected=boolean], [ctime=boolean],
    [currentDate=boolean], [currentTime=boolean], [customVersion=boolean],
    [customVersionClient=boolean], [customVersionMajor=boolean],
    [customVersionMinor=boolean], [customVersionString=boolean], [cutIdentifier=boolean],
    [date=boolean], [environmentFile=boolean], [evalVersion=boolean], [file=boolean],
    [fontInfo=boolean], [helpDataDirectory=boolean], [installedVersion=boolean],
    [ioVersion=boolean], [irix=boolean], [is64=boolean], [languageResources=boolean],
    [linux=boolean], [linux64=boolean], [liveUpdate=boolean],
    [localizedResourceLocation=boolean], [ltVersion=boolean], [macOS=boolean],
    [macOSppc=boolean], [macOSx86=boolean], [majorVersion=boolean],
    [minorVersion=boolean], [ntOS=boolean], [operatingSystem=boolean],
    [operatingSystemVersion=boolean], [patchVersion=boolean], [preferences=boolean],
    [product=boolean], [qtVersion=boolean], [tablet=boolean], [tabletMode=boolean],
    [uiLanguage=boolean], [uiLanguageForStartup=boolean], [uiLanguageIsLocalized=boolean],
    [uiLocaleLanguage=boolean], [version=boolean], [win64=boolean],
    [windowManager=boolean], [windows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/about.html
    """
    return _wrapCommand(cmds.about, args, kwargs)


def addAttr(*args, **kwargs):  # noqa
    """This command is used to add a dynamic attribute to a node or nodes.

    addAttr([attributeType=string], [binaryTag=string], [cachedInternally=boolean],
    [category=string], [dataType=string], [defaultValue=float],
    [disconnectBehaviour=uint], [enumName=string], [exists=boolean], [fromPlugin=boolean],
    [hasMaxValue=boolean], [hasMinValue=boolean], [hasSoftMaxValue=boolean],
    [hasSoftMinValue=boolean], [hidden=boolean], [indexMatters=boolean],
    [internalSet=boolean], [keyable=boolean], [longName=string], [maxValue=float],
    [minValue=float], [multi=boolean], [niceName=string], [numberOfChildren=uint],
    [parent=string], [proxy=string], [readable=boolean], [shortName=string],
    [softMaxValue=float], [softMinValue=float], [storable=boolean], [usedAsColor=boolean],
    [usedAsFilename=boolean], [usedAsProxy=boolean], [worldSpace=boolean],
    [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/addAttr.html
    """
    return _wrapCommand(cmds.addAttr, args, kwargs)


def addDynamic(*args, **kwargs):  # noqa
    """Makes the "object" specified as second argument the source of an existing field or emitter
    specified as the first argument.

    addDynamic( object object )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/addDynamic.html
    """
    return _wrapCommand(cmds.addDynamic, args, kwargs)


def addExtension(*args, **kwargs):  # noqa
    """This command is used to add an extension attribute to a node type.

    addExtension([attributeType=string], [binaryTag=string], [cachedInternally=boolean],
    [category=string], [dataType=string], [defaultValue=float],
    [disconnectBehaviour=uint], [enumName=string], [exists=boolean], [fromPlugin=boolean],
    [hasMaxValue=boolean], [hasMinValue=boolean], [hasSoftMaxValue=boolean],
    [hasSoftMinValue=boolean], [hidden=boolean], [indexMatters=boolean],
    [internalSet=boolean], [keyable=boolean], [longName=string], [maxValue=float],
    [minValue=float], [multi=boolean], [niceName=string], [nodeType=string],
    [numberOfChildren=uint], [parent=string], [proxy=string], [readable=boolean],
    [shortName=string], [softMaxValue=float], [softMinValue=float], [storable=boolean],
    [usedAsColor=boolean], [usedAsFilename=boolean], [usedAsProxy=boolean],
    [worldSpace=boolean], [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/addExtension.html
    """
    return _wrapCommand(cmds.addExtension, args, kwargs)


def addMetadata(*args, **kwargs):  # noqa
    """Defines the attachment of a metadata structure to one or more selected objects.

    addMetadata([channelName=string], [channelType=string], [indexType=string],
    [scene=boolean], [streamName=string], [structure=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/addMetadata.html
    """
    return _wrapCommand(cmds.addMetadata, args, kwargs)


def addPP(*args, **kwargs):  # noqa
    """Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an attribute
    of an emitter or field.

    addPP( objects , [attribute=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/addPP.html
    """
    return _wrapCommand(cmds.addPP, args, kwargs)


def affectedNet(*args, **kwargs):  # noqa
    """This command gets the list of attributes on a node or node type and creates nodes of type
    TdnAffect, one for each attribute, that are connected iff the source node's attribute
    affects the destination node's attribute.

    affectedNet( [node...] , [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/affectedNet.html
    """
    return _wrapCommand(cmds.affectedNet, args, kwargs)


def affects(*args, **kwargs):  # noqa
    """This command returns the list of attributes on a node or node type which affect the named
    attribute.

    affects(string, [by=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/affects.html
    """
    return _wrapCommand(cmds.affects, args, kwargs)


def aimConstraint(*args, **kwargs):  # noqa
    """Constrain an object's orientation to point at a target object or at the average position
    of a number of targets.

    aimConstraint( [target...] object , [aimVector=[float, float, float]], [layer=string],
    [maintainOffset=boolean], [name=string], [offset=[float, float, float]],
    [remove=boolean], [skip=string], [targetList=boolean], [upVector=[float, float,
    float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name],
    [worldUpType=string], [worldUpVector=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/aimConstraint.html
    """
    return _wrapCommand(cmds.aimConstraint, args, kwargs)


def air(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    air( [objects] , [attenuation=float], [directionX=float], [directionY=float],
    [directionZ=float], [enableSpread=boolean], [fanSetup=boolean],
    [inheritRotation=boolean], [inheritVelocity=float], [magnitude=float],
    [maxDistance=linear], [name=string], [perVertex=boolean], [position=[linear, linear,
    linear]], [speed=float], [spread=float], [torusSectionRadius=linear],
    [velocityComponentOnly=boolean], [volumeExclusion=boolean], [volumeOffset=[linear,
    linear, linear]], [volumeShape=string], [volumeSweep=angle], [wakeSetup=boolean],
    [windSetup=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/air.html
    """
    return _wrapCommand(cmds.air, args, kwargs)


def aliasAttr(*args, **kwargs):  # noqa
    """Allows aliases (alternate names) to be defined for any attribute of a specified node.

    aliasAttr([remove=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/aliasAttr.html
    """
    return _wrapCommand(cmds.aliasAttr, args, kwargs)


def align(*args, **kwargs):  # noqa
    """Align or spread objects along X Y and Z axis.

    align([alignToLead=boolean], [coordinateSystem=name], [xAxis=string], [yAxis=string],
    [zAxis=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/align.html
    """
    return _wrapCommand(cmds.align, args, kwargs)


def alignCtx(*args, **kwargs):  # noqa
    """The alignCtx command creates a tool for aligning and distributing objects.

    alignCtx( [contextName] , [align=boolean], [anchorFirstObject=boolean],
    [distribute=boolean], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [showAlignTouch=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/alignCtx.html
    """
    return _wrapCommand(cmds.alignCtx, args, kwargs)


def alignCurve(*args, **kwargs):  # noqa
    """The curve align command is used to align curves in maya.

    alignCurve( [curve] [curve] , [attach=boolean], [caching=boolean],
    [constructionHistory=boolean], [curvatureContinuity=boolean], [curvatureScale1=float],
    [curvatureScale2=float], [joinParameter=float], [keepMultipleKnots=boolean],
    [name=string], [nodeState=int], [object=boolean], [positionalContinuity=boolean],
    [positionalContinuityType=int], [replaceOriginal=boolean], [reverse1=boolean],
    [reverse2=boolean], [tangentContinuity=boolean], [tangentContinuityType=int],
    [tangentScale1=float], [tangentScale2=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/alignCurve.html
    """
    return _wrapCommand(cmds.alignCurve, args, kwargs)


def alignSurface(*args, **kwargs):  # noqa
    """The surface align command is used to align surfaces in maya.

    alignSurface( [surface] [surface] , [attach=boolean], [caching=boolean],
    [constructionHistory=boolean], [curvatureContinuity=boolean], [curvatureScale1=float],
    [curvatureScale2=float], [directionU=boolean], [joinParameter=float],
    [keepMultipleKnots=boolean], [name=string], [nodeState=int], [object=boolean],
    [positionalContinuity=boolean], [positionalContinuityType=int],
    [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean], [swap1=boolean],
    [swap2=boolean], [tangentContinuity=boolean], [tangentContinuityType=int],
    [tangentScale1=float], [tangentScale2=float], [twist=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/alignSurface.html
    """
    return _wrapCommand(cmds.alignSurface, args, kwargs)


def allNodeTypes(*args, **kwargs):  # noqa
    """This command returns a list containing the type names of every kind of creatable node
    registered with the system.

    allNodeTypes([includeAbstract=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/allNodeTypes.html
    """
    return _wrapCommand(cmds.allNodeTypes, args, kwargs)


def ambientLight(*args, **kwargs):  # noqa
    """TlightCmd is the base class for other light commands.

    ambientLight([ambientShade=float], [discRadius=linear], [exclusive=boolean],
    [intensity=float], [name=string], [position=[linear, linear, linear]], [rgb=[float,
    float, float]], [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]],
    [shadowDither=float], [shadowSamples=int], [softShadow=boolean],
    [useRayTraceShadows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ambientLight.html
    """
    return _wrapCommand(cmds.ambientLight, args, kwargs)


def angleBetween(*args, **kwargs):  # noqa
    """Returns the axis and angle required to rotate one vector onto another.

    angleBetween([caching=boolean], [constructionHistory=boolean], [euler=boolean],
    [nodeState=int], [vector1=[linear, linear, linear]], [vector1X=linear],
    [vector1Y=linear], [vector1Z=linear], [vector2=[linear, linear, linear]],
    [vector2X=linear], [vector2Y=linear], [vector2Z=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/angleBetween.html
    """
    return _wrapCommand(cmds.angleBetween, args, kwargs)


def animCurveEditor(*args, **kwargs):  # noqa
    """Edit a characteristic of a graph editor.

    animCurveEditor( editorName , [areCurvesSelected=boolean], [autoFit=string],
    [autoFitTime=string], [classicMode=boolean], [clipTime=string], [constrainDrag=uint],
    [control=boolean], [curvesShown=boolean], [curvesShownForceUpdate=boolean],
    [defineTemplate=string], [denormalizeCurvesCommand=string],
    [displayActiveKeyTangents=string], [displayActiveKeys=string],
    [displayInfinities=string], [displayKeys=string], [displayNormalized=boolean],
    [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean],
    [filter=string], [forceMainConnection=string], [highlightAffectedCurves=boolean],
    [highlightConnection=string], [keyMinScale=float], [keyScale=float],
    [keyingTime=string], [lockMainConnection=boolean], [lockPlayRangeShades=string],
    [lookAt=string], [mainListConnection=string], [menu=script],
    [normalizeCurvesCommand=string], [outliner=string], [panel=string], [parent=string],
    [preSelectionHighlight=boolean], [renormalizeCurves=boolean], [resultSamples=time],
    [resultScreenSamples=int], [resultUpdate=string], [selectionConnection=string],
    [showActiveCurveNames=boolean], [showBufferCurves=string], [showCurveNames=boolean],
    [showPlayRangeShades=string], [showResults=string], [showUpstreamCurves=boolean],
    [simpleKeyView=boolean], [smoothness=string], [snapTime=string], [snapValue=string],
    [stackedCurves=boolean], [stackedCurvesMax=float], [stackedCurvesMin=float],
    [stackedCurvesSpace=float], [stateString=boolean], [timelinePositionTop=boolean],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string], [valueLinesToggle=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/animCurveEditor.html
    """
    return _wrapCommand(cmds.animCurveEditor, args, kwargs)


def animDisplay(*args, **kwargs):  # noqa
    """This command changes certain display options used by animation windows.

    animDisplay([modelUpdate=string], [refAnimCurvesEditable=boolean], [timeCode=string],
    [timeCodeOffset=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/animDisplay.html
    """
    return _wrapCommand(cmds.animDisplay, args, kwargs)


def animLayer(*args, **kwargs):  # noqa
    """This command creates and edits animation layers.

    animLayer([addRelatedKG=boolean], [addSelectedObjects=boolean], [affectedLayers=boolean],
    [animCurves=boolean], [attribute=string], [baseAnimCurves=boolean],
    [bestAnimLayer=boolean], [bestLayer=boolean], [blendNodes=boolean], [children=string],
    [collapse=boolean], [copy=string], [copyAnimation=string], [copyNoAnimation=string],
    [excludeBoolean=boolean], [excludeDynamic=boolean], [excludeEnum=boolean],
    [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean],
    [excludeVisibility=boolean], [exists=boolean], [extractAnimation=string],
    [findCurveForPlug=string], [forceUIRebuild=boolean], [forceUIRefresh=boolean],
    [layeredPlug=string], [lock=boolean], [maxLayers=boolean], [moveLayerAfter=string],
    [moveLayerBefore=string], [mute=boolean], [override=boolean], [parent=string],
    [passthrough=boolean], [preferred=boolean], [removeAllAttributes=boolean],
    [removeAttribute=string], [root=string], [selected=boolean], [solo=boolean],
    [weight=float], [writeBlendnodeDestinations=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/animLayer.html
    """
    return _wrapCommand(cmds.animLayer, args, kwargs)


def animView(*args, **kwargs):  # noqa
    """This command allows you to specify the current view range within an animation editor.

    animView( string[] , [endTime=time], [maxValue=float], [minValue=float],
    [nextView=boolean], [previousView=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/animView.html
    """
    return _wrapCommand(cmds.animView, args, kwargs)


def annotate(*args, **kwargs):  # noqa
    """This command is used to create an annotation to be attached to the specified objects at
    the specified point.

    annotate( [objects] , [point=[linear, linear, linear]], [text=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/annotate.html
    """
    return _wrapCommand(cmds.annotate, args, kwargs)


def appHome(*args, **kwargs):  # noqa
    """Used for displaying and hiding application home.

    appHome([iconVisible=boolean], [instrument=string], [setTab=string],
    [toggleVisibility=boolean], [updateRecentFiles=boolean], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/appHome.html
    """
    return _wrapCommand(cmds.appHome, args, kwargs)


def applyAttrPattern(*args, **kwargs):  # noqa
    """Take the attribute structure described by a pre-defined pattern and apply it either to a
    node (as dynamic attributes) or a node type (as extension attributes).

    applyAttrPattern([nodeType=string], [patternName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/applyAttrPattern.html
    """
    return _wrapCommand(cmds.applyAttrPattern, args, kwargs)


def applyMetadata(*args, **kwargs):  # noqa
    """Define the values of a particular set of metadata on selected objects.

    applyMetadata([format=string], [scene=boolean], [value=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/applyMetadata.html
    """
    return _wrapCommand(cmds.applyMetadata, args, kwargs)


def applyTake(*args, **kwargs):  # noqa
    """This command takes data in a device (refered to as a take) and converts it into a form
    that may be played back and reviewed.

    applyTake([channel=string], [device=string], [filter=string], [preview=boolean],
    [recurseChannel=boolean], [reset=boolean], [specifyChannel=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/applyTake.html
    """
    return _wrapCommand(cmds.applyTake, args, kwargs)


def arclen(*args, **kwargs):  # noqa
    """This command returns the arclength of a curve if the history flag is not set (the
    default).

    arclen( curve , [caching=boolean], [constructionHistory=boolean], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/arclen.html
    """
    return _wrapCommand(cmds.arclen, args, kwargs)


def arcLenDimContext(*args, **kwargs):  # noqa
    """Command used to register the arcLenDimCtx tool.

    arcLenDimContext([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/arcLenDimContext.html
    """
    return _wrapCommand(cmds.arcLenDimContext, args, kwargs)


def arcLengthDimension(*args, **kwargs):  # noqa
    """This command is used to create an arcLength dimension to display the arcLength of a
    curve/surface at a specified point on the curve/surface.

    arcLengthDimension( [curve|surface] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/arcLengthDimension.html
    """
    return _wrapCommand(cmds.arcLengthDimension, args, kwargs)


def arrayMapper(*args, **kwargs):  # noqa
    """Create an arrayMapper node and connect it to a target object.

    arrayMapper([destAttr=string], [inputU=string], [inputV=string], [mapTo=string],
    [target=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/arrayMapper.html
    """
    return _wrapCommand(cmds.arrayMapper, args, kwargs)


def art3dPaintCtx(*args, **kwargs):  # noqa
    """This is a tool context command for 3d Paint tool.

    art3dPaintCtx([accopacity=boolean], [afterStrokeCmd=string], [alphablendmode=string],
    [assigntxt=boolean], [attrnames=string], [beforeStrokeCmd=string],
    [brushalignment=boolean], [brushdepth=float], [brushfeedback=boolean],
    [brushtype=string], [clear=boolean], [commonattr=string], [dragSlider=string],
    [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean],
    [extendFillColor=boolean], [fileformat=string], [filetxtaspectratio=float],
    [filetxtsizex=int], [filetxtsizey=int], [floodOpacity=float], [floodall=boolean],
    [floodselect=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [keepaspectratio=boolean], [lastRecorderCmd=string],
    [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string],
    [name=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean],
    [paintmode=string], [paintoperationtype=string], [painttxtattr=string],
    [painttxtattrname=string], [pfxScale=float], [pfxWidth=float], [pickColor=boolean],
    [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [pressureMapping1=int], [pressureMapping2=int],
    [pressureMapping3=int], [pressureMax1=float], [pressureMax2=float],
    [pressureMax3=float], [pressureMin1=float], [pressureMin2=float],
    [pressureMin3=float], [profileShapeFile=string], [projective=boolean], [radius=float],
    [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean],
    [reflectionaxis=string], [reloadtexfile=boolean], [resizeratio=float],
    [resizetxt=boolean], [rgbcolor=[float, float, float]], [rgbflood=[float, float,
    float]], [saveTextureOnStroke=boolean], [saveonstroke=boolean], [savetexture=boolean],
    [screenRadius=float], [selectclonesource=boolean], [shadernames=string],
    [shapeattr=boolean], [shapenames=string], [showactive=boolean],
    [soloAsDiffuse=boolean], [stampDepth=float], [stampProfile=string],
    [stampSpacing=float], [strokesmooth=string], [surfaceConformedBrushVertices=boolean],
    [tablet=boolean], [tangentOutline=boolean], [textureFilenames=boolean],
    [updateEraseTex=boolean], [usepressure=boolean], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/art3dPaintCtx.html
    """
    return _wrapCommand(cmds.art3dPaintCtx, args, kwargs)


def artAttrCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artAttrCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string],
    [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float],
    [attrSelected=string], [beforeStrokeCmd=string], [brushalignment=boolean],
    [brushfeedback=boolean], [clamp=string], [clamplower=float], [clampupper=float],
    [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float, float, float,
    float]], [colorRGBValue=[float, float, float]], [colorRamp=string],
    [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float],
    [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean],
    [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean],
    [exists=boolean], [expandfilename=boolean], [exportaspectratio=float],
    [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int],
    [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [importfileload=string], [importfilemode=string], [importreassign=boolean],
    [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string],
    [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float],
    [minvalue=float], [name=string], [objattrArray=string], [opacity=float],
    [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string],
    [paintattrselected=string], [paintmode=string], [paintoperationtype=string],
    [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]],
    [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string],
    [projective=boolean], [radius=float], [rampMaxColor=[float, float, float]],
    [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean],
    [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float],
    [selectclonesource=boolean], [selectedattroper=string], [showactive=boolean],
    [stampDepth=float], [stampProfile=string], [stampSpacing=float],
    [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean],
    [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string],
    [useColorRamp=boolean], [useMaxMinColor=boolean], [usepressure=boolean],
    [value=float], [whichTool=string], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artAttrCtx.html
    """
    return _wrapCommand(cmds.artAttrCtx, args, kwargs)


def artAttrPaintVertexCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artAttrPaintVertexCtx( [context] , [accopacity=boolean], [activeListChangedProc=string],
    [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float],
    [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string],
    [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float],
    [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float,
    float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string],
    [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float],
    [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean],
    [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean],
    [exists=boolean], [expandfilename=boolean], [exportaspectratio=float],
    [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int],
    [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [importfileload=string], [importfilemode=string], [importreassign=boolean],
    [interactiveUpdate=boolean], [lastRecorderCmd=string], [lastStampName=string],
    [lowerradius=float], [makeStroke=uint], [mappressure=string], [maxvalue=float],
    [minvalue=float], [name=string], [objattrArray=string], [opacity=float],
    [outline=boolean], [outwhilepaint=boolean], [paintChannel=string],
    [paintComponent=int], [paintNodeArray=string], [paintNumChannels=int],
    [paintRGBA=boolean], [paintVertexFace=boolean], [paintattrselected=string],
    [paintmode=string], [paintoperationtype=string], [pickColor=boolean],
    [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean],
    [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float,
    float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean],
    [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean],
    [selectedattroper=string], [showactive=boolean], [stampDepth=float],
    [stampProfile=string], [stampSpacing=float], [strokesmooth=string],
    [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean],
    [toolOffProc=string], [toolOnProc=string], [useColorRamp=boolean],
    [useMaxMinColor=boolean], [usepressure=boolean], [value=float],
    [vertexColorRange=boolean], [vertexColorRangeLower=float],
    [vertexColorRangeUpper=float], [whichTool=string], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artAttrPaintVertexCtx.html
    """
    return _wrapCommand(cmds.artAttrPaintVertexCtx, args, kwargs)


def artAttrSkinPaintCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artAttrSkinPaintCtx( [context] , [accopacity=boolean], [activeListChangedProc=string],
    [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float],
    [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string],
    [brushalignment=boolean], [brushfeedback=boolean], [clamp=string], [clamplower=float],
    [clampupper=float], [clear=boolean], [colorAlphaValue=float], [colorRGBAValue=[float,
    float, float, float]], [colorRGBValue=[float, float, float]], [colorRamp=string],
    [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float],
    [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean],
    [dragSlider=string], [duringStrokeCmd=string], [dynclonemode=boolean],
    [exists=boolean], [expandfilename=boolean], [exportaspectratio=float],
    [exportfilemode=string], [exportfilesave=string], [exportfilesizex=int],
    [exportfilesizey=int], [exportfiletype=string], [filterNodes=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [importfileload=string], [importfilemode=string], [importreassign=boolean],
    [influence=string], [interactiveUpdate=boolean], [lastRecorderCmd=string],
    [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string],
    [maxvalue=float], [minvalue=float], [name=string], [objattrArray=string],
    [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string],
    [paintSelectMode=int], [paintattrselected=string], [paintmode=string],
    [paintoperationtype=string], [pickColor=boolean], [pickValue=boolean],
    [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean],
    [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float,
    float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean],
    [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean],
    [selectedattroper=string], [showactive=boolean], [skinPaintMode=int],
    [stampDepth=float], [stampProfile=string], [stampSpacing=float],
    [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean],
    [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string],
    [useColorRamp=boolean], [useMaxMinColor=boolean], [usepressure=boolean],
    [value=float], [whichTool=string], [worldRadius=float], [xrayJoints=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artAttrSkinPaintCtx.html
    """
    return _wrapCommand(cmds.artAttrSkinPaintCtx, args, kwargs)


def artAttrTool(*args, **kwargs):  # noqa
    """The artAttrTool command manages the list of tool types which are used for attribute
    painting.

    artAttrTool([add=string], [exists=string], [remove=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artAttrTool.html
    """
    return _wrapCommand(cmds.artAttrTool, args, kwargs)


def artBuildPaintMenu(*args, **kwargs):  # noqa
    """??.

    artBuildPaintMenu()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artBuildPaintMenu.html
    """
    return _wrapCommand(cmds.artBuildPaintMenu, args, kwargs)


def artFluidAttrCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artFluidAttrCtx([accopacity=boolean], [activeListChangedProc=string],
    [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float],
    [alphaclampupper=float], [attrSelected=string], [autoSave=string],
    [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean],
    [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean],
    [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]],
    [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean],
    [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float],
    [currentPaintableFluid=string], [dataTypeIndex=int], [delaySelectionChanged=boolean],
    [disablelighting=boolean], [displayAsRender=boolean], [displayVelocity=boolean],
    [doAutoSave=boolean], [dragSlider=string], [duringStrokeCmd=string],
    [dynclonemode=boolean], [exists=boolean], [expandfilename=boolean],
    [exportaspectratio=float], [exportfilemode=string], [exportfilesave=string],
    [exportfilesizex=int], [exportfilesizey=int], [exportfiletype=string],
    [filterNodes=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [importfileload=string], [importfilemode=string],
    [importreassign=boolean], [interactiveUpdate=boolean], [lastRecorderCmd=string],
    [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string],
    [maxvalue=float], [minvalue=float], [name=string], [objattrArray=string],
    [opacity=float], [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string],
    [paintattrselected=string], [paintmode=string], [paintoperationtype=string],
    [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]],
    [playbackPressure=float], [preserveclonesource=boolean], [profileShapeFile=string],
    [projective=boolean], [property=string], [radius=float], [rampMaxColor=[float, float,
    float]], [rampMinColor=[float, float, float]], [record=boolean], [reflection=boolean],
    [reflectionaboutorigin=boolean], [reflectionaxis=string], [rgbValue=[float, float,
    float]], [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string],
    [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float],
    [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean],
    [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string],
    [useColorRamp=boolean], [useMaxMinColor=boolean], [useStrokeDirection=boolean],
    [usepressure=boolean], [value=float], [velocity=[float, float, float]],
    [whichTool=string], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artFluidAttrCtx.html
    """
    return _wrapCommand(cmds.artFluidAttrCtx, args, kwargs)


def artPuttyCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artPuttyCtx([accopacity=boolean], [activeListChangedProc=string], [afterStrokeCmd=string],
    [alphaclamp=string], [alphaclamplower=float], [alphaclampupper=float],
    [attrSelected=string], [autosmooth=boolean], [beforeStrokeCmd=string],
    [brushStrength=float], [brushalignment=boolean], [brushfeedback=boolean],
    [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean],
    [collapsecvtol=float], [colorAlphaValue=float], [colorRGBAValue=[float, float, float,
    float]], [colorRGBValue=[float, float, float]], [colorRamp=string],
    [colorfeedback=boolean], [colorfeedbackOverride=boolean], [colorrangelower=float],
    [colorrangeupper=float], [dataTypeIndex=int], [disablelighting=boolean],
    [dispdecr=boolean], [dispincr=boolean], [dragSlider=string], [duringStrokeCmd=string],
    [dynclonemode=boolean], [erasesrfupd=boolean], [exists=boolean],
    [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string],
    [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int],
    [exportfiletype=string], [filterNodes=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [importfileload=string], [importfilemode=string],
    [importreassign=boolean], [interactiveUpdate=boolean], [invertrefvector=boolean],
    [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float],
    [makeStroke=uint], [mappressure=string], [maxdisp=float], [maxvalue=float],
    [minvalue=float], [mouldtypehead=string], [mouldtypemouse=string],
    [mouldtypetail=string], [name=string], [objattrArray=string], [opacity=float],
    [outline=boolean], [outwhilepaint=boolean], [paintNodeArray=string],
    [paintattrselected=string], [paintmode=string], [paintoperationtype=string],
    [pickColor=boolean], [pickValue=boolean], [playbackCursor=[float, float]],
    [playbackPressure=float], [polecv=boolean], [preserveclonesource=boolean],
    [profileShapeFile=string], [projective=boolean], [radius=float], [rampMaxColor=[float,
    float, float]], [rampMinColor=[float, float, float]], [record=boolean],
    [reflection=boolean], [reflectionaboutorigin=boolean], [reflectionaxis=string],
    [refsurface=boolean], [refvector=string], [refvectoru=float], [refvectorv=float],
    [screenRadius=float], [selectclonesource=boolean], [selectedattroper=string],
    [showactive=boolean], [smoothiters=int], [stampDepth=float], [stampProfile=string],
    [stampSpacing=float], [stitchcorner=boolean], [stitchedgeflood=boolean],
    [stitchtype=string], [strokesmooth=string], [surfaceConformedBrushVertices=boolean],
    [tablet=boolean], [tangentOutline=boolean], [toolOffProc=string], [toolOnProc=string],
    [updateerasesrf=boolean], [updaterefsrf=boolean], [useColorRamp=boolean],
    [useMaxMinColor=boolean], [usepressure=boolean], [value=float], [whichTool=string],
    [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artPuttyCtx.html
    """
    return _wrapCommand(cmds.artPuttyCtx, args, kwargs)


def artSelectCtx(*args, **kwargs):  # noqa
    """This command is used to select/deselect/toggle components on selected surfaces using a
    brush interface (Maya Artisan).

    artSelectCtx([accopacity=boolean], [addselection=boolean], [afterStrokeCmd=string],
    [beforeStrokeCmd=string], [brushalignment=boolean], [brushfeedback=boolean],
    [clear=boolean], [dragSlider=string], [dynclonemode=boolean], [exists=boolean],
    [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string],
    [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int],
    [exportfiletype=string], [history=boolean], [image1=string], [image2=string],
    [image3=string], [importfileload=string], [importfilemode=string],
    [importreassign=boolean], [importthreshold=float], [lastRecorderCmd=string],
    [lastStampName=string], [lowerradius=float], [makeStroke=uint], [mappressure=string],
    [name=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean],
    [paintmode=string], [paintoperationtype=string], [pickColor=boolean],
    [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean],
    [radius=float], [record=boolean], [reflection=boolean],
    [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float],
    [selectall=boolean], [selectclonesource=boolean], [selectop=string],
    [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float],
    [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean],
    [tangentOutline=boolean], [toggleall=boolean], [unselectall=boolean],
    [usepressure=boolean], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artSelectCtx.html
    """
    return _wrapCommand(cmds.artSelectCtx, args, kwargs)


def artSetPaintCtx(*args, **kwargs):  # noqa
    """This tool allows the user to modify the set membership (add, transfer, remove cvs) on
    nurbs surfaces using Maya Artisan's interface.

    artSetPaintCtx([accopacity=boolean], [afterStrokeCmd=string], [beforeStrokeCmd=string],
    [brushalignment=boolean], [brushfeedback=boolean], [clear=boolean],
    [dragSlider=string], [dynclonemode=boolean], [exists=boolean],
    [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string],
    [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int],
    [exportfiletype=string], [history=boolean], [image1=string], [image2=string],
    [image3=string], [importfileload=string], [importfilemode=string],
    [importreassign=boolean], [lastRecorderCmd=string], [lastStampName=string],
    [lowerradius=float], [makeStroke=uint], [mappressure=string], [name=string],
    [objectsetnames=string], [opacity=float], [outline=boolean], [outwhilepaint=boolean],
    [paintmode=string], [paintoperationtype=string], [pickColor=boolean],
    [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean],
    [radius=float], [record=boolean], [reflection=boolean],
    [reflectionaboutorigin=boolean], [reflectionaxis=string], [screenRadius=float],
    [selectclonesource=boolean], [setcolorfeedback=boolean], [setdisplaycvs=boolean],
    [setopertype=string], [settomodify=string], [showactive=boolean], [stampDepth=float],
    [stampProfile=string], [stampSpacing=float], [strokesmooth=string],
    [surfaceConformedBrushVertices=boolean], [tablet=boolean], [tangentOutline=boolean],
    [usepressure=boolean], [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artSetPaintCtx.html
    """
    return _wrapCommand(cmds.artSetPaintCtx, args, kwargs)


def artUserPaintCtx(*args, **kwargs):  # noqa
    """This is a context command to set the flags on the artAttrContext, which is the base
    context for attribute painting operations.

    artUserPaintCtx([accopacity=boolean], [activeListChangedProc=string],
    [afterStrokeCmd=string], [alphaclamp=string], [alphaclamplower=float],
    [alphaclampupper=float], [attrSelected=string], [beforeStrokeCmd=string],
    [brushalignment=boolean], [brushfeedback=boolean], [chunkCommand=string],
    [clamp=string], [clamplower=float], [clampupper=float], [clear=boolean],
    [colorAlphaValue=float], [colorRGBAValue=[float, float, float, float]],
    [colorRGBValue=[float, float, float]], [colorRamp=string], [colorfeedback=boolean],
    [colorfeedbackOverride=boolean], [colorrangelower=float], [colorrangeupper=float],
    [dataTypeIndex=int], [disablelighting=boolean], [dragSlider=string],
    [duringStrokeCmd=string], [dynclonemode=boolean], [exists=boolean],
    [expandfilename=boolean], [exportaspectratio=float], [exportfilemode=string],
    [exportfilesave=string], [exportfilesizex=int], [exportfilesizey=int],
    [exportfiletype=string], [filterNodes=boolean], [finalizeCmd=string],
    [fullpaths=boolean], [getArrayAttrCommand=string], [getSurfaceCommand=string],
    [getValueCommand=string], [history=boolean], [image1=string], [image2=string],
    [image3=string], [importfileload=string], [importfilemode=string],
    [importreassign=boolean], [initializeCmd=string], [interactiveUpdate=boolean],
    [lastRecorderCmd=string], [lastStampName=string], [lowerradius=float],
    [makeStroke=uint], [mappressure=string], [maxvalue=float], [minvalue=float],
    [name=string], [objattrArray=string], [opacity=float], [outline=boolean],
    [outwhilepaint=boolean], [paintNodeArray=string], [paintattrselected=string],
    [paintmode=string], [paintoperationtype=string], [pickColor=boolean],
    [pickValue=boolean], [playbackCursor=[float, float]], [playbackPressure=float],
    [preserveclonesource=boolean], [profileShapeFile=string], [projective=boolean],
    [radius=float], [rampMaxColor=[float, float, float]], [rampMinColor=[float, float,
    float]], [record=boolean], [reflection=boolean], [reflectionaboutorigin=boolean],
    [reflectionaxis=string], [screenRadius=float], [selectclonesource=boolean],
    [selectedattroper=string], [setArrayValueCommand=string], [setValueCommand=string],
    [showactive=boolean], [stampDepth=float], [stampProfile=string], [stampSpacing=float],
    [strokesmooth=string], [surfaceConformedBrushVertices=boolean], [tablet=boolean],
    [tangentOutline=boolean], [toolCleanupCmd=string], [toolOffProc=string],
    [toolOnProc=string], [toolSetupCmd=string], [useColorRamp=boolean],
    [useMaxMinColor=boolean], [usepressure=boolean], [value=float], [whichTool=string],
    [worldRadius=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/artUserPaintCtx.html
    """
    return _wrapCommand(cmds.artUserPaintCtx, args, kwargs)


def arubaNurbsToPoly(*args, **kwargs):  # noqa
    """This command tesselates a NURBS surface and produces a polygonal surface.

    arubaNurbsToPoly( [surface] , [caching=boolean], [constructionHistory=boolean],
    [localSpace=boolean], [name=string], [nodeState=int], [object=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/arubaNurbsToPoly.html
    """
    return _wrapCommand(cmds.arubaNurbsToPoly, args, kwargs)


def assembly(*args, **kwargs):  # noqa
    """Command to register assemblies for the scene assembly framework, to create them, and to
    edit and query them.

    assembly([active=string], [activeLabel=string], [canCreate=string],
    [createOptionBoxProc=script], [createRepresentation=string], [defaultType=string],
    [deleteRepresentation=string], [deregister=string], [input=string], [isAType=string],
    [isTrackingMemberEdits=string], [label=string], [listRepTypes=boolean],
    [listRepTypesProc=script], [listRepresentations=boolean], [listTypes=boolean],
    [name=string], [newRepLabel=string], [postCreateUIProc=script], [proc=script],
    [renameRepresentation=string], [repLabel=string], [repName=string],
    [repNamespace=string], [repPostCreateUIProc=string], [repPreCreateUIProc=string],
    [repType=string], [repTypeLabel=string], [repTypeLabelProc=script], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/assembly.html
    """
    return _wrapCommand(cmds.assembly, args, kwargs)


def assignCommand(*args, **kwargs):  # noqa
    """This command allows the user to assign hotkeys and manipulate the internal array of named
    command objects.

    assignCommand( int , [addDivider=string], [altModifier=boolean], [annotation=string],
    [command=script], [commandModifier=boolean], [ctrlModifier=boolean], [data1=string],
    [data2=string], [data3=string], [delete=int], [dividerString=string],
    [enableCommandRepeat=boolean], [factorySettings=boolean], [index=int],
    [keyArray=boolean], [keyString=string], [keyUp=boolean], [name=boolean],
    [numDividersPreceding=int], [numElements=boolean], [optionModifier=boolean],
    [sortByKey=boolean], [sourceUserCommands=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/assignCommand.html
    """
    return _wrapCommand(cmds.assignCommand, args, kwargs)


def assignInputDevice(*args, **kwargs):  # noqa
    """This command associates a command string (i.

    assignInputDevice([clutch=string], [continuous=boolean], [device=string],
    [immediate=boolean], [multiple=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/assignInputDevice.html
    """
    return _wrapCommand(cmds.assignInputDevice, args, kwargs)


def assignViewportFactories(*args, **kwargs):  # noqa
    """Sets viewport factories for displays as materials or textures.

    assignViewportFactories([string], [materialFactory=string], [nodeType=string],
    [textureFactory=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/assignViewportFactories.html
    """
    return _wrapCommand(cmds.assignViewportFactories, args, kwargs)


def attachCurve(*args, **kwargs):  # noqa
    """This attach command is used to attach curves.

    attachCurve( curve curve [curve...] , [blendBias=float], [blendKnotInsertion=boolean],
    [caching=boolean], [constructionHistory=boolean], [keepMultipleKnots=boolean],
    [method=int], [name=string], [nodeState=int], [object=boolean], [parameter=float],
    [replaceOriginal=boolean], [reverse1=boolean], [reverse2=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attachCurve.html
    """
    return _wrapCommand(cmds.attachCurve, args, kwargs)


def attachDeviceAttr(*args, **kwargs):  # noqa
    """This command associates a device/axis pair with a node/attribute pair.

    attachDeviceAttr([attribute=string], [axis=string], [camera=boolean],
    [cameraRotate=boolean], [cameraTranslate=boolean], [clutch=string], [device=string],
    [selection=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attachDeviceAttr.html
    """
    return _wrapCommand(cmds.attachDeviceAttr, args, kwargs)


def attachSurface(*args, **kwargs):  # noqa
    """This attach command is used to attach surfaces.

    attachSurface( [surface] [surface] , [blendBias=float], [blendKnotInsertion=boolean],
    [caching=boolean], [constructionHistory=boolean], [directionU=boolean],
    [keepMultipleKnots=boolean], [method=int], [name=string], [nodeState=int],
    [object=boolean], [parameter=float], [replaceOriginal=boolean], [reverse1=boolean],
    [reverse2=boolean], [swap1=boolean], [swap2=boolean], [twist=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attachSurface.html
    """
    return _wrapCommand(cmds.attachSurface, args, kwargs)


def attrColorSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    attrColorSliderGrp( groupName , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [alphaValue=float], [annotation=string],
    [attrNavDecision=[name, string]], [attribute=string], [backgroundColor=[float, float,
    float]], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [hsvValue=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [rgbValue=[float, float, float]], [rowAttach=[int, string, int]],
    [showButton=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrColorSliderGrp.html
    """
    return _wrapCommand(cmds.attrColorSliderGrp, args, kwargs)


def attrControlGrp(*args, **kwargs):  # noqa
    """This command creates a control of the type most appropriate for the specified attribute,
    and associates the control with the attribute.

    attrControlGrp([annotation=string], [attribute=name], [changeCommand=script],
    [enable=boolean], [exists=boolean], [handlesAttribute=name], [hideMapButton=boolean],
    [label=string], [preventOverride=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrControlGrp.html
    """
    return _wrapCommand(cmds.attrControlGrp, args, kwargs)


def attrEnumOptionMenu(*args, **kwargs):  # noqa
    """This command creates an enumerated attribute control.

    attrEnumOptionMenu( [string] , [annotation=string], [attribute=name],
    [backgroundColor=[float, float, float]], [changeCommand=script],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enumeratedItem=[int, string]], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrEnumOptionMenu.html
    """
    return _wrapCommand(cmds.attrEnumOptionMenu, args, kwargs)


def attrEnumOptionMenuGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    attrEnumOptionMenuGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [attribute=name],
    [backgroundColor=[float, float, float]], [columnAlign=[int, string]],
    [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enumeratedItem=[int, string]], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrEnumOptionMenuGrp.html
    """
    return _wrapCommand(cmds.attrEnumOptionMenuGrp, args, kwargs)


def attrFieldGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    attrFieldGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [attribute=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [extraButton=boolean],
    [extraButtonCommand=script], [extraButtonIcon=string], [extraLabel=string],
    [forceAddMapButton=boolean], [fullPathName=boolean], [height=int],
    [hideMapButton=boolean], [highlightColor=[float, float, float]], [isObscured=boolean],
    [label=string], [manage=boolean], [maxValue=float], [minValue=float],
    [noBackground=boolean], [numberOfFields=int], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [precision=int], [preventOverride=boolean],
    [rowAttach=[int, string, int]], [statusBarMessage=string], [step=float],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrFieldGrp.html
    """
    return _wrapCommand(cmds.attrFieldGrp, args, kwargs)


def attrFieldSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    attrFieldSliderGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [attribute=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [extraButton=boolean],
    [extraButtonCommand=script], [extraButtonIcon=string], [fieldMaxValue=float],
    [fieldMinValue=float], [fieldStep=float], [forceAddMapButton=boolean],
    [fullPathName=boolean], [height=int], [hideMapButton=boolean], [highlightColor=[float,
    float, float]], [isObscured=boolean], [label=string], [manage=boolean],
    [maxValue=float], [minValue=float], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]],
    [sliderMaxValue=float], [sliderMinValue=float], [sliderStep=float],
    [statusBarMessage=string], [step=float], [useTemplate=string], [vertical=boolean],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrFieldSliderGrp.html
    """
    return _wrapCommand(cmds.attrFieldSliderGrp, args, kwargs)


def attributeInfo(*args, **kwargs):  # noqa
    """This command lists all of the attributes that are marked with certain flags.

    attributeInfo([allAttributes=boolean], [bool=boolean], [enumerated=boolean],
    [hidden=boolean], [inherited=boolean], [internal=boolean], [leaf=boolean],
    [logicalAnd=boolean], [multi=boolean], [short=boolean], [type=string],
    [userInterface=boolean], [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attributeInfo.html
    """
    return _wrapCommand(cmds.attributeInfo, args, kwargs)


def attributeMenu(*args, **kwargs):  # noqa
    """Action to generate popup connection menus for Hypershade.

    attributeMenu([beginMenu=boolean], [editor=string], [finishMenu=boolean],
    [inputs=boolean], [plug=name], [regPulldownMenuCommand=string],
    [unregPulldownMenuCommand=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attributeMenu.html
    """
    return _wrapCommand(cmds.attributeMenu, args, kwargs)


def attributeName(*args, **kwargs):  # noqa
    """This command takes one "node.

    attributeName([leaf=boolean], [long=boolean], [nice=boolean], [short=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attributeName.html
    """
    return _wrapCommand(cmds.attributeName, args, kwargs)


def attributeQuery(*args, **kwargs):  # noqa
    """attributeQuery returns information about the configuration of an attribute.

    attributeQuery([affectsAppearance=boolean], [affectsWorldspace=boolean],
    [attributeType=boolean], [cachedInternally=boolean], [categories=boolean],
    [channelBox=boolean], [connectable=boolean], [enum=boolean], [exists=boolean],
    [hidden=boolean], [indeterminant=boolean], [indexMatters=boolean], [internal=boolean],
    [internalGet=boolean], [internalSet=boolean], [keyable=boolean],
    [listChildren=boolean], [listDefault=boolean], [listEnum=boolean],
    [listParent=boolean], [listSiblings=boolean], [localizedListEnum=boolean],
    [longName=boolean], [maxExists=boolean], [maximum=boolean], [message=boolean],
    [minExists=boolean], [minimum=boolean], [multi=boolean], [niceName=boolean],
    [node=name], [numberOfChildren=boolean], [range=boolean], [rangeExists=boolean],
    [readable=boolean], [renderSource=boolean], [shortName=boolean], [softMax=boolean],
    [softMaxExists=boolean], [softMin=boolean], [softMinExists=boolean],
    [softRange=boolean], [softRangeExists=boolean], [storable=boolean], [type=string],
    [typeExact=string], [usedAsColor=boolean], [usedAsFilename=boolean],
    [usesMultiBuilder=boolean], [worldspace=boolean], [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attributeQuery.html
    """
    return _wrapCommand(cmds.attributeQuery, args, kwargs)


def attrNavigationControlGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    attrNavigationControlGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [attrNavDecision=[name, string]],
    [attribute=name], [backgroundColor=[float, float, float]], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [connectAttrToDropped=script], [connectNodeToDropped=script],
    [connectToExisting=script], [createNew=script], [defaultTraversal=script],
    [defineTemplate=string], [delete=string], [disconnect=script], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [extraButton=boolean], [extraButtonCommand=script], [extraButtonIcon=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [ignore=script], [ignoreNotSupported=boolean], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [noIgnorableMenu=boolean],
    [noKeyableMenu=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [relatedNodes=script],
    [rowAttach=[int, string, int]], [statusBarMessage=string], [unignore=script],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/attrNavigationControlGrp.html
    """
    return _wrapCommand(cmds.attrNavigationControlGrp, args, kwargs)


def audioTrack(*args, **kwargs):  # noqa
    """This command is used for inserting and removing tracks related to the audio clips
    displayed in the sequencer.

    audioTrack([insertTrack=uint], [lock=boolean], [mute=boolean], [numTracks=uint],
    [removeEmptyTracks=boolean], [removeTrack=uint], [solo=boolean], [swapTracks=[uint,
    uint]], [title=string], [track=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/audioTrack.html
    """
    return _wrapCommand(cmds.audioTrack, args, kwargs)


def autoKeyframe(*args, **kwargs):  # noqa
    """With no flags, this command will set keyframes on all attributes that have been modified
    since an "autoKeyframe -state on" command was issued.

    autoKeyframe([addAttr=name], [characterOption=string], [listAttr=boolean],
    [noReset=boolean], [state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/autoKeyframe.html
    """
    return _wrapCommand(cmds.autoKeyframe, args, kwargs)


def autoPlace(*args, **kwargs):  # noqa
    """This command takes a point in the centre of the current modeling pane and projects it onto
    the live surface.

    autoPlace([useMouse=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/autoPlace.html
    """
    return _wrapCommand(cmds.autoPlace, args, kwargs)


def autoSave(*args, **kwargs):  # noqa
    """Provides an interface to the auto-save mechanism.

    autoSave([destination=int], [destinationFolder=boolean], [enable=boolean],
    [folder=string], [interval=float], [limitBackups=boolean], [maxBackups=int],
    [perform=boolean], [prompt=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/autoSave.html
    """
    return _wrapCommand(cmds.autoSave, args, kwargs)


def backgroundEvaluationManager(*args, **kwargs):  # noqa
    """Allows user to pause and restart background evaluations.

    backgroundEvaluationManager([interrupt=boolean], [mode=string], [pause=boolean],
    [resume=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/backgroundEvaluationManager.html
    """
    return _wrapCommand(cmds.backgroundEvaluationManager, args, kwargs)


def bakeClip(*args, **kwargs):  # noqa
    """This command is used to bake clips and blends into a single clip.

    bakeClip([blend=[uint, uint]], [clipIndex=uint], [keepOriginals=boolean], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bakeClip.html
    """
    return _wrapCommand(cmds.bakeClip, args, kwargs)


def bakeDeformer(*args, **kwargs):  # noqa
    """Given a rigged character, whose mesh shape is determined by a set of deformers,
    bakeDeformer calculates linear blend skin weights most closely approximating observed
    deformations.

    bakeDeformer([colorizeSkeleton=boolean], [customRangeOfMotion=timerange],
    [dstMeshName=string], [dstSkeletonName=string], [hierarchy=boolean],
    [influences=string[]], [maxInfluences=int], [pruneWeights=float], [smoothWeights=int],
    [srcMeshName=string], [srcSkeletonName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bakeDeformer.html
    """
    return _wrapCommand(cmds.bakeDeformer, args, kwargs)


def bakePartialHistory(*args, **kwargs):  # noqa
    """This command is used to bake sections of the construction history of a shape node when
    possible.

    bakePartialHistory([allShapes=boolean], [postSmooth=boolean], [preCache=boolean],
    [preDeformers=boolean], [prePostDeformers=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bakePartialHistory.html
    """
    return _wrapCommand(cmds.bakePartialHistory, args, kwargs)


def bakeResults(*args, **kwargs):  # noqa
    """This command allows the user to replace a chain of dependency nodes which define the value
    for an attribute with a single animation curve.

    bakeResults( objects , [animation=string], [attribute=string],
    [bakeOnOverrideLayer=boolean], [controlPoints=boolean], [destinationLayer=string],
    [disableImplicitControl=boolean], [float=floatrange], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [minimizeRotation=boolean],
    [oversamplingRate=uint], [preserveOutsideKeys=boolean],
    [removeBakedAnimFromLayer=boolean], [removeBakedAttributeFromLayer=boolean],
    [resolveWithoutLayer=string], [sampleBy=time], [shape=boolean], [simulation=boolean],
    [smart=[[, boolean, float, ]]], [sparseAnimCurveBake=boolean], [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bakeResults.html
    """
    return _wrapCommand(cmds.bakeResults, args, kwargs)


def bakeSimulation(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    bakeSimulation( objects , [animation=string], [attribute=string],
    [bakeOnOverrideLayer=boolean], [controlPoints=boolean], [destinationLayer=string],
    [disableImplicitControl=boolean], [float=floatrange], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [minimizeRotation=boolean],
    [preserveOutsideKeys=boolean], [removeBakedAnimFromLayer=boolean],
    [removeBakedAttributeFromLayer=boolean], [resolveWithoutLayer=string],
    [sampleBy=time], [shape=boolean], [simulation=boolean], [smart=[[, boolean, float,
    ]]], [sparseAnimCurveBake=boolean], [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bakeSimulation.html
    """
    return _wrapCommand(cmds.bakeSimulation, args, kwargs)


def baseTemplate(*args, **kwargs):  # noqa
    """This is the class for the commands that edit and/or query templates.

    baseTemplate([string], [exists=boolean], [fileName=string], [force=boolean],
    [load=boolean], [matchFile=string], [silent=boolean], [unload=boolean],
    [viewList=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/baseTemplate.html
    """
    return _wrapCommand(cmds.baseTemplate, args, kwargs)


def baseView(*args, **kwargs):  # noqa
    """A view defines the layout information for the attributes of a particular node type or
    container.

    baseView(string, [itemInfo=string], [itemList=boolean], [viewDescription=boolean],
    [viewLabel=boolean], [viewList=boolean], [viewName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/baseView.html
    """
    return _wrapCommand(cmds.baseView, args, kwargs)


def batchRender(*args, **kwargs):  # noqa
    """The batchRender command is used to spawn off a separate rendering session of the current
    maya file.

    batchRender([filename=string], [melCommand=string], [numProcs=int],
    [preRenderCommand=string], [remoteRenderMachine=string],
    [renderCommandOptions=string], [showImage=boolean], [status=string],
    [useRemoteRender=boolean], [useStandalone=boolean], [verbosity=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/batchRender.html
    """
    return _wrapCommand(cmds.batchRender, args, kwargs)


def bevel(*args, **kwargs):  # noqa
    """The bevel command creates a new bevel surface for the specified curve.

    bevel( [object] , [bevelShapeType=int], [caching=boolean], [constructionHistory=boolean],
    [cornerType=int], [depth=linear], [extrudeDepth=linear], [joinSurfaces=boolean],
    [name=string], [nodeState=int], [numberOfSides=int], [object=boolean], [polygon=int],
    [range=boolean], [tolerance=linear], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bevel.html
    """
    return _wrapCommand(cmds.bevel, args, kwargs)


def bevelPlus(*args, **kwargs):  # noqa
    """The bevelPlus command creates a new bevel surface for the specified curves using a given
    style curve.

    bevelPlus( curve [curve curve...] , [bevelInside=boolean], [capSides=int],
    [constructionHistory=boolean], [innerStyle=int], [joinSurfaces=boolean],
    [name=string], [normalsOutwards=boolean], [numberOfSides=int], [outerStyle=int],
    [polygon=int], [range=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bevelPlus.html
    """
    return _wrapCommand(cmds.bevelPlus, args, kwargs)


def bezierAnchorPreset(*args, **kwargs):  # noqa
    """This command provides a queryable interface for Bezier curve shapes.

    bezierAnchorPreset([preset=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorPreset.html
    """
    return _wrapCommand(cmds.bezierAnchorPreset, args, kwargs)


def bezierAnchorState(*args, **kwargs):  # noqa
    """The bezierAnchorState command provides an easy interface to modify anchor states:.

    bezierAnchorState([even=boolean], [smooth=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bezierAnchorState.html
    """
    return _wrapCommand(cmds.bezierAnchorState, args, kwargs)


def bezierCurveToNurbs(*args, **kwargs):  # noqa
    """The bezierCurveToNurbs command attempts to convert an existing NURBS curve to a Bezier
    curve.

    bezierCurveToNurbs( curve )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bezierCurveToNurbs.html
    """
    return _wrapCommand(cmds.bezierCurveToNurbs, args, kwargs)


def bezierInfo(*args, **kwargs):  # noqa
    """This command provides a queryable interface for Bezier curve shapes.

    bezierInfo([anchorFromCV=int], [cvFromAnchor=int], [isAnchorSelected=boolean],
    [isTangentSelected=boolean], [onlyAnchorsSelected=boolean],
    [onlyTangentsSelected=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bezierInfo.html
    """
    return _wrapCommand(cmds.bezierInfo, args, kwargs)


def bindSkin(*args, **kwargs):  # noqa
    """This command binds the currently selected objects to the currently selected skeletons.

    bindSkin( [objects] , [byClosestPoint=boolean], [byPartition=boolean],
    [colorJoints=boolean], [delete=boolean], [doNotDescend=boolean], [enable=boolean],
    [name=string], [partition=string], [toAll=boolean], [toSelectedBones=boolean],
    [toSkeleton=boolean], [unbind=boolean], [unbindKeepHistory=boolean], [unlock=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bindSkin.html
    """
    return _wrapCommand(cmds.bindSkin, args, kwargs)


def binMembership(*args, **kwargs):  # noqa
    """Command to assign nodes to bins.

    binMembership([addToBin=string], [exists=string], [inheritBinsFromNodes=name],
    [isValidBinName=string], [listBins=boolean], [makeExclusive=string],
    [notifyChanged=boolean], [removeFromBin=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/binMembership.html
    """
    return _wrapCommand(cmds.binMembership, args, kwargs)


def blend2(*args, **kwargs):  # noqa
    """This command creates a surface by blending between given curves.

    blend2( curve curve [curve...] , [autoAnchor=boolean], [autoNormal=boolean],
    [caching=boolean], [constructionHistory=boolean], [crvsInFirstRail=int],
    [flipLeftNormal=boolean], [flipRightNormal=boolean], [leftAnchor=float],
    [leftEnd=float], [leftStart=float], [multipleKnots=boolean], [name=string],
    [nodeState=int], [object=boolean], [polygon=int], [positionTolerance=float],
    [reverseLeft=boolean], [reverseRight=boolean], [rightAnchor=float], [rightEnd=float],
    [rightStart=float], [tangentTolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blend2.html
    """
    return _wrapCommand(cmds.blend2, args, kwargs)


def blendShape(*args, **kwargs):  # noqa
    """This command creates a blendShape deformer, which blends in specified amounts of each
    target shape to the initial base shape.

    blendShape( [objects] , [after=boolean], [afterReference=boolean], [automatic=boolean],
    [before=boolean], [components=boolean], [copyDelta=[uint, uint, uint]],
    [copyInBetweenDelta=[uint, uint, uint, uint]], [copyWeights=[uint, uint, uint]],
    [deformerTools=boolean], [envelope=float], [exclusive=string], [export=string],
    [exportTarget=[int, int]], [flipTarget=[uint, uint]], [frontOfChain=boolean],
    [geometry=string], [geometryIndices=boolean], [ignoreSelected=boolean],
    [inBetween=boolean], [inBetweenIndex=uint], [inBetweenType=string],
    [includeHiddenSelections=boolean], [ip=string], [mergeSource=int], [mergeTarget=uint],
    [mirrorDirection=uint], [mirrorTarget=[uint, uint]], [name=string],
    [normalizationGroups=boolean], [origin=string], [parallel=boolean], [prune=boolean],
    [remove=boolean], [resetTargetDelta=[uint, uint]], [selectedComponents=boolean],
    [split=boolean], [suppressDialog=boolean], [symmetryAxis=string],
    [symmetryEdge=string], [symmetrySpace=uint], [tangentSpace=boolean], [target=[string,
    uint, string, float]], [topologyCheck=boolean], [transform=string],
    [useComponentTags=boolean], [weight=[uint, float]], [weightCount=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blendShape.html
    """
    return _wrapCommand(cmds.blendShape, args, kwargs)


def blendShapeEditor(*args, **kwargs):  # noqa
    """This command creates an editor that derives from the base editor class that has controls
    for blendShape, control nodes.

    blendShapeEditor( string , [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string],
    [selectionConnection=string], [stateString=boolean], [targetControlList=boolean],
    [targetList=boolean], [unParent=boolean], [unlockMainConnection=boolean],
    [updateMainConnection=boolean], [useTemplate=string], [verticalSliders=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blendShapeEditor.html
    """
    return _wrapCommand(cmds.blendShapeEditor, args, kwargs)


def blendShapePanel(*args, **kwargs):  # noqa
    """This command creates a panel that derives from the base panel class that houses a
    blendShapeEditor.

    blendShapePanel( string , [blendShapeEditor=boolean], [control=boolean], [copy=string],
    [createString=boolean], [defineTemplate=string], [docTag=string],
    [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean],
    [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean],
    [needsInit=boolean], [parent=string], [popupMenuProcedure=script],
    [replacePanel=string], [tearOff=boolean], [tearOffCopy=string],
    [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blendShapePanel.html
    """
    return _wrapCommand(cmds.blendShapePanel, args, kwargs)


def blendTwoAttr(*args, **kwargs):  # noqa
    """A blendTwoAttr nodes takes two inputs, and blends the values of the inputs from one to the
    other, into an output value.

    blendTwoAttr( [objects] , [attribute=string], [attribute0=name], [attribute1=name],
    [blender=name], [controlPoints=boolean], [driver=int], [name=string], [shape=boolean],
    [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blendTwoAttr.html
    """
    return _wrapCommand(cmds.blendTwoAttr, args, kwargs)


def blindDataType(*args, **kwargs):  # noqa
    """This command creates a blind data type, which is represented by a blindDataTemplate node
    in the DG.

    blindDataType([dataType=string], [longDataName=string], [longNames=boolean],
    [query=boolean], [shortDataName=string], [shortNames=boolean], [typeId=int],
    [typeNames=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/blindDataType.html
    """
    return _wrapCommand(cmds.blindDataType, args, kwargs)


def boneLattice(*args, **kwargs):  # noqa
    """This command creates/edits/queries a boneLattice deformer.

    boneLattice( objects , [after=boolean], [afterReference=boolean], [before=boolean],
    [bicep=float], [components=boolean], [deformerTools=boolean], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [joint=string],
    [lengthIn=float], [lengthOut=float], [name=string], [parallel=boolean],
    [prune=boolean], [remove=boolean], [selectedComponents=boolean], [split=boolean],
    [transform=string], [tricep=float], [useComponentTags=boolean], [widthLeft=float],
    [widthRight=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/boneLattice.html
    """
    return _wrapCommand(cmds.boneLattice, args, kwargs)


def boundary(*args, **kwargs):  # noqa
    """This command produces a boundary surface given 3 or 4 curves.

    boundary( string string string [string] , [caching=boolean],
    [constructionHistory=boolean], [endPoint=boolean], [endPointTolerance=linear],
    [name=string], [nodeState=int], [object=boolean], [order=boolean], [polygon=int],
    [range=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/boundary.html
    """
    return _wrapCommand(cmds.boundary, args, kwargs)


def boxDollyCtx(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a dolly context.

    boxDollyCtx([alternateContext=boolean], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [toolName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/boxDollyCtx.html
    """
    return _wrapCommand(cmds.boxDollyCtx, args, kwargs)


def boxZoomCtx(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a box zoom context.

    boxZoomCtx( object , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [zoomScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/boxZoomCtx.html
    """
    return _wrapCommand(cmds.boxZoomCtx, args, kwargs)


def bufferCurve(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    bufferCurve( animatedObject , [animation=string], [attribute=string],
    [controlPoints=boolean], [exists=boolean], [float=floatrange], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [overwrite=boolean], [shape=boolean],
    [swap=boolean], [time=timerange], [useReferencedCurve=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/bufferCurve.html
    """
    return _wrapCommand(cmds.bufferCurve, args, kwargs)


def buildBookmarkMenu(*args, **kwargs):  # noqa
    """This command handles building the "dynamic" Bookmark menu, to show all bookmarks ("sets")
    of a specified type ("sets -text").

    buildBookmarkMenu( string , [editor=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/buildBookmarkMenu.html
    """
    return _wrapCommand(cmds.buildBookmarkMenu, args, kwargs)


def buildKeyframeMenu(*args, **kwargs):  # noqa
    """This command handles building the "dynamic" Keyframe menu, to show attributes of currently
    selected objects, filtered by the current manipulator.

    buildKeyframeMenu( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/buildKeyframeMenu.html
    """
    return _wrapCommand(cmds.buildKeyframeMenu, args, kwargs)


def button(*args, **kwargs):  # noqa
    """Create a button control capable of displaying a textual label and executing a command when
    selected by the user.

    button( [string] , [actOnPress=boolean], [actionIsSubstitute=boolean], [align=string],
    [annotation=string], [backgroundColor=[float, float, float]], [command=script],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [recomputeSize=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/button.html
    """
    return _wrapCommand(cmds.button, args, kwargs)


def buttonManip(*args, **kwargs):  # noqa
    """This creates a button manipulator.

    buttonManip( script [selectionItem] , [icon=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/buttonManip.html
    """
    return _wrapCommand(cmds.buttonManip, args, kwargs)


def cacheEvaluator(*args, **kwargs):  # noqa
    """This command controls caching configuration.

    cacheEvaluator([cacheFillMode=string], [cacheFillOrder=string],
    [cacheInvalidate=timerange], [cacheName=string], [cachedFrames=boolean],
    [cachingPoints=boolean], [creationParameters=boolean], [delegateEvaluation=boolean],
    [dynamicsAsyncRefresh=boolean], [dynamicsSupportActive=boolean],
    [dynamicsSupportEnabled=boolean], [flushCache=string], [flushCacheRange=[timerange,
    boolean]], [flushCacheSync=boolean], [flushCacheWait=boolean],
    [hybridCacheMode=string], [layeredEvaluationActive=boolean],
    [layeredEvaluationCachingPoints=boolean], [layeredEvaluationEnabled=boolean],
    [listCacheNames=boolean], [listCachedNodes=boolean], [listValueNames=boolean],
    [newAction=string], [newActionParam=string], [newFilter=string],
    [newFilterParam=string], [newRule=string], [newRuleParam=string],
    [pauseInvalidation=boolean], [preventFrameSkip=boolean], [resetRules=boolean],
    [resourceUsage=boolean], [resumeInvalidation=boolean], [safeMode=boolean],
    [safeModeMessages=boolean], [safeModeTriggered=boolean], [valueName=string],
    [waitForCache=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cacheEvaluator.html
    """
    return _wrapCommand(cmds.cacheEvaluator, args, kwargs)


def cacheFile(*args, **kwargs):  # noqa
    """Creates one or more cache files on disk to store attribute data for a span of frames.

    cacheFile([appendFrame=boolean], [attachFile=boolean], [cacheFileNode=string],
    [cacheFormat=string], [cacheInfo=string], [cacheableAttrs=string],
    [cacheableNode=string], [channelIndex=boolean], [channelName=string],
    [convertPc2=boolean], [createCacheNode=boolean], [creationChannelName=string],
    [dataSize=boolean], [deleteCachedFrame=boolean], [descriptionFileName=boolean],
    [directory=string], [doubleToFloat=boolean], [endTime=time], [fileName=string],
    [format=string], [geometry=boolean], [inAttr=string], [inTangent=string],
    [interpEndTime=time], [interpStartTime=time], [noBackup=boolean], [outAttr=string],
    [outTangent=string], [pc2File=string], [pointCount=boolean], [points=string],
    [pointsAndNormals=string], [prefix=boolean], [refresh=boolean],
    [replaceCachedFrame=boolean], [replaceWithoutSimulating=boolean], [runupFrames=int],
    [sampleMultiplier=int], [simulationRate=time], [singleCache=boolean],
    [startTime=time], [staticCache=boolean], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cacheFile.html
    """
    return _wrapCommand(cmds.cacheFile, args, kwargs)


def cacheFileCombine(*args, **kwargs):  # noqa
    """Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles
    for a given object.

    cacheFileCombine([cacheIndex=boolean], [channelName=string], [connectCache=string],
    [keepWeights=boolean], [layerNode=boolean], [nextAvailable=boolean], [object=string],
    [objectIndex=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cacheFileCombine.html
    """
    return _wrapCommand(cmds.cacheFileCombine, args, kwargs)


def cacheFileMerge(*args, **kwargs):  # noqa
    """If selected/specified caches can be successfully merged, will return the start/end frames
    of the new cache followed by the start/end frames of any gaps in the merged cache for
    which no data should be written to file.

    cacheFileMerge([endTime=time], [geometry=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cacheFileMerge.html
    """
    return _wrapCommand(cmds.cacheFileMerge, args, kwargs)


def cacheFileTrack(*args, **kwargs):  # noqa
    """This command is used for inserting and removing tracks related to the caches displayed in
    the trax editor.

    cacheFileTrack([insertTrack=uint], [lock=boolean], [mute=boolean],
    [removeEmptyTracks=boolean], [removeTrack=uint], [solo=boolean], [track=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cacheFileTrack.html
    """
    return _wrapCommand(cmds.cacheFileTrack, args, kwargs)


def callbacks(*args, **kwargs):  # noqa
    """This command allows you to add callbacks at key times during UI creation so that the Maya
    UI can be extended.

    callbacks([addCallback=script], [clearAllCallbacks=boolean], [clearCallbacks=boolean],
    [describeHooks=boolean], [dumpCallbacks=boolean], [executeCallbacks=boolean],
    [hook=string], [listCallbacks=boolean], [owner=string], [removeCallback=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/callbacks.html
    """
    return _wrapCommand(cmds.callbacks, args, kwargs)


def camera(*args, **kwargs):  # noqa
    """Create, edit, or query a camera with the specified properties.

    camera( [camera] , [aspectRatio=float], [cameraScale=float], [centerOfInterest=linear],
    [clippingPlanes=boolean], [depthOfField=boolean], [displayFieldChart=boolean],
    [displayFilmGate=boolean], [displayFilmOrigin=boolean], [displayFilmPivot=boolean],
    [displayGateMask=boolean], [displayResolution=boolean], [displaySafeAction=boolean],
    [displaySafeTitle=boolean], [fStop=float], [farClipPlane=linear],
    [farFocusDistance=linear], [filmFit=string], [filmFitOffset=float],
    [filmRollOrder=string], [filmRollValue=angle], [filmTranslateH=float],
    [filmTranslateV=float], [focalLength=float], [focusDistance=linear],
    [homeCommand=string], [horizontalFieldOfView=angle], [horizontalFilmAperture=float],
    [horizontalFilmOffset=float], [horizontalPan=float], [horizontalRollPivot=float],
    [horizontalShake=float], [journalCommand=boolean], [lensSqueezeRatio=float],
    [lockTransform=boolean], [motionBlur=boolean], [name=string], [nearClipPlane=linear],
    [nearFocusDistance=linear], [orthographic=boolean], [orthographicWidth=linear],
    [overscan=float], [panZoomEnabled=boolean], [position=[linear, linear, linear]],
    [postScale=float], [preScale=float], [renderPanZoom=boolean], [rotation=[angle, angle,
    angle]], [shakeEnabled=boolean], [shakeOverscan=float],
    [shakeOverscanEnabled=boolean], [shutterAngle=angle], [startupCamera=boolean],
    [stereoHorizontalImageTranslate=float],
    [stereoHorizontalImageTranslateEnabled=boolean], [verticalFieldOfView=angle],
    [verticalFilmAperture=float], [verticalFilmOffset=float], [verticalLock=boolean],
    [verticalPan=float], [verticalRollPivot=float], [verticalShake=float],
    [worldCenterOfInterest=[linear, linear, linear]], [worldUp=[linear, linear, linear]],
    [zoom=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/camera.html
    """
    return _wrapCommand(cmds.camera, args, kwargs)


def cameraSet(*args, **kwargs):  # noqa
    """This command manages camera set nodes.

    cameraSet([active=boolean], [appendTo=boolean], [camera=string], [clearDepth=boolean],
    [deleteAll=boolean], [deleteLayer=boolean], [insertAt=boolean], [layer=int],
    [name=string], [numLayers=boolean], [objectSet=string], [order=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cameraSet.html
    """
    return _wrapCommand(cmds.cameraSet, args, kwargs)


def cameraView(*args, **kwargs):  # noqa
    """This command creates a preset view for a camera which is then independent of the camera.

    cameraView( [object] , [addBookmark=boolean], [animate=boolean], [bookmarkType=int],
    [camera=name], [name=string], [removeBookmark=boolean], [setCamera=boolean],
    [setView=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cameraView.html
    """
    return _wrapCommand(cmds.cameraView, args, kwargs)


def canCreateCaddyManip(*args, **kwargs):  # noqa
    """This command returns true if there can be a manipulator made for the specified selection,
    false otherwise.

    canCreateCaddyManip( object )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/canCreateCaddyManip.html
    """
    return _wrapCommand(cmds.canCreateCaddyManip, args, kwargs)


def canCreateManip(*args, **kwargs):  # noqa
    """This command returns true if there can be a manipulator made for the specified selection,
    false otherwise.

    canCreateManip( object )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/canCreateManip.html
    """
    return _wrapCommand(cmds.canCreateManip, args, kwargs)


def canvas(*args, **kwargs):  # noqa
    """Creates a control capable of displaying a color swatch.

    canvas( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [hsvValue=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [pressCommand=script], [preventOverride=boolean], [rgbValue=[float, float, float]],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/canvas.html
    """
    return _wrapCommand(cmds.canvas, args, kwargs)


def changeSubdivComponentDisplayLevel(*args, **kwargs):  # noqa
    """Explicitly forces the subdivision surface to display components at a particular level of
    refinement.

    changeSubdivComponentDisplayLevel([level=int], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivComponentDisplayLevel.html
    """
    return _wrapCommand(cmds.changeSubdivComponentDisplayLevel, args, kwargs)


def changeSubdivRegion(*args, **kwargs):  # noqa
    """Changes a subdivision surface region based on the command parameters.

    changeSubdivRegion([action=int], [level=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/changeSubdivRegion.html
    """
    return _wrapCommand(cmds.changeSubdivRegion, args, kwargs)


def channelBox(*args, **kwargs):  # noqa
    """This command creates a channel box, which is sensitive to the active list.

    channelBox( [string] , [annotation=string], [attrBgColor=[float, float, float]],
    [attrColor=[float, float, float]], [attrFilter=string], [attrRegex=string],
    [attributeEditorMode=boolean], [backgroundColor=[float, float, float]],
    [containerAtTop=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [enableLabelSelection=boolean], [execute=[string, boolean]], [exists=boolean],
    [fieldWidth=int], [fixedAttrList=string[]], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [historyObjectList=boolean],
    [hyperbolic=boolean], [inputs=boolean], [isObscured=boolean], [labelWidth=int],
    [longNames=boolean], [mainListConnection=string], [mainObjectList=boolean],
    [manage=boolean], [maxHeight=int], [maxWidth=int], [niceNames=boolean],
    [noBackground=boolean], [nodeRegex=string], [numberOfPopupMenus=boolean],
    [outputObjectList=boolean], [outputs=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [select=string],
    [selectedHistoryAttributes=boolean], [selectedMainAttributes=boolean],
    [selectedOutputAttributes=boolean], [selectedShapeAttributes=boolean],
    [shapeObjectList=boolean], [shapes=boolean], [showNamespace=boolean],
    [showTransforms=boolean], [speed=float], [statusBarMessage=string],
    [takeFocus=boolean], [ufeFixedAttrList=[string, string[]]], [update=boolean],
    [useManips=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/channelBox.html
    """
    return _wrapCommand(cmds.channelBox, args, kwargs)


def character(*args, **kwargs):  # noqa
    """This command is used to manage the membership of a character.

    character( objects , [addElement=name], [addOffsetObject=string], [anyMember=name],
    [characterPlug=boolean], [clear=name], [empty=boolean], [excludeDynamic=boolean],
    [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean],
    [excludeVisibility=boolean], [flatten=name], [forceElement=name], [include=name],
    [intersection=name], [isIntersecting=name], [isMember=name], [library=boolean],
    [memberIndex=uint], [name=string], [noWarnings=boolean], [nodesOnly=boolean],
    [offsetNode=boolean], [remove=name], [removeOffsetObject=string], [root=string],
    [scheduler=boolean], [split=name], [subtract=name], [text=string], [union=name],
    [userAlias=name])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/character.html
    """
    return _wrapCommand(cmds.character, args, kwargs)


def characterize(*args, **kwargs):  # noqa
    """This command is used to scan a joint hierarchy for predefined joint names or labels.

    characterize([activatePivot=boolean], [addAuxEffector=boolean],
    [addFloorContactPlane=boolean], [addMissingEffectors=boolean],
    [attributeFromHIKProperty=string], [attributeFromHIKPropertyMode=string],
    [autoActivateBodyPart=boolean], [changePivotPlacement=boolean], [effectors=string],
    [fkSkeleton=string], [name=string], [pinHandFeet=boolean], [placeNewPivot=boolean],
    [posture=string], [sourceSkeleton=string], [stancePose=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/characterize.html
    """
    return _wrapCommand(cmds.characterize, args, kwargs)


def characterMap(*args, **kwargs):  # noqa
    """This command is used to create a correlation between the attributes of 2 or more
    characters.

    characterMap([mapAttr=[string, string]], [mapMethod=string], [mapNode=[string, string]],
    [mapping=string], [proposedMapping=boolean], [unmapAttr=[string, string]],
    [unmapNode=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/characterMap.html
    """
    return _wrapCommand(cmds.characterMap, args, kwargs)


def checkBox(*args, **kwargs):  # noqa
    """This command creates a check box.

    checkBox( [string] , [align=string], [annotation=string], [backgroundColor=[float, float,
    float]], [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [recomputeSize=boolean], [statusBarMessage=string], [useTemplate=string],
    [value=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/checkBox.html
    """
    return _wrapCommand(cmds.checkBox, args, kwargs)


def checkBoxGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    checkBoxGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [changeCommand1=script], [changeCommand2=script],
    [changeCommand3=script], [changeCommand4=script], [columnAlign=[int, string]],
    [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [editable=boolean], [enable=boolean], [enable1=boolean],
    [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [label1=string], [label2=string], [label3=string], [label4=string],
    [labelArray2=[string, string]], [labelArray3=[string, string, string]],
    [labelArray4=[string, string, string, string]], [manage=boolean],
    [noBackground=boolean], [numberOfCheckBoxes=int], [numberOfPopupMenus=boolean],
    [offCommand=script], [offCommand1=script], [offCommand2=script], [offCommand3=script],
    [offCommand4=script], [onCommand=script], [onCommand1=script], [onCommand2=script],
    [onCommand3=script], [onCommand4=script], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string],
    [useTemplate=string], [value1=boolean], [value2=boolean], [value3=boolean],
    [value4=boolean], [valueArray2=[boolean, boolean]], [valueArray3=[boolean, boolean,
    boolean]], [valueArray4=[boolean, boolean, boolean, boolean]], [vertical=boolean],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/checkBoxGrp.html
    """
    return _wrapCommand(cmds.checkBoxGrp, args, kwargs)


def checkDefaultRenderGlobals(*args, **kwargs):  # noqa
    """To query whether or not the defaultRenderGlobals node has been modified since the last
    file save, use `ls -modified`.

    checkDefaultRenderGlobals([string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/checkDefaultRenderGlobals.html
    """
    return _wrapCommand(cmds.checkDefaultRenderGlobals, args, kwargs)


def choice(*args, **kwargs):  # noqa
    """The choice command provides a mechanism for changing the inputs to an attribute based on
    some (usually time-based) criteria.

    choice( [objects] , [attribute=string], [controlPoints=boolean], [index=uint],
    [name=string], [selector=name], [shape=boolean], [sourceAttribute=name], [time=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/choice.html
    """
    return _wrapCommand(cmds.choice, args, kwargs)


def circle(*args, **kwargs):  # noqa
    """The circle command creates a circle or partial circle (arc).

    circle([caching=boolean], [center=[linear, linear, linear]], [centerX=linear],
    [centerY=linear], [centerZ=linear], [constructionHistory=boolean], [degree=int],
    [first=[linear, linear, linear]], [firstPointX=linear], [firstPointY=linear],
    [firstPointZ=linear], [fixCenter=boolean], [name=string], [nodeState=int],
    [normal=[linear, linear, linear]], [normalX=linear], [normalY=linear],
    [normalZ=linear], [object=boolean], [radius=linear], [sections=int], [sweep=angle],
    [tolerance=linear], [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/circle.html
    """
    return _wrapCommand(cmds.circle, args, kwargs)


def circularFillet(*args, **kwargs):  # noqa
    """The cmd is used to compute the rolling ball surface fillet ( circular fillet ) between two
    given NURBS surfaces.

    circularFillet( [surface] [surface] , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [name=string], [nodeState=int], [object=boolean],
    [positionTolerance=float], [primaryRadius=linear], [secondaryRadius=linear],
    [tangentTolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/circularFillet.html
    """
    return _wrapCommand(cmds.circularFillet, args, kwargs)


def clearCache(*args, **kwargs):  # noqa
    """Even though dependency graph values are computed or dirty they may still occupy space
    temporarily within the nodes.

    clearCache([allNodes=boolean], [computed=boolean], [dirty=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clearCache.html
    """
    return _wrapCommand(cmds.clearCache, args, kwargs)


def clip(*args, **kwargs):  # noqa
    """This command is used to create, edit and query character clips.

    clip([absolute=boolean], [absoluteRotations=boolean], [active=string], [addTrack=boolean],
    [allAbsolute=boolean], [allClips=boolean], [allRelative=boolean],
    [allSourceClips=boolean], [animCurveRange=boolean], [character=boolean],
    [constraint=boolean], [copy=boolean], [defaultAbsolute=boolean], [duplicate=boolean],
    [endTime=time], [expression=boolean], [ignoreSubcharacters=boolean],
    [isolate=boolean], [leaveOriginal=boolean], [mapMethod=string], [name=string],
    [newName=string], [paste=boolean], [pasteInstance=boolean], [remove=boolean],
    [removeTrack=boolean], [rotationOffset=[float, float, float]],
    [rotationsAbsolute=boolean], [scheduleClip=boolean], [sourceClipName=boolean],
    [split=time], [startTime=time], [translationOffset=[float, float, float]],
    [useChannel=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clip.html
    """
    return _wrapCommand(cmds.clip, args, kwargs)


def clipEditor(*args, **kwargs):  # noqa
    """Create a clip editor with the given name.

    clipEditor( editorName , [allTrackHeights=int], [autoFit=string], [autoFitTime=string],
    [clipDropCmd=string], [clipStyle=int], [control=boolean], [defineTemplate=string],
    [deleteCmd=string], [deselectAll=boolean], [displayActiveKeyTangents=string],
    [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string],
    [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean],
    [filter=string], [forceMainConnection=string], [frameAll=boolean], [frameRange=[float,
    float]], [highlightConnection=string], [highlightedBlend=[string, string]],
    [highlightedClip=[string, string]], [initialized=boolean],
    [listAllCharacters=boolean], [listCurrentCharacters=boolean],
    [lockMainConnection=boolean], [lookAt=string], [mainListConnection=string],
    [manageSequencer=boolean], [menuContext=string], [panel=string], [parent=string],
    [selectBlend=[string, string, string]], [selectClip=[string, string]],
    [selectionConnection=string], [snapTime=string], [snapValue=string],
    [stateString=boolean], [unParent=boolean], [unlockMainConnection=boolean],
    [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clipEditor.html
    """
    return _wrapCommand(cmds.clipEditor, args, kwargs)


def clipEditorCurrentTimeCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to change current time within the track
    area of a clip editor.

    clipEditorCurrentTimeCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clipEditorCurrentTimeCtx.html
    """
    return _wrapCommand(cmds.clipEditorCurrentTimeCtx, args, kwargs)


def clipMatching(*args, **kwargs):  # noqa
    """This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.

    clipMatching([clipDst=[string, float]], [clipSrc=[string, float]], [matchRotation=uint],
    [matchTranslation=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clipMatching.html
    """
    return _wrapCommand(cmds.clipMatching, args, kwargs)


def clipSchedule(*args, **kwargs):  # noqa
    """This command is used to create, edit and query clips and blends in the Trax editor.

    clipSchedule([allAbsolute=boolean], [allRelative=boolean], [blend=[uint, uint]],
    [blendNode=[uint, uint]], [blendUsingNode=string], [character=boolean],
    [clipIndex=uint], [cycle=float], [defaultAbsolute=boolean], [enable=boolean],
    [group=boolean], [groupIndex=uint], [groupName=string], [hold=time],
    [insertTrack=uint], [instance=string], [listCurves=boolean], [listPairs=boolean],
    [lock=boolean], [mute=boolean], [name=string], [postCycle=float], [preCycle=float],
    [remove=boolean], [removeBlend=[uint, uint]], [removeEmptyTracks=boolean],
    [removeTrack=uint], [rotationsAbsolute=boolean], [scale=float], [shift=int],
    [shiftIndex=uint], [solo=boolean], [sourceClipName=boolean], [sourceEnd=time],
    [sourceStart=time], [start=time], [track=uint], [weight=float], [weightStyle=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clipSchedule.html
    """
    return _wrapCommand(cmds.clipSchedule, args, kwargs)


def clipSchedulerOutliner(*args, **kwargs):  # noqa
    """This command creates/edits/queries a clip scheduler outliner control.

    clipSchedulerOutliner( string , [annotation=string], [backgroundColor=[float, float,
    float]], [clipScheduler=string], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/clipSchedulerOutliner.html
    """
    return _wrapCommand(cmds.clipSchedulerOutliner, args, kwargs)


def closeCurve(*args, **kwargs):  # noqa
    """The closeCurve command closes a curve, making it periodic.

    closeCurve( curve , [blendBias=float], [blendKnotInsertion=boolean], [caching=boolean],
    [constructionHistory=boolean], [curveOnSurface=boolean], [name=string],
    [nodeState=int], [object=boolean], [parameter=float], [preserveShape=int],
    [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/closeCurve.html
    """
    return _wrapCommand(cmds.closeCurve, args, kwargs)


def closeSurface(*args, **kwargs):  # noqa
    """The closeSurface command closes a surface in the U, V, or both directions, making it
    periodic.

    closeSurface( [surface|surfaceIsoparm] , [blendBias=float], [blendKnotInsertion=boolean],
    [caching=boolean], [constructionHistory=boolean], [direction=int], [name=string],
    [nodeState=int], [object=boolean], [parameter=float], [preserveShape=int],
    [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/closeSurface.html
    """
    return _wrapCommand(cmds.closeSurface, args, kwargs)


def cluster(*args, **kwargs):  # noqa
    """The cluster command creates a cluster or edits the membership of an existing cluster.

    cluster( [objects] , [after=boolean], [afterReference=boolean], [before=boolean],
    [bindState=boolean], [components=boolean], [deformerTools=boolean], [envelope=float],
    [exclusive=string], [frontOfChain=boolean], [geometry=string],
    [geometryIndices=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [name=string], [parallel=boolean], [prune=boolean],
    [relative=boolean], [remove=boolean], [resetGeometry=boolean],
    [selectedComponents=boolean], [split=boolean], [useComponentTags=boolean],
    [weightedNode=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cluster.html
    """
    return _wrapCommand(cmds.cluster, args, kwargs)


def cmdFileOutput(*args, **kwargs):  # noqa
    """This command will open a text file to receive all of the commands and results that
    normally get printed to the Script Editor window or console.

    cmdFileOutput([close=uint], [closeAll=boolean], [open=string], [status=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cmdFileOutput.html
    """
    return _wrapCommand(cmds.cmdFileOutput, args, kwargs)


def cmdScrollFieldExecuter(*args, **kwargs):  # noqa
    """A script editor executer control used to issue script commands to Maya.

    cmdScrollFieldExecuter([annotation=string], [appendText=string],
    [autoCloseBraces=boolean], [backgroundColor=[float, float, float]], [clear=boolean],
    [commandCompletion=boolean], [copySelection=boolean], [currentLine=uint],
    [cutSelection=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [execute=boolean],
    [executeAll=boolean], [exists=boolean], [fileChangedCommand=script],
    [filename=boolean], [filterKeyPress=script], [fullPathName=boolean],
    [hasFocus=boolean], [hasSelection=boolean], [height=int], [highlightColor=[float,
    float, float]], [insertText=string], [isObscured=boolean], [load=boolean],
    [loadContents=string], [loadFile=string], [manage=boolean],
    [modificationChangedCommand=script], [modified=boolean], [noBackground=boolean],
    [numberOfLines=uint], [numberOfPopupMenus=boolean], [objectPathCompletion=boolean],
    [parent=string], [pasteSelection=boolean], [popupMenuArray=boolean],
    [preventOverride=boolean], [redo=boolean], [removeStoredContents=string],
    [replaceAll=[string, string]], [saveFile=string], [saveSelection=string],
    [saveSelectionToShelf=boolean], [searchAndSelect=boolean], [searchDown=boolean],
    [searchMatchCase=boolean], [searchString=string], [searchWraps=boolean],
    [select=[uint, uint]], [selectAll=boolean], [selectedText=boolean],
    [showLineNumbers=boolean], [showTabsAndSpaces=boolean], [showTooltipHelp=boolean],
    [source=boolean], [sourceType=string], [spacesPerTab=uint], [statusBarMessage=string],
    [storeContents=string], [tabsForIndent=boolean], [text=string], [textLength=boolean],
    [undo=boolean], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cmdScrollFieldExecuter.html
    """
    return _wrapCommand(cmds.cmdScrollFieldExecuter, args, kwargs)


def cmdScrollFieldReporter(*args, **kwargs):  # noqa
    """A script editor reporter control used to receive and display the history of processed
    commmands.

    cmdScrollFieldReporter([annotation=string], [backgroundColor=[float, float, float]],
    [clear=boolean], [copySelection=boolean], [cutSelection=boolean],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [echoAllCommands=boolean], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [filterSourceType=string], [fullPathName=boolean], [hasFocus=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [lineNumbers=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [pasteSelection=boolean], [popupMenuArray=boolean],
    [preventOverride=boolean], [receiveFocusCommand=script], [saveSelection=string],
    [saveSelectionToShelf=boolean], [select=[uint, uint]], [selectAll=boolean],
    [stackTrace=boolean], [statusBarMessage=string], [suppressErrors=boolean],
    [suppressInfo=boolean], [suppressResults=boolean], [suppressStackTrace=boolean],
    [suppressWarnings=boolean], [text=string], [textLength=boolean], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cmdScrollFieldReporter.html
    """
    return _wrapCommand(cmds.cmdScrollFieldReporter, args, kwargs)


def cmdShell(*args, **kwargs):  # noqa
    """This command creates a scrolling field that behaves similar to a unix shell for entering
    user input.

    cmdShell( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [clear=boolean], [command=string], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfHistoryLines=int], [numberOfPopupMenus=boolean], [numberOfSavedLines=int],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [prompt=string],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cmdShell.html
    """
    return _wrapCommand(cmds.cmdShell, args, kwargs)


def coarsenSubdivSelectionList(*args, **kwargs):  # noqa
    """Coarsens a subdivision surface set of components based on the selection list.

    coarsenSubdivSelectionList()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/coarsenSubdivSelectionList.html
    """
    return _wrapCommand(cmds.coarsenSubdivSelectionList, args, kwargs)


def collision(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    collision( [objects] , [friction=float], [name=string], [offset=float],
    [resilience=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/collision.html
    """
    return _wrapCommand(cmds.collision, args, kwargs)


def color(*args, **kwargs):  # noqa
    """This command sets the dormant wireframe color of the specified objects to be their class
    color or if the -ud/userDefined flag is specified, one of the user defined colors.

    color( [objects] , [rgbColor=[float, float, float]], [userDefined=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/color.html
    """
    return _wrapCommand(cmds.color, args, kwargs)


def colorAtPoint(*args, **kwargs):  # noqa
    """The `colorAtPoint` command is used to query textures or ocean shaders at passed in uv
    coordinates.

    colorAtPoint([coordU=float], [coordV=float], [maxU=float], [maxV=float], [minU=float],
    [minV=float], [output=string], [samplesU=uint], [samplesV=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorAtPoint.html
    """
    return _wrapCommand(cmds.colorAtPoint, args, kwargs)


def colorEditor(*args, **kwargs):  # noqa
    """The `colorEditor` command displays a modal dialog that may be used to specify colors in
    RGB or HSV.

    colorEditor([alpha=float], [hsvValue=[float, float, float]], [mini=boolean],
    [parent=string], [position=[int, int]], [result=boolean], [rgbValue=[float, float,
    float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorEditor.html
    """
    return _wrapCommand(cmds.colorEditor, args, kwargs)


def colorIndex(*args, **kwargs):  # noqa
    """The index specifies a color index in the color palette.

    colorIndex( int [float float float] , [hueSaturationValue=boolean],
    [resetToFactory=boolean], [resetToSaved=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorIndex.html
    """
    return _wrapCommand(cmds.colorIndex, args, kwargs)


def colorIndexSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    colorIndexSliderGrp( groupName , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [forceDragRefresh=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [invisible=int], [isObscured=boolean], [label=string], [manage=boolean],
    [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int,
    string, int]], [statusBarMessage=string], [useTemplate=string], [value=int],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorIndexSliderGrp.html
    """
    return _wrapCommand(cmds.colorIndexSliderGrp, args, kwargs)


def colorInputWidgetGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    colorInputWidgetGrp( groupName , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [alphaValue=float], [annotation=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [forceDragRefresh=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [hsvValue=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [rgbValue=[float, float, float]], [rowAttach=[int, string, int]],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorInputWidgetGrp.html
    """
    return _wrapCommand(cmds.colorInputWidgetGrp, args, kwargs)


def colorManagementCatalog(*args, **kwargs):  # noqa
    """This non-undoable action performs additions and removals of custom color transforms from
    the Autodesk native color transform catalog.

    colorManagementCatalog([addTransform=string], [editUserTransformPath=string],
    [listSupportedExtensions=boolean], [listTransformConnections=boolean], [path=string],
    [queryUserTransformPath=boolean], [removeTransform=string],
    [transformConnection=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorManagementCatalog.html
    """
    return _wrapCommand(cmds.colorManagementCatalog, args, kwargs)


def colorManagementConvert(*args, **kwargs):  # noqa
    """This command can be used to convert rendering (a.

    colorManagementConvert([toDisplaySpace=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorManagementConvert.html
    """
    return _wrapCommand(cmds.colorManagementConvert, args, kwargs)


def colorManagementFileRules(*args, **kwargs):  # noqa
    """This non-undoable action manages the list of rules that Maya uses to assign an initial
    input color space to dependency graph nodes that read in color information from a
    file.

    colorManagementFileRules([addRule=string], [colorSpace=string],
    [colorSpaceDescription=string], [colorSpaceFamilies=string],
    [colorSpaceNames=boolean], [down=string], [enabled=boolean], [evaluate=string],
    [extension=string], [listRules=boolean], [load=boolean], [moveUp=string],
    [pattern=string], [remove=string], [restoreDefaults=boolean], [save=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorManagementFileRules.html
    """
    return _wrapCommand(cmds.colorManagementFileRules, args, kwargs)


def colorManagementPrefs(*args, **kwargs):  # noqa
    """This command allows querying and editing the color management global data in a scene.

    colorManagementPrefs([cmConfigFileEnabled=boolean], [cmEnabled=boolean],
    [colorManageAllNodes=boolean], [colorManagePots=boolean], [colorManagedNodes=boolean],
    [colorManagementSDKVersion=string], [configFilePath=string],
    [configFileVersion=string], [defaultInputSpaceName=string], [displayName=string],
    [displayNames=boolean], [equalsToPolicyFile=string], [exportPolicy=string],
    [inhibitEvents=boolean], [inputSpaceDescription=string], [inputSpaceFamilies=string],
    [inputSpaceNames=boolean], [loadPolicy=string], [loadedDefaultInputSpaceName=string],
    [loadedDisplayName=string], [loadedOutputTransformName=string],
    [loadedRenderingSpaceName=string], [loadedViewName=string],
    [loadedViewTransformName=string], [missingColorSpaceNodes=boolean],
    [ocioRulesEnabled=boolean], [ociov2Enabled=boolean], [outputTarget=string],
    [outputTransformEnabled=boolean], [outputTransformName=string],
    [outputTransformNames=boolean], [outputTransformUseColorConversion=boolean],
    [outputUseViewTransform=boolean], [policyFileName=string], [popupOnError=boolean],
    [refresh=boolean], [renderingSpaceName=string], [renderingSpaceNames=boolean],
    [restoreDefaults=boolean], [viewDisplayNames=string], [viewName=string],
    [viewNames=boolean], [viewTransformName=string], [viewTransformNames=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorManagementPrefs.html
    """
    return _wrapCommand(cmds.colorManagementPrefs, args, kwargs)


def colorSliderButtonGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    colorSliderButtonGrp( [string] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [alphaValue=float], [annotation=string],
    [backgroundColor=[float, float, float]], [buttonCommand=script], [buttonLabel=string],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [forceDragRefresh=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [hsvValue=[float, float, float]],
    [image=string], [isObscured=boolean], [label=string], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [rgbValue=[float, float, float]],
    [rowAttach=[int, string, int]], [statusBarMessage=string],
    [symbolButtonCommand=script], [symbolButtonDisplay=boolean],
    [useDisplaySpace=boolean], [useTemplate=string], [useVpColorPicker=boolean],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorSliderButtonGrp.html
    """
    return _wrapCommand(cmds.colorSliderButtonGrp, args, kwargs)


def colorSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    colorSliderGrp( name , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [alphaValue=float], [annotation=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dragCommand=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [forceDragRefresh=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [hsvValue=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rgbValue=[float, float, float]], [rowAttach=[int, string,
    int]], [statusBarMessage=string], [useDisplaySpace=boolean], [useTemplate=string],
    [useVpColorPicker=boolean], [visible=boolean], [visibleChangeCommand=script],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/colorSliderGrp.html
    """
    return _wrapCommand(cmds.colorSliderGrp, args, kwargs)


def columnLayout(*args, **kwargs):  # noqa
    """This command creates a layout that arranges its children in a single column.

    columnLayout( [string] , [adjustableColumn=boolean], [annotation=string],
    [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=string],
    [columnAttach=[string, int]], [columnOffset=[string, int]], [columnWidth=int],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [rowSpacing=int], [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/columnLayout.html
    """
    return _wrapCommand(cmds.columnLayout, args, kwargs)


def combinationShape(*args, **kwargs):  # noqa
    """Command to create or edit drive relationship of blend shape targets.

    combinationShape([addDriver=boolean], [allDrivers=boolean], [blendShape=string],
    [combinationTargetIndex=int], [combinationTargetName=string], [combineMethod=int],
    [driverTargetIndex=int], [driverTargetName=string], [exist=boolean],
    [removeDriver=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/combinationShape.html
    """
    return _wrapCommand(cmds.combinationShape, args, kwargs)


def commandEcho(*args, **kwargs):  # noqa
    """This command controls what is echoed to the command window.

    commandEcho([addFilter=string[]], [filter=string[]], [lineNumbers=boolean],
    [state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/commandEcho.html
    """
    return _wrapCommand(cmds.commandEcho, args, kwargs)


def commandLine(*args, **kwargs):  # noqa
    """This command creates a single line for command input/output.

    commandLine( [name] , [annotation=string], [backgroundColor=[float, float, float]],
    [command=script], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [holdFocus=boolean], [inputAnnotation=string], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfHistoryLines=int], [numberOfPopupMenus=boolean],
    [outputAnnotation=string], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [sourceType=string], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/commandLine.html
    """
    return _wrapCommand(cmds.commandLine, args, kwargs)


def commandLogging(*args, **kwargs):  # noqa
    """This command controls logging of Maya commands, in memory and on disk.

    commandLogging([historySize=uint], [logCommands=boolean], [logFile=string],
    [recordCommands=boolean], [resetLogFile=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/commandLogging.html
    """
    return _wrapCommand(cmds.commandLogging, args, kwargs)


def commandPort(*args, **kwargs):  # noqa
    """Opens or closes the Maya command port.

    commandPort([bufferSize=int], [close=boolean], [echoOutput=boolean], [listPorts=boolean],
    [name=string], [noreturn=boolean], [pickleOutput=boolean], [prefix=string],
    [returnNumCommands=boolean], [securityWarning=boolean], [sourceType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/commandPort.html
    """
    return _wrapCommand(cmds.commandPort, args, kwargs)


def componentBox(*args, **kwargs):  # noqa
    """This command creates a component box, which is sensitive to the active list.

    componentBox( [name] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [execute=[string, boolean]], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [labelWidth=int], [manage=boolean], [maxHeight=int],
    [maxWidth=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowHeight=int],
    [selectedAttr=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/componentBox.html
    """
    return _wrapCommand(cmds.componentBox, args, kwargs)


def componentEditor(*args, **kwargs):  # noqa
    """This command creates a new component editor in the current layout.

    componentEditor( name , [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [floatField=string], [floatSlider=string],
    [forceMainConnection=string], [hidePathName=boolean], [hideZeroColumns=boolean],
    [highlightConnection=string], [justifyHeaders=int], [lockInput=boolean],
    [lockMainConnection=boolean], [mainListConnection=string], [newTab=[string, string,
    string]], [normalizeWeights=int], [operationCount=boolean], [operationLabels=boolean],
    [operationType=int], [panel=string], [parent=string], [precision=int],
    [removeTab=string], [selected=boolean], [selectionConnection=string],
    [setOperationLabel=[int, string]], [showNamespaces=boolean], [showObjects=boolean],
    [showSelected=boolean], [sortAlpha=boolean], [stateString=boolean],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/componentEditor.html
    """
    return _wrapCommand(cmds.componentEditor, args, kwargs)


def condition(*args, **kwargs):  # noqa
    """This command creates a new named condition object whose true/false value is calculated by
    running a mel script.

    condition( string , [delete=boolean], [dependency=string], [initialize=boolean],
    [script=string], [state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/condition.html
    """
    return _wrapCommand(cmds.condition, args, kwargs)


def cone(*args, **kwargs):  # noqa
    """The cone command creates a new cone and/or a dependency node that creates one, and returns
    their names.

    cone([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean],
    [degree=int], [endSweep=angle], [heightRatio=float], [name=string], [nodeState=int],
    [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear],
    [sections=int], [spans=int], [startSweep=angle], [tolerance=linear],
    [useOldInitBehaviour=boolean], [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cone.html
    """
    return _wrapCommand(cmds.cone, args, kwargs)


def confirmDialog(*args, **kwargs):  # noqa
    """The confirmDialog command creates a modal dialog with a message to the user and a variable
    number of buttons to dismiss the dialog.

    confirmDialog([annotation=string], [backgroundColor=[float, float, float]],
    [button=string], [cancelButton=string], [defaultButton=string],
    [dismissString=string], [icon=string], [message=string], [messageAlign=string],
    [parent=string], [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/confirmDialog.html
    """
    return _wrapCommand(cmds.confirmDialog, args, kwargs)


def connectAttr(*args, **kwargs):  # noqa
    """Connect the attributes of two dependency nodes and return the names of the two connected
    attributes.

    connectAttr( attribute attribute , [force=boolean], [lock=boolean],
    [nextAvailable=boolean], [referenceDest=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/connectAttr.html
    """
    return _wrapCommand(cmds.connectAttr, args, kwargs)


def connectControl(*args, **kwargs):  # noqa
    """This command attaches a UI widget, specified as the first argument, to one or more
    dependency node attributes.

    connectControl( string attribute... , [fileName=boolean], [index=uint],
    [preventContextualMenu=boolean], [preventOverride=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/connectControl.html
    """
    return _wrapCommand(cmds.connectControl, args, kwargs)


def connectDynamic(*args, **kwargs):  # noqa
    """Dynamic connection specifies that the force fields, emitters, or collisions of an object
    affect another dynamic object.

    connectDynamic( [objects] , [addScriptHandler=script], [collisions=string],
    [delete=boolean], [emitters=string], [fields=string], [removeScriptHandler=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/connectDynamic.html
    """
    return _wrapCommand(cmds.connectDynamic, args, kwargs)


def connectionInfo(*args, **kwargs):  # noqa
    """The `connectionInfo` command is used to get information about connection sources and
    destinations.

    connectionInfo( string , [destinationFromSource=boolean], [getExactDestination=boolean],
    [getExactSource=boolean], [getLockedAncestor=boolean], [isDestination=boolean],
    [isExactDestination=boolean], [isExactSource=boolean], [isLocked=boolean],
    [isSource=boolean], [sourceFromDestination=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/connectionInfo.html
    """
    return _wrapCommand(cmds.connectionInfo, args, kwargs)


def connectJoint(*args, **kwargs):  # noqa
    """This command will connect two skeletons based on the two selected joints.

    connectJoint( [objects] , [connectMode=boolean], [parentMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/connectJoint.html
    """
    return _wrapCommand(cmds.connectJoint, args, kwargs)


def constrain(*args, **kwargs):  # noqa
    """This command constrains rigid bodies to the world or other rigid bodies.

    constrain([barrier=boolean], [damping=float], [directionalHinge=boolean], [hinge=boolean],
    [interpenetrate=boolean], [nail=boolean], [name=string], [orientation=[float, float,
    float]], [pinConstraint=boolean], [position=[float, float, float]],
    [restLength=float], [spring=boolean], [stiffness=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/constrain.html
    """
    return _wrapCommand(cmds.constrain, args, kwargs)


def constructionHistory(*args, **kwargs):  # noqa
    """This command turns construction history on or off.

    constructionHistory([toggle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/constructionHistory.html
    """
    return _wrapCommand(cmds.constructionHistory, args, kwargs)


def container(*args, **kwargs):  # noqa
    """This command can be used to create and query container nodes.

    container( [string...] , [addNode=string[]], [asset=string[]], [assetMember=string],
    [bindAttr=[string, string]], [connectionList=boolean], [current=boolean],
    [fileName=string[]], [findContainer=string[]], [force=boolean],
    [includeHierarchyAbove=boolean], [includeHierarchyBelow=boolean],
    [includeNetwork=boolean], [includeNetworkDetails=string], [includeShaders=boolean],
    [includeShapes=boolean], [includeTransform=boolean], [isContainer=boolean],
    [name=string], [nodeList=boolean], [nodeNamePrefix=boolean],
    [parentContainer=boolean], [preview=boolean], [publishAndBind=[string, string]],
    [publishAsChild=[string, string]], [publishAsParent=[string, string]],
    [publishAsRoot=[string, boolean]], [publishAttr=string], [publishConnections=boolean],
    [publishName=string], [removeContainer=boolean], [removeNode=string[]], [type=string],
    [unbindAndUnpublish=string], [unbindAttr=[string, string]], [unbindChild=string],
    [unbindParent=string], [unpublishChild=string], [unpublishName=string],
    [unpublishParent=string], [unsortedOrder=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/container.html
    """
    return _wrapCommand(cmds.container, args, kwargs)


def containerBind(*args, **kwargs):  # noqa
    """This is an accessory command to the container command which is used for some automated
    binding operations on the container.

    containerBind([allNames=boolean], [bindingSet=string], [bindingSetConditions=boolean],
    [bindingSetList=boolean], [force=boolean], [preview=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/containerBind.html
    """
    return _wrapCommand(cmds.containerBind, args, kwargs)


def containerProxy(*args, **kwargs):  # noqa
    """Creates a new container with the same published interface, dynamic attributes and
    attribute values as the specified container but with fewer container members.

    containerProxy([fromTemplate=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/containerProxy.html
    """
    return _wrapCommand(cmds.containerProxy, args, kwargs)


def containerPublish(*args, **kwargs):  # noqa
    """This is an accessory command to the container command which is used for some advanced
    publishing operations on the container.

    containerPublish([bindNode=[string, string]], [bindTemplateStandins=boolean],
    [inConnections=boolean], [mergeShared=boolean], [outConnections=boolean],
    [publishNode=[string, string]], [unbindNode=string], [unpublishNode=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/containerPublish.html
    """
    return _wrapCommand(cmds.containerPublish, args, kwargs)


def containerTemplate(*args, **kwargs):  # noqa
    """A container template is a description of a container's published interface.

    containerTemplate([addBindingSet=string], [addNames=boolean], [addView=string],
    [allKeyable=boolean], [attribute=string], [attributeList=string], [baseName=string],
    [bindingSetList=string], [childAnchor=boolean], [delete=boolean], [exists=boolean],
    [expandCompounds=boolean], [fileName=string], [force=boolean], [fromContainer=string],
    [fromSelection=boolean], [layoutMode=int], [load=boolean], [matchFile=string],
    [matchName=string], [parentAnchor=boolean], [publishedNodeList=string],
    [removeBindingSet=string], [removeView=string], [rootTransform=boolean],
    [save=boolean], [searchPath=string], [silent=boolean], [templateList=string],
    [unload=boolean], [updateBindingSet=string], [useHierarchy=boolean],
    [viewList=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/containerTemplate.html
    """
    return _wrapCommand(cmds.containerTemplate, args, kwargs)


def containerView(*args, **kwargs):  # noqa
    """A container view defines the layout information for the published attributes of a
    particular container.

    containerView([itemInfo=string], [itemList=boolean], [viewDescription=boolean],
    [viewLabel=boolean], [viewList=boolean], [viewName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/containerView.html
    """
    return _wrapCommand(cmds.containerView, args, kwargs)


def contentBrowser(*args, **kwargs):  # noqa
    """This command is used to edit and query a Content Browser.

    contentBrowser( [string] , [addContentPath=string], [context=[string, [, string, ], [,
    string, ]]], [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [location=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string], [preview=boolean],
    [refreshTreeView=boolean], [removeContentPath=string], [saveCurrentContext=boolean],
    [selectionConnection=string], [stateString=boolean], [thumbnailView=boolean],
    [treeView=boolean], [unParent=boolean], [unlockMainConnection=boolean],
    [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/contentBrowser.html
    """
    return _wrapCommand(cmds.contentBrowser, args, kwargs)


def contextInfo(*args, **kwargs):  # noqa
    """This command allows you to get information on named contexts.

    contextInfo( [context name] , [c=boolean], [escapeContext=boolean], [exists=boolean],
    [image1=boolean], [image2=boolean], [image3=boolean], [title=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/contextInfo.html
    """
    return _wrapCommand(cmds.contextInfo, args, kwargs)


def control(*args, **kwargs):  # noqa
    """This command allows you to edit or query the properties of any control.

    control( string , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/control.html
    """
    return _wrapCommand(cmds.control, args, kwargs)


def controller(*args, **kwargs):  # noqa
    """Commands for managing animation sources.

    controller([allControllers=boolean], [children=boolean], [group=boolean], [index=int],
    [isController=string], [parent=boolean], [pickWalkDown=boolean],
    [pickWalkLeft=boolean], [pickWalkRight=boolean], [pickWalkUp=boolean],
    [unparent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/controller.html
    """
    return _wrapCommand(cmds.controller, args, kwargs)


def convertIffToPsd(*args, **kwargs):  # noqa
    """Converts iff file to PSD file of given size.

    convertIffToPsd([iffFileName=string], [psdFileName=string], [xResolution=int],
    [yResolution=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/convertIffToPsd.html
    """
    return _wrapCommand(cmds.convertIffToPsd, args, kwargs)


def convertSolidTx(*args, **kwargs):  # noqa
    """Command to convert a texture on a surface to a file texture.

    convertSolidTx( [node|attribute] [object...] , [alpha=boolean], [antiAlias=boolean],
    [backgroundColor=[int, int, int]], [backgroundMode=string], [camera=name],
    [componentRange=boolean], [doubleSided=boolean], [fileFormat=string],
    [fileImageName=string], [fillTextureSeams=boolean], [force=boolean],
    [fullUvRange=boolean], [name=string], [pixelFormat=string], [resolutionX=int],
    [resolutionY=int], [reuseDepthMap=boolean], [samplePlane=boolean],
    [samplePlaneRange=[float, float, float, float]], [shadows=boolean],
    [uvBBoxIntersect=boolean], [uvRange=[float, float, float, float]], [uvSetName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/convertSolidTx.html
    """
    return _wrapCommand(cmds.convertSolidTx, args, kwargs)


def convertTessellation(*args, **kwargs):  # noqa
    """Command to translate the basic tessellation attributes to advanced.

    convertTessellation([allCameras=boolean], [camera=name])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/convertTessellation.html
    """
    return _wrapCommand(cmds.convertTessellation, args, kwargs)


def convertUnit(*args, **kwargs):  # noqa
    """This command converts values between different units of measure.

    convertUnit( string , [fromUnit=string], [toUnit=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/convertUnit.html
    """
    return _wrapCommand(cmds.convertUnit, args, kwargs)


def copyAttr(*args, **kwargs):  # noqa
    """Given two nodes, transfer the connections and/or the values from the first node to the
    second for all attributes whose names and data types match.

    copyAttr([attribute=string], [containerParentChild=boolean], [inConnections=boolean],
    [keepSourceConnections=boolean], [outConnections=boolean],
    [renameTargetContainer=boolean], [values=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/copyAttr.html
    """
    return _wrapCommand(cmds.copyAttr, args, kwargs)


def copyDeformerWeights(*args, **kwargs):  # noqa
    """Command to copy or mirror the deformer weights accross one of the three major axes.

    copyDeformerWeights([destinationDeformer=string], [destinationShape=string],
    [mirrorInverse=boolean], [mirrorMode=string], [noMirror=boolean], [smooth=boolean],
    [sourceDeformer=string], [sourceShape=string], [surfaceAssociation=string],
    [uvSpace=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/copyDeformerWeights.html
    """
    return _wrapCommand(cmds.copyDeformerWeights, args, kwargs)


def copyFlexor(*args, **kwargs):  # noqa
    """This command copies an existing bone or joint flexor from one bone (joint) to another.

    copyFlexor( [objects] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/copyFlexor.html
    """
    return _wrapCommand(cmds.copyFlexor, args, kwargs)


def copyKey(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    copyKey( [objects] , [animLayer=string], [animation=string], [attribute=string],
    [clipboard=string], [controlPoints=boolean], [float=floatrange],
    [forceIndependentEulerAngles=boolean], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [option=string], [shape=boolean],
    [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/copyKey.html
    """
    return _wrapCommand(cmds.copyKey, args, kwargs)


def copySkinWeights(*args, **kwargs):  # noqa
    """Command to copy or mirror the skinCluster weights accross one of the three major axes.

    copySkinWeights([destinationSkin=string], [influenceAssociation=string],
    [mirrorInverse=boolean], [mirrorMode=string], [noBlendWeight=boolean],
    [noMirror=boolean], [normalize=boolean], [sampleSpace=uint], [smooth=boolean],
    [sourceSkin=string], [surfaceAssociation=string], [uvSpace=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/copySkinWeights.html
    """
    return _wrapCommand(cmds.copySkinWeights, args, kwargs)


def crashInfo(*args, **kwargs):  # noqa
    """Provides an interface to the crash file information.

    crashInfo([crashFile=boolean], [crashLog=boolean], [savedBeforeCrash=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/crashInfo.html
    """
    return _wrapCommand(cmds.crashInfo, args, kwargs)


def createAttrPatterns(*args, **kwargs):  # noqa
    """Create a new instance of an attribute pattern given a pattern type (e.

    createAttrPatterns([patternDefinition=string], [patternFile=string], [patternType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createAttrPatterns.html
    """
    return _wrapCommand(cmds.createAttrPatterns, args, kwargs)


def createDisplayLayer(*args, **kwargs):  # noqa
    """Create a new display layer.

    createDisplayLayer([empty=boolean], [makeCurrent=boolean], [name=string],
    [noRecurse=boolean], [number=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createDisplayLayer.html
    """
    return _wrapCommand(cmds.createDisplayLayer, args, kwargs)


def createEditor(*args, **kwargs):  # noqa
    """This command creates a property sheet for any dependency node.

    createEditor( string node , [noCloseOnDelete=boolean], [queueForDelete=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createEditor.html
    """
    return _wrapCommand(cmds.createEditor, args, kwargs)


def createLayeredPsdFile(*args, **kwargs):  # noqa
    """Creates a layered PSD file with image names as input to individual layers.

    createLayeredPsdFile([imageFileName=[string, string, string]], [psdFileName=string],
    [xResolution=uint], [yResolution=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createLayeredPsdFile.html
    """
    return _wrapCommand(cmds.createLayeredPsdFile, args, kwargs)


def createNode(*args, **kwargs):  # noqa
    """This command creates a new node in the dependency graph of the specified type.

    createNode( string , [name=string], [parent=string], [shared=boolean],
    [skipSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createNode.html
    """
    return _wrapCommand(cmds.createNode, args, kwargs)


def createRenderLayer(*args, **kwargs):  # noqa
    """Create a new render layer.

    createRenderLayer([empty=boolean], [g=boolean], [makeCurrent=boolean], [name=string],
    [noRecurse=boolean], [number=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createRenderLayer.html
    """
    return _wrapCommand(cmds.createRenderLayer, args, kwargs)


def createSubdivRegion(*args, **kwargs):  # noqa
    """Creates a subdivision surface region based on the selection list.

    createSubdivRegion()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/createSubdivRegion.html
    """
    return _wrapCommand(cmds.createSubdivRegion, args, kwargs)


def ctxAbort(*args, **kwargs):  # noqa
    """This command tells the current context to reset itself, losing what has been done so far.

    ctxAbort()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ctxAbort.html
    """
    return _wrapCommand(cmds.ctxAbort, args, kwargs)


def ctxCompletion(*args, **kwargs):  # noqa
    """This command tells the current context to finish what it is doing and create any objects
    that is is working on.

    ctxCompletion()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ctxCompletion.html
    """
    return _wrapCommand(cmds.ctxCompletion, args, kwargs)


def ctxEditMode(*args, **kwargs):  # noqa
    """This command tells the current context to switch edit modes.

    ctxEditMode([buttonDown=boolean], [buttonUp=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ctxEditMode.html
    """
    return _wrapCommand(cmds.ctxEditMode, args, kwargs)


def ctxTraverse(*args, **kwargs):  # noqa
    """This command tells the current context to do a traversal.

    ctxTraverse([down=boolean], [left=boolean], [right=boolean], [up=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ctxTraverse.html
    """
    return _wrapCommand(cmds.ctxTraverse, args, kwargs)


def currentCtx(*args, **kwargs):  # noqa
    """This command returns the currently selected tool context.

    currentCtx()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/currentCtx.html
    """
    return _wrapCommand(cmds.currentCtx, args, kwargs)


def currentTime(*args, **kwargs):  # noqa
    """When given a time argument (with or without the -edit flag) this command sets the current
    global time.

    currentTime( [time] , [update=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/currentTime.html
    """
    return _wrapCommand(cmds.currentTime, args, kwargs)


def currentTimeCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to change current time within the graph
    editor.

    currentTimeCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/currentTimeCtx.html
    """
    return _wrapCommand(cmds.currentTimeCtx, args, kwargs)


def currentUnit(*args, **kwargs):  # noqa
    """This command allows you to change the units in which you will work in Maya.

    currentUnit([angle=string], [fullName=boolean], [linear=string], [time=string],
    [updateAnimation=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/currentUnit.html
    """
    return _wrapCommand(cmds.currentUnit, args, kwargs)


def curve(*args, **kwargs):  # noqa
    """The curve command creates a new curve from a list of control vertices (CVs).

    curve( string , [append=boolean], [bezier=boolean], [degree=float], [editPoint=[linear,
    linear, linear]], [knot=float], [name=string], [objectSpace=boolean],
    [periodic=boolean], [point=[linear, linear, linear]], [pointWeight=[linear, linear,
    linear, float]], [replace=boolean], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curve.html
    """
    return _wrapCommand(cmds.curve, args, kwargs)


def curveAddPtCtx(*args, **kwargs):  # noqa
    """The curveAddPtCtx command creates a new curve add points context, which adds either
    control vertices (CVs) or edit points to an existing curve.

    curveAddPtCtx([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveAddPtCtx.html
    """
    return _wrapCommand(cmds.curveAddPtCtx, args, kwargs)


def curveCVCtx(*args, **kwargs):  # noqa
    """The curveCVCtx command creates a new context for creating curves by placing control
    vertices (CVs).

    curveCVCtx([bezier=boolean], [degree=uint], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [multEndKnots=boolean],
    [name=string], [preserveShape=boolean], [rational=boolean], [refit=boolean],
    [symmetry=boolean], [uniform=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveCVCtx.html
    """
    return _wrapCommand(cmds.curveCVCtx, args, kwargs)


def curveEditorCtx(*args, **kwargs):  # noqa
    """The curveEditorCtx command creates a new NURBS editor context, which is used to edit a
    NURBS curve or surface.

    curveEditorCtx([direction=int], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [relativeTangentSize=float],
    [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveEditorCtx.html
    """
    return _wrapCommand(cmds.curveEditorCtx, args, kwargs)


def curveEPCtx(*args, **kwargs):  # noqa
    """The curveEPCtx command creates a new context for creating curves by placing edit points.

    curveEPCtx([bezier=boolean], [degree=uint], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string],
    [preserveShape=boolean], [preserveShapeFraction=float], [refit=boolean],
    [uniform=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveEPCtx.html
    """
    return _wrapCommand(cmds.curveEPCtx, args, kwargs)


def curveIntersect(*args, **kwargs):  # noqa
    """You must specify two curves to intersect.

    curveIntersect( string string , [caching=boolean], [constructionHistory=boolean],
    [direction=[linear, linear, linear]], [directionX=linear], [directionY=linear],
    [directionZ=linear], [nodeState=int], [tolerance=linear], [useDirection=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveIntersect.html
    """
    return _wrapCommand(cmds.curveIntersect, args, kwargs)


def curveMoveEPCtx(*args, **kwargs):  # noqa
    """The curveMoveEPCtx command creates a new context for moving curve edit points using a
    manipulator.

    curveMoveEPCtx([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveMoveEPCtx.html
    """
    return _wrapCommand(cmds.curveMoveEPCtx, args, kwargs)


def curveOnSurface(*args, **kwargs):  # noqa
    """The curve command creates a new curve from a list of control vertices (CVs).

    curveOnSurface( string string , [append=boolean], [degree=float], [knot=float],
    [name=string], [periodic=boolean], [positionUV=[float, float]], [replace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveOnSurface.html
    """
    return _wrapCommand(cmds.curveOnSurface, args, kwargs)


def curveRGBColor(*args, **kwargs):  # noqa
    """This command creates, changes or removes custom curve colors, which are used to draw the
    curves in the Graph Editor.

    curveRGBColor([hueSaturationValue=boolean], [list=boolean], [listNames=boolean],
    [remove=boolean], [resetToFactory=boolean], [resetToSaved=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveRGBColor.html
    """
    return _wrapCommand(cmds.curveRGBColor, args, kwargs)


def curveSketchCtx(*args, **kwargs):  # noqa
    """The curveSketchCtx command creates a new curve sketch context, also known as the "pencil
    context".

    curveSketchCtx( [object] , [degree=uint], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/curveSketchCtx.html
    """
    return _wrapCommand(cmds.curveSketchCtx, args, kwargs)


def cutKey(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    cutKey( [targetList] , [animation=string], [attribute=string], [clear=boolean],
    [controlPoints=boolean], [float=floatrange], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [option=string], [selectKey=boolean],
    [shape=boolean], [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cutKey.html
    """
    return _wrapCommand(cmds.cutKey, args, kwargs)


def cycleCheck(*args, **kwargs):  # noqa
    """This command searches for plug cycles in the dependency graph.

    cycleCheck( string[] , [all=boolean], [children=boolean], [dag=boolean],
    [evaluation=boolean], [firstCycleOnly=boolean], [firstPlugPerNode=boolean],
    [lastPlugPerNode=boolean], [list=boolean], [listSeparator=string], [parents=boolean],
    [secondary=boolean], [timeLimit=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cycleCheck.html
    """
    return _wrapCommand(cmds.cycleCheck, args, kwargs)


def cylinder(*args, **kwargs):  # noqa
    """The cylinder command creates a new cylinder and/or a dependency node that creates one, and
    returns their names.

    cylinder([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [degree=int], [endSweep=angle], [heightRatio=float],
    [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]],
    [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle],
    [tolerance=linear], [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/cylinder.html
    """
    return _wrapCommand(cmds.cylinder, args, kwargs)


def dagObjectCompare(*args, **kwargs):  # noqa
    """dagObjectCompare can be used to compare to compare objects based on:

    - type - Currently supports transform nodes and shape nodes
    - relatives - Compares DAG objects' children and parents
    - connections - Checks to make sure the two dags are connected to the same sources and
      destinations
    - attributes - Checks to make sure that the properties of active attributes are the
      same.

    dagObjectCompare([attribute=boolean], [bail=string], [connection=boolean],
    [namespace=string], [relative=boolean], [short=boolean], [type=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dagObjectCompare.html
    """
    return _wrapCommand(cmds.dagObjectCompare, args, kwargs)


def dagPose(*args, **kwargs):  # noqa
    """This command is used to save and restore the matrix information for a dag hierarchy.

    dagPose( [objects] , [addToPose=boolean], [atPose=boolean], [bindPose=boolean],
    [g=boolean], [members=boolean], [name=string], [remove=boolean], [reset=boolean],
    [restore=boolean], [save=boolean], [selection=boolean], [worldParent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dagPose.html
    """
    return _wrapCommand(cmds.dagPose, args, kwargs)


def dataStructure(*args, **kwargs):  # noqa
    """Takes in a description of the structure and creates it, adding it to the list of available
    data structures.

    dataStructure([asFile=string], [asString=string], [dataType=boolean], [format=string],
    [listMemberNames=string], [name=string], [remove=boolean], [removeAll=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dataStructure.html
    """
    return _wrapCommand(cmds.dataStructure, args, kwargs)


def date(*args, **kwargs):  # noqa
    """Returns information about current time and date.

    date([date=boolean], [format=string], [shortDate=boolean], [shortTime=boolean],
    [time=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/date.html
    """
    return _wrapCommand(cmds.date, args, kwargs)


def dbcount(*args, **kwargs):  # noqa
    """The `dbcount` command is used to print and manage a list of statistics collected for
    counting operations.

    dbcount([enabled=boolean], [file=string], [keyword=string], [list=boolean],
    [maxdepth=uint], [quick=boolean], [reset=boolean], [spreadsheet=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dbcount.html
    """
    return _wrapCommand(cmds.dbcount, args, kwargs)


def dbfootprint(*args, **kwargs):  # noqa
    """This command lets you explore the memory usage of specific parts of the scene.

    dbfootprint([allObjects=boolean], [outputFile=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dbfootprint.html
    """
    return _wrapCommand(cmds.dbfootprint, args, kwargs)


def dbmessage(*args, **kwargs):  # noqa
    """The `dbmessage` command is used to install monitors for certain message types, dumping
    debug information as they are sent so that the flow of messages can be examined.

    dbmessage([file=string], [list=boolean], [monitor=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dbmessage.html
    """
    return _wrapCommand(cmds.dbmessage, args, kwargs)


def dbpeek(*args, **kwargs):  # noqa
    """The `dbpeek` command is used to analyze the Maya data for information of interest.

    dbpeek([allObjects=boolean], [argument=string], [count=uint], [evaluationGraph=boolean],
    [operation=string], [outputFile=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dbpeek.html
    """
    return _wrapCommand(cmds.dbpeek, args, kwargs)


def dbtrace(*args, **kwargs):  # noqa
    """The `dbtrace` command is used to manipulate trace objects.

    dbtrace([filter=string], [info=boolean], [keyword=string], [mark=boolean], [off=boolean],
    [output=string], [timed=boolean], [title=string], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dbtrace.html
    """
    return _wrapCommand(cmds.dbtrace, args, kwargs)


def defaultLightListCheckBox(*args, **kwargs):  # noqa
    """This command creates a checkBox that controls whether a shadingGroup is
    connected/disconnected from the defaultLightList.

    defaultLightListCheckBox([annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [shadingGroup=name], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/defaultLightListCheckBox.html
    """
    return _wrapCommand(cmds.defaultLightListCheckBox, args, kwargs)


def defaultNavigation(*args, **kwargs):  # noqa
    """The defaultNavigation command defines default behaviours when creating or manipulating
    connections between nodes and when navigating between nodes via those connections.

    defaultNavigation([connectToExisting=boolean], [createNew=boolean],
    [defaultAttribute=boolean], [defaultTraversal=boolean], [defaultWorkingNode=boolean],
    [delete=boolean], [destination=name], [disconnect=boolean], [force=boolean],
    [ignore=boolean], [navigatorDecisionString=string], [quiet=boolean],
    [relatedNodes=boolean], [source=name], [unignore=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/defaultNavigation.html
    """
    return _wrapCommand(cmds.defaultNavigation, args, kwargs)


def defineDataServer(*args, **kwargs):  # noqa
    """Connects to the specified data servername, creating a named device which then can be
    attached to device handlers.

    defineDataServer([device=string], [server=string], [undefine=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/defineDataServer.html
    """
    return _wrapCommand(cmds.defineDataServer, args, kwargs)


def defineVirtualDevice(*args, **kwargs):  # noqa
    """This command defines a virtual device.

    defineVirtualDevice([axis=int], [channel=string], [clear=boolean], [create=boolean],
    [device=string], [parent=string], [undefine=boolean], [usage=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/defineVirtualDevice.html
    """
    return _wrapCommand(cmds.defineVirtualDevice, args, kwargs)


def deformableShape(*args, **kwargs):  # noqa
    """This command finds information about deforming shape(s).

    deformableShape( [objects...] , [chain=boolean], [createOriginalGeometry=boolean],
    [createTweakNode=boolean], [createUpstreamTagInjectionNode=boolean],
    [deformShapeInAttr=boolean], [deformShapeOutAttr=boolean], [frontOfChain=boolean],
    [localShapeInAttr=boolean], [localShapeOutAttr=boolean], [nodeChain=boolean],
    [originalGeometry=boolean], [outputPlugChain=boolean], [plugChain=boolean],
    [supportsComponentTags=boolean], [tagInjectionList=boolean],
    [tagInjectionNode=boolean], [tweakNode=boolean], [upstreamTagInjectionNode=boolean],
    [worldShapeOutAttr=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deformableShape.html
    """
    return _wrapCommand(cmds.deformableShape, args, kwargs)


def deformer(*args, **kwargs):  # noqa
    """This command creates a deformer of the specified type.

    deformer( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [deformerTools=boolean], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string],
    [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean],
    [split=boolean], [type=string], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deformer.html
    """
    return _wrapCommand(cmds.deformer, args, kwargs)


def deformerEvaluator(*args, **kwargs):  # noqa
    """Print debug information about deformer evaluator status.

    deformerEvaluator([active=boolean], [asNodeName=boolean], [asText=boolean],
    [chains=boolean], [deformerChain=boolean], [deformers=boolean], [dumpInfo=boolean],
    [limitMinimumVerts=boolean], [list=boolean], [members=boolean], [meshes=boolean],
    [message=boolean], [nodeInfo=boolean], [nodeStatus=boolean], [partition=boolean],
    [purge=boolean], [reuseMode=[string, string, string]], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deformerEvaluator.html
    """
    return _wrapCommand(cmds.deformerEvaluator, args, kwargs)


def deformerWeights(*args, **kwargs):  # noqa
    """Command to import and export deformer weights to and from a simple XML file.

    deformerWeights([attribute=string], [defaultValue=float], [deformer=string],
    [export=boolean], [format=string], [ignoreName=boolean], [im=boolean],
    [method=string], [path=string], [positionTolerance=float], [remap=string],
    [shape=string], [skip=string], [vertexConnections=boolean], [weightPrecision=uint],
    [weightTolerance=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deformerWeights.html
    """
    return _wrapCommand(cmds.deformerWeights, args, kwargs)


def delete(*args, **kwargs):  # noqa
    """This command is used to delete selected objects, or all objects, or objects specified
    along with the command.

    delete( objects , [all=boolean], [attribute=string], [channels=boolean],
    [constraints=boolean], [constructionHistory=boolean], [controlPoints=boolean],
    [expressions=boolean], [hierarchy=string], [inputConnectionsAndNodes=boolean],
    [motionPaths=boolean], [shape=boolean], [staticChannels=boolean],
    [timeAnimationCurves=boolean], [unitlessAnimationCurves=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/delete.html
    """
    return _wrapCommand(cmds.delete, args, kwargs)


def deleteAttr(*args, **kwargs):  # noqa
    """This command is used to delete a dynamic attribute from a node or nodes.

    deleteAttr( node...|attribute... , [attribute=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deleteAttr.html
    """
    return _wrapCommand(cmds.deleteAttr, args, kwargs)


def deleteAttrPattern(*args, **kwargs):  # noqa
    """After a while the list of attribute patterns could become cluttered.

    deleteAttrPattern([allPatterns=boolean], [patternName=string], [patternType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deleteAttrPattern.html
    """
    return _wrapCommand(cmds.deleteAttrPattern, args, kwargs)


def deleteExtension(*args, **kwargs):  # noqa
    """This command is used to delete an extension attribute from a node type.

    deleteExtension([attribute=string], [forceDelete=boolean], [nodeType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deleteExtension.html
    """
    return _wrapCommand(cmds.deleteExtension, args, kwargs)


def deleteUI(*args, **kwargs):  # noqa
    """This command deletes UI objects such as windows and controls.

    deleteUI( string [string...] , [collection=boolean], [control=boolean], [editor=boolean],
    [layout=boolean], [menu=boolean], [menuItem=boolean], [panel=boolean],
    [panelConfig=boolean], [radioMenuItemCollection=boolean], [toolContext=boolean],
    [uiTemplate=boolean], [window=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deleteUI.html
    """
    return _wrapCommand(cmds.deleteUI, args, kwargs)


def deltaMush(*args, **kwargs):  # noqa
    """This command is used to create, edit and query deltaMush nodes.

    deltaMush( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [deformerTools=boolean], [envelope=float], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [inwardConstraint=float],
    [name=string], [outwardConstraint=float], [parallel=boolean],
    [pinBorderVertices=boolean], [prune=boolean], [remove=boolean],
    [selectedComponents=boolean], [smoothingIterations=uint], [smoothingStep=float],
    [split=boolean], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deltaMush.html
    """
    return _wrapCommand(cmds.deltaMush, args, kwargs)


def detachCurve(*args, **kwargs):  # noqa
    """The detachCurve command detaches a curve into pieces, given a list of parameter values.

    detachCurve( curve , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [keep=boolean], [name=string], [nodeState=int],
    [object=boolean], [parameter=float], [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/detachCurve.html
    """
    return _wrapCommand(cmds.detachCurve, args, kwargs)


def detachDeviceAttr(*args, **kwargs):  # noqa
    """This command detaches connections between device axes and node attributes.

    detachDeviceAttr([all=boolean], [attribute=string], [axis=string], [device=string],
    [selection=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/detachDeviceAttr.html
    """
    return _wrapCommand(cmds.detachDeviceAttr, args, kwargs)


def detachSurface(*args, **kwargs):  # noqa
    """The detachSurface command detaches a surface into pieces, given a list of parameter values
    and a direction.

    detachSurface( surface , [caching=boolean], [constructionHistory=boolean],
    [direction=int], [keep=boolean], [name=string], [nodeState=int], [object=boolean],
    [parameter=float], [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/detachSurface.html
    """
    return _wrapCommand(cmds.detachSurface, args, kwargs)


def deviceEditor(*args, **kwargs):  # noqa
    """This creates an editor for creating/modifying attachments to input devices.

    deviceEditor([control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string],
    [selectionConnection=string], [stateString=boolean], [takePath=string],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deviceEditor.html
    """
    return _wrapCommand(cmds.deviceEditor, args, kwargs)


def deviceManager(*args, **kwargs):  # noqa
    """This command queriers the internal device manager for information on attached devices.

    deviceManager([attachment=boolean], [axisCoordChanges=boolean], [axisIndex=int],
    [axisName=boolean], [axisOffset=boolean], [axisScale=boolean], [deviceIndex=int],
    [deviceNameFromIndex=int], [numAxis=boolean], [numDevices=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/deviceManager.html
    """
    return _wrapCommand(cmds.deviceManager, args, kwargs)


def devicePanel(*args, **kwargs):  # noqa
    """This command is now obsolete.

    devicePanel([control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean],
    [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/devicePanel.html
    """
    return _wrapCommand(cmds.devicePanel, args, kwargs)


def dgdirty(*args, **kwargs):  # noqa
    """The `dgdirty` command is used to force a dependency graph dirty message on a node or plug.

    dgdirty([allPlugs=boolean], [clean=boolean], [implicit=boolean], [list=string],
    [propagation=boolean], [showTiming=boolean], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgdirty.html
    """
    return _wrapCommand(cmds.dgdirty, args, kwargs)


def dgeval(*args, **kwargs):  # noqa
    """The `dgeval` command is used to force a dependency graph evaluate of a node or plug.

    dgeval( [objects] , [src=boolean], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgeval.html
    """
    return _wrapCommand(cmds.dgeval, args, kwargs)


def dgfilter(*args, **kwargs):  # noqa
    """The `dgfilter` command is used to define Dependency Graph filters that select DG objects
    based on certain criteria.

    dgfilter([attribute=string], [list=boolean], [logicalAnd=[string, string]],
    [logicalNot=string], [logicalOr=[string, string]], [name=string], [node=string],
    [nodeType=string], [plug=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgfilter.html
    """
    return _wrapCommand(cmds.dgfilter, args, kwargs)


def dgInfo(*args, **kwargs):  # noqa
    """This command prints information about the DG in plain text.

    dgInfo([allNodes=boolean], [connections=boolean], [dirty=boolean], [nodes=boolean],
    [nonDeletable=boolean], [outputFile=string], [propagation=boolean], [short=boolean],
    [size=boolean], [subgraph=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgInfo.html
    """
    return _wrapCommand(cmds.dgInfo, args, kwargs)


def dgmodified(*args, **kwargs):  # noqa
    """The `dgmodified` command is used to find out which nodes in the dependency graph have been
    modified.

    dgmodified()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgmodified.html
    """
    return _wrapCommand(cmds.dgmodified, args, kwargs)


def dgtimer(*args, **kwargs):  # noqa
    """This command measures dependency graph node performance by managing timers on a per-node
    basis.

    dgtimer([combineType=boolean], [hide=string], [hierarchy=boolean], [maxDisplay=int],
    [name=string], [noHeader=boolean], [outputFile=string], [overhead=boolean],
    [rangeLower=float], [rangeUpper=float], [reset=boolean], [returnCode=string],
    [returnType=string], [show=string], [sortMetric=string], [sortType=string],
    [threshold=float], [timerOff=boolean], [timerOn=boolean], [trace=boolean],
    [type=string], [uniqueName=boolean], [updateHeatMap=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgtimer.html
    """
    return _wrapCommand(cmds.dgtimer, args, kwargs)


def dgValidateCurve(*args, **kwargs):  # noqa
    """The `dgValidateCurve` command is used to make sure the curve internal status matches their
    actual state.

    dgValidateCurve([allCurves=boolean], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dgValidateCurve.html
    """
    return _wrapCommand(cmds.dgValidateCurve, args, kwargs)


def dimWhen(*args, **kwargs):  # noqa
    """This method attaches the named UI object (first argument) to the named condition (second
    argument) so that the object will be dimmed when the condition is in a particular
    state.

    dimWhen( string string , [clear=boolean], [false=boolean], [true=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dimWhen.html
    """
    return _wrapCommand(cmds.dimWhen, args, kwargs)


def directionalLight(*args, **kwargs):  # noqa
    """TlightCmd is the base class for other light commands.

    directionalLight([decayRate=int], [discRadius=linear], [exclusive=boolean],
    [intensity=float], [name=string], [position=[linear, linear, linear]], [rgb=[float,
    float, float]], [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]],
    [shadowDither=float], [shadowSamples=int], [softShadow=boolean],
    [useRayTraceShadows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/directionalLight.html
    """
    return _wrapCommand(cmds.directionalLight, args, kwargs)


def directKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to directly manipulate keyframes within
    the graph editor.

    directKeyCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [option=string],
    [selectedOnly=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/directKeyCtx.html
    """
    return _wrapCommand(cmds.directKeyCtx, args, kwargs)


def dirmap(*args, **kwargs):  # noqa
    """Use this command to map a directory to another directory.

    dirmap( string string , [convertDirectory=string], [enable=boolean],
    [getAllMappings=boolean], [getMappedDirectory=string], [mapDirectory=[string,
    string]], [unmapDirectory=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dirmap.html
    """
    return _wrapCommand(cmds.dirmap, args, kwargs)


def disable(*args, **kwargs):  # noqa
    """This command enables or disables the control passed as argument.

    disable( [string] , [value=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/disable.html
    """
    return _wrapCommand(cmds.disable, args, kwargs)


def disableIncorrectNameWarning(*args, **kwargs):  # noqa
    """Disable the warning dialog which complains about incorrect node names when opening Maya
    files.

    disableIncorrectNameWarning()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/disableIncorrectNameWarning.html
    """
    return _wrapCommand(cmds.disableIncorrectNameWarning, args, kwargs)


def disconnectAttr(*args, **kwargs):  # noqa
    """Disconnects two connected attributes.

    disconnectAttr( attribute attribute , [nextAvailable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/disconnectAttr.html
    """
    return _wrapCommand(cmds.disconnectAttr, args, kwargs)


def disconnectJoint(*args, **kwargs):  # noqa
    """This command will break a skeleton at the selected joint and delete any associated
    handles.

    disconnectJoint([attachHandleMode=boolean], [deleteHandleMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/disconnectJoint.html
    """
    return _wrapCommand(cmds.disconnectJoint, args, kwargs)


def diskCache(*args, **kwargs):  # noqa
    """Command to create, clear, or close disk cache(s).

    diskCache([append=boolean], [cacheType=string], [close=string], [closeAll=boolean],
    [delete=string], [deleteAll=boolean], [empty=string], [emptyAll=boolean],
    [enabledCachesOnly=boolean], [endTime=time], [frameRangeType=string],
    [overSample=boolean], [samplingRate=int], [startTime=time], [tempDir=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/diskCache.html
    """
    return _wrapCommand(cmds.diskCache, args, kwargs)


def displacementToPoly(*args, **kwargs):  # noqa
    """Command bakes geometry with displacement mapping into a polygonal object.

    displacementToPoly([findBboxOnly=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displacementToPoly.html
    """
    return _wrapCommand(cmds.displacementToPoly, args, kwargs)


def displayAffected(*args, **kwargs):  # noqa
    """Turns on/off the special coloring of objects that are affected by the objects that are
    currently in the selection list.

    displayAffected()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayAffected.html
    """
    return _wrapCommand(cmds.displayAffected, args, kwargs)


def displayColor(*args, **kwargs):  # noqa
    """This command changes or queries the display color for anything in the application that
    allows the user to set its color.

    displayColor( string , [active=boolean], [create=boolean], [dormant=boolean],
    [list=boolean], [queryIndex=int], [resetToFactory=boolean], [resetToSaved=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayColor.html
    """
    return _wrapCommand(cmds.displayColor, args, kwargs)


def displayCull(*args, **kwargs):  # noqa
    """This command is responsible for setting the display culling property of back faces of
    surfaces.

    displayCull( [objects] , [backFaceCulling=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayCull.html
    """
    return _wrapCommand(cmds.displayCull, args, kwargs)


def displayLevelOfDetail(*args, **kwargs):  # noqa
    """This command is responsible for setting the display level-of-detail for edit refreshes.

    displayLevelOfDetail([levelOfDetail=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayLevelOfDetail.html
    """
    return _wrapCommand(cmds.displayLevelOfDetail, args, kwargs)


def displayPref(*args, **kwargs):  # noqa
    """This command sets/queries the state of global display parameters.

    displayPref([activeObjectPivots=boolean], [displayAffected=boolean],
    [displayGradient=boolean], [ghostFrames=[int, int, int]],
    [materialLoadingMode=string], [maxHardwareTextureResolution=boolean],
    [maxTextureResolution=int], [purgeExistingTextures=boolean], [regionOfEffect=boolean],
    [shadeTemplates=boolean], [textureDrawPixel=boolean],
    [wireframeOnShadedActive=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayPref.html
    """
    return _wrapCommand(cmds.displayPref, args, kwargs)


def displayRGBColor(*args, **kwargs):  # noqa
    """This command changes or queries the display color for anything in the application that
    allows the user to set its color.

    displayRGBColor( string , [alpha=boolean], [create=boolean], [hueSaturationValue=boolean],
    [list=boolean], [resetToFactory=boolean], [resetToSaved=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayRGBColor.html
    """
    return _wrapCommand(cmds.displayRGBColor, args, kwargs)


def displaySmoothness(*args, **kwargs):  # noqa
    """This command is responsible for setting the display smoothness of NURBS curves and
    surfaces to either predefined or custom values.

    displaySmoothness( [objects] , [all=boolean], [boundary=boolean],
    [defaultCreation=boolean], [divisionsU=int], [divisionsV=int], [full=boolean],
    [hull=boolean], [pointsShaded=int], [pointsWire=int], [polygonObject=int],
    [renderTessellation=boolean], [simplifyU=int], [simplifyV=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displaySmoothness.html
    """
    return _wrapCommand(cmds.displaySmoothness, args, kwargs)


def displayString(*args, **kwargs):  # noqa
    """Assign a string value to a string identifier.

    displayString([string][string][string][string], [delete=boolean], [exists=boolean],
    [keys=boolean], [replace=boolean], [value=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displayString.html
    """
    return _wrapCommand(cmds.displayString, args, kwargs)


def displaySurface(*args, **kwargs):  # noqa
    """This command toggles display options on the specified or active surfaces.

    displaySurface( [objects...] , [flipNormals=boolean], [twoSidedLighting=boolean],
    [xRay=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/displaySurface.html
    """
    return _wrapCommand(cmds.displaySurface, args, kwargs)


def distanceDimContext(*args, **kwargs):  # noqa
    """Command used to register the distanceDimCtx tool.

    distanceDimContext([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/distanceDimContext.html
    """
    return _wrapCommand(cmds.distanceDimContext, args, kwargs)


def distanceDimension(*args, **kwargs):  # noqa
    """This command is used to create a distance dimension to display the distance between two
    specified points.

    distanceDimension([endPoint=[linear, linear, linear]], [startPoint=[linear, linear,
    linear]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/distanceDimension.html
    """
    return _wrapCommand(cmds.distanceDimension, args, kwargs)


def doBlur(*args, **kwargs):  # noqa
    """The doBlur command will invoke the blur2d, which is a Maya stand-alone application to do
    2.

    doBlur([colorFile=string], [length=float], [memCapSize=float], [sharpness=float],
    [smooth=float], [smoothColor=boolean], [vectorFile=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/doBlur.html
    """
    return _wrapCommand(cmds.doBlur, args, kwargs)


def dockControl(*args, **kwargs):  # noqa
    """Create a dockable control, also known as tool palette or utility window.

    dockControl( [name] , [allowedArea=string], [annotation=string], [area=string],
    [backgroundColor=[float, float, float]], [closeCommand=script], [content=string],
    [defineTemplate=string], [docTag=string], [dockStation=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enablePopupOption=boolean], [exists=boolean],
    [fixedHeight=boolean], [fixedWidth=boolean], [floatChangeCommand=script],
    [floating=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float,
    float, float]], [isObscured=boolean], [label=string], [manage=boolean],
    [moveable=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean], [r=boolean],
    [retain=boolean], [sizeable=boolean], [splitLayout=string], [state=string],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dockControl.html
    """
    return _wrapCommand(cmds.dockControl, args, kwargs)


def dolly(*args, **kwargs):  # noqa
    """The dolly command moves a camera along the viewing direction in the world space.

    dolly( [camera] , [absolute=boolean], [distance=linear], [dollyTowardsCenter=boolean],
    [orthoScale=float], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dolly.html
    """
    return _wrapCommand(cmds.dolly, args, kwargs)


def dollyCtx(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a dolly context.

    dollyCtx( object , [alternateContext=boolean], [boxDollyType=string],
    [centerOfInterestDolly=boolean], [dollyTowardsCenter=boolean], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [localDolly=boolean], [name=string], [orthoZoom=boolean], [scale=float],
    [toolName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dollyCtx.html
    """
    return _wrapCommand(cmds.dollyCtx, args, kwargs)


def dopeSheetEditor(*args, **kwargs):  # noqa
    """Edit a characteristic of a dope sheet editor.

    dopeSheetEditor( editorName , [autoFit=string], [autoFitTime=string], [control=boolean],
    [defineTemplate=string], [displayActiveKeyTangents=string],
    [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string],
    [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean],
    [filter=string], [forceMainConnection=string], [hierarchyBelow=boolean],
    [highlightConnection=string], [lockMainConnection=boolean], [lookAt=string],
    [mainListConnection=string], [outliner=string], [panel=string], [parent=string],
    [selectionConnection=string], [selectionWindow=[float, float, float, float]],
    [showScene=boolean], [showSummary=boolean], [showTicks=boolean], [snapTime=string],
    [snapValue=string], [stateString=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dopeSheetEditor.html
    """
    return _wrapCommand(cmds.dopeSheetEditor, args, kwargs)


def doubleProfileBirailSurface(*args, **kwargs):  # noqa
    """The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".

    doubleProfileBirailSurface( curve curve curve curve , [blendFactor=float],
    [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int],
    [object=boolean], [polygon=int], [tangentContinuityProfile1=boolean],
    [tangentContinuityProfile2=boolean], [transformMode=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/doubleProfileBirailSurface.html
    """
    return _wrapCommand(cmds.doubleProfileBirailSurface, args, kwargs)


def drag(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    drag( [objects] , [attenuation=float], [directionX=float], [directionY=float],
    [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string],
    [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [useDirection=boolean], [volumeExclusion=boolean], [volumeOffset=[linear, linear,
    linear]], [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/drag.html
    """
    return _wrapCommand(cmds.drag, args, kwargs)


def dragAttrContext(*args, **kwargs):  # noqa
    """The dragAttrContext allows a user to manipulate the attributes of an object by using a
    virtual slider within the viewport.

    dragAttrContext( [name] , [connectTo=name], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [reset=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dragAttrContext.html
    """
    return _wrapCommand(cmds.dragAttrContext, args, kwargs)


def draggerContext(*args, **kwargs):  # noqa
    """The draggerContext allows the user to program the behavior of the mouse or an equivalent
    dragging device in MEL.

    draggerContext( [name] , [anchorPoint=[float, float, float]], [button=int],
    [currentStep=int], [cursor=string], [dragCommand=script], [dragPoint=[float, float,
    float]], [drawString=string], [exists=boolean], [finalize=script],
    [helpString=string], [history=boolean], [holdCommand=script], [image1=string],
    [image2=string], [image3=string], [initialize=script], [modifier=string],
    [name=string], [plane=[float, float, float]], [prePressCommand=script],
    [pressCommand=script], [projection=string], [releaseCommand=script],
    [snapping=boolean], [space=string], [stepsCount=int], [undoMode=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/draggerContext.html
    """
    return _wrapCommand(cmds.draggerContext, args, kwargs)


def dropoffLocator(*args, **kwargs):  # noqa
    """This command adds one or more dropoff locators to a wire curve, one for each selected
    curve point.

    dropoffLocator( float float string selectionList )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dropoffLocator.html
    """
    return _wrapCommand(cmds.dropoffLocator, args, kwargs)


def duplicate(*args, **kwargs):  # noqa
    """This command duplicates the given objects.

    duplicate( [objects...] , [fullPath=boolean], [inputConnections=boolean],
    [instanceLeaf=boolean], [name=string], [parentOnly=boolean], [renameChildren=boolean],
    [returnRootsOnly=boolean], [smartTransform=boolean], [transformsOnly=boolean],
    [upstreamNodes=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/duplicate.html
    """
    return _wrapCommand(cmds.duplicate, args, kwargs)


def duplicateCurve(*args, **kwargs):  # noqa
    """The duplicateCurve command takes a curve on a surface and and returns the 3D curve.

    duplicateCurve([caching=boolean], [constructionHistory=boolean], [local=boolean],
    [maxValue=float], [mergeItems=boolean], [minValue=float], [name=string],
    [nodeState=int], [range=boolean], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/duplicateCurve.html
    """
    return _wrapCommand(cmds.duplicateCurve, args, kwargs)


def duplicateSurface(*args, **kwargs):  # noqa
    """The duplicateSurface command takes a surface patch (face) and and returns the 3D surface.

    duplicateSurface([caching=boolean], [constructionHistory=boolean], [faceCountU=int],
    [faceCountV=int], [firstFaceU=int], [firstFaceV=int], [local=boolean],
    [mergeItems=boolean], [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/duplicateSurface.html
    """
    return _wrapCommand(cmds.duplicateSurface, args, kwargs)


def dynamicLoad(*args, **kwargs):  # noqa
    """Dynamically load the DLL passed as argument.

    dynamicLoad( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynamicLoad.html
    """
    return _wrapCommand(cmds.dynamicLoad, args, kwargs)


def dynCache(*args, **kwargs):  # noqa
    """Cache the current state of all particle shapes at the current time.

    dynCache()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynCache.html
    """
    return _wrapCommand(cmds.dynCache, args, kwargs)


def dynExport(*args, **kwargs):  # noqa
    """Export particle data to disk files.

    dynExport( [objects] , [allObjects=boolean], [attribute=string], [format=string],
    [maxFrame=time], [minFrame=time], [onlyUpdateParticles=boolean], [overSampling=int],
    [path=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynExport.html
    """
    return _wrapCommand(cmds.dynExport, args, kwargs)


def dynExpression(*args, **kwargs):  # noqa
    """This command describes an expression that belongs to the specified particle shape.

    dynExpression( selectionItem , [creation=boolean], [runtime=boolean],
    [runtimeAfterDynamics=boolean], [runtimeBeforeDynamics=boolean], [string=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynExpression.html
    """
    return _wrapCommand(cmds.dynExpression, args, kwargs)


def dynGlobals(*args, **kwargs):  # noqa
    """This node edits and queries the attributes of the active dynGlobals node in the scene.

    dynGlobals([active=boolean], [listAll=boolean], [overSampling=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynGlobals.html
    """
    return _wrapCommand(cmds.dynGlobals, args, kwargs)


def dynPaintEditor(*args, **kwargs):  # noqa
    """Create a editor window that can be painted into.

    dynPaintEditor( editorName , [activeOnly=boolean], [autoSave=boolean], [camera=string],
    [canvasMode=boolean], [canvasUndo=boolean], [changeCommand=[string, string, string,
    string]], [clear=[float, float, float]], [control=boolean],
    [currentCanvasSize=boolean], [defineTemplate=string], [displayAppearance=string],
    [displayFog=boolean], [displayImage=int], [displayLights=string],
    [displayStyle=string], [displayTextures=boolean], [docTag=string],
    [doubleBuffer=boolean], [drawAxis=boolean], [drawContext=boolean], [exists=boolean],
    [fastUpdate=int], [fileName=string], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [iconGrab=boolean], [loadImage=string],
    [lockMainConnection=boolean], [mainListConnection=string], [menu=string],
    [nbImages=boolean], [newImage=[int, int, float, float, float]], [paintAll=float],
    [panel=string], [parent=string], [redrawLast=boolean], [refresh=boolean],
    [refreshMode=int], [removeAllImages=boolean], [removeImage=boolean],
    [rollImage=[float, float]], [saveAlpha=boolean], [saveBumpmap=string],
    [saveImage=boolean], [scaleBlue=float], [scaleGreen=float], [scaleRed=float],
    [selectionConnection=string], [singleBuffer=boolean], [snapShot=boolean],
    [stateString=boolean], [swap=int], [tileSize=int], [unParent=boolean],
    [undoCache=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string], [wrap=[boolean, boolean]], [writeImage=string], [zoom=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynPaintEditor.html
    """
    return _wrapCommand(cmds.dynPaintEditor, args, kwargs)


def dynParticleCtx(*args, **kwargs):  # noqa
    """The particle context command creates a particle context.

    dynParticleCtx( string , [conserve=float], [cursorPlacement=boolean], [exists=boolean],
    [grid=boolean], [gridSpacing=float], [history=boolean], [image1=string],
    [image2=string], [image3=string], [jitterRadius=float], [lowerLeftX=float],
    [lowerLeftY=float], [lowerLeftZ=float], [name=string], [nucleus=boolean],
    [numJitters=int], [particleName=string], [sketch=boolean], [sketchInterval=int],
    [textPlacement=boolean], [upperRightX=float], [upperRightY=float], [upperZ=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynParticleCtx.html
    """
    return _wrapCommand(cmds.dynParticleCtx, args, kwargs)


def dynPref(*args, **kwargs):  # noqa
    """This action modifies and queries the current state of "autoCreate rigid bodies", "run up
    to current time", and "run up from" (previous time or start time).

    dynPref([autoCreate=boolean], [echoCollision=boolean], [runupFrom=int],
    [runupToCurrentTime=boolean], [saveOnQuit=boolean], [saveRuntimeState=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/dynPref.html
    """
    return _wrapCommand(cmds.dynPref, args, kwargs)


def editDisplayLayerGlobals(*args, **kwargs):  # noqa
    """Edit the parameter values common to all display layers.

    editDisplayLayerGlobals([baseId=int], [currentDisplayLayer=name], [mergeType=int],
    [useCurrent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerGlobals.html
    """
    return _wrapCommand(cmds.editDisplayLayerGlobals, args, kwargs)


def editDisplayLayerMembers(*args, **kwargs):  # noqa
    """This command is used to query and edit membership of display layers.

    editDisplayLayerMembers([fullNames=boolean], [noRecurse=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editDisplayLayerMembers.html
    """
    return _wrapCommand(cmds.editDisplayLayerMembers, args, kwargs)


def editMetadata(*args, **kwargs):  # noqa
    """This command is used to set metadata elements onto or remove metadata elements from an
    object.

    editMetadata([channelName=string], [channelType=string], [endIndex=string],
    [index=string], [indexType=string], [memberName=string], [remove=boolean],
    [scene=boolean], [startIndex=string], [streamName=string], [stringValue=string],
    [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editMetadata.html
    """
    return _wrapCommand(cmds.editMetadata, args, kwargs)


def editor(*args, **kwargs):  # noqa
    """Edit the characteristic of an editor.

    editor( editorName , [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string],
    [selectionConnection=string], [stateString=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editor.html
    """
    return _wrapCommand(cmds.editor, args, kwargs)


def editorTemplate(*args, **kwargs):  # noqa
    """The editorTemplate command allows the user to specify the conceptual layout of an
    attribute editor and leave the details of exactly which UI elements are used in the
    final result to the automatic dialog generation mechanism.

    editorTemplate([addAdskAssetControls=boolean], [addComponents=boolean],
    [addControl=[string, script]], [addDynamicControl=[string, script]],
    [addExtraControls=boolean], [addSeparator=boolean], [annotateFieldOnly=boolean],
    [annotation=string], [beginLayout=string], [beginNoOptimize=boolean],
    [beginScrollLayout=boolean], [callCustom=[script, script]], [collapse=boolean],
    [debugMode=boolean], [dimControl=[string, string, boolean]], [endLayout=boolean],
    [endNoOptimize=boolean], [endScrollLayout=boolean], [extraControlsLabel=string],
    [forceRebuild=boolean], [interruptOptimize=boolean], [label=string],
    [listExtraAttributes=string], [preventOverride=boolean], [queryControl=[string,
    string]], [queryLabel=[string, string]], [queryName=[string, string]],
    [suppress=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editorTemplate.html
    """
    return _wrapCommand(cmds.editorTemplate, args, kwargs)


def editRenderLayerAdjustment(*args, **kwargs):  # noqa
    """This command is used to create, edit, and query adjustments to render layers.

    editRenderLayerAdjustment([attributeLog=boolean], [layer=name], [nodeLog=boolean],
    [remove=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerAdjustment.html
    """
    return _wrapCommand(cmds.editRenderLayerAdjustment, args, kwargs)


def editRenderLayerGlobals(*args, **kwargs):  # noqa
    """Edit the parameter values common to all render layers.

    editRenderLayerGlobals([baseId=int], [currentRenderLayer=name],
    [enableAutoAdjustments=boolean], [mergeType=int], [useCurrent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerGlobals.html
    """
    return _wrapCommand(cmds.editRenderLayerGlobals, args, kwargs)


def editRenderLayerMembers(*args, **kwargs):  # noqa
    """This command is used to query and edit memberships to render layers.

    editRenderLayerMembers([fullNames=boolean], [noRecurse=boolean], [remove=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/editRenderLayerMembers.html
    """
    return _wrapCommand(cmds.editRenderLayerMembers, args, kwargs)


def effector(*args, **kwargs):  # noqa
    """The effector command is used to set the name or hidden flag for the effector.

    effector( [object] , [hide=boolean], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/effector.html
    """
    return _wrapCommand(cmds.effector, args, kwargs)


def emit(*args, **kwargs):  # noqa
    """The `emit` action allows users to add particles to an existing particle object without the
    use of an emitter.

    emit([attribute=string], [floatValue=float], [object=string], [position=[float, float,
    float]], [vectorValue=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/emit.html
    """
    return _wrapCommand(cmds.emit, args, kwargs)


def emitter(*args, **kwargs):  # noqa
    """Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter).

    emitter( [objects] , [alongAxis=float], [aroundAxis=float], [awayFromAxis=float],
    [awayFromCenter=float], [cycleEmission=string], [cycleInterval=int],
    [directionX=linear], [directionY=linear], [directionZ=linear],
    [directionalSpeed=float], [maxDistance=linear], [minDistance=linear], [name=string],
    [needParentUV=boolean], [normalSpeed=float], [position=[linear, linear, linear]],
    [randomDirection=float], [rate=float], [scaleRateByObjectSize=boolean],
    [scaleSpeedBySize=boolean], [speed=float], [speedRandom=float], [spread=float],
    [tangentSpeed=float], [torusSectionRadius=linear], [type=string],
    [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/emitter.html
    """
    return _wrapCommand(cmds.emitter, args, kwargs)


def enableDevice(*args, **kwargs):  # noqa
    """Sets (or queries) the device enable state for actions involving the device.

    enableDevice([apply=boolean], [device=string], [enable=boolean], [monitor=boolean],
    [record=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/enableDevice.html
    """
    return _wrapCommand(cmds.enableDevice, args, kwargs)


def encodeString(*args, **kwargs):  # noqa
    """This action will take a string and encode any character that would need to be escaped
    before being sent to some other command.

    encodeString( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/encodeString.html
    """
    return _wrapCommand(cmds.encodeString, args, kwargs)


def error(*args, **kwargs):  # noqa
    """The error command is provided so that the user can issue error messages from his/her
    scripts and control execution in the event of runtime errors.

    error([noContext=boolean], [showLineNumber=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/error.html
    """
    return _wrapCommand(cmds.error, args, kwargs)


def eval(*args, **kwargs):  # noqa
    """This function takes a string which contains MEL code and evaluates it using the MEL
    interpreter.

    eval( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/eval.html
    """
    return _wrapCommand(cmds.eval, args, kwargs)


def evalDeferred(*args, **kwargs):  # noqa
    """This command takes the string it is given and evaluates it during the next available idle
    time.

    evalDeferred( [script] , [evaluateNext=boolean], [list=boolean], [lowPriority=boolean],
    [lowestPriority=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/evalDeferred.html
    """
    return _wrapCommand(cmds.evalDeferred, args, kwargs)


def evaluationManager(*args, **kwargs):  # noqa
    """Handles turning on and off the evaluation manager method of evaluating the DG.

    evaluationManager([cycleCluster=string], [disableInfo=string], [downstreamFrom=string],
    [empty=boolean], [enabled=boolean], [fallbackTriggered=boolean], [idleAction=int],
    [idleBuild=boolean], [invalidate=boolean], [manipulation=boolean],
    [manipulationPrevalidation=boolean], [manipulationReady=boolean], [mode=string],
    [nodeTypeGloballySerialize=boolean], [nodeTypeParallel=boolean],
    [nodeTypeSerialize=boolean], [nodeTypeUntrusted=boolean],
    [reduceGraphRebuild=boolean], [safeMode=boolean], [upstreamFrom=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/evaluationManager.html
    """
    return _wrapCommand(cmds.evaluationManager, args, kwargs)


def evaluator(*args, **kwargs):  # noqa
    """Handles turning on and off custom evaluation overrides used by the evaluation manager.

    evaluator([clusters=boolean], [configuration=string], [enable=boolean], [info=boolean],
    [name=string], [nodeType=string], [nodeTypeChildren=boolean], [priority=int],
    [valueName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/evaluator.html
    """
    return _wrapCommand(cmds.evaluator, args, kwargs)


def event(*args, **kwargs):  # noqa
    """The event command assigns collision events to a particle object.

    event( [object] , [count=uint], [delete=boolean], [dieAtCollision=boolean], [emit=uint],
    [list=boolean], [name=string], [proc=script], [random=boolean], [rename=string],
    [select=boolean], [split=uint], [spread=float], [target=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/event.html
    """
    return _wrapCommand(cmds.event, args, kwargs)


def exactWorldBoundingBox(*args, **kwargs):  # noqa
    """This command figures out an exact-fit bounding box for the specified objects (or selected
    objects if none are specified) This bounding box is always in world space.

    exactWorldBoundingBox( [dagObject...] , [calculateExactly=boolean],
    [ignoreInvisible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/exactWorldBoundingBox.html
    """
    return _wrapCommand(cmds.exactWorldBoundingBox, args, kwargs)


def exclusiveLightCheckBox(*args, **kwargs):  # noqa
    """This command creates a checkBox that controls a light's exclusive non-exclusive status.

    exclusiveLightCheckBox([annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [light=name], [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/exclusiveLightCheckBox.html
    """
    return _wrapCommand(cmds.exclusiveLightCheckBox, args, kwargs)


def expandedSelection(*args, **kwargs):  # noqa
    """Examines the current selection list and returns that list, expanded to meet certain
    criteria.

    expandedSelection([depth=uint], [expansionType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/expandedSelection.html
    """
    return _wrapCommand(cmds.expandedSelection, args, kwargs)


def exportEdits(*args, **kwargs):  # noqa
    """Use this command to export edits made in the scene to a file.

    exportEdits([editCommand=string], [excludeHierarchy=boolean], [excludeNode=string],
    [exportSelected=boolean], [force=boolean], [includeAnimation=boolean],
    [includeConstraints=boolean], [includeDeformers=boolean], [includeNetwork=boolean],
    [includeNode=string], [includeSetAttrs=boolean], [includeSetDrivenKeys=boolean],
    [includeShaders=boolean], [onReferenceNode=string], [selected=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/exportEdits.html
    """
    return _wrapCommand(cmds.exportEdits, args, kwargs)


def expression(*args, **kwargs):  # noqa
    """This command describes an expression that belongs to the current scene.

    expression([alwaysEvaluate=uint], [animated=uint], [attribute=string], [name=string],
    [object=string], [safe=boolean], [shortNames=boolean], [string=string],
    [timeDependent=boolean], [unitConversion=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/expression.html
    """
    return _wrapCommand(cmds.expression, args, kwargs)


def expressionEditorListen(*args, **kwargs):  # noqa
    """Listens for messages for the Expression Editor, at its request, and communicates them to
    it.

    expressionEditorListen([listenFile=string], [listenForAttr=string],
    [listenForExpression=string], [listenForName=string], [stopListenForAttr=string],
    [stopListenForExpression=string], [stopListenForName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/expressionEditorListen.html
    """
    return _wrapCommand(cmds.expressionEditorListen, args, kwargs)


def extendCurve(*args, **kwargs):  # noqa
    """This command extends a curve or creates a new curve as an extension.

    extendCurve( object , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [distance=linear], [extendMethod=int], [extensionType=int],
    [inputPoint=[linear, linear, linear]], [join=boolean], [name=string],
    [noChanges=boolean], [nodeState=int], [object=boolean], [pointX=linear],
    [pointY=linear], [pointZ=linear], [range=boolean], [removeMultipleKnots=boolean],
    [replaceOriginal=boolean], [start=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/extendCurve.html
    """
    return _wrapCommand(cmds.extendCurve, args, kwargs)


def extendSurface(*args, **kwargs):  # noqa
    """This command extends a surface or creates a new surface as an extension.

    extendSurface( surface [surface] , [caching=boolean], [constructionHistory=boolean],
    [distance=linear], [extendDirection=int], [extendMethod=int], [extendSide=int],
    [extensionType=int], [join=boolean], [name=string], [nodeState=int], [object=boolean],
    [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/extendSurface.html
    """
    return _wrapCommand(cmds.extendSurface, args, kwargs)


def extrude(*args, **kwargs):  # noqa
    """This command computes a surface given a profile curve and possibly a path curve.

    extrude( curve [curve] , [caching=boolean], [constructionHistory=boolean],
    [degreeAlongLength=int], [direction=[linear, linear, linear]], [directionX=linear],
    [directionY=linear], [directionZ=linear], [extrudeType=int], [fixedPath=boolean],
    [length=linear], [mergeItems=boolean], [name=string], [nodeState=int],
    [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [range=boolean],
    [rebuild=boolean], [reverseSurfaceIfPathReversed=boolean], [rotation=angle],
    [scale=float], [subCurveSubSurface=boolean], [useComponentPivot=int],
    [useProfileNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/extrude.html
    """
    return _wrapCommand(cmds.extrude, args, kwargs)


def falloffCurve(*args, **kwargs):  # noqa
    """This command creates a control for editing a 2D control curve.

    falloffCurve( [string] , [addControlVertex=string], [annotation=string],
    [asString=string], [backgroundColor=[float, float, float]], [changeCommand=script],
    [currentKey=int], [currentKeyValue=[float, float]], [customCurveWidget=boolean],
    [defineTemplate=string], [deleteControlVertex=int], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [optionVar=string], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [readOnly=boolean],
    [snapToGrid=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/falloffCurve.html
    """
    return _wrapCommand(cmds.falloffCurve, args, kwargs)


def falloffCurveAttr(*args, **kwargs):  # noqa
    """This command creates a control for editing a 2D control curve.

    falloffCurveAttr( [string] , [addControlVertex=string], [annotation=string],
    [asString=string], [attribute=name], [backgroundColor=[float, float, float]],
    [changeCommand=script], [currentKey=int], [currentKeyValue=[float, float]],
    [customCurveWidget=int], [defineTemplate=string], [deleteControlVertex=int],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [readOnly=int], [selectedPositionControl=string],
    [selectedValueControl=string], [snapToGrid=int], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/falloffCurveAttr.html
    """
    return _wrapCommand(cmds.falloffCurveAttr, args, kwargs)


def fcheck(*args, **kwargs):  # noqa
    """Invokes the fcheck program to display images in a separate window.

    fcheck()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fcheck.html
    """
    return _wrapCommand(cmds.fcheck, args, kwargs)


def file(*args, **kwargs):  # noqa
    """<h4>Opening, importing, exporting, referencing, saving, or renaming a file</h4>.

    file( string , [absoluteName=boolean], [activate=boolean], [activeProxy=boolean],
    [add=boolean], [anyModified=boolean], [applyTo=string], [buildLoadSettings=boolean],
    [channels=boolean], [cleanReference=string], [command=[string, string]],
    [compress=boolean], [constraints=boolean], [constructionHistory=boolean],
    [copyNumberList=boolean], [defaultExtensions=boolean], [defaultNamespace=boolean],
    [deferReference=boolean], [editCommand=string], [errorStatus=boolean],
    [executeScriptNodes=boolean], [exists=boolean], [expandName=boolean],
    [exportAll=boolean], [exportAnim=boolean], [exportAnimFromReference=boolean],
    [exportAsReference=boolean], [exportAsSegment=boolean], [exportSelected=boolean],
    [exportSelectedAnim=boolean], [exportSelectedAnimFromReference=boolean],
    [exportSelectedNoReference=boolean], [exportSelectedStrict=boolean],
    [exportSnapshotCallback=[script, string]], [exportUnloadedReferences=boolean],
    [expressions=boolean], [fileMetaData=boolean], [flushReference=string],
    [force=boolean], [groupLocator=boolean], [groupName=string], [groupReference=boolean],
    [i=boolean], [ignoreVersion=boolean], [importFrameRate=boolean],
    [importReference=boolean], [importTimeRange=string], [lastFileOption=boolean],
    [lastTempFile=boolean], [list=boolean], [loadAllDeferred=boolean],
    [loadAllReferences=boolean], [loadNoReferences=boolean], [loadReference=string],
    [loadReferenceDepth=string], [loadReferencePreview=string], [loadSettings=string],
    [location=boolean], [lockContainerUnpublished=boolean], [lockFile=boolean],
    [lockReference=boolean], [mapPlaceHolderNamespace=[string, string]],
    [mergeBaseAnimLayer=boolean], [mergeNamespaceWithParent=boolean],
    [mergeNamespaceWithRoot=boolean], [mergeNamespacesOnClash=boolean],
    [modified=boolean], [moveSelected=boolean], [namespace=string], [newFile=boolean],
    [open=boolean], [options=string], [parentNamespace=boolean], [postSaveScript=string],
    [preSaveScript=string], [preserveName=boolean], [preserveReferences=boolean],
    [preview=boolean], [prompt=boolean], [proxyManager=string], [proxyTag=string],
    [reference=boolean], [referenceDepthInfo=uint], [referenceNode=string],
    [relativeNamespace=string], [removeDuplicateNetworks=boolean],
    [removeReference=boolean], [rename=string], [renameAll=boolean],
    [renameToSave=boolean], [renamingPrefix=string], [renamingPrefixList=boolean],
    [replaceName=[string, string]], [reserveNamespaces=boolean], [resetError=boolean],
    [returnNewNodes=boolean], [save=boolean], [saveDiskCache=string],
    [saveReference=boolean], [saveReferencesUnloaded=boolean], [saveTextures=string],
    [sceneName=boolean], [segment=string], [selectAll=boolean], [shader=boolean],
    [sharedNodes=string], [sharedReferenceFile=boolean], [shortName=boolean],
    [strict=boolean], [swapNamespace=[string, string]], [type=string],
    [uiConfiguration=boolean], [uiLoadConfiguration=boolean], [unloadReference=string],
    [unresolvedName=boolean], [usingNamespaces=boolean], [withoutCopyNumber=boolean],
    [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/file.html
    """
    return _wrapCommand(cmds.file, args, kwargs)


def fileBrowserDialog(*args, **kwargs):  # noqa
    """The fileBrowserDialog and fileDialog commands have now been deprecated.

    fileBrowserDialog([actionName=string], [dialogStyle=int], [fileCommand=script],
    [fileType=string], [filterList=string], [includeName=string], [mode=int],
    [operationMode=string], [tipMessage=string], [windowTitle=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fileBrowserDialog.html
    """
    return _wrapCommand(cmds.fileBrowserDialog, args, kwargs)


def fileDialog(*args, **kwargs):  # noqa
    """The fileBrowserDialog and fileDialog commands have now been deprecated.

    fileDialog([application=boolean], [defaultFileName=string], [directoryMask=string],
    [mode=int], [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fileDialog.html
    """
    return _wrapCommand(cmds.fileDialog, args, kwargs)


def fileDialog2(*args, **kwargs):  # noqa
    """This command provides a dialog that allows users to select files or directories.

    fileDialog2([buttonBoxOrientation=int], [cancelCaption=string], [caption=string],
    [dialogStyle=int], [fileFilter=string], [fileMode=int], [fileTypeChanged=script],
    [hideNameEdit=boolean], [okCaption=string], [optionsUICancel=script],
    [optionsUICommit=script], [optionsUICommit2=script], [optionsUICreate=script],
    [optionsUIInit=script], [optionsUITitle=string], [returnFilter=boolean],
    [selectFileFilter=string], [selectionChanged=script], [setProjectBtnEnabled=boolean],
    [startingDirectory=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fileDialog2.html
    """
    return _wrapCommand(cmds.fileDialog2, args, kwargs)


def fileInfo(*args, **kwargs):  # noqa
    """fileInfo provides a mechanism for keeping information related to a Maya scene file.

    fileInfo([string][string], [referenceNode=string], [remove=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fileInfo.html
    """
    return _wrapCommand(cmds.fileInfo, args, kwargs)


def filePathEditor(*args, **kwargs):  # noqa
    """Maya can reference and use external files, such as textures or other Maya scenes.

    filePathEditor([attributeOnly=boolean], [attributeType=string], [byType=string],
    [copyAndRepath=[string, string]], [deregisterType=string], [force=boolean],
    [listDirectories=string], [listFiles=string], [listRegisteredTypes=boolean],
    [preview=boolean], [recursive=boolean], [refresh=boolean], [registerType=string],
    [relativeNames=boolean], [repath=string], [replaceAll=boolean], [replaceField=string],
    [replaceString=[string, string]], [status=boolean], [temporary=boolean],
    [typeLabel=string], [unresolved=boolean], [withAttribute=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filePathEditor.html
    """
    return _wrapCommand(cmds.filePathEditor, args, kwargs)


def filletCurve(*args, **kwargs):  # noqa
    """The curve fillet command creates a fillet curve between two curves.

    filletCurve( [curve] [curve] , [bias=linear], [blendControl=boolean], [caching=boolean],
    [circular=boolean], [constructionHistory=boolean], [curveParameter1=float],
    [curveParameter2=float], [depth=linear], [freeformBlend=boolean], [join=boolean],
    [name=string], [nodeState=int], [object=boolean], [radius=linear],
    [replaceOriginal=boolean], [trim=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filletCurve.html
    """
    return _wrapCommand(cmds.filletCurve, args, kwargs)


def filter(*args, **kwargs):  # noqa
    """Creates or modifies a filter node.

    filter([name=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filter.html
    """
    return _wrapCommand(cmds.filter, args, kwargs)


def filterButterworthCtx(*args, **kwargs):  # noqa
    """Creates/edits a Butterworth filter context.

    filterButterworthCtx( contextName , [apply=boolean], [cutoffFrequency=float],
    [endTime=time], [exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [keepKeysOnFrame=boolean], [name=string], [samplingRate=float],
    [selectedKeys=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterButterworthCtx.html
    """
    return _wrapCommand(cmds.filterButterworthCtx, args, kwargs)


def filterCurve(*args, **kwargs):  # noqa
    """The filterCurve command takes a list of anim curve and filters them using a specified
    filter.

    filterCurve([cutoffFrequency=float], [endTime=time], [filter=string],
    [keepKeysOnFrame=boolean], [kernel=string], [keySync=boolean], [maxTimeStep=float],
    [minTimeStep=float], [period=float], [precision=float], [precisionMode=int],
    [preserveKeyTangent=string], [sampleCount=int], [samplingRate=float],
    [selectedKeys=boolean], [startTime=time], [timeTolerance=float], [tolerance=float],
    [useQuaternion=boolean], [width=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterCurve.html
    """
    return _wrapCommand(cmds.filterCurve, args, kwargs)


def filterExpand(*args, **kwargs):  # noqa
    """Based on selected components (or components specified on the command line), the command
    filters and/or expands the list given the options.

    filterExpand([expand=boolean], [fullPath=boolean], [selectionMask=int],
    [symActive=boolean], [symNegative=boolean], [symPositive=boolean], [symSeam=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterExpand.html
    """
    return _wrapCommand(cmds.filterExpand, args, kwargs)


def filterGaussianCtx(*args, **kwargs):  # noqa
    """Creates a smooth (gaussian) filter context.

    filterGaussianCtx( contextName , [apply=boolean], [endTime=time], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string],
    [sampleCount=int], [selectedKeys=boolean], [startTime=time], [useQuaternion=boolean],
    [width=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterGaussianCtx.html
    """
    return _wrapCommand(cmds.filterGaussianCtx, args, kwargs)


def filterInstances(*args, **kwargs):  # noqa
    """This command filters the selection list to remove duplicate instances that refer to the
    same object/components.

    filterInstances([shapes=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterInstances.html
    """
    return _wrapCommand(cmds.filterInstances, args, kwargs)


def filterKeyReducerCtx(*args, **kwargs):  # noqa
    """Creates/edits a KeyReducer filter context.

    filterKeyReducerCtx( contextName , [apply=boolean], [endTime=time], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [keySync=boolean], [name=string], [precision=float], [precisionMode=int],
    [preserveKeyTangent=string], [selectedKeys=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterKeyReducerCtx.html
    """
    return _wrapCommand(cmds.filterKeyReducerCtx, args, kwargs)


def filterStudioImport(*args, **kwargs):  # noqa
    """Directly sets the filter options on the studioImport plugin from anywhere in MEL without
    having to use the UI.

    filterStudioImport([convertShellToPoly=boolean], [includeCameras=boolean],
    [includeLights=boolean], [transferDirectoryName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/filterStudioImport.html
    """
    return _wrapCommand(cmds.filterStudioImport, args, kwargs)


def findDeformers(*args, **kwargs):  # noqa
    """This command finds all deformers for the specified shape(s).

    findDeformers( [objects...] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/findDeformers.html
    """
    return _wrapCommand(cmds.findDeformers, args, kwargs)


def findKeyframe(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    findKeyframe( [animatedObject] , [animation=string], [attribute=string],
    [controlPoints=boolean], [curve=boolean], [float=floatrange], [hierarchy=string],
    [includeUpperBound=boolean], [index=uint], [shape=boolean], [time=timerange],
    [timeSlider=boolean], [which=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/findKeyframe.html
    """
    return _wrapCommand(cmds.findKeyframe, args, kwargs)


def findType(*args, **kwargs):  # noqa
    """The `findType` command is used to search through a dependency subgraph on a certain node
    to find all nodes of the given type.

    findType([deep=boolean], [exact=boolean], [forward=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/findType.html
    """
    return _wrapCommand(cmds.findType, args, kwargs)


def fitBspline(*args, **kwargs):  # noqa
    """The fitBspline command fits the CVs from an input curve and and returns a 3D curve.

    fitBspline([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [object=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fitBspline.html
    """
    return _wrapCommand(cmds.fitBspline, args, kwargs)


def flexor(*args, **kwargs):  # noqa
    """This command creates a flexor.

    flexor( [objects] , [atBones=boolean], [atJoints=boolean], [deformerCommand=string],
    [list=boolean], [name=string], [noScale=boolean], [toSkeleton=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/flexor.html
    """
    return _wrapCommand(cmds.flexor, args, kwargs)


def floatField(*args, **kwargs):  # noqa
    """Create a field control that accepts only float values and is bound by a minimum and
    maximum value.

    floatField( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [editable=boolean], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [maxValue=float], [minValue=float],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean],
    [receiveFocusCommand=script], [showTrailingZeros=boolean], [statusBarMessage=string],
    [step=float], [useTemplate=string], [value=float], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatField.html
    """
    return _wrapCommand(cmds.floatField, args, kwargs)


def floatFieldGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    floatFieldGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean],
    [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfFields=int],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]],
    [showTrailingZeros=boolean], [statusBarMessage=string], [step=float],
    [useTemplate=string], [value=[float, float, float, float]], [value1=float],
    [value2=float], [value3=float], [value4=float], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatFieldGrp.html
    """
    return _wrapCommand(cmds.floatFieldGrp, args, kwargs)


def floatScrollBar(*args, **kwargs):  # noqa
    """Create a scroll bar control that accepts only float values and is bound by a minimum and
    maximum value.

    floatScrollBar( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontal=boolean], [isObscured=boolean], [largeStep=float], [manage=boolean],
    [maxValue=float], [minValue=float], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [step=float],
    [useTemplate=string], [value=float], [visible=boolean], [visibleChangeCommand=script],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatScrollBar.html
    """
    return _wrapCommand(cmds.floatScrollBar, args, kwargs)


def floatSlider(*args, **kwargs):  # noqa
    """Create a slider control that accepts only float values and is bound by a minimum and
    maximum value.

    floatSlider( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontal=boolean], [isObscured=boolean], [manage=boolean], [maxValue=float],
    [minValue=float], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [step=float], [useTemplate=string], [value=float],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatSlider.html
    """
    return _wrapCommand(cmds.floatSlider, args, kwargs)


def floatSlider2(*args, **kwargs):  # noqa
    """This command creates a float slider containing two handles.

    floatSlider2( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand1=string], [changeCommand2=string], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [maximum=float], [minimum=float],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string], [polarity=int],
    [popupMenuArray=boolean], [positionControl1=string], [positionControl2=string],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [value1=float], [value2=float], [values=[float, float]], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatSlider2.html
    """
    return _wrapCommand(cmds.floatSlider2, args, kwargs)


def floatSliderButtonGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    floatSliderButtonGrp( [name] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [buttonCommand=script], [buttonLabel=string], [changeCommand=script],
    [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string,
    string, string]], [columnAlign4=[string, string, string, string]],
    [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string,
    string, string, string, string, string]], [columnAttach=[int, string, int]],
    [columnAttach2=[string, string]], [columnAttach3=[string, string, string]],
    [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string,
    string, string, string]], [columnAttach6=[string, string, string, string, string,
    string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=float],
    [fieldMinValue=float], [fieldStep=float], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [isObscured=boolean],
    [label=string], [manage=boolean], [maxValue=float], [minValue=float],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int,
    string, int]], [sliderStep=float], [statusBarMessage=string], [step=float],
    [symbolButtonCommand=script], [symbolButtonDisplay=boolean], [useTemplate=string],
    [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatSliderButtonGrp.html
    """
    return _wrapCommand(cmds.floatSliderButtonGrp, args, kwargs)


def floatSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    floatSliderGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=float],
    [fieldMinValue=float], [fieldStep=float], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [maxValue=float], [minValue=float], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]],
    [sliderStep=float], [statusBarMessage=string], [step=float], [useTemplate=string],
    [value=float], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/floatSliderGrp.html
    """
    return _wrapCommand(cmds.floatSliderGrp, args, kwargs)


def flow(*args, **kwargs):  # noqa
    """The flow command creates a deformation lattice to `bend' the object that is animated along
    a curve of a motion path animation.

    flow( objects , [divisions=[uint, uint, uint]], [localCompute=boolean],
    [localDivisions=[uint, uint, uint]], [objectCentered=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/flow.html
    """
    return _wrapCommand(cmds.flow, args, kwargs)


def flowLayout(*args, **kwargs):  # noqa
    """This command creates a layout that arranges its children along a single line (either
    horizontal or vertical).

    flowLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [childArray=boolean], [columnSpacing=int], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontal=boolean], [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [vertical=boolean], [visible=boolean],
    [visibleChangeCommand=script], [width=int], [wrap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/flowLayout.html
    """
    return _wrapCommand(cmds.flowLayout, args, kwargs)


def fluidCacheInfo(*args, **kwargs):  # noqa
    """A command to get information about the fluids cache.

    fluidCacheInfo([attribute=string], [cacheTime=time], [endFrame=boolean],
    [hasCache=boolean], [hasData=boolean], [initialConditions=boolean],
    [playback=boolean], [resolution=boolean], [startFrame=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fluidCacheInfo.html
    """
    return _wrapCommand(cmds.fluidCacheInfo, args, kwargs)


def fluidEmitter(*args, **kwargs):  # noqa
    """Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter).

    fluidEmitter( selectionList , [cycleEmission=string], [cycleInterval=int],
    [densityEmissionRate=float], [fluidDropoff=float], [fuelEmissionRate=float],
    [heatEmissionRate=float], [maxDistance=linear], [minDistance=linear], [name=string],
    [position=[linear, linear, linear]], [rate=float], [torusSectionRadius=linear],
    [type=string], [volumeOffset=[linear, linear, linear]], [volumeShape=string],
    [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fluidEmitter.html
    """
    return _wrapCommand(cmds.fluidEmitter, args, kwargs)


def fluidVoxelInfo(*args, **kwargs):  # noqa
    """Provides basic information about the mapping of a fluid voxel grid into world- or object
    space of the fluid.

    fluidVoxelInfo([checkBounds=boolean], [inBounds=[int, int, int]], [objectSpace=boolean],
    [radius=float], [voxel=[float, float, float]], [voxelCenter=boolean], [xIndex=int],
    [yIndex=int], [zIndex=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fluidVoxelInfo.html
    """
    return _wrapCommand(cmds.fluidVoxelInfo, args, kwargs)


def flushUndo(*args, **kwargs):  # noqa
    """Removes everything from the undo queue, freeing up memory.

    flushUndo()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/flushUndo.html
    """
    return _wrapCommand(cmds.flushUndo, args, kwargs)


def fontDialog(*args, **kwargs):  # noqa
    """Displays a dialog of available fonts for the user to select from.

    fontDialog([FontList=boolean], [scalable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/fontDialog.html
    """
    return _wrapCommand(cmds.fontDialog, args, kwargs)


def format(*args, **kwargs):  # noqa
    """This command takes a format string, where the format string contains format specifiers.

    format([stringArg=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/format.html
    """
    return _wrapCommand(cmds.format, args, kwargs)


def formLayout(*args, **kwargs):  # noqa
    """This command creates a form layout control.

    formLayout( [string] , [annotation=string], [attachControl=[string, string, int, string]],
    [attachForm=[string, string, int]], [attachNone=[string, string]],
    [attachOppositeControl=[string, string, int, string]], [attachOppositeForm=[string,
    string, int]], [attachPosition=[string, string, int, int]], [backgroundColor=[float,
    float, float]], [childArray=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfDivisions=int], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/formLayout.html
    """
    return _wrapCommand(cmds.formLayout, args, kwargs)


def frameBufferName(*args, **kwargs):  # noqa
    """Returns the frame buffer name for a given renderPass renderLayer and camera combination.

    frameBufferName([autoTruncate=boolean], [camera=string], [renderLayer=string],
    [renderPass=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/frameBufferName.html
    """
    return _wrapCommand(cmds.frameBufferName, args, kwargs)


def frameLayout(*args, **kwargs):  # noqa
    """This command creates frame layout control.

    frameLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [backgroundShade=boolean], [borderStyle=string], [borderVisible=boolean],
    [childArray=boolean], [collapsable=boolean], [collapse=boolean],
    [collapseCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [expandCommand=script], [font=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [labelAlign=string], [labelIndent=int], [labelVisible=boolean], [labelWidth=int],
    [manage=boolean], [marginHeight=int], [marginWidth=int], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preCollapseCommand=script], [preExpandCommand=script],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/frameLayout.html
    """
    return _wrapCommand(cmds.frameLayout, args, kwargs)


def framelessDialog(*args, **kwargs):  # noqa
    """The framelessDialog command creates a modal dialog with a message to the user and a
    variable number of buttons to dismiss the dialog.

    framelessDialog([button=string], [message=string], [parent=string], [path=string],
    [primary=string], [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/framelessDialog.html
    """
    return _wrapCommand(cmds.framelessDialog, args, kwargs)


def freeFormFillet(*args, **kwargs):  # noqa
    """This command creates a free form surface fillet across two surface trim edges or isoparms
    or curve on surface.

    freeFormFillet( [surfaceIsoparm] [surfaceIsoparm] , [bias=float], [caching=boolean],
    [constructionHistory=boolean], [depth=float], [name=string], [nodeState=int],
    [object=boolean], [polygon=int], [positionTolerance=float], [range=boolean],
    [tangentTolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/freeFormFillet.html
    """
    return _wrapCommand(cmds.freeFormFillet, args, kwargs)


def freeze(*args, **kwargs):  # noqa
    """When a node is frozen none of its inputs will be requested when they change, the node will
    use the inputs that existed at the time of freezing until the node is unfrozen.

    freeze([allNodes=boolean], [displayLayers=boolean], [downstream=boolean],
    [forceDownstream=boolean], [frozen=boolean], [invisible=boolean], [noFreeze=boolean],
    [unfreeze=boolean], [upstream=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/freeze.html
    """
    return _wrapCommand(cmds.freeze, args, kwargs)


def freezeOptions(*args, **kwargs):  # noqa
    """This command provides access to the options used by the evaluation manager to handle
    propagation and recognition of when a node is in a frozen state.

    freezeOptions([displayLayers=boolean], [downstream=string], [explicitPropagation=boolean],
    [invisible=boolean], [referencedNodes=boolean], [runtimePropagation=boolean],
    [upstream=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/freezeOptions.html
    """
    return _wrapCommand(cmds.freezeOptions, args, kwargs)


def geomBind(*args, **kwargs):  # noqa
    """This command is used to compute weights using geodesic voxel binding algorithm.

    geomBind([bindMethod=uint], [falloff=float], [geodesicVoxelParams=[uint, boolean]],
    [maxInfluences=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/geomBind.html
    """
    return _wrapCommand(cmds.geomBind, args, kwargs)


def geometryAttrInfo(*args, **kwargs):  # noqa
    """This command provides information about the geometry in an attribute.

    geometryAttrInfo( attribute , [boundingBox=boolean], [castToEdges=boolean],
    [castToFaces=boolean], [castToVerts=boolean], [componentTagCategory=boolean],
    [componentTagExpression=string], [componentTagHash=boolean],
    [componentTagHistory=boolean], [componentTagHistoryHash=boolean],
    [componentTagNames=boolean], [components=boolean], [deformerChain=boolean],
    [elementCount=boolean], [groupId=int], [matrix=boolean], [nodeChain=boolean],
    [originalGeometry=boolean], [outputPlugChain=boolean], [plugChain=boolean],
    [pointCount=boolean], [pointIndices=boolean], [points=boolean], [subsetState=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/geometryAttrInfo.html
    """
    return _wrapCommand(cmds.geometryAttrInfo, args, kwargs)


def geometryConstraint(*args, **kwargs):  # noqa
    """Constrain an object's position based on the shape of the target surface(s) at the closest
    point(s) to the object.

    geometryConstraint( [target...] object , [layer=string], [name=string], [remove=boolean],
    [targetList=boolean], [weight=float], [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/geometryConstraint.html
    """
    return _wrapCommand(cmds.geometryConstraint, args, kwargs)


def geomToBBox(*args, **kwargs):  # noqa
    """Create polygonal mesh bounding boxes for geometry.

    geomToBBox([bakeAnimation=boolean], [combineMesh=boolean], [endTime=time],
    [keepOriginal=boolean], [name=string], [nameSuffix=string], [sampleBy=time],
    [shaderColor=[float, float, float]], [single=boolean], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/geomToBBox.html
    """
    return _wrapCommand(cmds.geomToBBox, args, kwargs)


def getAttr(*args, **kwargs):  # noqa
    """This command returns the value of the named object's attribute.

    getAttr( attribute , [asString=boolean], [caching=boolean], [channelBox=boolean],
    [expandEnvironmentVariables=boolean], [keyable=boolean], [lock=boolean],
    [multiIndices=boolean], [settable=boolean], [silent=boolean], [size=boolean],
    [time=time], [type=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getAttr.html
    """
    return _wrapCommand(cmds.getAttr, args, kwargs)


def getClassification(*args, **kwargs):  # noqa
    """Returns the classification string for a given node type.

    getClassification( string , [satisfies=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getClassification.html
    """
    return _wrapCommand(cmds.getClassification, args, kwargs)


def getDefaultBrush(*args, **kwargs):  # noqa
    """The command returns the name of the default Paint Effects brush.

    getDefaultBrush()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getDefaultBrush.html
    """
    return _wrapCommand(cmds.getDefaultBrush, args, kwargs)


def getFileList(*args, **kwargs):  # noqa
    """Returns a list of files matching an optional wildcard pattern.

    getFileList([filespec=string], [folder=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getFileList.html
    """
    return _wrapCommand(cmds.getFileList, args, kwargs)


def getFluidAttr(*args, **kwargs):  # noqa
    """Returns values of built-in fluid attributes such as density, velocity, etc.

    getFluidAttr([attribute=string], [lowerFace=boolean], [xIndex=int], [xvalue=boolean],
    [yIndex=int], [yvalue=boolean], [zIndex=int], [zvalue=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getFluidAttr.html
    """
    return _wrapCommand(cmds.getFluidAttr, args, kwargs)


def getInputDeviceRange(*args, **kwargs):  # noqa
    """This command lists the minimum and maximum values the device axis can return.

    getInputDeviceRange([maxValue=boolean], [minValue=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getInputDeviceRange.html
    """
    return _wrapCommand(cmds.getInputDeviceRange, args, kwargs)


def getMetadata(*args, **kwargs):  # noqa
    """This command is used to retrieve the values of metadata elements from a node or scene.

    getMetadata([channelName=string], [channelType=string], [dataType=boolean],
    [endIndex=string], [index=string], [indexType=string], [listChannelNames=boolean],
    [listMemberNames=boolean], [listStreamNames=boolean], [memberName=string],
    [scene=boolean], [startIndex=string], [streamName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getMetadata.html
    """
    return _wrapCommand(cmds.getMetadata, args, kwargs)


def getModifiers(*args, **kwargs):  # noqa
    """This command returns the current state of the modifier keys.

    getModifiers()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getModifiers.html
    """
    return _wrapCommand(cmds.getModifiers, args, kwargs)


def getModulePath(*args, **kwargs):  # noqa
    """Returns the module path for a given module name.

    getModulePath([moduleName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getModulePath.html
    """
    return _wrapCommand(cmds.getModulePath, args, kwargs)


def getPanel(*args, **kwargs):  # noqa
    """This command returns panel and panel configuration information.

    getPanel([allConfigs=boolean], [allPanels=boolean], [allScriptedTypes=boolean],
    [allTypes=boolean], [atPosition=[int, int]], [configWithLabel=string],
    [containing=string], [invisiblePanels=boolean], [scriptType=string], [type=string],
    [typeOf=string], [underPointer=boolean], [visiblePanels=boolean], [withFocus=boolean],
    [withLabel=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getPanel.html
    """
    return _wrapCommand(cmds.getPanel, args, kwargs)


def getParticleAttr(*args, **kwargs):  # noqa
    """This action will return either an array of values, or the average value and maximum
    offset, for a specied per-particle attribute of a particle object or component.

    getParticleAttr( selectionItem , [array=boolean], [attribute=string], [object=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getParticleAttr.html
    """
    return _wrapCommand(cmds.getParticleAttr, args, kwargs)


def getRenderDependencies(*args, **kwargs):  # noqa
    """Command to return dependencies of an image source.

    getRenderDependencies(string)

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getRenderDependencies.html
    """
    return _wrapCommand(cmds.getRenderDependencies, args, kwargs)


def getRenderTasks(*args, **kwargs):  # noqa
    """Command to return render tasks to render an image source.

    getRenderTasks(string, [camera=string], [renderLayer=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/getRenderTasks.html
    """
    return _wrapCommand(cmds.getRenderTasks, args, kwargs)


def ghosting(*args, **kwargs):  # noqa
    """Provides an aggregated interface to all of the node-base ghosting parameters, as well as
    the global preferences used by this command for ghosting actions.

    ghosting([action=string], [allGhostedObjects=boolean], [allInRange=boolean],
    [customFrames=int], [enable=boolean], [farOpacity=float], [frames=boolean],
    [geometryFilter=boolean], [ghostedObjects=boolean], [ghostsStep=int],
    [hierarchy=boolean], [jointFilter=boolean], [locatorFilter=boolean], [mode=string],
    [nearOpacity=float], [postColor=[float, float, float]], [postFrames=int],
    [preColor=[float, float, float]], [preFrames=int], [preset=string],
    [resetAll=boolean], [useDriver=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ghosting.html
    """
    return _wrapCommand(cmds.ghosting, args, kwargs)


def globalStitch(*args, **kwargs):  # noqa
    """This command computes a globalStitch of NURBS surfaces.

    globalStitch( surface surface... , [caching=boolean], [constructionHistory=boolean],
    [lockSurface=boolean], [maxSeparation=linear], [modificationResistance=float],
    [name=string], [nodeState=int], [object=boolean], [sampling=int], [stitchCorners=int],
    [stitchEdges=int], [stitchPartialEdges=boolean], [stitchSmoothness=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/globalStitch.html
    """
    return _wrapCommand(cmds.globalStitch, args, kwargs)


def glRender(*args, **kwargs):  # noqa
    """This command provides access to the Hardware Render Manager (HRM).

    glRender([accumBufferPasses=int], [alphaSource=string], [antiAliasMethod=string],
    [cameraIcons=boolean], [clearClr=[float, float, float]], [collisionIcons=boolean],
    [crossingEffect=boolean], [currentFrame=boolean], [drawStyle=string],
    [edgeSmoothness=float], [emitterIcons=boolean], [fieldIcons=boolean],
    [flipbookCallback=string], [frameEnd=int], [frameIncrement=int], [frameStart=int],
    [fullResolution=boolean], [grid=boolean], [imageDirectory=string], [imageName=string],
    [imageSize=[int, int, float]], [lightIcons=boolean], [lightingMode=string],
    [lineSmoothing=boolean], [offScreen=boolean], [renderFrame=string],
    [renderSequence=string], [sharpness=float], [shutterAngle=float],
    [textureDisplay=boolean], [transformIcons=boolean], [useAccumBuffer=boolean],
    [viewport=[int, int, float]], [writeDepthMap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/glRender.html
    """
    return _wrapCommand(cmds.glRender, args, kwargs)


def glRenderEditor(*args, **kwargs):  # noqa
    """Create a glRender view.

    glRenderEditor( name , [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean], [lookThru=string],
    [mainListConnection=string], [panel=string], [parent=string],
    [selectionConnection=string], [stateString=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string],
    [viewCameraName=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/glRenderEditor.html
    """
    return _wrapCommand(cmds.glRenderEditor, args, kwargs)


def goal(*args, **kwargs):  # noqa
    """Specifies the given objects as being goals for the given particle object.

    goal( selectionList , [goal=string], [index=boolean], [useTransformAsGoal=boolean],
    [weight=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/goal.html
    """
    return _wrapCommand(cmds.goal, args, kwargs)


def grabColor(*args, **kwargs):  # noqa
    """This command changes the cursor and enters a modal state which will be exited by pressing
    a mouse button.

    grabColor([alpha=boolean], [hsvValue=boolean], [rgbValue=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/grabColor.html
    """
    return _wrapCommand(cmds.grabColor, args, kwargs)


def gradientControl(*args, **kwargs):  # noqa
    """This command creates a control that displays the gradient attribute specified.

    gradientControl( [string] , [adaptiveScaling=boolean], [annotation=string],
    [attribute=name], [backgroundColor=[float, float, float]], [clearAttribute=boolean],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfControls=uint], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [refreshOnRelease=uint], [selectedColorControl=string],
    [selectedInterpControl=string], [selectedPositionControl=string],
    [staticNumberOfControls=boolean], [staticPositions=boolean],
    [statusBarMessage=string], [upperLimitControl=string], [useTemplate=string],
    [verticalLayout=boolean], [visible=boolean], [visibleChangeCommand=script],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/gradientControl.html
    """
    return _wrapCommand(cmds.gradientControl, args, kwargs)


def gradientControlNoAttr(*args, **kwargs):  # noqa
    """This command creates a control for editing a ramp (2D control curve).

    gradientControlNoAttr( [string] , [annotation=string], [asString=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [currentKey=int],
    [currentKeyChanged=script], [currentKeyColorValue=[float, float, float]],
    [currentKeyCurveValue=boolean], [currentKeyInterpValue=int], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [optionVar=string], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [rampAsColor=boolean],
    [statusBarMessage=string], [useTemplate=string], [valueAtPoint=float],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/gradientControlNoAttr.html
    """
    return _wrapCommand(cmds.gradientControlNoAttr, args, kwargs)


def graphDollyCtx(*args, **kwargs):  # noqa
    """This command can be used to create a dolly context for the graph editor.

    graphDollyCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/graphDollyCtx.html
    """
    return _wrapCommand(cmds.graphDollyCtx, args, kwargs)


def graphSelectContext(*args, **kwargs):  # noqa
    """This command can be used to create a selection context for the hypergraph editor.

    graphSelectContext([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/graphSelectContext.html
    """
    return _wrapCommand(cmds.graphSelectContext, args, kwargs)


def graphTrackCtx(*args, **kwargs):  # noqa
    """This command can be used to create a track context for the graph editor.

    graphTrackCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/graphTrackCtx.html
    """
    return _wrapCommand(cmds.graphTrackCtx, args, kwargs)


def gravity(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    gravity( [objects] , [attenuation=float], [directionX=float], [directionY=float],
    [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string],
    [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]],
    [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/gravity.html
    """
    return _wrapCommand(cmds.gravity, args, kwargs)


def grid(*args, **kwargs):  # noqa
    """This command changes the size and spacing of lines on the ground plane displayed in the
    perspective and orthographic views.

    grid([default=boolean], [displayAxes=boolean], [displayAxesBold=boolean],
    [displayDivisionLines=boolean], [displayGridLines=boolean],
    [displayOrthographicLabels=boolean], [displayPerspectiveLabels=boolean],
    [divisions=uint], [orthographicLabelPosition=string],
    [perspectiveLabelPosition=string], [reset=boolean], [size=linear], [spacing=linear],
    [style=uint], [toggle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/grid.html
    """
    return _wrapCommand(cmds.grid, args, kwargs)


def gridLayout(*args, **kwargs):  # noqa
    """This layout arranges children in a grid fashion where every cell in the grid is the same
    size.

    gridLayout( [string] , [allowEmptyCells=boolean], [annotation=string], [autoGrow=boolean],
    [backgroundColor=[float, float, float]], [cellHeight=int], [cellWidth=int],
    [cellWidthHeight=[int, int]], [childArray=boolean], [columnsResizable=boolean],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean],
    [gridOrder=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfColumns=int], [numberOfPopupMenus=boolean],
    [numberOfRows=int], [numberOfRowsColumns=[int, int]], [parent=string],
    [popupMenuArray=boolean], [position=[string, int]], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/gridLayout.html
    """
    return _wrapCommand(cmds.gridLayout, args, kwargs)


def group(*args, **kwargs):  # noqa
    """This command groups the specified objects under a new group and returns the name of the
    new group.

    group( [objects...] , [absolute=boolean], [empty=boolean], [name=string], [parent=string],
    [relative=boolean], [useAsGroup=string], [world=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/group.html
    """
    return _wrapCommand(cmds.group, args, kwargs)


def hardenPointCurve(*args, **kwargs):  # noqa
    """The hardenPointCurve command changes the knots of a curve given a list of control point
    indices so that the knot corresponding to that control point gets the specified
    multiplicity.

    hardenPointCurve( curve , [caching=boolean], [constructionHistory=boolean],
    [multiplicity=int], [name=string], [nodeState=int], [object=boolean],
    [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hardenPointCurve.html
    """
    return _wrapCommand(cmds.hardenPointCurve, args, kwargs)


def hardware(*args, **kwargs):  # noqa
    """Return description of the hardware available in the machine.

    hardware([brdType=boolean], [cpuType=boolean], [graphicsType=boolean],
    [megaHertz=boolean], [numProcessors=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hardware.html
    """
    return _wrapCommand(cmds.hardware, args, kwargs)


def hardwareRenderPanel(*args, **kwargs):  # noqa
    """This command creates, edit and queries hardware render panels which contain only a
    hardware render editor.

    hardwareRenderPanel( panelName , [camera=string], [control=boolean], [copy=string],
    [createString=boolean], [defineTemplate=string], [docTag=string],
    [editString=boolean], [exists=boolean], [glRenderEditor=boolean], [init=boolean],
    [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean],
    [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hardwareRenderPanel.html
    """
    return _wrapCommand(cmds.hardwareRenderPanel, args, kwargs)


def hasMetadata(*args, **kwargs):  # noqa
    """This command is used to query for the presence of metadata elements on a node, components,
    or scene.

    hasMetadata([asList=boolean], [channelName=string], [channelType=string],
    [endIndex=string], [ignoreDefault=boolean], [index=string], [indexType=string],
    [memberName=string], [scene=boolean], [startIndex=string], [streamName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hasMetadata.html
    """
    return _wrapCommand(cmds.hasMetadata, args, kwargs)


def headsUpDisplay(*args, **kwargs):  # noqa
    """This command creates a Heads-up Display (HUD) object which is placed in a 2D inactive
    overlay plane on the 3D viewport.

    headsUpDisplay([string], [allDescendants=boolean], [allowOverlap=boolean],
    [attachToRefresh=boolean], [attributeChange=string], [block=int],
    [blockAlignment=string], [blockSize=string], [command=script],
    [conditionChange=string], [conditionFalse=string], [conditionTrue=string],
    [connectionChange=string], [dataAlignment=string], [dataFontSize=string],
    [dataWidth=int], [decimalPrecision=int], [disregardIndex=boolean], [event=string],
    [exists=boolean], [getOption=string], [gridColor=int], [label=string],
    [labelFontSize=string], [labelWidth=int], [lastOccupiedBlock=int],
    [layoutVisibility=boolean], [listConditions=boolean], [listEvents=boolean],
    [listHeadsUpDisplays=boolean], [listNodeChanges=boolean], [listPresets=boolean],
    [name=string], [nextFreeBlock=int], [nodeChanges=string], [padding=int],
    [preset=string], [refresh=boolean], [remove=boolean], [removeID=int],
    [removePosition=[int, int]], [resetNodeChanges=string], [scriptResult=boolean],
    [section=int], [setOption=[string, string]], [showGrid=boolean], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/headsUpDisplay.html
    """
    return _wrapCommand(cmds.headsUpDisplay, args, kwargs)


def headsUpMessage(*args, **kwargs):  # noqa
    """This command draws a message in the 3d view.

    headsUpMessage( [message string] , [horizontalOffset=int], [object=string],
    [selection=boolean], [time=float], [uvTextureEditor=boolean], [verticalOffset=int],
    [viewport=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/headsUpMessage.html
    """
    return _wrapCommand(cmds.headsUpMessage, args, kwargs)


def help(*args, **kwargs):  # noqa
    """With no arguments, help tells how to use help.

    help( [string] , [documentation=boolean], [language=string], [list=boolean],
    [popupDisplayTime=uint], [popupMode=boolean], [popupPauseTime=uint],
    [popupSimpleMode=boolean], [rolloverMode=boolean], [syntaxOnly=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/help.html
    """
    return _wrapCommand(cmds.help, args, kwargs)


def helpLine(*args, **kwargs):  # noqa
    """This command creates a help line where tool help/hints are shown.

    helpLine( [name] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/helpLine.html
    """
    return _wrapCommand(cmds.helpLine, args, kwargs)


def hide(*args, **kwargs):  # noqa
    """The `hide` command is used to make objects invisible.

    hide( [objects] , [allObjects=boolean], [clearLastHidden=boolean],
    [clearSelection=boolean], [invertComponents=boolean], [returnHidden=boolean],
    [testVisibility=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hide.html
    """
    return _wrapCommand(cmds.hide, args, kwargs)


def hikGlobals(*args, **kwargs):  # noqa
    """Sets global HumanIK flags for the application.

    hikGlobals([releaseAllPinning=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hikGlobals.html
    """
    return _wrapCommand(cmds.hikGlobals, args, kwargs)


def hilite(*args, **kwargs):  # noqa
    """Hilites/Unhilites the specified object(s).

    hilite( [objects] , [replace=boolean], [toggle=boolean], [unHilite=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hilite.html
    """
    return _wrapCommand(cmds.hilite, args, kwargs)


def hitTest(*args, **kwargs):  # noqa
    """The `hitTest` command hit-tests a point in the named control and returns a list of items
    underneath the point.

    hitTest(stringintint)

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hitTest.html
    """
    return _wrapCommand(cmds.hitTest, args, kwargs)


def hotBox(*args, **kwargs):  # noqa
    """This command controls parameters related to the hotBox menubar palette.

    hotBox([PaneOnlyMenus=boolean], [PaneToggleMenus=boolean], [animationOnlyMenus=boolean],
    [animationToggleMenus=boolean], [clothOnlyMenus=boolean], [clothToggleMenus=boolean],
    [commonOnlyMenus=boolean], [commonToggleMenus=boolean],
    [customMenuSetsToggleMenus=boolean], [displayCenterOnly=boolean],
    [displayHotbox=boolean], [displayStyle=boolean], [displayZonesOnly=boolean],
    [dynamicsOnlyMenus=boolean], [dynamicsToggleMenus=boolean], [liveOnlyMenus=boolean],
    [liveToggleMenus=boolean], [menuSetOnly=string], [menuSetToggle=[string, boolean]],
    [modelingOnlyMenus=boolean], [modelingToggleMenus=boolean], [noClickCommand=script],
    [noClickDelay=float], [noClickPosition=boolean], [noKeyPress=boolean],
    [polygonsOnlyMenus=boolean], [polygonsToggleMenus=boolean], [position=[uint, uint]],
    [release=boolean], [renderingOnlyMenus=boolean], [renderingToggleMenus=boolean],
    [riggingOnlyMenus=boolean], [riggingToggleMenus=boolean], [rmbPopups=boolean],
    [showAllToggleMenus=boolean], [surfacesOnlyMenus=boolean],
    [surfacesToggleMenus=boolean], [transparenyLevel=int], [updateMenus=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotBox.html
    """
    return _wrapCommand(cmds.hotBox, args, kwargs)


def hotkey(*args, **kwargs):  # noqa
    """This command sets the single-key hotkeys for the entire application.

    hotkey([altModifier=boolean], [autoSave=boolean], [commandModifier=boolean],
    [ctrlModifier=boolean], [ctxClient=string], [dragPress=boolean],
    [factorySettings=boolean], [isModifier=boolean], [keyShortcut=string], [name=string],
    [pressCommandRepeat=boolean], [releaseCommandRepeat=boolean], [releaseName=string],
    [shiftModifier=boolean], [sourceUserHotkeys=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotkey.html
    """
    return _wrapCommand(cmds.hotkey, args, kwargs)


def hotkeyCheck(*args, **kwargs):  # noqa
    """This command checks if the given hotkey is mapped to a nameCommand object.

    hotkeyCheck([altModifier=boolean], [commandModifier=boolean], [ctrlModifier=boolean],
    [isRepeatable=boolean], [keyString=string], [keyUp=boolean], [optionModifier=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotkeyCheck.html
    """
    return _wrapCommand(cmds.hotkeyCheck, args, kwargs)


def hotkeyCtx(*args, **kwargs):  # noqa
    """This command sets the hotkey context for the entire application.

    hotkeyCtx([addClient=string], [clientArray=boolean], [currentClient=string],
    [insertTypeAt=[string, string]], [removeAllClients=boolean], [removeClient=string],
    [removeType=string], [type=string], [typeArray=boolean], [typeExists=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotkeyCtx.html
    """
    return _wrapCommand(cmds.hotkeyCtx, args, kwargs)


def hotkeyEditorPanel(*args, **kwargs):  # noqa
    """A hotkeyEditor creates a new hotkey editor in the current layout.

    hotkeyEditorPanel( [name] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotkeyEditorPanel.html
    """
    return _wrapCommand(cmds.hotkeyEditorPanel, args, kwargs)


def hotkeySet(*args, **kwargs):  # noqa
    """Manages hotkey sets in Maya.

    hotkeySet( [name] , [current=boolean], [delete=boolean], [exists=boolean],
    [export=string], [hotkeySetArray=boolean], [ip=string], [rename=string],
    [source=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hotkeySet.html
    """
    return _wrapCommand(cmds.hotkeySet, args, kwargs)


def hudButton(*args, **kwargs):  # noqa
    """This command creates a Heads-up Display (HUD) button control which is placed in a 2D
    inactive overlay plane on the 3D viewport.

    hudButton([string], [allowOverlap=boolean], [block=int], [blockAlignment=string],
    [blockSize=string], [buttonShape=string], [buttonWidth=int], [label=string],
    [labelFontSize=string], [padding=int], [pressCommand=script], [releaseCommand=script],
    [section=int], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hudButton.html
    """
    return _wrapCommand(cmds.hudButton, args, kwargs)


def hudSlider(*args, **kwargs):  # noqa
    """This command creates a Heads-up Display (HUD) slider control which is placed in a 2D
    inactive overlay plane on the 3D viewport.

    hudSlider([string], [allowOverlap=boolean], [block=int], [blockAlignment=string],
    [blockSize=string], [decimalPrecision=int], [dragCommand=script],
    [internalPadding=int], [label=string], [labelFontSize=string], [labelWidth=int],
    [maxValue=float], [minValue=float], [padding=int], [pressCommand=script],
    [releaseCommand=script], [section=int], [sliderIncrement=float], [sliderLength=int],
    [type=string], [value=float], [valueAlignment=string], [valueFontSize=string],
    [valueWidth=int], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hudSlider.html
    """
    return _wrapCommand(cmds.hudSlider, args, kwargs)


def hudSliderButton(*args, **kwargs):  # noqa
    """This command creates a Heads-up Display (HUD) slider button control which is placed in a
    2D inactive overlay plane on the 3D viewport.

    hudSliderButton([string], [allowOverlap=boolean], [block=int], [blockAlignment=string],
    [blockSize=string], [buttonLabel=string], [buttonLabelFontSize=string],
    [buttonPressCommand=script], [buttonReleaseCommand=script], [buttonShape=string],
    [buttonWidth=int], [decimalPrecision=int], [internalPadding=int], [maxValue=float],
    [minValue=float], [padding=int], [section=int], [sliderDragCommand=script],
    [sliderIncrement=float], [sliderLabel=string], [sliderLabelFontSize=string],
    [sliderLabelWidth=int], [sliderLength=int], [sliderPressCommand=script],
    [sliderReleaseCommand=script], [type=string], [value=float], [valueAlignment=string],
    [valueFontSize=string], [valueWidth=int], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hudSliderButton.html
    """
    return _wrapCommand(cmds.hudSliderButton, args, kwargs)


def hwReflectionMap(*args, **kwargs):  # noqa
    """This command creates a hwReflectionMap node for having reflection on textured surfaces
    that currently have their boolean attribute displayHWEnvironment set to true.

    hwReflectionMap([backTextureName=string], [bottomTextureName=string], [cubeMap=boolean],
    [decalMode=boolean], [enable=boolean], [frontTextureName=string],
    [leftTextureName=string], [rightTextureName=string], [sphereMapTextureName=string],
    [topTextureName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hwReflectionMap.html
    """
    return _wrapCommand(cmds.hwReflectionMap, args, kwargs)


def hwRender(*args, **kwargs):  # noqa
    """Renders an image or a sequence using the hardware rendering engine.

    hwRender([acceleratedMultiSampleSupport=boolean], [activeTextureCount=boolean],
    [camera=string], [currentFrame=boolean], [currentView=boolean],
    [edgeAntiAliasing=[uint, uint]], [fixFileNameNumberPattern=boolean], [frame=float],
    [fullRenderSupport=boolean], [height=uint], [imageFileName=boolean], [layer=name],
    [limitedRenderSupport=boolean], [lowQualityLighting=boolean], [noRenderView=boolean],
    [notWriteToFile=boolean], [printGeometry=boolean], [renderHardwareName=boolean],
    [renderRegion=[uint, uint, uint, uint]], [renderSelected=boolean],
    [textureResolution=uint], [width=uint], [writeAlpha=boolean], [writeDepth=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hwRender.html
    """
    return _wrapCommand(cmds.hwRender, args, kwargs)


def hwRenderLoad(*args, **kwargs):  # noqa
    """Empty command used to force the dynamic load of HR render.

    hwRenderLoad()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hwRenderLoad.html
    """
    return _wrapCommand(cmds.hwRenderLoad, args, kwargs)


def hyperGraph(*args, **kwargs):  # noqa
    """The following is an overview of the basic features of the hypergraph.

    hyperGraph( [string] , [addBookmark=boolean], [addDependGraph=name], [addDependNode=name],
    [animateTransition=boolean], [attributeEditor=string], [backward=boolean],
    [bookmarkName=boolean], [breakConnectionCommand=string], [clear=boolean],
    [collapseContainer=boolean], [connectionDrawStyle=string], [control=boolean],
    [currentEdge=string], [currentNode=string], [debug=string], [defineTemplate=string],
    [deleteBookmark=string], [dependGraph=boolean], [dependNode=string],
    [directoryPressCommand=string], [docTag=string], [down=boolean], [downstream=boolean],
    [dragAndDropBehaviorCommand=string], [dropNode=string], [dropTargetNode=string],
    [edgeDblClickCommand=string], [edgeDimmedDblClickCommand=string],
    [edgeDropCommand=string], [edgePressCommand=string], [edgeReleaseCommand=string],
    [enableAutomaticLayout=boolean], [exists=boolean], [expandContainer=boolean],
    [feedbackGadget=string], [feedbackNode=string], [filter=string],
    [filterDetail=[string, boolean]], [fitImageToHeight=boolean],
    [fitImageToWidth=boolean], [focusCommand=string], [fold=boolean],
    [forceMainConnection=string], [forceRefresh=boolean], [forward=boolean],
    [frame=boolean], [frameBranch=boolean], [frameGraph=boolean],
    [frameGraphNoRebuild=boolean], [frameHierarchy=boolean], [freeform=boolean],
    [fromAttr=string], [fromNode=string], [getNodeList=boolean], [getNodePosition=string],
    [graphDescription=boolean], [graphLayoutStyle=string], [graphType=string],
    [heatMapDisplay=boolean], [highlightConnection=string], [iconSize=string],
    [image=string], [imageEnabled=boolean], [imageForContainer=boolean],
    [imagePosition=[float, float]], [imageScale=float], [initializeScript=string],
    [isHotkeyTarget=boolean], [layout=boolean], [layoutSelected=string],
    [limitGraphTraversal=int], [lockMainConnection=boolean], [look=[float, float]],
    [mainListConnection=string], [mergeConnections=boolean], [navigateHome=boolean],
    [navup=boolean], [newInputConnection=string], [newOutputConnection=string],
    [nextView=boolean], [nodeConnectCommand=string], [nodeDblClickCommand=string],
    [nodeDropCommand=string], [nodeMenuCommand=string], [nodePressCommand=string],
    [nodeReleaseCommand=string], [opaqueContainers=boolean], [orientation=string],
    [panView=[float, float]], [panel=string], [parent=string], [popupMenuScript=string],
    [previousView=boolean], [range=[float, float]], [rebuild=boolean],
    [removeNode=string], [rename=boolean], [resetFreeform=boolean],
    [restoreBookmark=string], [scrollUpDownNoZoom=boolean], [selectionConnection=string],
    [setNodePosition=[string, float, float]], [showCachedConnections=boolean],
    [showConnectionFromSelected=boolean], [showConnectionToSelected=boolean],
    [showConstraintLabels=boolean], [showConstraints=boolean], [showDeformers=boolean],
    [showExpressions=boolean], [showInvisible=boolean], [showRelationships=boolean],
    [showShapes=boolean], [showUnderworld=boolean], [stateString=boolean],
    [toAttr=string], [toNode=string], [transitionFrames=int], [unParent=boolean],
    [unfold=boolean], [unfoldAll=boolean], [unfoldAllShapes=boolean],
    [unfoldHidden=boolean], [unlockMainConnection=boolean],
    [updateMainConnection=boolean], [updateNodeAdded=boolean], [updateSelection=boolean],
    [upstream=boolean], [useDrawOverrideColor=boolean], [useFeedbackList=boolean],
    [useTemplate=string], [viewOption=string], [visibility=boolean], [zoom=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hyperGraph.html
    """
    return _wrapCommand(cmds.hyperGraph, args, kwargs)


def hyperPanel(*args, **kwargs):  # noqa
    """This command creates, edit and queries hypergraph panels which contain only a hypergraph
    editor.

    hyperPanel( [panelName] , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [hyperEditor=boolean], [init=boolean], [isUnique=boolean], [label=string],
    [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean],
    [parent=string], [popupMenuProcedure=script], [replacePanel=string],
    [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hyperPanel.html
    """
    return _wrapCommand(cmds.hyperPanel, args, kwargs)


def hyperShade(*args, **kwargs):  # noqa
    """Commands for shader editing in the hypergraph.

    hyperShade([assign=string], [clearWorkArea=boolean], [collapse=string],
    [createNode=string], [dependGraphArea=boolean], [downStream=boolean],
    [duplicate=boolean], [fixRenderSize=boolean], [incremental=boolean],
    [listDownstreamNodes=name], [listDownstreamShaderNodes=name],
    [listUpstreamNodes=name], [name=string], [networks=boolean], [noSGShapes=boolean],
    [noShapes=boolean], [noTransforms=boolean], [objects=string],
    [renderCreateAndDrop=string], [reset=boolean], [resetGraph=boolean],
    [resetSwatch=boolean], [setAllowsRegraphing=boolean], [setWorkArea=string],
    [shaderNetwork=string], [shaderNetworks=boolean],
    [shaderNetworksSelectMaterialNodes=boolean], [snapShot=boolean], [uncollapse=string],
    [upStream=boolean], [userDefinedLayout=boolean], [workAreaAddCmd=string],
    [workAreaDeleteCmd=string], [workAreaSelectCmd=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/hyperShade.html
    """
    return _wrapCommand(cmds.hyperShade, args, kwargs)


def iconTextButton(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    iconTextButton( [string] , [align=string], [annotation=string], [backgroundColor=[float,
    float, float]], [command=script], [commandRepeatable=boolean],
    [defineTemplate=string], [disabledImage=string], [docTag=string],
    [doubleClickCommand=script], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string],
    [fullPathName=boolean], [handleNodeDropCallback=script], [height=int],
    [highlightColor=[float, float, float]], [highlightImage=string], [image=string],
    [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string],
    [isObscured=boolean], [label=string], [labelEditingCallback=script],
    [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float,
    float, float, float]], [overlayLabelColor=[float, float, float]], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [rotation=float],
    [scaleIcon=boolean], [selectionImage=string], [sourceType=string],
    [statusBarMessage=string], [style=string], [useAlpha=boolean], [useTemplate=string],
    [version=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextButton.html
    """
    return _wrapCommand(cmds.iconTextButton, args, kwargs)


def iconTextCheckBox(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    iconTextCheckBox( [string] , [align=string], [annotation=string], [backgroundColor=[float,
    float, float]], [changeCommand=script], [defineTemplate=string],
    [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [highlightImage=string], [image=string], [image1=string], [image2=string],
    [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string],
    [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script],
    [onCommand=script], [overlayLabelBackColor=[float, float, float, float]],
    [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rotation=float], [selectionHighlightImage=string],
    [selectionImage=string], [statusBarMessage=string], [style=string],
    [useAlpha=boolean], [useTemplate=string], [value=boolean], [version=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextCheckBox.html
    """
    return _wrapCommand(cmds.iconTextCheckBox, args, kwargs)


def iconTextRadioButton(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    iconTextRadioButton( string , [align=string], [annotation=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [collection=string],
    [defineTemplate=string], [disabledImage=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [flat=boolean], [flipX=boolean], [flipY=boolean], [font=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [highlightImage=string], [image=string], [image1=string], [image2=string],
    [image3=string], [imageOverlayLabel=string], [isObscured=boolean], [label=string],
    [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [offCommand=script],
    [onCommand=script], [overlayLabelBackColor=[float, float, float, float]],
    [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rotation=float], [select=boolean],
    [selectionHighlightImage=string], [selectionImage=string], [statusBarMessage=string],
    [style=string], [useAlpha=boolean], [useTemplate=string], [version=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextRadioButton.html
    """
    return _wrapCommand(cmds.iconTextRadioButton, args, kwargs)


def iconTextRadioCollection(*args, **kwargs):  # noqa
    """This command creates a cluster for iconTextRadioButtons.

    iconTextRadioCollection( [string] , [collectionItemArray=boolean],
    [defineTemplate=string], [disableCommands=boolean], [exists=boolean], [gl=boolean],
    [numberOfCollectionItems=boolean], [parent=string], [select=string],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextRadioCollection.html
    """
    return _wrapCommand(cmds.iconTextRadioCollection, args, kwargs)


def iconTextScrollList(*args, **kwargs):  # noqa
    """This command creates/edits/queries a text scrolling list.

    iconTextScrollList( [string] , [allowMultiSelection=boolean], [annotation=string],
    [append=string], [backgroundColor=[float, float, float]], [changeCommand=script],
    [defineTemplate=string], [deselectAll=boolean], [docTag=string],
    [doubleClickCommand=script], [dragCallback=script], [dragFeedbackVisible=boolean],
    [dropCallback=script], [dropRectCallback=script], [editIndexed=uint],
    [editable=boolean], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [itemAt=[int, int]],
    [itemTextColor=[int, float, float, float]], [manage=boolean], [noBackground=boolean],
    [numberOfIcons=uint], [numberOfPopupMenus=boolean], [numberOfRows=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [removeAll=boolean], [selectCommand=script], [selectIndexedItem=int],
    [selectItem=string], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [visualRectAt=[int, int]],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextScrollList.html
    """
    return _wrapCommand(cmds.iconTextScrollList, args, kwargs)


def iconTextStaticLabel(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    iconTextStaticLabel( string , [align=string], [annotation=string],
    [backgroundColor=[float, float, float]], [defineTemplate=string],
    [disabledImage=string], [docTag=string], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [flipX=boolean], [flipY=boolean], [font=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [image=string], [image1=string], [image2=string], [image3=string],
    [imageOverlayLabel=string], [isObscured=boolean], [label=string], [labelOffset=int],
    [manage=boolean], [marginHeight=uint], [marginWidth=uint], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]],
    [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rotation=float], [statusBarMessage=string],
    [style=string], [useAlpha=boolean], [useTemplate=string], [version=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iconTextStaticLabel.html
    """
    return _wrapCommand(cmds.iconTextStaticLabel, args, kwargs)


def ikfkDisplayMethod(*args, **kwargs):  # noqa
    """The `ikfkDisplayMethod` command is used to specify how ik/fk blending should be shown.

    ikfkDisplayMethod([display=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikfkDisplayMethod.html
    """
    return _wrapCommand(cmds.ikfkDisplayMethod, args, kwargs)


def ikHandle(*args, **kwargs):  # noqa
    """The handle command is used to create, edit, and query a handle within Maya.

    ikHandle( object , [autoPriority=boolean], [connectEffector=boolean],
    [createCurve=boolean], [createRootAxis=boolean], [curve=name],
    [disableHandles=boolean], [enableHandles=boolean], [endEffector=string],
    [exists=string], [forceSolver=boolean], [freezeJoints=boolean], [jointList=boolean],
    [name=string], [numSpans=int], [parentCurve=boolean], [positionWeight=float],
    [priority=int], [rootOnCurve=boolean], [rootTwistMode=boolean],
    [setupForRPsolver=boolean], [simplifyCurve=boolean], [snapCurve=boolean],
    [snapHandleFlagToggle=boolean], [snapHandleToEffector=boolean], [solver=string],
    [startJoint=string], [sticky=string], [twistType=string], [weight=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikHandle.html
    """
    return _wrapCommand(cmds.ikHandle, args, kwargs)


def ikHandleCtx(*args, **kwargs):  # noqa
    """The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool.

    ikHandleCtx( object , [autoPriorityH=boolean], [createCurve=boolean],
    [createRootAxis=boolean], [exists=boolean], [forceSolverH=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [numSpans=int],
    [parentCurve=boolean], [poWeightH=float], [priorityH=int], [rootOnCurve=boolean],
    [rootTwistMode=boolean], [simplifyCurve=boolean], [snapCurve=boolean],
    [snapHandleH=boolean], [solverTypeH=string], [stickyH=string], [twistType=string],
    [weightH=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikHandleCtx.html
    """
    return _wrapCommand(cmds.ikHandleCtx, args, kwargs)


def ikHandleDisplayScale(*args, **kwargs):  # noqa
    """This action modifies and queries the current display size of ikHandle.

    ikHandleDisplayScale( float )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikHandleDisplayScale.html
    """
    return _wrapCommand(cmds.ikHandleDisplayScale, args, kwargs)


def ikSolver(*args, **kwargs):  # noqa
    """The ikSolver command is used to set the attributes for an IK Solver or create a new one.

    ikSolver( [object] , [epsilon=float], [maxIterations=int], [name=string],
    [solverType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikSolver.html
    """
    return _wrapCommand(cmds.ikSolver, args, kwargs)


def ikSplineHandleCtx(*args, **kwargs):  # noqa
    """The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool.

    ikSplineHandleCtx( object , [autoPriorityH=boolean], [createCurve=boolean],
    [createRootAxis=boolean], [exists=boolean], [forceSolverH=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [numSpans=int],
    [parentCurve=boolean], [poWeightH=float], [priorityH=int], [rootOnCurve=boolean],
    [rootTwistMode=boolean], [simplifyCurve=boolean], [snapCurve=boolean],
    [snapHandleH=boolean], [solverTypeH=string], [stickyH=string], [twistType=string],
    [weightH=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikSplineHandleCtx.html
    """
    return _wrapCommand(cmds.ikSplineHandleCtx, args, kwargs)


def ikSystem(*args, **kwargs):  # noqa
    """The ikSystem command is used to set the global snapping flag for handles and set the
    global solve flag for solvers.

    ikSystem( [object] , [allowRotation=boolean], [autoPriority=boolean],
    [autoPriorityMC=boolean], [autoPrioritySC=boolean], [list=[int, int]], [snap=boolean],
    [solve=boolean], [solverTypes=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikSystem.html
    """
    return _wrapCommand(cmds.ikSystem, args, kwargs)


def ikSystemInfo(*args, **kwargs):  # noqa
    """This action modifies and queries the current ikSystem controls.

    ikSystemInfo( boolean , [globalSnapHandle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ikSystemInfo.html
    """
    return _wrapCommand(cmds.ikSystemInfo, args, kwargs)


def illustratorCurves(*args, **kwargs):  # noqa
    """The illustratorCurves command creates NURBS curves from an input Adobe(R) Illustrator(R)
    file.

    illustratorCurves( [string] , [caching=boolean], [constructionHistory=boolean],
    [illustratorFilename=string], [nodeState=int], [object=boolean], [tolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/illustratorCurves.html
    """
    return _wrapCommand(cmds.illustratorCurves, args, kwargs)


def image(*args, **kwargs):  # noqa
    """This command creates a static image for non-xpm files.

    image( [imageName] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [isObscured=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/image.html
    """
    return _wrapCommand(cmds.image, args, kwargs)


def imagePlane(*args, **kwargs):  # noqa
    """The imagePlane command allows querying of various properties of an image plane and any
    movie in use by the image plane.

    imagePlane([camera=string], [counter=boolean], [detach=boolean], [dropFrame=boolean],
    [fileName=string], [frameDuration=int], [height=float], [imageSize=[int, int]],
    [lookThrough=string], [maintainRatio=boolean], [name=string], [negTimesOK=boolean],
    [numFrames=int], [quickTime=boolean], [showInAllViews=boolean], [timeCode=int],
    [timeCodeTrack=boolean], [timeScale=int], [twentyFourHourMax=boolean], [width=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/imagePlane.html
    """
    return _wrapCommand(cmds.imagePlane, args, kwargs)


def imfPlugins(*args, **kwargs):  # noqa
    """This command queries all the available imf plugins for its name, keyword or image file
    extension.

    imfPlugins([string], [extension=string], [keyword=string], [multiFrameSupport=string],
    [pluginName=string], [readSupport=string], [writeSupport=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/imfPlugins.html
    """
    return _wrapCommand(cmds.imfPlugins, args, kwargs)


def inheritTransform(*args, **kwargs):  # noqa
    """This command toggles the inherit state of an object.

    inheritTransform( [objects...] , [off=boolean], [on=boolean], [preserve=boolean],
    [toggle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/inheritTransform.html
    """
    return _wrapCommand(cmds.inheritTransform, args, kwargs)


def insertJoint(*args, **kwargs):  # noqa
    """This command will insert a new joint under the given or selected joint.

    insertJoint( [object] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/insertJoint.html
    """
    return _wrapCommand(cmds.insertJoint, args, kwargs)


def insertJointCtx(*args, **kwargs):  # noqa
    """The command will create an insert joint context.

    insertJointCtx([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/insertJointCtx.html
    """
    return _wrapCommand(cmds.insertJointCtx, args, kwargs)


def insertKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to insert keys within the graph editor.

    insertKeyCtx( contextName , [breakdown=boolean], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string],
    [preserveTangent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/insertKeyCtx.html
    """
    return _wrapCommand(cmds.insertKeyCtx, args, kwargs)


def insertKnotCurve(*args, **kwargs):  # noqa
    """The insertKnotCurve command inserts knots into a curve given a list of parameter values.

    insertKnotCurve( curve , [addKnots=boolean], [caching=boolean],
    [constructionHistory=boolean], [curveOnSurface=boolean], [insertBetween=boolean],
    [name=string], [nodeState=int], [numberOfKnots=int], [object=boolean],
    [parameter=float], [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/insertKnotCurve.html
    """
    return _wrapCommand(cmds.insertKnotCurve, args, kwargs)


def insertKnotSurface(*args, **kwargs):  # noqa
    """The insertKnotSurface command inserts knots (aka isoparms) into a surface given a list of
    parameter values.

    insertKnotSurface( surface , [addKnots=boolean], [caching=boolean],
    [constructionHistory=boolean], [direction=int], [insertBetween=boolean],
    [name=string], [nodeState=int], [numberOfKnots=int], [object=boolean],
    [parameter=float], [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/insertKnotSurface.html
    """
    return _wrapCommand(cmds.insertKnotSurface, args, kwargs)


def instance(*args, **kwargs):  # noqa
    """Instancing is a way of making the same object appear twice in the scene.

    instance( [objects] , [leaf=boolean], [name=string], [smartTransform=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/instance.html
    """
    return _wrapCommand(cmds.instance, args, kwargs)


def instanceable(*args, **kwargs):  # noqa
    """Flags one or more DAG nodes so that they can (or cannot) be instanced.

    instanceable([allow=boolean], [recursive=boolean], [shape=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/instanceable.html
    """
    return _wrapCommand(cmds.instanceable, args, kwargs)


def instancer(*args, **kwargs):  # noqa
    """This command is used to create a instancer node and set the proper attributes in the node.

    instancer([addObject=boolean], [cycle=string], [cycleStep=float], [cycleStepUnits=string],
    [index=int], [levelOfDetail=string], [name=string], [object=string],
    [objectPosition=string], [objectRotation=string], [objectScale=string],
    [pointDataSource=boolean], [removeObject=boolean], [rotationOrder=string],
    [rotationUnits=string], [valueName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/instancer.html
    """
    return _wrapCommand(cmds.instancer, args, kwargs)


def internalVar(*args, **kwargs):  # noqa
    """This command returns the values of internal variables.

    internalVar([mayaInstallDir=boolean], [userAppDir=boolean], [userBitmapsDir=boolean],
    [userHotkeyDir=boolean], [userMarkingMenuDir=boolean], [userPrefDir=boolean],
    [userPresetsDir=boolean], [userScriptDir=boolean], [userShelfDir=boolean],
    [userTmpDir=boolean], [userWorkspaceDir=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/internalVar.html
    """
    return _wrapCommand(cmds.internalVar, args, kwargs)


def intersect(*args, **kwargs):  # noqa
    """The intersect command creates a curve on surface where all surfaces intersect with each
    other.

    intersect( [surface] [surface] , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [firstSurface=boolean], [name=string], [nodeState=int],
    [object=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intersect.html
    """
    return _wrapCommand(cmds.intersect, args, kwargs)


def intField(*args, **kwargs):  # noqa
    """Create a field control that accepts only integer values and is bound by a minimum and
    maximum value.

    intField( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [editable=boolean], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [maxValue=int], [minValue=int],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [receiveFocusCommand=script],
    [statusBarMessage=string], [step=int], [useTemplate=string], [value=int],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intField.html
    """
    return _wrapCommand(cmds.intField, args, kwargs)


def intFieldGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    intFieldGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean],
    [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfFields=int],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string],
    [useTemplate=string], [value=[int, int, int, int]], [value1=int], [value2=int],
    [value3=int], [value4=int], [visible=boolean], [visibleChangeCommand=script],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intFieldGrp.html
    """
    return _wrapCommand(cmds.intFieldGrp, args, kwargs)


def intScrollBar(*args, **kwargs):  # noqa
    """Create a scroll bar control that accepts only integer values and is bound by a minimum and
    maximum value.

    intScrollBar( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontal=boolean], [isObscured=boolean], [largeStep=int], [manage=boolean],
    [maxValue=int], [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [step=int], [useTemplate=string], [value=int],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intScrollBar.html
    """
    return _wrapCommand(cmds.intScrollBar, args, kwargs)


def intSlider(*args, **kwargs):  # noqa
    """Create a slider control that accepts only integer values and is bound by a minimum and
    maximum value.

    intSlider( string , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontal=boolean], [isObscured=boolean], [manage=boolean], [maxValue=int],
    [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [step=int], [useTemplate=string], [value=int], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intSlider.html
    """
    return _wrapCommand(cmds.intSlider, args, kwargs)


def intSliderGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    intSliderGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [field=boolean], [fieldMaxValue=int],
    [fieldMinValue=int], [fieldStep=int], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [maxValue=int], [minValue=int], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [sliderStep=int],
    [statusBarMessage=string], [step=int], [useTemplate=string], [value=int],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/intSliderGrp.html
    """
    return _wrapCommand(cmds.intSliderGrp, args, kwargs)


def inViewEditor(*args, **kwargs):  # noqa
    """Mel access to the In-View Editor.

    inViewEditor([visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/inViewEditor.html
    """
    return _wrapCommand(cmds.inViewEditor, args, kwargs)


def inViewMessage(*args, **kwargs):  # noqa
    """Used for displaying in-view messages.

    inViewMessage([alpha=float], [assistMessage=string], [backColor=uint], [clear=string],
    [clickKill=boolean], [dragKill=boolean], [fade=boolean], [fadeInTime=uint],
    [fadeOutTime=uint], [fadeStayTime=uint], [font=string], [fontSize=uint],
    [frameOffset=uint], [hide=boolean], [message=string], [minimize=boolean],
    [position=string], [restore=boolean], [show=boolean], [statusMessage=string],
    [textAlpha=float], [textOffset=uint], [uvEditor=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/inViewMessage.html
    """
    return _wrapCommand(cmds.inViewMessage, args, kwargs)


def iprEngine(*args, **kwargs):  # noqa
    """Command to create or edit an iprEngine.

    iprEngine([copy=string], [defineTemplate=string], [diagnostics=boolean],
    [estimatedMemory=boolean], [exists=boolean], [iprImage=string],
    [motionVectorFile=boolean], [object=name], [region=[int, int, int, int]],
    [relatedFiles=boolean], [releaseIprImage=boolean], [resolution=boolean],
    [scanlineIncrement=string], [showProgressBar=boolean], [startTuning=boolean],
    [stopTuning=boolean], [underPixel=[int, int]], [update=boolean],
    [updateDepthOfField=boolean], [updateLightGlow=boolean], [updateMotionBlur=boolean],
    [updatePort=string], [updateShaderGlow=boolean], [updateShading=boolean],
    [updateShadowMaps=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/iprEngine.html
    """
    return _wrapCommand(cmds.iprEngine, args, kwargs)


def isConnected(*args, **kwargs):  # noqa
    """The `isConnected` command is used to check if two plugs are connected in the dependency
    graph.

    isConnected( string string , [ignoreUnitConversion=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/isConnected.html
    """
    return _wrapCommand(cmds.isConnected, args, kwargs)


def isDirty(*args, **kwargs):  # noqa
    """The `isDirty` command is used to check if a plug is dirty.

    isDirty( string... , [connection=boolean], [datablock=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/isDirty.html
    """
    return _wrapCommand(cmds.isDirty, args, kwargs)


def isolateSelect(*args, **kwargs):  # noqa
    """This command turns on/off isolate select mode in a specified modeling view, specified as
    the argument.

    isolateSelect( string , [addDagObject=name], [addSelected=boolean],
    [addSelectedObjects=boolean], [loadSelected=boolean], [removeDagObject=name],
    [removeSelected=boolean], [state=boolean], [update=boolean], [viewObjects=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/isolateSelect.html
    """
    return _wrapCommand(cmds.isolateSelect, args, kwargs)


def isTrue(*args, **kwargs):  # noqa
    """This commmand returns the state of the named condition.

    isTrue( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/isTrue.html
    """
    return _wrapCommand(cmds.isTrue, args, kwargs)


def itemFilter(*args, **kwargs):  # noqa
    """This command creates a named itemFilter object.

    itemFilter( [string] , [byBin=string], [byName=string], [byScript=string],
    [byType=string], [category=string], [classification=string], [clearByBin=boolean],
    [clearByType=boolean], [difference=[string, string]], [exists=boolean],
    [intersect=[string, string]], [listBuiltInFilters=boolean],
    [listOtherFilters=boolean], [listUserFilters=boolean], [negate=boolean],
    [parent=string], [pythonModule=string], [secondScript=string], [text=string],
    [union=[string, string]], [uniqueNodeNames=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/itemFilter.html
    """
    return _wrapCommand(cmds.itemFilter, args, kwargs)


def itemFilterAttr(*args, **kwargs):  # noqa
    """This command creates a named itemFilterAttr object.

    itemFilterAttr( [string] , [byName=string], [byNameString=string], [byScript=string],
    [classification=string], [dynamic=boolean], [exists=boolean], [hasCurve=boolean],
    [hasDrivenKey=boolean], [hasExpression=boolean], [hidden=boolean], [intersect=[string,
    string]], [keyable=boolean], [listBuiltInFilters=boolean], [listOtherFilters=boolean],
    [listUserFilters=boolean], [negate=boolean], [parent=string], [published=boolean],
    [readable=boolean], [scaleRotateTranslate=boolean], [secondScript=string],
    [text=string], [union=[string, string]], [writable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/itemFilterAttr.html
    """
    return _wrapCommand(cmds.itemFilterAttr, args, kwargs)


def itemFilterType(*args, **kwargs):  # noqa
    """This command queries a named itemFilter object.

    itemFilterType( string , [text=string], [type=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/itemFilterType.html
    """
    return _wrapCommand(cmds.itemFilterType, args, kwargs)


def joint(*args, **kwargs):  # noqa
    """The joint command is used to create, edit, and query, joints within Maya.

    joint( [objects] , [absolute=boolean], [angleX=angle], [angleY=angle], [angleZ=angle],
    [assumePreferredAngles=boolean], [automaticLimits=boolean], [children=boolean],
    [component=boolean], [degreeOfFreedom=string], [exists=string],
    [limitSwitchX=boolean], [limitSwitchY=boolean], [limitSwitchZ=boolean],
    [limitX=[angle, angle]], [limitY=[angle, angle]], [limitZ=[angle, angle]],
    [name=string], [orientJoint=string], [orientation=[angle, angle, angle]],
    [position=[linear, linear, linear]], [radius=float], [relative=boolean],
    [rotationOrder=string], [scale=[float, float, float]], [scaleCompensate=boolean],
    [scaleOrientation=[angle, angle, angle]], [secondaryAxisOrient=string],
    [setPreferredAngles=boolean], [stiffnessX=float], [stiffnessY=float],
    [stiffnessZ=float], [symmetry=boolean], [symmetryAxis=string],
    [zeroScaleOrient=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/joint.html
    """
    return _wrapCommand(cmds.joint, args, kwargs)


def jointCluster(*args, **kwargs):  # noqa
    """The joint cluster command adds high-level controls to manage the cluster percentage values
    on a bound skin around a joint.

    jointCluster( string , [aboveBound=float], [aboveCluster=boolean],
    [aboveDropoffType=string], [aboveValue=float], [belowBound=float],
    [belowCluster=boolean], [belowDropoffType=string], [belowValue=float],
    [deformerTools=boolean], [joint=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/jointCluster.html
    """
    return _wrapCommand(cmds.jointCluster, args, kwargs)


def jointCtx(*args, **kwargs):  # noqa
    """The joint context command (jointCtx) updates the parameters of the joint tool.

    jointCtx( [object] , [autoJointOrient=string], [autoPriorityH=boolean],
    [createIKHandle=boolean], [degreeOfFreedomJ=string], [exists=boolean],
    [forceSolverH=boolean], [image1=string], [image2=string], [image3=string],
    [jointAutoLimits=boolean], [jointOrientationJ=[angle, angle, angle]],
    [largeBoneLength=float], [largeBoneRadius=float], [poWeightH=float], [priorityH=int],
    [scaleCompensateJ=boolean], [scaleJ=[float, float, float]], [scaleOrientationJ=[angle,
    angle, angle]], [secondaryAxisOrient=string], [smallBoneLength=float],
    [smallBoneRadius=float], [snapHandleH=boolean], [solverTypeH=string],
    [stickyH=string], [symmetry=boolean], [symmetryAxis=string],
    [variableBoneSize=boolean], [weightH=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/jointCtx.html
    """
    return _wrapCommand(cmds.jointCtx, args, kwargs)


def jointDisplayScale(*args, **kwargs):  # noqa
    """This action modifies and queries the current display size of skeleton joints.

    jointDisplayScale( float , [absolute=boolean], [ikfk=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/jointDisplayScale.html
    """
    return _wrapCommand(cmds.jointDisplayScale, args, kwargs)


def jointLattice(*args, **kwargs):  # noqa
    """This command creates/edits/queries a jointLattice deformer.

    jointLattice( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [creasing=float], [deformerTools=boolean], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [joint=string],
    [lengthIn=float], [lengthOut=float], [lowerBindSkin=string], [lowerTransform=string],
    [name=string], [parallel=boolean], [prune=boolean], [remove=boolean],
    [rounding=float], [selectedComponents=boolean], [split=boolean],
    [upperBindSkin=string], [upperTransform=string], [useComponentTags=boolean],
    [widthLeft=float], [widthRight=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/jointLattice.html
    """
    return _wrapCommand(cmds.jointLattice, args, kwargs)


def keyframe(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    keyframe( [objects] , [absolute=boolean], [adjustBreakdown=boolean], [animation=string],
    [attribute=string], [breakdown=boolean], [clipTime=[time, time, float]],
    [controlPoints=boolean], [eval=boolean], [float=floatrange], [floatChange=float],
    [hierarchy=string], [includeUpperBound=boolean], [index=uint], [indexValue=boolean],
    [keyframeCount=boolean], [lastSelected=boolean], [name=boolean], [option=string],
    [relative=boolean], [selected=boolean], [shape=boolean], [tickDrawSpecial=boolean],
    [time=timerange], [timeChange=time], [valueChange=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframe.html
    """
    return _wrapCommand(cmds.keyframe, args, kwargs)


def keyframeOutliner(*args, **kwargs):  # noqa
    """This command creates/edits/queries a keyframe outliner control.

    keyframeOutliner( string , [animCurve=string], [annotation=string],
    [backgroundColor=[float, float, float]], [defineTemplate=string], [display=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeOutliner.html
    """
    return _wrapCommand(cmds.keyframeOutliner, args, kwargs)


def keyframeRegionCurrentTimeCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to change current time within the
    keyframe region of the dope sheet editor.

    keyframeRegionCurrentTimeCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionCurrentTimeCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionCurrentTimeCtx, args, kwargs)


def keyframeRegionDirectKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to directly manipulate keyframes within
    the dope sheet editor.

    keyframeRegionDirectKeyCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [option=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDirectKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionDirectKeyCtx, args, kwargs)


def keyframeRegionDollyCtx(*args, **kwargs):  # noqa
    """This command can be used to create a dolly context for the dope sheet editor.

    keyframeRegionDollyCtx([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionDollyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionDollyCtx, args, kwargs)


def keyframeRegionInsertKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to insert keys within the keyframe region
    of the dope sheet editor.

    keyframeRegionInsertKeyCtx( contextName , [breakdown=boolean], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionInsertKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionInsertKeyCtx, args, kwargs)


def keyframeRegionMoveKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to move keyframes within the keyframe
    region of the dope sheet editor.

    keyframeRegionMoveKeyCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [option=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionMoveKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionMoveKeyCtx, args, kwargs)


def keyframeRegionScaleKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to scale keyframes within the keyframe
    region of the dope sheet editor.

    keyframeRegionScaleKeyCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string],
    [scaleSpecifiedKeys=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionScaleKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionScaleKeyCtx, args, kwargs)


def keyframeRegionSelectKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to select keyframes within the keyframe
    region of the dope sheet editor.

    keyframeRegionSelectKeyCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSelectKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionSelectKeyCtx, args, kwargs)


def keyframeRegionSetKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to set keys within the keyframe region of
    the dope sheet editor.

    keyframeRegionSetKeyCtx( contextName , [breakdown=boolean], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionSetKeyCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionSetKeyCtx, args, kwargs)


def keyframeRegionTrackCtx(*args, **kwargs):  # noqa
    """This command can be used to create a track context for the dope sheet editor.

    keyframeRegionTrackCtx([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeRegionTrackCtx.html
    """
    return _wrapCommand(cmds.keyframeRegionTrackCtx, args, kwargs)


def keyframeStats(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    keyframeStats( string , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [animEditor=string], [annotation=string],
    [backgroundColor=[float, float, float]], [classicMode=boolean], [columnAlign=[int,
    string]], [columnAlign2=[string, string]], [columnAlign3=[string, string, string]],
    [columnAlign4=[string, string, string, string]], [columnAlign5=[string, string,
    string, string, string]], [columnAlign6=[string, string, string, string, string,
    string]], [columnAttach=[int, string, int]], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset2=[int,
    int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int, int, int]],
    [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int, int, int,
    int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int, int]],
    [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean], [rowAttach=[int,
    string, int]], [statusBarMessage=string], [timeAnnotation=string],
    [useTemplate=string], [valueAnnotation=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeStats.html
    """
    return _wrapCommand(cmds.keyframeStats, args, kwargs)


def keyframeTangentControl(*args, **kwargs):  # noqa
    """This command creates, edits, queries a keyframe tangent control.

    keyframeTangentControl( string , [annotation=string], [backgroundColor=[float, float,
    float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [precision=int], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyframeTangentControl.html
    """
    return _wrapCommand(cmds.keyframeTangentControl, args, kwargs)


def keyingGroup(*args, **kwargs):  # noqa
    """This command is used to manage the membership of a keying group.

    keyingGroup( objects , [activator=name], [addElement=name], [afterFilters=boolean],
    [anyMember=name], [category=string], [clear=name], [color=int], [copy=name],
    [edges=boolean], [editPoints=boolean], [empty=boolean], [excludeDynamic=boolean],
    [excludeRotate=boolean], [excludeScale=boolean], [excludeTranslate=boolean],
    [excludeVisibility=boolean], [facets=boolean], [flatten=name], [forceElement=name],
    [include=name], [intersection=name], [isIntersecting=name], [isMember=name],
    [layer=boolean], [minimizeRotation=boolean], [name=string], [noIntermediate=boolean],
    [noSurfaceShader=boolean], [noWarnings=boolean], [nodesOnly=boolean], [remove=name],
    [removeActivator=name], [renderable=boolean], [setActiveFilter=string],
    [size=boolean], [split=name], [subtract=name], [text=string], [union=name],
    [vertices=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyingGroup.html
    """
    return _wrapCommand(cmds.keyingGroup, args, kwargs)


def keyTangent(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    keyTangent( [objects] , [absolute=boolean], [animation=string], [attribute=string],
    [controlPoints=boolean], [float=floatrange], [g=boolean], [hierarchy=string],
    [inAngle=angle], [inTangentType=string], [inWeight=float],
    [includeUpperBound=boolean], [index=uint], [ix=float], [iy=float], [lock=boolean],
    [outAngle=angle], [outTangentType=string], [outWeight=float], [ox=float], [oy=float],
    [pluginTangentTypes=string], [relative=boolean], [shape=boolean],
    [stepAttributes=boolean], [time=timerange], [unify=boolean], [weightLock=boolean],
    [weightedTangents=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/keyTangent.html
    """
    return _wrapCommand(cmds.keyTangent, args, kwargs)


def lassoContext(*args, **kwargs):  # noqa
    """Creates a context to perform selection via a "lasso".

    lassoContext( string , [drawClosed=boolean], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lassoContext.html
    """
    return _wrapCommand(cmds.lassoContext, args, kwargs)


def lattice(*args, **kwargs):  # noqa
    """This command creates a lattice deformer that will deform the selected objects.

    lattice( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [commonParent=boolean], [components=boolean], [deformerTools=boolean],
    [divisions=[uint, uint, uint]], [dualBase=boolean], [exclusive=string],
    [freezeMapping=boolean], [frontOfChain=boolean], [geometry=string],
    [geometryIndices=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [latticeReset=boolean], [ldivisions=[uint, uint,
    uint]], [name=string], [objectCentered=boolean], [outsideFalloffDistance=float],
    [outsideLattice=uint], [parallel=boolean], [position=[linear, linear, linear]],
    [prune=boolean], [remove=boolean], [removeTweaks=boolean], [rotation=[angle, angle,
    angle]], [scale=[linear, linear, linear]], [selectedComponents=boolean],
    [split=boolean], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lattice.html
    """
    return _wrapCommand(cmds.lattice, args, kwargs)


def latticeDeformKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to deform key frames with lattice
    manipulator.

    latticeDeformKeyCtx( contextName , [envelope=float], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [latticeColumns=uint],
    [latticeRows=uint], [name=string], [scaleLatticePts=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/latticeDeformKeyCtx.html
    """
    return _wrapCommand(cmds.latticeDeformKeyCtx, args, kwargs)


def launch(*args, **kwargs):  # noqa
    """Launch the appropriate application to open the document, web page or directory specified.

    launch([directory=string], [movie=string], [pdfFile=string], [webPage=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/launch.html
    """
    return _wrapCommand(cmds.launch, args, kwargs)


def launchImageEditor(*args, **kwargs):  # noqa
    """Launch the appropriate application to edit/view the image files specified.

    launchImageEditor( [filename] , [editImageFile=string], [viewImageFile=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/launchImageEditor.html
    """
    return _wrapCommand(cmds.launchImageEditor, args, kwargs)


def layerButton(*args, **kwargs):  # noqa
    """Creates a layer bar button widget.

    layerButton([annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [color=[float, float, float]], [command=script],
    [current=boolean], [defineTemplate=string], [docTag=string],
    [doubleClickCommand=script], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int],
    [hideOnPlaybackCommand=script], [highlightColor=[float, float, float]],
    [identification=int], [isObscured=boolean], [label=string], [labelWidth=boolean],
    [layerHideOnPlayback=boolean], [layerState=string], [layerVisible=boolean],
    [manage=boolean], [name=string], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [renameCommand=string], [select=boolean], [statusBarMessage=string],
    [transparent=boolean], [typeCommand=script], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [visibleCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/layerButton.html
    """
    return _wrapCommand(cmds.layerButton, args, kwargs)


def layeredShaderPort(*args, **kwargs):  # noqa
    """This command creates a 3dPort that displays an image representing the layered shader node
    specified.

    layeredShaderPort( [string] , [annotation=string], [backgroundColor=[float, float,
    float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [selectedColorControl=string],
    [selectedTransparencyControl=string], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/layeredShaderPort.html
    """
    return _wrapCommand(cmds.layeredShaderPort, args, kwargs)


def layeredTexturePort(*args, **kwargs):  # noqa
    """This command creates a 3dPort that displays an image representing the layered texture node
    specified.

    layeredTexturePort( [string] , [annotation=string], [backgroundColor=[float, float,
    float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [selectedAlphaControl=string],
    [selectedBlendModeControl=string], [selectedColorControl=string],
    [selectedIsVisibleControl=string], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/layeredTexturePort.html
    """
    return _wrapCommand(cmds.layeredTexturePort, args, kwargs)


def layout(*args, **kwargs):  # noqa
    """This command allows you to edit or query the properties of any layout.

    layout( string , [annotation=string], [backgroundColor=[float, float, float]],
    [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/layout.html
    """
    return _wrapCommand(cmds.layout, args, kwargs)


def layoutDialog(*args, **kwargs):  # noqa
    """The layoutDialog command creates a modal dialog containing a formLayout with 100
    divisions.

    layoutDialog([backgroundColor=[float, float, float]], [dismiss=string], [parent=string],
    [title=string], [uiScript=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/layoutDialog.html
    """
    return _wrapCommand(cmds.layoutDialog, args, kwargs)


def license(*args, **kwargs):  # noqa
    """This command displays version information about the application if it is executed without
    flags.

    license([borrow=boolean], [info=boolean], [isBorrowed=boolean], [isExported=boolean],
    [isTrial=boolean], [licenseMethod=boolean], [productChoice=boolean], [r=boolean],
    [showBorrowInfo=boolean], [showProductInfoDialog=boolean], [status=boolean],
    [usage=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/license.html
    """
    return _wrapCommand(cmds.license, args, kwargs)


def lightlink(*args, **kwargs):  # noqa
    """This command is used to make, break and query light linking relationships between
    lights/sets of lights and objects/sets of objects.

    lightlink( objects , [b=boolean], [hierarchy=boolean], [light=name], [make=boolean],
    [object=name], [sets=boolean], [shadow=boolean], [shapes=boolean],
    [transforms=boolean], [useActiveLights=boolean], [useActiveObjects=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lightlink.html
    """
    return _wrapCommand(cmds.lightlink, args, kwargs)


def lightList(*args, **kwargs):  # noqa
    """Add/Remove a relationship between an object and the current light.

    lightList([add=name], [remove=name])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lightList.html
    """
    return _wrapCommand(cmds.lightList, args, kwargs)


def linearPrecision(*args, **kwargs):  # noqa
    """This command controls the display of linear strings in the interface.

    linearPrecision( int )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/linearPrecision.html
    """
    return _wrapCommand(cmds.linearPrecision, args, kwargs)


def listAnimatable(*args, **kwargs):  # noqa
    """This command list the animatable attributes of a node.

    listAnimatable([active=boolean], [manip=boolean], [manipHandle=boolean], [shape=boolean],
    [type=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listAnimatable.html
    """
    return _wrapCommand(cmds.listAnimatable, args, kwargs)


def listAttr(*args, **kwargs):  # noqa
    """This command lists the attributes of a node.

    listAttr( [objects] , [array=boolean], [caching=boolean], [category=string],
    [changedSinceFileOpen=boolean], [channelBox=boolean], [connectable=boolean],
    [extension=boolean], [fromPlugin=boolean], [hasData=boolean], [hasNullData=boolean],
    [inUse=boolean], [keyable=boolean], [leaf=boolean], [locked=boolean], [multi=boolean],
    [output=boolean], [ramp=boolean], [read=boolean], [readOnly=boolean],
    [scalar=boolean], [scalarAndArray=boolean], [settable=boolean], [shortNames=boolean],
    [string=string], [unlocked=boolean], [usedAsFilename=boolean], [userDefined=boolean],
    [visible=boolean], [write=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listAttr.html
    """
    return _wrapCommand(cmds.listAttr, args, kwargs)


def listAttrPatterns(*args, **kwargs):  # noqa
    """Attribute patterns are plain text descriptions of an entire Maya attribute forest.

    listAttrPatterns([patternType=boolean], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listAttrPatterns.html
    """
    return _wrapCommand(cmds.listAttrPatterns, args, kwargs)


def listCameras(*args, **kwargs):  # noqa
    """Command to list all cameras.

    listCameras([orthographic=boolean], [perspective=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listCameras.html
    """
    return _wrapCommand(cmds.listCameras, args, kwargs)


def listConnections(*args, **kwargs):  # noqa
    """This command returns a list of all attributes/objects of a specified type that are
    connected to the given object(s).

    listConnections([connections=boolean], [destination=boolean], [exactType=boolean],
    [plugs=boolean], [shapes=boolean], [skipConversionNodes=boolean], [source=boolean],
    [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listConnections.html
    """
    return _wrapCommand(cmds.listConnections, args, kwargs)


def listDeviceAttachments(*args, **kwargs):  # noqa
    """This command lists the current set of device attachments.

    listDeviceAttachments([attribute=string], [axis=string], [clutch=string], [device=string],
    [file=string], [selection=boolean], [write=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listDeviceAttachments.html
    """
    return _wrapCommand(cmds.listDeviceAttachments, args, kwargs)


def listHistory(*args, **kwargs):  # noqa
    """This command traverses backwards or forwards in the graph from the specified node and
    returns all of the nodes whose construction history it passes through.

    listHistory( objects , [allConnections=boolean], [allFuture=boolean], [allGraphs=boolean],
    [breadthFirst=boolean], [fastIteration=boolean], [future=boolean],
    [futureLocalAttr=boolean], [futureWorldAttr=boolean], [groupLevels=boolean],
    [historyAttr=boolean], [interestLevel=int], [leaf=boolean], [levels=uint],
    [pruneDagObjects=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listHistory.html
    """
    return _wrapCommand(cmds.listHistory, args, kwargs)


def listInputDeviceAxes(*args, **kwargs):  # noqa
    """This command lists all of the axes of the specified input device.

    listInputDeviceAxes( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceAxes.html
    """
    return _wrapCommand(cmds.listInputDeviceAxes, args, kwargs)


def listInputDeviceButtons(*args, **kwargs):  # noqa
    """This command lists all of the buttons of the specified input device specified as an
    argument.

    listInputDeviceButtons( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listInputDeviceButtons.html
    """
    return _wrapCommand(cmds.listInputDeviceButtons, args, kwargs)


def listInputDevices(*args, **kwargs):  # noqa
    """This command lists all input devices that maya knows about.

    listInputDevices([free=boolean], [primary=boolean], [secondary=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listInputDevices.html
    """
    return _wrapCommand(cmds.listInputDevices, args, kwargs)


def listNodesWithIncorrectNames(*args, **kwargs):  # noqa
    """List all nodes with incorrect names in the Script Editor.

    listNodesWithIncorrectNames()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listNodesWithIncorrectNames.html
    """
    return _wrapCommand(cmds.listNodesWithIncorrectNames, args, kwargs)


def listNodeTypes(*args, **kwargs):  # noqa
    """Lists dependency node types satisfying a specified classification string.

    listNodeTypes( string , [exclude=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listNodeTypes.html
    """
    return _wrapCommand(cmds.listNodeTypes, args, kwargs)


def listRelatives(*args, **kwargs):  # noqa
    """This command lists parents and children of DAG objects.

    listRelatives( [objects] , [allDescendents=boolean], [allParents=boolean],
    [children=boolean], [fullPath=boolean], [noIntermediate=boolean], [parent=boolean],
    [path=boolean], [shapes=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listRelatives.html
    """
    return _wrapCommand(cmds.listRelatives, args, kwargs)


def listSets(*args, **kwargs):  # noqa
    """The listSets command is used to get a list of all the sets an object belongs to.

    listSets( [object] , [allSets=boolean], [extendToShape=boolean], [object=name],
    [type=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/listSets.html
    """
    return _wrapCommand(cmds.listSets, args, kwargs)


def loadFluid(*args, **kwargs):  # noqa
    """A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in
    the grid from the initial state cache.

    loadFluid([currentTime=boolean], [frame=float], [initialConditions=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loadFluid.html
    """
    return _wrapCommand(cmds.loadFluid, args, kwargs)


def loadModule(*args, **kwargs):  # noqa
    """Maya plug-ins may be installed individually within one of Maya's standard plug-in
    directories, or they may be packaged up with other resources in a "module".

    loadModule([allModules=boolean], [load=string], [scan=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loadModule.html
    """
    return _wrapCommand(cmds.loadModule, args, kwargs)


def loadPlugin(*args, **kwargs):  # noqa
    """Load plug-ins into Maya.

    loadPlugin( string [string...] , [addCallback=script], [allPlugins=boolean],
    [name=string], [quiet=boolean], [removeCallback=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loadPlugin.html
    """
    return _wrapCommand(cmds.loadPlugin, args, kwargs)


def loadPrefObjects(*args, **kwargs):  # noqa
    """This command loads preference dependency nodes from "userPrefObjects.

    loadPrefObjects()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loadPrefObjects.html
    """
    return _wrapCommand(cmds.loadPrefObjects, args, kwargs)


def loadUI(*args, **kwargs):  # noqa
    """loadUI lets you generate a Maya user interface from a Qt user interface (.

    loadUI([listTypes=boolean], [uiFile=string], [uiString=string], [verbose=boolean],
    [workingDirectory=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loadUI.html
    """
    return _wrapCommand(cmds.loadUI, args, kwargs)


def lockNode(*args, **kwargs):  # noqa
    """Locks or unlocks one or more dependency nodes.

    lockNode([ignoreComponents=boolean], [lock=boolean], [lockName=boolean],
    [lockUnpublished=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lockNode.html
    """
    return _wrapCommand(cmds.lockNode, args, kwargs)


def loft(*args, **kwargs):  # noqa
    """This command computes a skinned (lofted) surface passing through a number of NURBS curves.

    loft( curve curve [curve...] , [autoReverse=boolean], [caching=boolean], [close=boolean],
    [constructionHistory=boolean], [createCusp=boolean], [degree=int], [name=string],
    [nodeState=int], [object=boolean], [polygon=int], [range=boolean], [rebuild=boolean],
    [reverse=boolean], [reverseSurfaceNormals=boolean], [sectionSpans=int],
    [uniform=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/loft.html
    """
    return _wrapCommand(cmds.loft, args, kwargs)


def lookThru(*args, **kwargs):  # noqa
    """This command sets a particular camera to look through in a view.

    lookThru( [editorName] [object] , [farClip=float], [nearClip=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lookThru.html
    """
    return _wrapCommand(cmds.lookThru, args, kwargs)


def ls(*args, **kwargs):  # noqa
    """The `<code>ls</code>` command returns the names (and optionally the type names) of objects
    in the scene.

    ls( [object [object...]] , [absoluteName=boolean], [allPaths=boolean],
    [assemblies=boolean], [cameras=boolean], [containerType=string], [containers=boolean],
    [dagObjects=boolean], [defaultNodes=boolean], [dependencyNodes=boolean],
    [exactType=string], [excludeType=string], [flatten=boolean], [geometry=boolean],
    [ghost=boolean], [head=int], [hilite=boolean], [intermediateObjects=boolean],
    [invisible=boolean], [leaf=boolean], [lights=boolean], [live=boolean],
    [lockedNodes=boolean], [long=boolean], [materials=boolean], [modified=boolean],
    [noIntermediate=boolean], [nodeTypes=boolean], [objectsOnly=boolean],
    [orderedSelection=boolean], [partitions=boolean], [persistentNodes=boolean],
    [planes=boolean], [preSelectHilite=boolean], [readOnly=boolean], [recursive=boolean],
    [referencedNodes=boolean], [references=boolean], [renderGlobals=boolean],
    [renderQualities=boolean], [renderResolutions=boolean], [renderSetups=boolean],
    [selection=boolean], [sets=boolean], [shapes=boolean], [shortNames=boolean],
    [showNamespace=boolean], [showType=boolean], [tail=int], [templated=boolean],
    [textures=boolean], [transforms=boolean], [type=string], [ufeObjects=boolean],
    [undeletable=boolean], [untemplated=boolean], [uuid=boolean], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ls.html
    """
    return _wrapCommand(cmds.ls, args, kwargs)


def lsThroughFilter(*args, **kwargs):  # noqa
    """List all objects in the world that pass a given filter.

    lsThroughFilter( string , [item=string], [nodeArray=boolean], [reverse=boolean],
    [selection=boolean], [sort=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lsThroughFilter.html
    """
    return _wrapCommand(cmds.lsThroughFilter, args, kwargs)


def lsUI(*args, **kwargs):  # noqa
    """This command returns the names of UI objects.

    lsUI( [objects] , [cmdTemplates=boolean], [collection=boolean], [contexts=boolean],
    [controlLayouts=boolean], [controls=boolean], [dumpWidgets=boolean],
    [editors=boolean], [head=int], [long=boolean], [menuItems=boolean], [menus=boolean],
    [numWidgets=boolean], [panels=boolean], [radioMenuItemCollections=boolean],
    [tail=int], [type=string], [windows=boolean], [workspaceControls=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/lsUI.html
    """
    return _wrapCommand(cmds.lsUI, args, kwargs)


def makebot(*args, **kwargs):  # noqa
    """The makebot command takes an image file and produces a block ordered texture (BOT) file,
    to be used for texture caching.

    makebot([checkdepends=boolean], [checkres=uint], [input=string], [nooverwrite=boolean],
    [output=string], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/makebot.html
    """
    return _wrapCommand(cmds.makebot, args, kwargs)


def makeIdentity(*args, **kwargs):  # noqa
    """The makeIdentity command is a quick way to reset the selected transform and all of its
    children down to the shape level by the identity transformation.

    makeIdentity( [dagObject] , [apply=boolean], [jointOrient=boolean], [normal=uint],
    [preserveNormals=boolean], [rotate=boolean], [scale=boolean], [translate=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/makeIdentity.html
    """
    return _wrapCommand(cmds.makeIdentity, args, kwargs)


def makeLive(*args, **kwargs):  # noqa
    """This commmand makes an object live.

    makeLive( [surface] , [none=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/makeLive.html
    """
    return _wrapCommand(cmds.makeLive, args, kwargs)


def makePaintable(*args, **kwargs):  # noqa
    """Make attributes of nodes paintable to Attribute Paint Tool.

    makePaintable([string][string], [activate=boolean], [activateAll=boolean],
    [altAttribute=string], [attrType=string], [clearAll=boolean], [remove=boolean],
    [shapeMode=string], [uiName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/makePaintable.html
    """
    return _wrapCommand(cmds.makePaintable, args, kwargs)


def makeSingleSurface(*args, **kwargs):  # noqa
    """This command performs a stitch and tessellate operation.

    makeSingleSurface( surface , [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [object=boolean], [stitchTolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/makeSingleSurface.html
    """
    return _wrapCommand(cmds.makeSingleSurface, args, kwargs)


def manipMoveContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a move manip context.

    manipMoveContext( [object] , [activeHandle=int], [activeHandleNormal=int],
    [alignAlong=[float, float, float]], [bakePivotOri=boolean],
    [constrainAlongNormal=boolean], [currentActiveHandle=int], [editPivotMode=boolean],
    [editPivotPosition=boolean], [exists=boolean], [image1=string], [image2=string],
    [image3=string], [interactiveUpdate=boolean], [lastMode=int], [manipVisible=boolean],
    [mode=int], [orientAxes=[float, float, float]], [orientJoint=string],
    [orientJointEnabled=boolean], [orientObject=string], [orientTowards=[float, float,
    float]], [pinPivot=boolean], [pivotOriHandle=boolean], [position=boolean],
    [postCommand=script], [postDragCommand=[script, string]], [preCommand=script],
    [preDragCommand=[script, string]], [preserveChildPosition=boolean],
    [preserveUV=boolean], [reflection=boolean], [reflectionAbout=int],
    [reflectionAxis=int], [reflectionTolerance=float], [secondaryAxisOrient=string],
    [snap=boolean], [snapComponentsRelative=boolean], [snapLiveFaceCenter=boolean],
    [snapLivePoint=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean],
    [snapRelative=boolean], [snapValue=float], [translate=[float, float, float]],
    [tweakMode=boolean], [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipMoveContext.html
    """
    return _wrapCommand(cmds.manipMoveContext, args, kwargs)


def manipMoveLimitsCtx(*args, **kwargs):  # noqa
    """Create a context for the translate limits manipulator.

    manipMoveLimitsCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipMoveLimitsCtx.html
    """
    return _wrapCommand(cmds.manipMoveLimitsCtx, args, kwargs)


def manipOptions(*args, **kwargs):  # noqa
    """Changes the global manipulator parameters.

    manipOptions([enableSmartDuplicate=boolean], [enableSmartExtrude=boolean],
    [forceRefresh=boolean], [handleSize=float], [hideManipOnCtrl=boolean],
    [hideManipOnShift=boolean], [hideManipOnShiftCtrl=boolean], [linePick=float],
    [lineSize=float], [middleMouseRepositioning=boolean], [pivotRotateHandleOffset=int],
    [planeHandleOffset=int], [pointSize=float], [preselectHighlight=boolean],
    [refreshMode=int], [relative=boolean], [rememberActiveHandle=boolean],
    [rememberActiveHandleAfterToolSwitch=boolean], [scale=float],
    [showExtrudeSliders=boolean], [showPivotRotateHandle=boolean],
    [showPlaneHandles=boolean], [smartDuplicateType=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipOptions.html
    """
    return _wrapCommand(cmds.manipOptions, args, kwargs)


def manipPivot(*args, **kwargs):  # noqa
    """Changes transform component pivot used by the move/rotate/scale manipulators.

    manipPivot([bakeOri=boolean], [moveToolOri=int], [ori=[float, float, float]],
    [oriValid=boolean], [pinPivot=boolean], [pos=[float, float, float]],
    [posValid=boolean], [reset=boolean], [resetOri=boolean], [resetPos=boolean],
    [rotateToolOri=int], [scaleToolOri=int], [snapOri=boolean], [snapPos=boolean],
    [valid=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipPivot.html
    """
    return _wrapCommand(cmds.manipPivot, args, kwargs)


def manipRotateContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a rotate manip context.

    manipRotateContext( [object] , [activeHandle=int], [alignAlong=[float, float, float]],
    [bakePivotOri=boolean], [centerTrackball=boolean], [constrainAlongNormal=boolean],
    [currentActiveHandle=int], [editPivotMode=boolean], [editPivotPosition=boolean],
    [exists=boolean], [image1=string], [image2=string], [image3=string], [lastMode=int],
    [manipVisible=boolean], [mode=int], [modifyTranslation=boolean], [orientAxes=[float,
    float, float]], [orientObject=string], [orientTowards=[float, float, float]],
    [pinPivot=boolean], [pivotOriHandle=boolean], [position=boolean],
    [postCommand=script], [postDragCommand=[script, string]], [preCommand=script],
    [preDragCommand=[script, string]], [preserveChildPosition=boolean],
    [preserveUV=boolean], [reflection=boolean], [reflectionAbout=int],
    [reflectionAxis=int], [reflectionTolerance=float], [rotate=[float, float, float]],
    [snap=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean],
    [snapRelative=boolean], [snapValue=float], [tweakMode=boolean],
    [useCenterPivot=boolean], [useManipPivot=boolean], [useObjectPivot=boolean],
    [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipRotateContext.html
    """
    return _wrapCommand(cmds.manipRotateContext, args, kwargs)


def manipRotateLimitsCtx(*args, **kwargs):  # noqa
    """Create a context for the rotate limits manipulator.

    manipRotateLimitsCtx([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipRotateLimitsCtx.html
    """
    return _wrapCommand(cmds.manipRotateLimitsCtx, args, kwargs)


def manipScaleContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a scale manip context.

    manipScaleContext( [object] , [activeHandle=int], [alignAlong=[float, float, float]],
    [bakePivotOri=boolean], [constrainAlongNormal=boolean], [currentActiveHandle=int],
    [editPivotMode=boolean], [editPivotPosition=boolean], [exists=boolean],
    [image1=string], [image2=string], [image3=string], [lastMode=int],
    [manipVisible=boolean], [mode=int], [orientAxes=[float, float, float]],
    [orientObject=string], [orientTowards=[float, float, float]], [pinPivot=boolean],
    [pivotOriHandle=boolean], [position=boolean], [postCommand=script],
    [postDragCommand=[script, string]], [preCommand=script], [preDragCommand=[script,
    string]], [preserveChildPosition=boolean], [preserveUV=boolean],
    [preventNegativeScale=boolean], [reflection=boolean], [reflectionAbout=int],
    [reflectionAxis=int], [reflectionTolerance=float], [scale=[float, float, float]],
    [snap=boolean], [snapPivotOri=boolean], [snapPivotPos=boolean],
    [snapRelative=boolean], [snapValue=float], [tweakMode=boolean],
    [useManipPivot=boolean], [useObjectPivot=boolean], [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipScaleContext.html
    """
    return _wrapCommand(cmds.manipScaleContext, args, kwargs)


def manipScaleLimitsCtx(*args, **kwargs):  # noqa
    """Create a context for the scale limits manipulator.

    manipScaleLimitsCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/manipScaleLimitsCtx.html
    """
    return _wrapCommand(cmds.manipScaleLimitsCtx, args, kwargs)


def marker(*args, **kwargs):  # noqa
    """The marker command creates one or two markers, on a motion path curve, at the specified
    time and location.

    marker( [string] , [attach=boolean], [detach=boolean], [frontTwist=angle],
    [orientationMarker=boolean], [positionMarker=boolean], [sideTwist=angle], [time=time],
    [upTwist=angle], [valueU=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/marker.html
    """
    return _wrapCommand(cmds.marker, args, kwargs)


def matchTransform(*args, **kwargs):  # noqa
    """This command modifies the source object's transform to match the target object's
    transform.

    matchTransform( [objects...] , [pivots=boolean], [position=boolean], [positionX=boolean],
    [positionY=boolean], [positionZ=boolean], [rotatePivot=boolean], [rotation=boolean],
    [rotationX=boolean], [rotationY=boolean], [rotationZ=boolean], [scale=boolean],
    [scaleBox=boolean], [scalePivot=boolean], [scaleX=boolean], [scaleY=boolean],
    [scaleZ=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/matchTransform.html
    """
    return _wrapCommand(cmds.matchTransform, args, kwargs)


def matrixUtil(*args, **kwargs):  # noqa
    """Command to deal with matrix, composition and decomposition.

    matrixUtil([inverse=boolean], [quaternion=[float, float, float, float]],
    [relative=boolean], [rotation=[float, float, float]], [scale=[float, float, float]],
    [shear=[float, float, float]], [translation=[float, float, float]],
    [transpose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/matrixUtil.html
    """
    return _wrapCommand(cmds.matrixUtil, args, kwargs)


def mayaDpiSetting(*args, **kwargs):  # noqa
    """Provide Maya interface scaling based on system DPI or custom scale setting or no scaling.

    mayaDpiSetting([mode=uint], [realScaleValue=boolean], [scaleValue=float],
    [systemDpi=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mayaDpiSetting.html
    """
    return _wrapCommand(cmds.mayaDpiSetting, args, kwargs)


def mayaHasRenderSetup(*args, **kwargs):  # noqa
    """This command controls and queries render setup states.

    mayaHasRenderSetup([enableCurrentSession=boolean], [enableDuringTests=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mayaHasRenderSetup.html
    """
    return _wrapCommand(cmds.mayaHasRenderSetup, args, kwargs)


def melInfo(*args, **kwargs):  # noqa
    """This command returns the names of all global MEL procedures that are currently defined as
    a string array.

    melInfo()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/melInfo.html
    """
    return _wrapCommand(cmds.melInfo, args, kwargs)


def melOptions(*args, **kwargs):  # noqa
    """Set and query options that affect the behavior of Maya's Embedded Language (MEL).

    melOptions([duplicateVariableWarnings=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/melOptions.html
    """
    return _wrapCommand(cmds.melOptions, args, kwargs)


def memory(*args, **kwargs):  # noqa
    """Used to query essential statistics on memory availability and usage.

    memory([adjustedVirtualMemory=boolean], [asFloat=boolean], [debug=boolean],
    [freeMemory=boolean], [gigaByte=boolean], [heapMemory=boolean], [kiloByte=boolean],
    [megaByte=boolean], [pageFaults=boolean], [pageReclaims=boolean],
    [physicalMemory=boolean], [processVirtualMemory=boolean], [summary=boolean],
    [swapFree=boolean], [swapLogical=boolean], [swapMax=boolean], [swapPhysical=boolean],
    [swapReserved=boolean], [swapVirtual=boolean], [swaps=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/memory.html
    """
    return _wrapCommand(cmds.memory, args, kwargs)


def menu(*args, **kwargs):  # noqa
    """This command creates a new menu and adds it to the default window's menubar if no parent
    is specified.

    menu( [string] , [allowOptionBoxes=boolean], [defineTemplate=string],
    [deleteAllItems=boolean], [docTag=string], [enable=boolean], [exists=boolean],
    [familyImage=string], [helpMenu=boolean], [itemArray=boolean], [label=string],
    [mnemonic=string], [numberOfItems=boolean], [parent=string], [postMenuCommand=script],
    [postMenuCommandOnce=boolean], [scrollable=boolean], [tearOff=boolean],
    [useTemplate=string], [version=string], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menu.html
    """
    return _wrapCommand(cmds.menu, args, kwargs)


def menuBarLayout(*args, **kwargs):  # noqa
    """Create a layout containing a menu bar.

    menuBarLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [menuArray=boolean], [menuBarVisible=boolean], [menuIndex=[string, uint]],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfMenus=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menuBarLayout.html
    """
    return _wrapCommand(cmds.menuBarLayout, args, kwargs)


def menuEditor(*args, **kwargs):  # noqa
    """A menuEditor displays the contents of a popup menu and allows the menu's items to be
    edited.

    menuEditor( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [cellHeight=int], [cellWidth=int], [cellWidthHeight=[int, int]],
    [checkBoxPresent=[boolean, string, int]], [checkBoxState=[boolean, string, int]],
    [childArray=boolean], [command=[string, string, int]], [defineTemplate=string],
    [delete=[string, int]], [docTag=string], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [iconMenuCallback=string], [image=[string, string, int]],
    [isObscured=boolean], [label=[string, string, int]], [manage=boolean],
    [menuItemTypes=boolean], [noBackground=boolean], [numberOfChildren=boolean],
    [numberOfPopupMenus=boolean], [optionBoxCommand=[string, string, int]],
    [optionBoxPresent=[boolean, string, int]], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [radioButtonPresent=[boolean, string, int]],
    [radioButtonState=[boolean, string, int]], [separator=[string, int]],
    [statusBarMessage=string], [style=string], [subMenuAt=[string, int]],
    [subMenuEditorWindow=string], [subMenuEditorsOpen=boolean], [subMenuOf=[string,
    string, int]], [topLevelMenu=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menuEditor.html
    """
    return _wrapCommand(cmds.menuEditor, args, kwargs)


def menuItem(*args, **kwargs):  # noqa
    """This command creates/edits/queries menu items.

    menuItem( [string] , [allowOptionBoxes=boolean], [annotation=string], [boldFont=boolean],
    [checkBox=boolean], [collection=string], [command=script], [data=int],
    [defineTemplate=string], [divider=boolean], [dividerLabel=string], [docTag=string],
    [dragDoubleClickCommand=script], [dragMenuCommand=script], [echoCommand=boolean],
    [enable=boolean], [enableCommandRepeat=boolean], [exists=boolean],
    [familyImage=string], [image=string], [imageOverlayLabel=string],
    [insertAfter=string], [isCheckBox=boolean], [isOptionBox=boolean],
    [isRadioButton=boolean], [italicized=boolean], [label=string], [longDivider=boolean],
    [optionBox=boolean], [optionBoxIcon=string], [parent=string],
    [postMenuCommand=script], [postMenuCommandOnce=boolean], [radialPosition=string],
    [radioButton=boolean], [runTimeCommand=string], [sourceType=string],
    [subMenu=boolean], [tearOff=boolean], [useTemplate=string], [version=string],
    [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menuItem.html
    """
    return _wrapCommand(cmds.menuItem, args, kwargs)


def menuSet(*args, **kwargs):  # noqa
    """Create a menu set which is used to logically order menus for display in the main menu bar.

    menuSet( [object] , [addMenu=string], [allMenuSets=boolean], [currentMenuSet=string],
    [exists=string], [hotBoxVisible=boolean], [insertMenu=[string, uint]], [label=string],
    [menuArray=string[]], [moveMenu=[string, uint]], [moveMenuSet=[string, uint]],
    [numberOfMenuSets=boolean], [numberOfMenus=boolean], [permanent=boolean],
    [removeMenu=string], [removeMenuSet=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menuSet.html
    """
    return _wrapCommand(cmds.menuSet, args, kwargs)


def menuSetPref(*args, **kwargs):  # noqa
    """Provides the functionality to save and load menuSets between sessions of Maya.

    menuSetPref( [object] , [exists=boolean], [force=boolean], [loadAll=boolean],
    [removeAll=boolean], [saveAll=boolean], [saveBackup=boolean], [version=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/menuSetPref.html
    """
    return _wrapCommand(cmds.menuSetPref, args, kwargs)


def messageLine(*args, **kwargs):  # noqa
    """This command creates a message line where tool feedback is shown.

    messageLine( [name] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/messageLine.html
    """
    return _wrapCommand(cmds.messageLine, args, kwargs)


def mimicManipulation(*args, **kwargs):  # noqa
    """This command mimics what various manipulators do to support Evaluation-Manager-accelerated
    manipulation.

    mimicManipulation([manipulations=string], [prevalidation=boolean], [refresh=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mimicManipulation.html
    """
    return _wrapCommand(cmds.mimicManipulation, args, kwargs)


def minimizeApp(*args, **kwargs):  # noqa
    """This command minimizes (iconifies) all of the application's windows into a single desktop
    icon.

    minimizeApp()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/minimizeApp.html
    """
    return _wrapCommand(cmds.minimizeApp, args, kwargs)


def mirrorJoint(*args, **kwargs):  # noqa
    """This command will duplicate a branch of the skeleton from the selected joint symmetrically
    about a plane in world space.

    mirrorJoint( object , [mirrorBehavior=boolean], [mirrorXY=boolean], [mirrorXZ=boolean],
    [mirrorYZ=boolean], [searchReplace=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mirrorJoint.html
    """
    return _wrapCommand(cmds.mirrorJoint, args, kwargs)


def modelCurrentTimeCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to change current time within the model
    views.

    modelCurrentTimeCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [percent=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/modelCurrentTimeCtx.html
    """
    return _wrapCommand(cmds.modelCurrentTimeCtx, args, kwargs)


def modelEditor(*args, **kwargs):  # noqa
    """Create, edit or query a model editor.

    modelEditor( [editorName] , [activeComponentsXray=boolean],
    [activeCustomEnvironment=string], [activeCustomGeometry=string],
    [activeCustomLighSet=string], [activeCustomOverrideGeometry=string],
    [activeCustomRenderer=string], [activeOnly=boolean], [activeShadingGraph=string],
    [activeView=boolean], [addObjects=string], [addSelected=boolean],
    [addSelectedObjects=boolean], [allObjects=boolean], [backfaceCulling=boolean],
    [bufferMode=string], [bumpResolution=[uint, uint]], [camera=string],
    [cameraName=string], [cameraSet=string], [cameraSetup=boolean], [cameras=boolean],
    [capture=string], [captureSequenceNumber=int], [clipGhosts=boolean],
    [cmEnabled=boolean], [colorMap=boolean], [colorResolution=[uint, uint]],
    [control=boolean], [controlVertices=boolean], [cullingOverride=string],
    [default=boolean], [defineTemplate=string], [deformers=boolean], [dimensions=boolean],
    [displayAppearance=string], [displayLights=string], [displayTextures=boolean],
    [docTag=string], [dynamicConstraints=boolean], [dynamics=boolean],
    [editorChanged=script], [exists=boolean], [exposure=float], [filter=string],
    [filteredObjectList=boolean], [fluids=boolean], [fogColor=[float, float, float,
    float]], [fogDensity=float], [fogEnd=float], [fogMode=string], [fogSource=string],
    [fogStart=float], [fogging=boolean], [follicles=boolean],
    [forceMainConnection=string], [gamma=float], [greasePencils=boolean], [grid=boolean],
    [hairSystems=boolean], [handles=boolean], [headsUpDisplay=boolean], [height=boolean],
    [highlightConnection=string], [hulls=boolean], [ignorePanZoom=boolean],
    [ikHandles=boolean], [imagePlane=boolean], [interactive=boolean],
    [interactiveBackFaceCull=boolean], [interactiveDisableShadows=boolean],
    [isFiltered=boolean], [jointXray=boolean], [joints=boolean], [lights=boolean],
    [lineWidth=float], [locators=boolean], [lockMainConnection=boolean],
    [lowQualityLighting=boolean], [mainListConnection=string], [manipulators=boolean],
    [maxConstantTransparency=float], [maximumNumHardwareLights=boolean],
    [modelPanel=string], [motionTrails=boolean], [nCloths=boolean], [nParticles=boolean],
    [nRigids=boolean], [noUndo=boolean], [nurbsCurves=boolean], [nurbsSurfaces=boolean],
    [objectFilter=script], [objectFilterList=script], [objectFilterListUI=script],
    [objectFilterShowInHUD=boolean], [objectFilterUI=script], [occlusionCulling=boolean],
    [panel=string], [parent=string], [particleInstancers=boolean], [pivots=boolean],
    [planes=boolean], [pluginObjects=[string, boolean]], [pluginShapes=boolean],
    [polymeshes=boolean], [queryPluginObjects=string], [removeSelected=boolean],
    [rendererDeviceName=boolean], [rendererList=boolean], [rendererListUI=boolean],
    [rendererName=string], [rendererOverrideList=boolean],
    [rendererOverrideListUI=boolean], [rendererOverrideName=string],
    [resetCustomCamera=boolean], [sceneRenderFilter=string], [selectionConnection=string],
    [selectionHiliteDisplay=boolean], [setSelected=boolean], [shadingModel=int],
    [shadows=boolean], [smallObjectCulling=boolean], [smallObjectThreshold=float],
    [smoothWireframe=boolean], [sortTransparent=boolean], [stateString=boolean],
    [stereoDrawMode=boolean], [strokes=boolean], [subdivSurfaces=boolean],
    [textureAnisotropic=boolean], [textureCompression=boolean], [textureDisplay=string],
    [textureEnvironmentMap=boolean], [textureHilight=boolean], [textureMaxSize=int],
    [textureMemoryUsed=boolean], [textureSampling=int], [textures=boolean],
    [toggleExposure=boolean], [toggleGamma=boolean], [transpInShadows=boolean],
    [transparencyAlgorithm=string], [twoSidedLighting=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateColorMode=boolean],
    [updateMainConnection=boolean], [useBaseRenderer=boolean], [useColorIndex=boolean],
    [useDefaultMaterial=boolean], [useInteractiveMode=boolean],
    [useRGBImagePlane=boolean], [useReducedRenderer=boolean], [useTemplate=string],
    [userNode=string], [viewObjects=boolean], [viewSelected=boolean],
    [viewTransformName=string], [viewType=boolean], [width=boolean],
    [wireframeBackingStore=boolean], [wireframeOnShaded=boolean], [xray=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/modelEditor.html
    """
    return _wrapCommand(cmds.modelEditor, args, kwargs)


def modelPanel(*args, **kwargs):  # noqa
    """This command creates a panel consisting of a model editor.

    modelPanel( panelName , [barLayout=boolean], [camera=string], [control=boolean],
    [copy=string], [createString=boolean], [defineTemplate=string], [docTag=string],
    [editString=boolean], [exists=boolean], [init=boolean], [isUnique=boolean],
    [label=string], [menuBarRepeatLast=boolean], [menuBarVisible=boolean],
    [modelEditor=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean],
    [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/modelPanel.html
    """
    return _wrapCommand(cmds.modelPanel, args, kwargs)


def moduleInfo(*args, **kwargs):  # noqa
    """Returns information on modules found by Maya.

    moduleInfo([definition=boolean], [listModules=boolean], [moduleName=string],
    [path=boolean], [version=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/moduleInfo.html
    """
    return _wrapCommand(cmds.moduleInfo, args, kwargs)


def mouse(*args, **kwargs):  # noqa
    """This command allows to configure mouse.

    mouse([enableScrollWheel=boolean], [mouseButtonTracking=int],
    [mouseButtonTrackingStatus=boolean], [scrollWheelStatus=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mouse.html
    """
    return _wrapCommand(cmds.mouse, args, kwargs)


def move(*args, **kwargs):  # noqa
    """The move command is used to change the positions of geometric objects.

    move( float float float [objects] , [absolute=boolean], [componentOffset=boolean],
    [componentSpace=boolean], [constrainAlongNormal=boolean],
    [deletePriorHistory=boolean], [localSpace=boolean], [moveX=boolean], [moveXY=boolean],
    [moveXYZ=boolean], [moveXZ=boolean], [moveY=boolean], [moveYZ=boolean],
    [moveZ=boolean], [objectSpace=boolean], [orientJoint=string], [parameter=boolean],
    [preserveChildPosition=boolean], [preserveGeometryPosition=boolean],
    [preserveUV=boolean], [reflection=boolean], [reflectionAboutBBox=boolean],
    [reflectionAboutOrigin=boolean], [reflectionAboutX=boolean],
    [reflectionAboutY=boolean], [reflectionAboutZ=boolean], [reflectionTolerance=float],
    [relative=boolean], [rotatePivotRelative=boolean], [scalePivotRelative=boolean],
    [secondaryAxisOrient=string], [symNegative=boolean], [worldSpace=boolean],
    [worldSpaceDistance=boolean], [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/move.html
    """
    return _wrapCommand(cmds.move, args, kwargs)


def moveKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to move keyframes within the graph
    editor.

    moveKeyCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [moveFunction=string], [name=string],
    [option=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/moveKeyCtx.html
    """
    return _wrapCommand(cmds.moveKeyCtx, args, kwargs)


def moveVertexAlongDirection(*args, **kwargs):  # noqa
    """The command moves the selected vertex ( control vertex ) in the specified unit direction
    by the given magnitude.

    moveVertexAlongDirection([direction=[float, float, float]], [magnitude=linear],
    [normalDirection=linear], [uDirection=linear], [uvNormalDirection=[linear, linear,
    linear]], [vDirection=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/moveVertexAlongDirection.html
    """
    return _wrapCommand(cmds.moveVertexAlongDirection, args, kwargs)


def movieInfo(*args, **kwargs):  # noqa
    """movieInfo provides a mechanism for querying information about movie files.

    movieInfo(string, [counter=boolean], [dropFrame=boolean], [frameCount=boolean],
    [frameDuration=boolean], [height=boolean], [movieTexture=boolean],
    [negTimesOK=boolean], [numFrames=boolean], [quickTime=boolean], [timeCode=boolean],
    [timeCodeTrack=boolean], [timeScale=boolean], [twentyFourHourMax=boolean],
    [width=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/movieInfo.html
    """
    return _wrapCommand(cmds.movieInfo, args, kwargs)


def movIn(*args, **kwargs):  # noqa
    """Imports a.

    movIn( [attributeList] , [file=string], [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/movIn.html
    """
    return _wrapCommand(cmds.movIn, args, kwargs)


def movOut(*args, **kwargs):  # noqa
    """Exports a.

    movOut( [targetList] , [comment=boolean], [file=string], [precision=uint],
    [time=timerange])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/movOut.html
    """
    return _wrapCommand(cmds.movOut, args, kwargs)


def multiProfileBirailSurface(*args, **kwargs):  # noqa
    """The cmd creates a railed surface by sweeping the profiles using two rail curves.

    multiProfileBirailSurface( curve curve curve... curve curve , [caching=boolean],
    [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean],
    [polygon=int], [tangentContinuityProfile1=boolean],
    [tangentContinuityProfile2=boolean], [transformMode=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/multiProfileBirailSurface.html
    """
    return _wrapCommand(cmds.multiProfileBirailSurface, args, kwargs)


def multiTouch(*args, **kwargs):  # noqa
    """Used to interact with the Gestura (multi-touch) library.

    multiTouch([gestures=boolean], [trackpad=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/multiTouch.html
    """
    return _wrapCommand(cmds.multiTouch, args, kwargs)


def mute(*args, **kwargs):  # noqa
    """The mute command is used to disable and enable playback on a channel.

    mute([disable=boolean], [force=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/mute.html
    """
    return _wrapCommand(cmds.mute, args, kwargs)


def nameCommand(*args, **kwargs):  # noqa
    """This command creates a nameCommand object.

    nameCommand( [string] , [annotation=string], [command=script], [data1=string],
    [data2=string], [data3=string], [default=boolean], [sourceType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nameCommand.html
    """
    return _wrapCommand(cmds.nameCommand, args, kwargs)


def nameField(*args, **kwargs):  # noqa
    """This command creates an editable field that can be linked to the name of a Maya object.

    nameField( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [drawInactiveFrame=boolean], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [isObscured=boolean], [manage=boolean], [nameChangeCommand=script],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [object=string],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [receiveFocusCommand=script], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nameField.html
    """
    return _wrapCommand(cmds.nameField, args, kwargs)


def namespace(*args, **kwargs):  # noqa
    """This command allows a namespace to be created, set or removed.

    namespace( [string] , [absoluteName=boolean], [addNamespace=string],
    [collapseAncestors=string], [deleteNamespaceContent=boolean], [exists=string],
    [force=boolean], [isRootNamespace=string], [mergeNamespaceWithOther=string],
    [mergeNamespaceWithParent=boolean], [mergeNamespaceWithRoot=boolean],
    [moveNamespace=[string, string]], [parent=string], [recurse=boolean],
    [relativeNames=boolean], [removeNamespace=string], [rename=[string, string]],
    [setNamespace=string], [validateName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/namespace.html
    """
    return _wrapCommand(cmds.namespace, args, kwargs)


def namespaceInfo(*args, **kwargs):  # noqa
    """This command displays information about a namespace.

    namespaceInfo( string , [absoluteName=boolean], [baseName=boolean],
    [currentNamespace=boolean], [dagPath=boolean], [fullName=boolean], [internal=boolean],
    [isRootNamespace=boolean], [listNamespace=boolean], [listOnlyDependencyNodes=boolean],
    [listOnlyNamespaces=boolean], [parent=boolean], [recurse=boolean],
    [shortName=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/namespaceInfo.html
    """
    return _wrapCommand(cmds.namespaceInfo, args, kwargs)


def nBase(*args, **kwargs):  # noqa
    """Edits one or more nBase objects.

    nBase([clearCachedTextureMap=string], [clearStart=boolean], [stuffStart=boolean],
    [textureToVertex=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nBase.html
    """
    return _wrapCommand(cmds.nBase, args, kwargs)


def newton(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    newton( selectionList , [attenuation=float], [magnitude=float], [maxDistance=linear],
    [minDistance=float], [name=string], [perVertex=boolean], [position=[linear, linear,
    linear]], [torusSectionRadius=linear], [volumeExclusion=boolean],
    [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/newton.html
    """
    return _wrapCommand(cmds.newton, args, kwargs)


def nodeCast(*args, **kwargs):  # noqa
    """Given two nodes, a source node of type A and a target node of type B, where type A is
    either type B or a sub-type of B, this command will replace the target node with the
    source node.

    nodeCast(stringstring, [copyDynamicAttrs=boolean], [disableAPICallbacks=boolean],
    [disableScriptJobCallbacks=boolean], [disconnectUnmatchedAttrs=boolean],
    [force=boolean], [swapNames=boolean], [swapValues=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeCast.html
    """
    return _wrapCommand(cmds.nodeCast, args, kwargs)


def nodeEditor(*args, **kwargs):  # noqa
    """This command creates/edits/queries a nodeEditor editor.

    nodeEditor( [string] , [activeTab=int], [addNewNodes=boolean], [addNode=string],
    [additiveGraphingMode=boolean], [allAttributes=boolean], [allNodes=boolean],
    [allowNewTabs=boolean], [allowTabTearoff=boolean], [autoSizeNodes=boolean],
    [beginCreateNode=boolean], [beginNewConnection=string],
    [breakSelectedConnections=boolean], [closeAllTabs=boolean], [closeTab=int],
    [connectSelectedNodes=boolean], [connectedGraphingMode=boolean],
    [connectionMinSegment=float], [connectionOffset=float], [connectionRoundness=float],
    [connectionStyle=string], [connectionTension=int], [consistentNameSize=boolean],
    [contentsChangedCommand=script], [control=boolean], [createInfo=string],
    [createNodeCommand=script], [createTab=[int, [, string, ]]],
    [crosshairOnEdgeDragging=boolean], [customAttributeListEdit=[string, [, string, ]]],
    [cycleHUD=boolean], [defaultPinnedState=boolean], [defineTemplate=string],
    [deleteSelected=boolean], [docTag=string], [dotFormat=string], [downstream=boolean],
    [duplicateTab=[int, [, int, ]]], [enableOpenGL=boolean], [exists=boolean],
    [extendToShapes=boolean], [feedbackConnection=boolean], [feedbackNode=boolean],
    [feedbackPlug=boolean], [feedbackTabIndex=boolean], [feedbackType=boolean],
    [filter=string], [filterCreateNodeTypes=script], [focusCommand=script],
    [forceMainConnection=string], [frameAll=boolean], [frameModelSelection=boolean],
    [frameSelected=boolean], [getNodeList=boolean], [graphSelectedConnections=boolean],
    [graphSelection=boolean], [gridSnap=boolean], [gridVisibility=boolean],
    [hasWatchpoint=boolean], [highlightConnection=string], [highlightConnections=[string,
    boolean]], [hudMessage=[string, int, float]], [ignoreAssets=boolean],
    [island=boolean], [keyPressCommand=script], [keyReleaseCommand=script],
    [layout=boolean], [layoutCommand=script], [lockMainConnection=boolean],
    [mainListConnection=string], [nodeSwatchSize=string], [nodeTitleMode=string],
    [nodeViewMode=string], [overrideNodeDropPosition=[float, float]], [panView=[float,
    float]], [panel=string], [parent=string], [pinSelectedNodes=boolean],
    [popupMenuScript=script], [primary=boolean], [redockTab=boolean],
    [removeDownstream=boolean], [removeNode=string], [removeUnselected=boolean],
    [removeUpstream=boolean], [renameNode=string], [renameTab=[int, [, string, ]]],
    [restoreInfo=string], [restoreLastClosedTab=boolean], [rootNode=string],
    [rootsFromSelection=boolean], [scaleView=float], [selectAll=boolean],
    [selectConnectionNodes=boolean], [selectDownstream=boolean],
    [selectFeedbackConnection=boolean], [selectNode=string], [selectUpstream=boolean],
    [selectionConnection=string], [setWatchpoint=boolean],
    [settingsChangedCallback=script], [shaderNetworks=boolean],
    [showAllNodeAttributes=string], [showNamespace=boolean], [showSGShapes=boolean],
    [showShapes=boolean], [showTabs=boolean], [showTransforms=boolean],
    [showUnitConversions=boolean], [stateString=boolean], [syncedSelection=boolean],
    [tabChangeCommand=script], [toggleAttrFilter=boolean], [toggleSelectedPins=boolean],
    [toggleSwatchSize=string], [toolTipCommand=script], [traversalDepthLimit=int],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [upstream=boolean], [useAssets=boolean], [useLongName=int], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeEditor.html
    """
    return _wrapCommand(cmds.nodeEditor, args, kwargs)


def nodeIconButton(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    nodeIconButton( [string] , [align=string], [annotation=string], [backgroundColor=[float,
    float, float]], [command=script], [defineTemplate=string], [disabledImage=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [flipX=boolean], [flipY=boolean], [font=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [image1=string],
    [image2=string], [image3=string], [imageOverlayLabel=string], [isObscured=boolean],
    [label=string], [labelOffset=int], [manage=boolean], [marginHeight=uint],
    [marginWidth=uint], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [overlayLabelBackColor=[float, float, float, float]], [overlayLabelColor=[float,
    float, float]], [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [rotation=float], [statusBarMessage=string], [style=string], [useAlpha=boolean],
    [useTemplate=string], [version=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeIconButton.html
    """
    return _wrapCommand(cmds.nodeIconButton, args, kwargs)


def nodeOutliner(*args, **kwargs):  # noqa
    """The nodeOutliner command creates, edits and queries an outline control that shows
    dependency nodes and their attributes.

    nodeOutliner( [string] , [addCommand=script], [addObject=name], [annotation=string],
    [attrAlphaOrder=string], [backgroundColor=[float, float, float]], [connectivity=name],
    [currentSelection=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [lastClickedNode=boolean], [lastMenuChoice=string],
    [longNames=boolean], [manage=boolean], [menuCommand=script],
    [menuMultiOption=boolean], [multiSelect=boolean], [niceNames=boolean],
    [noBackground=boolean], [noConnectivity=boolean], [nodesDisplayed=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [pressHighlightsUnconnected=boolean], [preventOverride=boolean], [redraw=boolean],
    [redrawRow=boolean], [remove=string], [removeAll=boolean], [replace=name],
    [selectCommand=script], [showConnectedOnly=boolean], [showHidden=boolean],
    [showInputs=boolean], [showNonConnectable=boolean], [showNonKeyable=boolean],
    [showOutputs=boolean], [showPublished=boolean], [showReadOnly=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeOutliner.html
    """
    return _wrapCommand(cmds.nodeOutliner, args, kwargs)


def nodePreset(*args, **kwargs):  # noqa
    """Command to save and load preset settings for a node.

    nodePreset([attributes=string], [custom=string], [delete=[name, string]], [exists=[name,
    string]], [isValidName=string], [list=name], [load=[name, string]], [save=[name,
    string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodePreset.html
    """
    return _wrapCommand(cmds.nodePreset, args, kwargs)


def nodeTreeLister(*args, **kwargs):  # noqa
    """This command creates/edits/queries the node tree lister control.

    nodeTreeLister( [string] , [addFavorite=string], [addItem=[string, string, script]],
    [addVnnItem=[string, string, string, string]], [annotation=string],
    [backgroundColor=[float, float, float]], [clearContents=boolean],
    [collapsePath=string], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [executeItem=string],
    [exists=boolean], [expandPath=string], [expandToDepth=int],
    [favoritesCallback=script], [favoritesList=boolean], [fullPathName=boolean],
    [height=int], [highlightColor=[float, float, float]], [isObscured=boolean],
    [itemScript=string], [manage=boolean], [noBackground=boolean], [nodeLibrary=string],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [refreshCommand=script], [removeFavorite=string],
    [removeItem=string], [resultsPathUnderCursor=boolean], [selectPath=string],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [vnnString=boolean], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeTreeLister.html
    """
    return _wrapCommand(cmds.nodeTreeLister, args, kwargs)


def nodeType(*args, **kwargs):  # noqa
    """This command returns a string which identifies the given node's type.

    nodeType( string , [apiType=boolean], [derived=boolean], [inherited=boolean],
    [isTypeName=boolean], [ufeRuntimeName=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nodeType.html
    """
    return _wrapCommand(cmds.nodeType, args, kwargs)


def nonLinear(*args, **kwargs):  # noqa
    """This command creates a functional deformer of the specified type that will deform the
    selected objects.

    nonLinear( objects , [after=boolean], [afterReference=boolean], [autoParent=boolean],
    [before=boolean], [commonParent=boolean], [components=boolean],
    [defaultScale=boolean], [deformerTools=boolean], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string],
    [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean],
    [split=boolean], [type=string], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nonLinear.html
    """
    return _wrapCommand(cmds.nonLinear, args, kwargs)


def normalConstraint(*args, **kwargs):  # noqa
    """Constrain an object's orientation based on the normal of the target surface(s) at the
    closest point(s) to the object.

    normalConstraint( [target...] object , [aimVector=[float, float, float]], [layer=string],
    [name=string], [remove=boolean], [targetList=boolean], [upVector=[float, float,
    float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name],
    [worldUpType=string], [worldUpVector=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/normalConstraint.html
    """
    return _wrapCommand(cmds.normalConstraint, args, kwargs)


def nParticle(*args, **kwargs):  # noqa
    """The nParticle command creates a new nParticle object from a list of world space points.

    nParticle( selectionItem , [attribute=string], [cache=boolean], [conserve=float],
    [count=boolean], [deleteCache=boolean], [dynamicAttrList=boolean], [floatValue=float],
    [gridSpacing=linear], [inherit=float], [jitterBasePoint=[linear, linear, linear]],
    [jitterRadius=linear], [lowerLeft=[linear, linear, linear]], [name=string],
    [numJitters=uint], [order=int], [particleId=int], [perParticleDouble=boolean],
    [perParticleVector=boolean], [position=[linear, linear, linear]], [shapeName=string],
    [upperRight=[linear, linear, linear]], [vectorValue=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nParticle.html
    """
    return _wrapCommand(cmds.nParticle, args, kwargs)


def nSoft(*args, **kwargs):  # noqa
    """Makes a nSoft body from the object(s) passed on the command line or in the selection list.

    nSoft( selectionList , [convert=boolean], [duplicate=boolean], [duplicateHistory=boolean],
    [goal=float], [hideOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nSoft.html
    """
    return _wrapCommand(cmds.nSoft, args, kwargs)


def nurbsBoolean(*args, **kwargs):  # noqa
    """This command performs a boolean operation.

    nurbsBoolean( surface surface , [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [nsrfsInFirstShell=int], [object=boolean],
    [operation=int], [smartConnection=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsBoolean.html
    """
    return _wrapCommand(cmds.nurbsBoolean, args, kwargs)


def nurbsCopyUVSet(*args, **kwargs):  # noqa
    """This is only a sample command for debugging purposes, which makes a copy of the implicit
    st parameterization on a nurbs surface to be the 1st explicit uvset.

    nurbsCopyUVSet()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsCopyUVSet.html
    """
    return _wrapCommand(cmds.nurbsCopyUVSet, args, kwargs)


def nurbsCube(*args, **kwargs):  # noqa
    """The nurbsCube command creates a new NURBS Cube made up of six planes.

    nurbsCube([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [degree=int], [heightRatio=float], [lengthRatio=float],
    [name=string], [nodeState=int], [object=boolean], [patchesU=int], [patchesV=int],
    [pivot=[linear, linear, linear]], [polygon=int], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsCube.html
    """
    return _wrapCommand(cmds.nurbsCube, args, kwargs)


def nurbsCurveToBezier(*args, **kwargs):  # noqa
    """The nurbsCurveToBezier command attempts to convert an existing NURBS curve to a Bezier
    curve.

    nurbsCurveToBezier( curve )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsCurveToBezier.html
    """
    return _wrapCommand(cmds.nurbsCurveToBezier, args, kwargs)


def nurbsEditUV(*args, **kwargs):  # noqa
    """Command Edits UVs on NURBS objects.

    nurbsEditUV([angle=float], [pivotU=float], [pivotV=float], [relative=boolean],
    [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float],
    [scaleV=float], [uValue=float], [vValue=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsEditUV.html
    """
    return _wrapCommand(cmds.nurbsEditUV, args, kwargs)


def nurbsPlane(*args, **kwargs):  # noqa
    """The nurbsPlane command creates a new NURBS Plane and return the name of the new surface.

    nurbsPlane([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [degree=int], [lengthRatio=float], [name=string],
    [nodeState=int], [object=boolean], [patchesU=int], [patchesV=int], [pivot=[linear,
    linear, linear]], [polygon=int], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsPlane.html
    """
    return _wrapCommand(cmds.nurbsPlane, args, kwargs)


def nurbsSelect(*args, **kwargs):  # noqa
    """Performs selection operations on NURBS objects.

    nurbsSelect([borderSelection=boolean], [bottomBorder=boolean], [growSelection=int],
    [leftBorder=boolean], [rightBorder=boolean], [shrinkSelection=int],
    [topBorder=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsSelect.html
    """
    return _wrapCommand(cmds.nurbsSelect, args, kwargs)


def nurbsSquare(*args, **kwargs):  # noqa
    """The nurbsSquare command creates a square.

    nurbsSquare([caching=boolean], [center=[linear, linear, linear]], [centerX=linear],
    [centerY=linear], [centerZ=linear], [constructionHistory=boolean], [degree=int],
    [name=string], [nodeState=int], [normal=[linear, linear, linear]], [normalX=linear],
    [normalY=linear], [normalZ=linear], [object=boolean], [sideLength1=linear],
    [sideLength2=linear], [spansPerSide=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsSquare.html
    """
    return _wrapCommand(cmds.nurbsSquare, args, kwargs)


def nurbsToPoly(*args, **kwargs):  # noqa
    """This command tesselates a NURBS surface and produces a polygonal surface.

    nurbsToPoly( [surface] , [caching=boolean], [constructionHistory=boolean],
    [curvatureTolerance=int], [explicitTessellationAttributes=boolean], [name=string],
    [nodeState=int], [object=boolean], [smoothEdge=boolean], [smoothEdgeRatio=float],
    [uDivisionsFactor=float], [vDivisionsFactor=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPoly.html
    """
    return _wrapCommand(cmds.nurbsToPoly, args, kwargs)


def nurbsToPolygonsPref(*args, **kwargs):  # noqa
    """This command sets the values used by the nurbs-to-polygons (or "tesselate") preference.

    nurbsToPolygonsPref([chordHeight=float], [chordHeightRatio=float], [delta3D=float],
    [edgeSwap=boolean], [format=uint], [fraction=float], [matchRenderTessellation=uint],
    [merge=uint], [mergeTolerance=float], [minEdgeLen=float], [polyCount=uint],
    [polyType=uint], [uNumber=uint], [uType=uint], [useChordHeight=boolean],
    [useChordHeightRatio=boolean], [vNumber=uint], [vType=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsToPolygonsPref.html
    """
    return _wrapCommand(cmds.nurbsToPolygonsPref, args, kwargs)


def nurbsToSubdiv(*args, **kwargs):  # noqa
    """This command converts a NURBS surface and produces a subd surface.

    nurbsToSubdiv( [surface] , [addUnderTransform=boolean], [caching=boolean],
    [collapsePoles=boolean], [constructionHistory=boolean], [matchPeriodic=boolean],
    [maxPolyCount=int], [name=string], [nodeState=int], [object=boolean],
    [reverseNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdiv.html
    """
    return _wrapCommand(cmds.nurbsToSubdiv, args, kwargs)


def nurbsToSubdivPref(*args, **kwargs):  # noqa
    """This command sets the values used by the nurbs-to-subdivision surface preference.

    nurbsToSubdivPref([bridge=int], [capType=int], [collapsePoles=boolean],
    [matchPeriodic=boolean], [maxPolyCount=int], [offset=linear], [reverseNormal=boolean],
    [solidType=int], [trans00=float], [trans01=float], [trans02=float], [trans10=float],
    [trans11=float], [trans12=float], [trans20=float], [trans21=float], [trans22=float],
    [trans30=float], [trans31=float], [trans32=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsToSubdivPref.html
    """
    return _wrapCommand(cmds.nurbsToSubdivPref, args, kwargs)


def nurbsUVSet(*args, **kwargs):  # noqa
    """Allows user to toggle between implicit and explicit UVs on a NURBS object.

    nurbsUVSet([create=boolean], [useExplicit=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/nurbsUVSet.html
    """
    return _wrapCommand(cmds.nurbsUVSet, args, kwargs)


def objectCenter(*args, **kwargs):  # noqa
    """This command returns the coordinates of the center of the bounding box of the specified
    object.

    objectCenter( object , [gl=boolean], [local=boolean], [x=boolean], [y=boolean],
    [z=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/objectCenter.html
    """
    return _wrapCommand(cmds.objectCenter, args, kwargs)


def objectType(*args, **kwargs):  # noqa
    """This command returns the type of elements.

    objectType( object , [isAType=string], [isType=string], [tagFromType=string],
    [typeFromTag=int], [typeTag=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/objectType.html
    """
    return _wrapCommand(cmds.objectType, args, kwargs)


def objectTypeUI(*args, **kwargs):  # noqa
    """This command returns the type of UI element such as button, sliders, etc.

    objectTypeUI( string , [isType=string], [listAll=boolean], [superClasses=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/objectTypeUI.html
    """
    return _wrapCommand(cmds.objectTypeUI, args, kwargs)


def objExists(*args, **kwargs):  # noqa
    """This command simply returns true or false depending on whether an object with the given
    name exists.

    objExists( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/objExists.html
    """
    return _wrapCommand(cmds.objExists, args, kwargs)


def offsetCurve(*args, **kwargs):  # noqa
    """The offset command creates new offset curves from the selected curves.

    offsetCurve( [curve] , [caching=boolean], [connectBreaks=int],
    [constructionHistory=boolean], [cutLoop=boolean], [cutRadius=linear],
    [distance=linear], [name=string], [nodeState=int], [normal=[linear, linear, linear]],
    [object=boolean], [range=boolean], [reparameterize=boolean], [stitch=boolean],
    [subdivisionDensity=int], [tolerance=linear], [useGivenNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/offsetCurve.html
    """
    return _wrapCommand(cmds.offsetCurve, args, kwargs)


def offsetCurveOnSurface(*args, **kwargs):  # noqa
    """The offsetCurveOnSurface command offsets a curve on surface resulting in another curve on
    surface.

    offsetCurveOnSurface( [curve] , [caching=boolean], [checkPoints=int], [connectBreaks=int],
    [constructionHistory=boolean], [cutLoop=boolean], [distance=linear], [name=string],
    [nodeState=int], [object=boolean], [range=boolean], [stitch=boolean],
    [subdivisionDensity=int], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/offsetCurveOnSurface.html
    """
    return _wrapCommand(cmds.offsetCurveOnSurface, args, kwargs)


def offsetSurface(*args, **kwargs):  # noqa
    """The offset command creates new offset surfaces from the selected surfaces.

    offsetSurface( [surface] , [caching=boolean], [constructionHistory=boolean],
    [distance=linear], [method=int], [name=string], [nodeState=int], [object=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/offsetSurface.html
    """
    return _wrapCommand(cmds.offsetSurface, args, kwargs)


def ogs(*args, **kwargs):  # noqa
    """OGS is one of the viewport renderers.

    ogs([deviceInformation=boolean], [disposeReleasableTextures=boolean],
    [dumpTexture=string], [enableHardwareInstancing=boolean], [fragmentEditor=string],
    [fragmentXML=string], [gpuMemoryTotal=int], [gpuMemoryUsed=boolean],
    [isLegacyViewportEnabled=boolean], [isRemoteGLSessionEnabled=boolean],
    [isWinRemoteSession=boolean], [pause=boolean], [rebakeTextures=boolean],
    [regenerateUVTilePreview=string], [reloadTextures=boolean], [reset=boolean],
    [shaderSource=string], [toggleTexturePaging=boolean], [traceRenderPipeline=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ogs.html
    """
    return _wrapCommand(cmds.ogs, args, kwargs)


def ogsRender(*args, **kwargs):  # noqa
    """Renders an image or a sequence using the OGS rendering engine.

    ogsRender([activeMultisampleType=string], [activeRenderOverride=string],
    [activeRenderTargetFormat=string], [availableFloatingPointTargetFormat=boolean],
    [availableMultisampleType=boolean], [availableRenderOverrides=boolean],
    [camera=string], [currentFrame=boolean], [currentView=boolean],
    [enableFloatingPointRenderTarget=boolean], [enableMultisample=boolean], [frame=float],
    [height=uint], [layer=name], [noRenderView=boolean], [width=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ogsRender.html
    """
    return _wrapCommand(cmds.ogsRender, args, kwargs)


def openCLInfo(*args, **kwargs):  # noqa
    """Query OpenCL information.

    openCLInfo([minVertexBuffer=boolean], [valid=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/openCLInfo.html
    """
    return _wrapCommand(cmds.openCLInfo, args, kwargs)


def openGLExtension(*args, **kwargs):  # noqa
    """Command returns the extension name depending on whether a given OpenGL extension is
    supported or not.

    openGLExtension([extension=string], [renderer=boolean], [vendor=boolean],
    [version=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/openGLExtension.html
    """
    return _wrapCommand(cmds.openGLExtension, args, kwargs)


def openMayaPref(*args, **kwargs):  # noqa
    """Set or query API preferences.

    openMayaPref([errlog=boolean], [lazyLoad=boolean], [oldPluginWarning=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/openMayaPref.html
    """
    return _wrapCommand(cmds.openMayaPref, args, kwargs)


def optionMenu(*args, **kwargs):  # noqa
    """This command creates a popup menu control.

    optionMenu( [string] , [alwaysCallChangeCommand=boolean], [annotation=string],
    [backgroundColor=[float, float, float]], [beforeShowPopup=script],
    [changeCommand=script], [defineTemplate=string], [deleteAllItems=boolean],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [itemListLong=boolean], [itemListShort=boolean], [label=string],
    [manage=boolean], [maxVisibleItems=int], [noBackground=boolean],
    [numberOfItems=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [postMenuCommand=script], [postMenuCommandOnce=boolean],
    [preventOverride=boolean], [select=int], [statusBarMessage=string],
    [useTemplate=string], [value=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/optionMenu.html
    """
    return _wrapCommand(cmds.optionMenu, args, kwargs)


def optionMenuGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    optionMenuGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [deleteAllItems=boolean], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [extraLabel=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [itemListLong=boolean], [itemListShort=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfItems=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [postMenuCommand=script], [postMenuCommandOnce=boolean], [preventOverride=boolean],
    [rowAttach=[int, string, int]], [select=int], [statusBarMessage=string],
    [useTemplate=string], [value=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/optionMenuGrp.html
    """
    return _wrapCommand(cmds.optionMenuGrp, args, kwargs)


def optionVar(*args, **kwargs):  # noqa
    """This command allows you to set and query variables which are persistent between different
    invocations of Maya.

    optionVar([arraySize=string], [category=string], [clearArray=string], [clearStash=string],
    [default=boolean], [exists=string], [floatArray=string], [floatValue=[string, float]],
    [floatValue2=[string, float, float]], [floatValue3=[string, float, float, float]],
    [floatValue4=[string, float, float, float, float]], [floatValueAppend=[string,
    float]], [init=boolean], [intArray=string], [intValue=[string, int]],
    [intValue2=[string, int, int]], [intValue3=[string, int, int, int]],
    [intValue4=[string, int, int, int, int]], [intValueAppend=[string, int]],
    [list=boolean], [listCategories=boolean], [listModified=boolean], [prefFile=string],
    [remove=string], [removeFromArray=[string, int]], [stash=string],
    [stringArray=string], [stringValue=[string, string]], [stringValueAppend=[string,
    string]], [transient=boolean], [unstash=string], [version=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/optionVar.html
    """
    return _wrapCommand(cmds.optionVar, args, kwargs)


def orbit(*args, **kwargs):  # noqa
    """The orbit command revolves the camera(s) horizontally and/or vertically in the perspective
    window.

    orbit( [camera] , [horizontalAngle=angle], [pivotPoint=[linear, linear, linear]],
    [rotationAngles=[angle, angle]], [verticalAngle=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/orbit.html
    """
    return _wrapCommand(cmds.orbit, args, kwargs)


def orbitCtx(*args, **kwargs):  # noqa
    """Create, edit, or query an orbit context.

    orbitCtx([alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [localOrbit=boolean], [name=string],
    [orbitScale=float], [toolName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/orbitCtx.html
    """
    return _wrapCommand(cmds.orbitCtx, args, kwargs)


def orientConstraint(*args, **kwargs):  # noqa
    """Constrain an object's orientation to match the orientation of the target or the average of
    a number of targets.

    orientConstraint( [target ...] [object] , [createCache=[float, float]],
    [deleteCache=boolean], [layer=string], [maintainOffset=boolean], [name=string],
    [offset=[float, float, float]], [remove=boolean], [skip=string], [targetList=boolean],
    [weight=float], [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/orientConstraint.html
    """
    return _wrapCommand(cmds.orientConstraint, args, kwargs)


def outlinerEditor(*args, **kwargs):  # noqa
    """This command creates an outliner editor which can be used to display a list of objects.

    outlinerEditor( editorName , [allowMultiSelection=boolean], [alwaysToggleSelect=boolean],
    [animLayerFilterOptions=string], [attrAlphaOrder=string], [attrFilter=string],
    [autoExpand=boolean], [autoExpandAnimatedShapes=boolean], [autoExpandLayers=boolean],
    [autoSelectNewObjects=boolean], [containersIgnoreFilters=boolean], [control=boolean],
    [defineTemplate=string], [directSelect=boolean], [displayMode=string],
    [doNotSelectNewObjects=boolean], [docTag=string], [dropIsParent=boolean],
    [editAttrName=boolean], [exists=boolean], [expandAllItems=boolean],
    [expandAllSelectedItems=boolean], [expandAttribute=boolean],
    [expandConnections=boolean], [expandObjects=boolean], [feedbackItemName=boolean],
    [feedbackRowNumber=boolean], [filter=string], [forceMainConnection=string],
    [getCurrentSetOfItem=int], [highlightActive=boolean], [highlightConnection=string],
    [highlightSecondary=boolean], [ignoreDagHierarchy=boolean],
    [ignoreHiddenAttribute=boolean], [ignoreOutlinerColor=boolean],
    [isChildSelected=name], [isSet=int], [isSetMember=int], [isUfeItem=int],
    [lockMainConnection=boolean], [longNames=boolean], [mainListConnection=string],
    [mapMotionTrails=boolean], [masterOutliner=string], [niceNames=boolean],
    [object=name], [organizeByClip=boolean], [organizeByLayer=boolean], [panel=string],
    [parent=string], [parentObject=boolean], [pinPlug=name], [refresh=boolean],
    [removeFromCurrentSet=int], [renameItem=int], [renameSelectedItem=boolean],
    [renderFilterActive=boolean], [renderFilterIndex=int], [renderFilterVisible=boolean],
    [selectCommand=script], [selectionConnection=string], [selectionOrder=string],
    [setFilter=string], [setsIgnoreFilters=boolean], [showAnimCurvesOnly=boolean],
    [showAnimLayerWeight=boolean], [showAssets=boolean], [showAssignedMaterials=boolean],
    [showAttrValues=boolean], [showAttributes=boolean], [showCompounds=boolean],
    [showConnected=boolean], [showContainedOnly=boolean], [showContainerContents=boolean],
    [showDagOnly=boolean], [showLeafs=boolean], [showMuteInfo=boolean],
    [showNamespace=boolean], [showNumericAttrsOnly=boolean],
    [showParentContainers=boolean], [showPinIcons=boolean],
    [showPublishedAsConnected=boolean], [showReferenceMembers=boolean],
    [showReferenceNodes=boolean], [showSelected=boolean], [showSetMembers=boolean],
    [showShapes=boolean], [showTextureNodesOnly=boolean], [showTimeEditor=boolean],
    [showUVAttrsOnly=boolean], [showUnitlessCurves=boolean], [showUpstreamCurves=boolean],
    [sortOrder=string], [stateString=boolean], [transmitFilters=boolean],
    [ufeFilter=[string, string]], [ufeFilterValue=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [unpinPlug=name], [updateMainConnection=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/outlinerEditor.html
    """
    return _wrapCommand(cmds.outlinerEditor, args, kwargs)


def outlinerPanel(*args, **kwargs):  # noqa
    """This command creates, edit and queries outliner panels which contain only an outliner
    editor.

    outlinerPanel( [panelName] , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [divider=int], [docTag=string], [editString=boolean],
    [exists=boolean], [init=boolean], [isUnique=boolean], [label=string],
    [menuBarRepeatLast=boolean], [menuBarVisible=boolean], [needsInit=boolean],
    [outlinerEditor=boolean], [parent=string], [popupMenuProcedure=script],
    [replacePanel=string], [tearOff=boolean], [tearOffCopy=string],
    [tearOffRestore=boolean], [unParent=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/outlinerPanel.html
    """
    return _wrapCommand(cmds.outlinerPanel, args, kwargs)


def outputWindow(*args, **kwargs):  # noqa
    """This command open the output window, if it exists.

    outputWindow([show=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/outputWindow.html
    """
    return _wrapCommand(cmds.outputWindow, args, kwargs)


def overrideModifier(*args, **kwargs):  # noqa
    """This command allows you to assign modifier key behaviour to other parts of the system.

    overrideModifier([clear=boolean], [press=string], [release=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/overrideModifier.html
    """
    return _wrapCommand(cmds.overrideModifier, args, kwargs)


def paintEffectsDisplay(*args, **kwargs):  # noqa
    """Command to set the global display methods for paint effects items.

    paintEffectsDisplay([meshDrawEnable=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/paintEffectsDisplay.html
    """
    return _wrapCommand(cmds.paintEffectsDisplay, args, kwargs)


def pairBlend(*args, **kwargs):  # noqa
    """The pairBlend node allows a weighted combinations of 2 inputs to be blended together.

    pairBlend([attribute=string], [input1=boolean], [input2=boolean], [node=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pairBlend.html
    """
    return _wrapCommand(cmds.pairBlend, args, kwargs)


def palettePort(*args, **kwargs):  # noqa
    """This command creates an array of color cells.

    palettePort( string , [actualTotal=int], [annotation=string], [backgroundColor=[float,
    float, float]], [changeCommand=script], [colorEditable=boolean], [colorEdited=script],
    [defineTemplate=string], [dimensions=[int, int]], [docTag=string],
    [dragCallback=script], [dropCallback=script], [editable=boolean], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [hsvValue=[int, int, float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [redraw=boolean], [rgbValue=[int,
    float, float, float]], [setCurCell=int], [statusBarMessage=string], [topDown=boolean],
    [transparent=int], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/palettePort.html
    """
    return _wrapCommand(cmds.palettePort, args, kwargs)


def panel(*args, **kwargs):  # noqa
    """This command allows editing or querying properties of any panels.

    panel( string , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean],
    [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/panel.html
    """
    return _wrapCommand(cmds.panel, args, kwargs)


def paneLayout(*args, **kwargs):  # noqa
    """This command creates a pane layout.

    paneLayout( [string] , [activeFrameThickness=int], [activePane=string],
    [activePaneIndex=int], [annotation=string], [backgroundColor=[float, float, float]],
    [childArray=boolean], [configuration=string], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfPopupMenus=boolean],
    [numberOfVisiblePanes=boolean], [pane1=boolean], [pane2=boolean], [pane3=boolean],
    [pane4=boolean], [paneSize=[int, int, int]], [paneUnderPointer=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [separatorMovedCommand=script], [separatorThickness=int], [setPane=[string, int]],
    [staticHeightPane=int], [staticWidthPane=int], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/paneLayout.html
    """
    return _wrapCommand(cmds.paneLayout, args, kwargs)


def panelConfiguration(*args, **kwargs):  # noqa
    """This command creates a panel configuration object.

    panelConfiguration( [name] , [addPanel=[boolean, string, string, string, string]],
    [configString=string], [createStrings=boolean], [defaultImage=string],
    [defineTemplate=string], [editStrings=boolean], [exists=boolean], [image=string],
    [isFixedState=boolean], [label=string], [labelStrings=boolean],
    [numberOfPanels=boolean], [removeAllPanels=boolean], [removeLastPanel=boolean],
    [replaceCreateString=[int, string]], [replaceEditString=[int, string]],
    [replaceFixedState=[int, boolean]], [replaceLabel=[int, string]], [replacePanel=[int,
    boolean, string, string, string, string]], [replaceTypeString=[int, string]],
    [sceneConfig=boolean], [typeStrings=boolean], [useTemplate=string],
    [userCreated=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/panelConfiguration.html
    """
    return _wrapCommand(cmds.panelConfiguration, args, kwargs)


def panelHistory(*args, **kwargs):  # noqa
    """This command creates a panel history object.

    panelHistory( [name] , [back=boolean], [clear=boolean], [defineTemplate=string],
    [exists=boolean], [forward=boolean], [historyDepth=int], [isEmpty=boolean],
    [suspend=boolean], [targetPane=string], [useTemplate=string], [wrap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/panelHistory.html
    """
    return _wrapCommand(cmds.panelHistory, args, kwargs)


def panZoom(*args, **kwargs):  # noqa
    """The panZoom command pans/zooms the 2D film.

    panZoom( [camera] , [absolute=boolean], [downDistance=float], [leftDistance=float],
    [relative=boolean], [rightDistance=float], [upDistance=float], [zoomRatio=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/panZoom.html
    """
    return _wrapCommand(cmds.panZoom, args, kwargs)


def panZoomCtx(*args, **kwargs):  # noqa
    """This command can be used to create camera 2D pan/zoom context.

    panZoomCtx([alternateContext=boolean], [buttonDown=boolean], [buttonUp=boolean],
    [exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string], [panMode=boolean], [toolName=string],
    [zoomMode=boolean], [zoomScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/panZoomCtx.html
    """
    return _wrapCommand(cmds.panZoomCtx, args, kwargs)


def paramDimContext(*args, **kwargs):  # noqa
    """Command used to register the paramDimCtx tool.

    paramDimContext([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/paramDimContext.html
    """
    return _wrapCommand(cmds.paramDimContext, args, kwargs)


def paramDimension(*args, **kwargs):  # noqa
    """This command is used to create a param dimension to display the parameter value of a
    curve/surface at a specified point on the curve/surface.

    paramDimension( [curve|surface] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/paramDimension.html
    """
    return _wrapCommand(cmds.paramDimension, args, kwargs)


def paramLocator(*args, **kwargs):  # noqa
    """The command creates a locator in the underworld of a NURBS curve or NURBS surface at the
    specified parameter value.

    paramLocator( [object] , [position=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/paramLocator.html
    """
    return _wrapCommand(cmds.paramLocator, args, kwargs)


def parent(*args, **kwargs):  # noqa
    """This command parents (moves) objects under a new group, removes objects from an existing
    group, or adds/removes parents.

    parent( [dagObject...] [dagObject] , [absolute=boolean], [addObject=boolean],
    [noConnections=boolean], [noInvScale=boolean], [relative=boolean],
    [removeObject=boolean], [shape=boolean], [world=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/parent.html
    """
    return _wrapCommand(cmds.parent, args, kwargs)


def parentConstraint(*args, **kwargs):  # noqa
    """Constrain an object's position and rotation so that it behaves as if it were a child of
    the target object(s).

    parentConstraint( [target ...] [object] , [createCache=[float, float]],
    [decompRotationToChild=boolean], [deleteCache=boolean], [layer=string],
    [maintainOffset=boolean], [name=string], [remove=boolean], [skipRotate=string],
    [skipTranslate=string], [targetList=boolean], [weight=float],
    [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/parentConstraint.html
    """
    return _wrapCommand(cmds.parentConstraint, args, kwargs)


def particle(*args, **kwargs):  # noqa
    """The particle command creates a new particle object from a list of world space points.

    particle( object , [attribute=string], [cache=boolean], [conserve=float], [count=boolean],
    [deleteCache=boolean], [dynamicAttrList=boolean], [floatValue=float],
    [gridSpacing=linear], [inherit=float], [jitterBasePoint=[linear, linear, linear]],
    [jitterRadius=linear], [lowerLeft=[linear, linear, linear]], [name=string],
    [numJitters=uint], [order=int], [particleId=int], [perParticleDouble=boolean],
    [perParticleVector=boolean], [position=[linear, linear, linear]], [shapeName=string],
    [upperRight=[linear, linear, linear]], [vectorValue=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/particle.html
    """
    return _wrapCommand(cmds.particle, args, kwargs)


def particleExists(*args, **kwargs):  # noqa
    """This command is used to query if a particle or soft object with the given name exists.

    particleExists( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/particleExists.html
    """
    return _wrapCommand(cmds.particleExists, args, kwargs)


def particleFill(*args, **kwargs):  # noqa
    """This command generates an nParticle system that fills the selected object with a grid of
    particles.

    particleFill([closePacking=boolean], [doubleWalled=boolean], [maxX=float], [maxY=float],
    [maxZ=float], [minX=float], [minY=float], [minZ=float], [particleDensity=float],
    [resolution=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/particleFill.html
    """
    return _wrapCommand(cmds.particleFill, args, kwargs)


def particleInstancer(*args, **kwargs):  # noqa
    """This command is used to create a particle instancer node and set the proper attributes in
    the particle shape and in the instancer node.

    particleInstancer([addObject=boolean], [aimAxis=string], [aimDirection=string],
    [aimPosition=string], [aimUpAxis=string], [aimWorldUp=string],
    [attributeMapping=boolean], [cycle=string], [cycleStartObject=string],
    [cycleStep=float], [cycleStepUnits=string], [index=int], [instanceId=string],
    [levelOfDetail=string], [name=string], [object=string], [objectIndex=string],
    [particleAge=string], [position=string], [removeObject=boolean], [rotation=string],
    [rotationOrder=string], [rotationType=string], [rotationUnits=string], [scale=string],
    [shear=string], [visibility=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/particleInstancer.html
    """
    return _wrapCommand(cmds.particleInstancer, args, kwargs)


def particleRenderInfo(*args, **kwargs):  # noqa
    """This action provides information access to the particle render subclasses.

    particleRenderInfo([attrList=int], [attrListAll=boolean], [name=int],
    [renderTypeCount=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/particleRenderInfo.html
    """
    return _wrapCommand(cmds.particleRenderInfo, args, kwargs)


def partition(*args, **kwargs):  # noqa
    """This command is used to create, query or add/remove sets to a partition.

    partition( [string] [string...] , [addSet=name], [name=string], [removeSet=name],
    [render=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/partition.html
    """
    return _wrapCommand(cmds.partition, args, kwargs)


def pasteKey(*args, **kwargs):  # noqa
    """The pasteKey command pastes curve segment hierarchies from the clipboard onto other
    objects or curves.

    pasteKey( [objects] , [animLayer=string], [animation=string], [attribute=string],
    [clipboard=string], [connect=boolean], [copies=uint], [float=floatrange],
    [floatOffset=float], [includeUpperBound=boolean], [index=uint], [matchByName=boolean],
    [option=string], [time=timerange], [timeOffset=time], [valueOffset=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pasteKey.html
    """
    return _wrapCommand(cmds.pasteKey, args, kwargs)


def pathAnimation(*args, **kwargs):  # noqa
    """The pathAnimation command constructs the necessary graph nodes and their interconnections
    for a motion path animation.

    pathAnimation( [objects] , [bank=boolean], [bankScale=float], [bankThreshold=angle],
    [curve=string], [endTimeU=time], [endU=float], [follow=boolean], [followAxis=string],
    [fractionMode=boolean], [inverseFront=boolean], [inverseUp=boolean], [name=string],
    [startTimeU=time], [startU=float], [upAxis=string], [useNormal=boolean],
    [worldUpObject=name], [worldUpType=string], [worldUpVector=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pathAnimation.html
    """
    return _wrapCommand(cmds.pathAnimation, args, kwargs)


def pause(*args, **kwargs):  # noqa
    """Pause for a specified number of seconds for canned demos or for test scripts to allow user
    to view results.

    pause([seconds=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pause.html
    """
    return _wrapCommand(cmds.pause, args, kwargs)


def perCameraVisibility(*args, **kwargs):  # noqa
    """The perCameraVisibility command creates, queries and removes visibility relationships
    between DAG objects and cameras.

    perCameraVisibility([camera=name], [exclusive=boolean], [hide=boolean], [remove=boolean],
    [removeAll=boolean], [removeCamera=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/perCameraVisibility.html
    """
    return _wrapCommand(cmds.perCameraVisibility, args, kwargs)


def percent(*args, **kwargs):  # noqa
    """This command sets percent values on members of a weighted node such as a cluster or a
    jointCluster.

    percent( node [objects] , [addPercent=boolean], [dropoffAxis=[linear, linear, linear]],
    [dropoffCurve=string], [dropoffDistance=linear], [dropoffPosition=[linear, linear,
    linear]], [dropoffType=string], [multiplyPercent=boolean], [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/percent.html
    """
    return _wrapCommand(cmds.percent, args, kwargs)


def performanceOptions(*args, **kwargs):  # noqa
    """Sets the global performance options for the application.

    performanceOptions([clusterResolution=float], [disableStitch=string],
    [disableTrimBoundaryDisplay=string], [disableTrimDisplay=string],
    [latticeResolution=float], [passThroughBindSkinAndFlexors=string],
    [passThroughBlendShape=string], [passThroughCluster=string],
    [passThroughDeltaMush=string], [passThroughFlexors=string],
    [passThroughLattice=string], [passThroughMeshBoolean=string],
    [passThroughPaintEffects=string], [passThroughSculpt=string],
    [passThroughWire=string], [regionOfEffect=string], [skipHierarchyTraversal=boolean],
    [useClusterResolution=string], [useLatticeResolution=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/performanceOptions.html
    """
    return _wrapCommand(cmds.performanceOptions, args, kwargs)


def pfxstrokes(*args, **kwargs):  # noqa
    """This command will loop through all the Paint Effects strokes, including pfxHair nodes, and
    write the current state of all the tubes to a file.

    pfxstrokes([filename=string], [postCallback=boolean], [selected=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pfxstrokes.html
    """
    return _wrapCommand(cmds.pfxstrokes, args, kwargs)


def pickWalk(*args, **kwargs):  # noqa
    """The pickWalk command allows you to quickly change the selection list relative to the nodes
    that are currently selected.

    pickWalk( [objects] , [direction=string], [recurse=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pickWalk.html
    """
    return _wrapCommand(cmds.pickWalk, args, kwargs)


def picture(*args, **kwargs):  # noqa
    """This command creates a static image.

    picture( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [isObscured=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [tile=boolean], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/picture.html
    """
    return _wrapCommand(cmds.picture, args, kwargs)


def pixelMove(*args, **kwargs):  # noqa
    """The pixelMove command moves objects by what appears as pixel units based on the current
    view.

    pixelMove( float float )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pixelMove.html
    """
    return _wrapCommand(cmds.pixelMove, args, kwargs)


def planarSrf(*args, **kwargs):  # noqa
    """This command computes a planar trimmed surface given planar boundary curves that form a
    closed region.

    planarSrf( objects , [caching=boolean], [constructionHistory=boolean], [degree=int],
    [keepOutside=boolean], [name=string], [nodeState=int], [object=boolean],
    [polygon=int], [range=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/planarSrf.html
    """
    return _wrapCommand(cmds.planarSrf, args, kwargs)


def plane(*args, **kwargs):  # noqa
    """The command creates a sketch plane (also known as a "construction plane") in space.

    plane([length=linear], [name=string], [position=[linear, linear, linear]],
    [rotation=[angle, angle, angle]], [size=linear], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/plane.html
    """
    return _wrapCommand(cmds.plane, args, kwargs)


def play(*args, **kwargs):  # noqa
    """This command starts and stops playback.

    play([forward=boolean], [playSound=boolean], [record=boolean], [sound=string],
    [state=boolean], [wait=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/play.html
    """
    return _wrapCommand(cmds.play, args, kwargs)


def playbackOptions(*args, **kwargs):  # noqa
    """This command sets/queries certain values associated with playback: looping style,
    start/end times, etc.

    playbackOptions([animationEndTime=time], [animationStartTime=time],
    [blockingAnim=boolean], [by=float], [framesPerSecond=boolean], [loop=string],
    [maxPlaybackSpeed=float], [maxTime=time], [minTime=time], [playbackSpeed=float],
    [stepLoop=boolean], [view=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/playbackOptions.html
    """
    return _wrapCommand(cmds.playbackOptions, args, kwargs)


def playblast(*args, **kwargs):  # noqa
    """This command playblasts the current playback range.

    playblast( filename , [activeEditor=boolean], [cameraSetup=[string, string]],
    [clearCache=boolean], [codecOptions=boolean], [combineSound=boolean],
    [completeFilename=string], [compression=string], [editorPanelName=string],
    [endTime=time], [filename=string], [forceOverwrite=boolean], [format=string],
    [frame=time], [framePadding=int], [height=int], [indexFromZero=boolean],
    [offScreen=boolean], [offScreenViewportUpdate=boolean], [options=boolean],
    [percent=int], [quality=int], [rawFrameNumbers=boolean], [replaceAudioOnly=boolean],
    [replaceEndTime=time], [replaceFilename=string], [replaceStartTime=time],
    [sequenceTime=boolean], [showOrnaments=boolean], [sound=string], [startTime=time],
    [throwOnError=boolean], [useTraxSounds=boolean], [viewer=boolean], [width=int],
    [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/playblast.html
    """
    return _wrapCommand(cmds.playblast, args, kwargs)


def pluginDisplayFilter(*args, **kwargs):  # noqa
    """Register, deregister or query a plugin display filter.

    pluginDisplayFilter([classification=string], [deregister=boolean], [exists=boolean],
    [label=string], [listFilters=boolean], [register=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pluginDisplayFilter.html
    """
    return _wrapCommand(cmds.pluginDisplayFilter, args, kwargs)


def pluginInfo(*args, **kwargs):  # noqa
    """This command provides access to the plug-in registry of the application.

    pluginInfo( [string] , [activeFile=boolean], [allEvaluators=boolean],
    [animCurveInterp=string], [apiVersion=boolean], [autoload=boolean],
    [cacheFormat=boolean], [changedCommand=script], [command=string],
    [constraintCommand=boolean], [controlCommand=boolean], [data=[string, string]],
    [dependNode=boolean], [dependNodeByType=string], [dependNodeId=string],
    [device=boolean], [dragAndDropBehavior=boolean], [evaluator=boolean],
    [iksolver=boolean], [listPlugins=boolean], [listPluginsPath=boolean],
    [loadPluginPrefs=boolean], [loaded=boolean], [modelEditorCommand=boolean],
    [name=string], [path=string], [pluginsInUse=boolean], [referenceTranslators=boolean],
    [registered=boolean], [remove=boolean], [renderer=boolean], [savePluginPrefs=boolean],
    [serviceDescriptions=boolean], [settings=boolean], [tool=string],
    [translator=boolean], [unloadOk=boolean], [userNamed=boolean], [vendor=string],
    [version=boolean], [writeRequires=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pluginInfo.html
    """
    return _wrapCommand(cmds.pluginInfo, args, kwargs)


def pointConstraint(*args, **kwargs):  # noqa
    """Constrain an object's position to the position of the target object or to the average
    position of a number of targets.

    pointConstraint( [target...] [object] , [layer=string], [maintainOffset=boolean],
    [name=string], [offset=[float, float, float]], [remove=boolean], [skip=string],
    [targetList=boolean], [weight=float], [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointConstraint.html
    """
    return _wrapCommand(cmds.pointConstraint, args, kwargs)


def pointCurveConstraint(*args, **kwargs):  # noqa
    """The command enables direct manipulation of a NURBS curve.

    pointCurveConstraint( selectionItem , [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [object=boolean], [pointConstraintUVW=[float, float,
    float]], [pointWeight=float], [position=[float, float, float]],
    [replaceOriginal=boolean], [weight=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointCurveConstraint.html
    """
    return _wrapCommand(cmds.pointCurveConstraint, args, kwargs)


def pointLight(*args, **kwargs):  # noqa
    """The pointLight command is used to edit the parameters of existing pointLights, or to
    create new ones.

    pointLight([decayRate=int], [discRadius=linear], [exclusive=boolean], [intensity=float],
    [name=string], [position=[linear, linear, linear]], [rgb=[float, float, float]],
    [rotation=[angle, angle, angle]], [shadowColor=[float, float, float]],
    [shadowDither=float], [shadowSamples=int], [softShadow=boolean],
    [useRayTraceShadows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointLight.html
    """
    return _wrapCommand(cmds.pointLight, args, kwargs)


def pointOnCurve(*args, **kwargs):  # noqa
    """This command returns information for a point on a NURBS curve.

    pointOnCurve( [objects] , [caching=boolean], [constructionHistory=boolean],
    [curvatureCenter=boolean], [curvatureRadius=boolean], [nodeState=int],
    [normal=boolean], [normalizedNormal=boolean], [normalizedTangent=boolean],
    [parameter=float], [position=boolean], [tangent=boolean], [turnOnPercentage=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointOnCurve.html
    """
    return _wrapCommand(cmds.pointOnCurve, args, kwargs)


def pointOnPolyConstraint(*args, **kwargs):  # noqa
    """Constrain an object's position to the position of the target object or to the average
    position of a number of targets.

    pointOnPolyConstraint( [target...] [object] , [layer=string], [maintainOffset=boolean],
    [name=string], [offset=[float, float, float]], [remove=boolean], [skip=string],
    [targetList=boolean], [weight=float], [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointOnPolyConstraint.html
    """
    return _wrapCommand(cmds.pointOnPolyConstraint, args, kwargs)


def pointOnSurface(*args, **kwargs):  # noqa
    """This command returns information for a point on a surface.

    pointOnSurface( [objects] , [caching=boolean], [constructionHistory=boolean],
    [nodeState=int], [normal=boolean], [normalizedNormal=boolean],
    [normalizedTangentU=boolean], [normalizedTangentV=boolean], [parameterU=float],
    [parameterV=float], [position=boolean], [tangentU=boolean], [tangentV=boolean],
    [turnOnPercentage=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointOnSurface.html
    """
    return _wrapCommand(cmds.pointOnSurface, args, kwargs)


def pointPosition(*args, **kwargs):  # noqa
    """This command returns the world or local space position for any type of point object.

    pointPosition( [object] , [local=boolean], [world=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pointPosition.html
    """
    return _wrapCommand(cmds.pointPosition, args, kwargs)


def poleVectorConstraint(*args, **kwargs):  # noqa
    """Constrains the poleVector of an ikRPsolve handle to point at a target object or at the
    average position of a number of targets.

    poleVectorConstraint( [target ...] [object] , [layer=string], [name=string],
    [remove=boolean], [targetList=boolean], [weight=float], [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/poleVectorConstraint.html
    """
    return _wrapCommand(cmds.poleVectorConstraint, args, kwargs)


def polyAppend(*args, **kwargs):  # noqa
    """Appends a new face to the selected polygonal object.

    polyAppend([append=[[, float, float, float, ]]], [constructionHistory=boolean],
    [edge=int], [hole=boolean], [name=string], [point=[float, float, float]],
    [subdivision=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAppend.html
    """
    return _wrapCommand(cmds.polyAppend, args, kwargs)


def polyAppendFacetCtx(*args, **kwargs):  # noqa
    """Create a new context to append facets on polygonal objects.

    polyAppendFacetCtx([append=boolean], [exists=boolean], [image1=string], [image2=string],
    [image3=string], [isRotateAvailable=boolean], [maximumNumberOfPoints=int],
    [planarConstraint=boolean], [rotate=float], [subdivision=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAppendFacetCtx.html
    """
    return _wrapCommand(cmds.polyAppendFacetCtx, args, kwargs)


def polyAppendVertex(*args, **kwargs):  # noqa
    """Appends a new face to the selected polygonal object.

    polyAppendVertex([append=[[, float, float, float, ]]], [constructionHistory=boolean],
    [hole=boolean], [name=string], [point=[float, float, float]], [texture=int],
    [vertex=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAppendVertex.html
    """
    return _wrapCommand(cmds.polyAppendVertex, args, kwargs)


def polyAutoProjection(*args, **kwargs):  # noqa
    """Projects a map onto an object, using several orthogonal projections simultaneously.

    polyAutoProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [insertBeforeDeformers=boolean], [layout=int],
    [layoutMethod=int], [name=string], [nodeState=int], [optimize=int],
    [percentageSpace=float], [pivot=[linear, linear, linear]], [pivotX=linear],
    [pivotY=linear], [pivotZ=linear], [planes=int], [projectBothDirections=boolean],
    [rotate=[angle, angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle],
    [scale=[float, float, float]], [scaleMode=int], [scaleX=float], [scaleY=float],
    [scaleZ=float], [skipIntersect=boolean], [translate=[linear, linear, linear]],
    [translateX=linear], [translateY=linear], [translateZ=linear], [uvSetName=string],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAutoProjection.html
    """
    return _wrapCommand(cmds.polyAutoProjection, args, kwargs)


def polyAverageNormal(*args, **kwargs):  # noqa
    """Set normals of vertices or vertex-faces to an average value when the vertices within a
    given threshold.

    polyAverageNormal([allowZeroNormal=boolean], [distance=float], [postnormalize=boolean],
    [prenormalize=boolean], [replaceNormalXYZ=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAverageNormal.html
    """
    return _wrapCommand(cmds.polyAverageNormal, args, kwargs)


def polyAverageVertex(*args, **kwargs):  # noqa
    """Moves the selected vertices of a polygonal object to round its shape.

    polyAverageVertex( selectionList , [caching=boolean], [constructionHistory=boolean],
    [iterations=int], [name=string], [nodeState=int], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyAverageVertex.html
    """
    return _wrapCommand(cmds.polyAverageVertex, args, kwargs)


def polyBevel(*args, **kwargs):  # noqa
    """Bevel edges.

    polyBevel([angleTolerance=float], [autoFit=boolean], [caching=boolean],
    [constructionHistory=boolean], [mergeVertexTolerance=linear], [mergeVertices=boolean],
    [miteringAngle=float], [name=string], [nodeState=int], [offset=linear],
    [offsetAsFraction=boolean], [roundness=float], [segments=int], [smoothingAngle=float],
    [subdivideNgons=boolean], [useLegacyBevelAlgorithm=boolean], [uvAssignment=int],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBevel.html
    """
    return _wrapCommand(cmds.polyBevel, args, kwargs)


def polyBevel3(*args, **kwargs):  # noqa
    """Bevel edges.

    polyBevel3([angleTolerance=float], [autoFit=boolean], [caching=boolean],
    [chamfer=boolean], [constructionHistory=boolean], [depth=float], [fillNgons=boolean],
    [mergeVertexTolerance=linear], [mergeVertices=boolean], [miterAlong=int],
    [mitering=int], [miteringAngle=float], [name=string], [nodeState=int],
    [offset=linear], [offsetAsFraction=boolean], [roundness=float], [segments=int],
    [smoothingAngle=float], [uvAssignment=int], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBevel3.html
    """
    return _wrapCommand(cmds.polyBevel3, args, kwargs)


def polyBlendColor(*args, **kwargs):  # noqa
    """Takes two color sets and blends them together into a third specified color set.

    polyBlendColor([baseColorName=string], [blendFunc=int], [blendWeightA=float],
    [blendWeightB=float], [blendWeightC=float], [blendWeightD=float], [caching=boolean],
    [constructionHistory=boolean], [dstColorName=string], [name=string], [nodeState=int],
    [srcColorName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBlendColor.html
    """
    return _wrapCommand(cmds.polyBlendColor, args, kwargs)


def polyBlindData(*args, **kwargs):  # noqa
    """Command creates blindData types (basically creates an instance of TdnPolyBlindData).

    polyBlindData([associationType=string], [binaryData=string], [booleanData=boolean],
    [delete=boolean], [doubleData=float], [int64Data=int64], [intData=int],
    [longDataName=string], [rescan=boolean], [reset=boolean], [shape=boolean],
    [shortDataName=string], [stringData=string], [typeId=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBlindData.html
    """
    return _wrapCommand(cmds.polyBlindData, args, kwargs)


def polyBoolOp(*args, **kwargs):  # noqa
    """This command creates a new poly as the result of a boolean operation on input polys :
    union, intersection, difference.

    polyBoolOp( poly poly , [caching=boolean], [faceAreaThreshold=linear], [mergeUVSets=int],
    [nodeState=int], [operation=int], [preserveColor=boolean], [useThresholds=boolean],
    [vertexDistanceThreshold=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBoolOp.html
    """
    return _wrapCommand(cmds.polyBoolOp, args, kwargs)


def polyBridgeEdge(*args, **kwargs):  # noqa
    """Bridges two sets of edges.

    polyBridgeEdge([bridgeOffset=int], [caching=boolean], [constructionHistory=boolean],
    [curveType=int], [divisions=int], [inputCurve=name], [name=string], [nodeState=int],
    [smoothingAngle=angle], [startVert1=int], [startVert2=int], [taper=float],
    [taperCurve_FloatValue=float], [taperCurve_Interp=int], [taperCurve_Position=float],
    [twist=angle], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyBridgeEdge.html
    """
    return _wrapCommand(cmds.polyBridgeEdge, args, kwargs)


def polyCacheMonitor(*args, **kwargs):  # noqa
    """When the cacheInput attribute has a positive value the midModifier node caches the output
    mesh improving performance in computations of downstream nodes.

    polyCacheMonitor([cacheValue=boolean], [nodeName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCacheMonitor.html
    """
    return _wrapCommand(cmds.polyCacheMonitor, args, kwargs)


def polyCanBridgeEdge(*args, **kwargs):  # noqa
    """Returns true if the specified poly edges can be bridged using polyBridgeEdge.

    polyCanBridgeEdge( poly poly... )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCanBridgeEdge.html
    """
    return _wrapCommand(cmds.polyCanBridgeEdge, args, kwargs)


def polyCBoolOp(*args, **kwargs):  # noqa
    """This command creates a new poly as the result of a boolean operation on input polys :
    union, intersection, difference.

    polyCBoolOp( poly poly , [caching=boolean], [classification=int],
    [faceAreaThreshold=linear], [mergeUVSets=int], [nodeState=int], [operation=int],
    [preserveColor=boolean], [tagIntersection=boolean], [useCarveBooleans=boolean],
    [useThresholds=boolean], [vertexDistanceThreshold=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCBoolOp.html
    """
    return _wrapCommand(cmds.polyCBoolOp, args, kwargs)


def polyCheck(*args, **kwargs):  # noqa
    """Dumps a description of internal memory representation of poly objects.

    polyCheck( poly poly... , [edge=boolean], [face=boolean], [faceOffset=boolean],
    [openFile=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCheck.html
    """
    return _wrapCommand(cmds.polyCheck, args, kwargs)


def polyChipOff(*args, **kwargs):  # noqa
    """Extract facets.

    polyChipOff([attraction=float], [caching=boolean], [constructionHistory=boolean],
    [duplicate=boolean], [gain=float], [gravity=[linear, linear, linear]],
    [gravityX=linear], [gravityY=linear], [gravityZ=linear], [keepFacesTogether=boolean],
    [keepFacetTogether=boolean], [localCenter=int], [localDirection=[linear, linear,
    linear]], [localDirectionX=linear], [localDirectionY=linear],
    [localDirectionZ=linear], [localRotate=[angle, angle, angle]], [localRotateX=angle],
    [localRotateY=angle], [localRotateZ=angle], [localScale=[float, float, float]],
    [localScaleX=float], [localScaleY=float], [localScaleZ=float],
    [localTranslate=[linear, linear, linear]], [localTranslateX=linear],
    [localTranslateY=linear], [localTranslateZ=linear], [magnX=linear], [magnY=linear],
    [magnZ=linear], [magnet=[linear, linear, linear]], [name=string], [nodeState=int],
    [offset=float], [pivot=[linear, linear, linear]], [pivotX=linear], [pivotY=linear],
    [pivotZ=linear], [random=float], [scale=[float, float, float]], [scaleX=float],
    [scaleY=float], [scaleZ=float], [translate=[linear, linear, linear]],
    [translateX=linear], [translateY=linear], [translateZ=linear], [weight=float],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyChipOff.html
    """
    return _wrapCommand(cmds.polyChipOff, args, kwargs)


def polyCircularize(*args, **kwargs):  # noqa
    """Mirror all the faces of the selected object.

    polyCircularize([alignment=int], [caching=boolean], [constructionHistory=boolean],
    [createCurve=boolean], [evenlyDistribute=boolean], [inputCurve=name], [name=string],
    [nodeState=int], [normalOrientation=int], [radialOffset=float],
    [smoothingAngle=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCircularize.html
    """
    return _wrapCommand(cmds.polyCircularize, args, kwargs)


def polyCircularizeEdge(*args, **kwargs):  # noqa
    """Mirror all the faces of the selected object.

    polyCircularizeEdge([alignment=int], [caching=boolean], [constructionHistory=boolean],
    [createCurve=boolean], [evenlyDistribute=boolean], [inputCurve=name], [name=string],
    [nodeState=int], [normalOrientation=int], [radialOffset=float],
    [smoothingAngle=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCircularizeEdge.html
    """
    return _wrapCommand(cmds.polyCircularizeEdge, args, kwargs)


def polyCircularizeFace(*args, **kwargs):  # noqa
    """Mirror all the faces of the selected object.

    polyCircularizeFace([alignment=int], [caching=boolean], [constructionHistory=boolean],
    [createCurve=boolean], [evenlyDistribute=boolean], [inputCurve=name], [name=string],
    [nodeState=int], [normalOrientation=int], [radialOffset=float],
    [smoothingAngle=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCircularizeFace.html
    """
    return _wrapCommand(cmds.polyCircularizeFace, args, kwargs)


def polyClean(*args, **kwargs):  # noqa
    """polyClean will attempt to remove components that are invalid in the description of a poly
    mesh.

    polyClean([caching=boolean], [cleanEdges=boolean], [cleanPartialUVMapping=boolean],
    [cleanUVs=boolean], [cleanVertices=boolean], [constructionHistory=boolean],
    [frozen=boolean], [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyClean.html
    """
    return _wrapCommand(cmds.polyClean, args, kwargs)


def polyClipboard(*args, **kwargs):  # noqa
    """The command allows the user to copy and paste certain polygonal attributes to a clipboard.

    polyClipboard([clear=boolean], [color=boolean], [copy=boolean], [paste=boolean],
    [shader=boolean], [uvCoordinates=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyClipboard.html
    """
    return _wrapCommand(cmds.polyClipboard, args, kwargs)


def polyCloseBorder(*args, **kwargs):  # noqa
    """Closes open borders of objects.

    polyCloseBorder([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCloseBorder.html
    """
    return _wrapCommand(cmds.polyCloseBorder, args, kwargs)


def polyCollapseEdge(*args, **kwargs):  # noqa
    """Turns each selected edge into a point.

    polyCollapseEdge([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseEdge.html
    """
    return _wrapCommand(cmds.polyCollapseEdge, args, kwargs)


def polyCollapseFacet(*args, **kwargs):  # noqa
    """Turns each selected facet into a point.

    polyCollapseFacet([areaThreshold=float], [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [useAreaThreshold=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseFacet.html
    """
    return _wrapCommand(cmds.polyCollapseFacet, args, kwargs)


def polyCollapseTweaks(*args, **kwargs):  # noqa
    """A command that updates a mesh's vertex tweaks by applying its tweak data (stored on the
    mesh node) onto its respective vertex data.

    polyCollapseTweaks([hasVertexTweaks=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCollapseTweaks.html
    """
    return _wrapCommand(cmds.polyCollapseTweaks, args, kwargs)


def polyColorBlindData(*args, **kwargs):  # noqa
    """This command applies false color to the selected polygonal components and objects,
    depending on whether or not blind data exists for the selected components (or, in the
    case of poly objects, dynamic attributes), and, depending on the color mode indicated,
    what the values are.

    polyColorBlindData([aboveMaxColorBlue=float], [aboveMaxColorGreen=float],
    [aboveMaxColorRed=float], [attrName=string], [belowMinColorBlue=float],
    [belowMinColorGreen=float], [belowMinColorRed=float], [clashColorBlue=float],
    [clashColorGreen=float], [clashColorRed=float], [colorBlue=float], [colorGreen=float],
    [colorRed=float], [dataType=string], [enableFalseColor=boolean], [maxColorBlue=float],
    [maxColorGreen=float], [maxColorRed=float], [maxValue=float], [minColorBlue=float],
    [minColorGreen=float], [minColorRed=float], [minValue=float], [mode=int],
    [noColorBlue=float], [noColorGreen=float], [noColorRed=float], [numIdTypes=int],
    [queryMode=boolean], [typeId=int], [useMax=boolean], [useMin=boolean], [value=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyColorBlindData.html
    """
    return _wrapCommand(cmds.polyColorBlindData, args, kwargs)


def polyColorDel(*args, **kwargs):  # noqa
    """Deletes color from selected components.

    polyColorDel([caching=boolean], [colorSetName=string], [constructionHistory=boolean],
    [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyColorDel.html
    """
    return _wrapCommand(cmds.polyColorDel, args, kwargs)


def polyColorMod(*args, **kwargs):  # noqa
    """Modifies the attributes of a poly color set.

    polyColorMod([alphaScale_FloatValue=float], [alphaScale_Interp=int],
    [alphaScale_Position=float], [baseColorName=string], [blueScale_FloatValue=float],
    [blueScale_Interp=int], [blueScale_Position=float], [caching=boolean],
    [constructionHistory=boolean], [greenScale_FloatValue=float], [greenScale_Interp=int],
    [greenScale_Position=float], [huev=float], [intensityScale_FloatValue=float],
    [intensityScale_Interp=int], [intensityScale_Position=float], [name=string],
    [nodeState=int], [redScale_FloatValue=float], [redScale_Interp=int],
    [redScale_Position=float], [satv=float], [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyColorMod.html
    """
    return _wrapCommand(cmds.polyColorMod, args, kwargs)


def polyColorPerVertex(*args, **kwargs):  # noqa
    """Command associates color(rgb and alpha) with vertices on polygonal objects.

    polyColorPerVertex([alpha=float], [clamped=boolean], [colorB=float],
    [colorDisplayOption=boolean], [colorG=float], [colorR=float], [colorRGB=[float, float,
    float]], [notUndoable=boolean], [relative=boolean], [remove=boolean],
    [representation=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyColorPerVertex.html
    """
    return _wrapCommand(cmds.polyColorPerVertex, args, kwargs)


def polyColorSet(*args, **kwargs):  # noqa
    """Command to do the following to color sets: - delete an existing color set.

    polyColorSet([allColorSets=boolean], [clamped=boolean], [colorSet=string], [copy=boolean],
    [create=boolean], [currentColorSet=boolean], [currentPerInstanceSet=boolean],
    [delete=boolean], [newColorSet=string], [perInstance=boolean], [rename=boolean],
    [representation=string], [shareInstances=boolean], [unshared=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyColorSet.html
    """
    return _wrapCommand(cmds.polyColorSet, args, kwargs)


def polyCompare(*args, **kwargs):  # noqa
    """Compares two Polygonal Geometry objects with a fine control on what to compare.

    polyCompare( poly poly , [colorSetIndices=boolean], [colorSets=boolean], [edges=boolean],
    [faceDesc=boolean], [userNormals=boolean], [uvSetIndices=boolean], [uvSets=boolean],
    [vertices=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCompare.html
    """
    return _wrapCommand(cmds.polyCompare, args, kwargs)


def polyCone(*args, **kwargs):  # noqa
    """The cone command creates a new polygonal cone.

    polyCone([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [height=linear], [name=string],
    [nodeState=int], [object=boolean], [radius=linear], [roundCap=boolean],
    [subdivisionsAxis=int], [subdivisionsCap=int], [subdivisionsHeight=int],
    [subdivisionsX=int], [subdivisionsY=int], [subdivisionsZ=int], [texture=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCone.html
    """
    return _wrapCommand(cmds.polyCone, args, kwargs)


def polyConnectComponents(*args, **kwargs):  # noqa
    """Splits polygon edges according to the selected components.

    polyConnectComponents([adjustEdgeFlow=float], [caching=boolean],
    [constructionHistory=boolean], [insertWithEdgeFlow=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyConnectComponents.html
    """
    return _wrapCommand(cmds.polyConnectComponents, args, kwargs)


def polyContourProjection(*args, **kwargs):  # noqa
    """Performs a contour stretch UV projection onto an object.

    polyContourProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [flipRails=boolean], [insertBeforeDeformers=boolean],
    [method=int], [name=string], [nodeState=int], [offset0=linear], [offset1=linear],
    [offset2=linear], [offset3=linear], [reduceShear=float], [smoothness0=float],
    [smoothness1=float], [smoothness2=float], [smoothness3=float],
    [userDefinedCorners=boolean], [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyContourProjection.html
    """
    return _wrapCommand(cmds.polyContourProjection, args, kwargs)


def polyCopyUV(*args, **kwargs):  # noqa
    """Copy some UVs from a UV set into another.

    polyCopyUV( [selectionList] , [caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [name=string], [nodeState=int], [uvSetName=string],
    [uvSetNameInput=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCopyUV.html
    """
    return _wrapCommand(cmds.polyCopyUV, args, kwargs)


def polyCrease(*args, **kwargs):  # noqa
    """Command to set the crease values on the edges or vertices of a poly.

    polyCrease([createHistory=boolean], [operation=uint], [relativeValue=float],
    [value=float], [vertexValue=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCrease.html
    """
    return _wrapCommand(cmds.polyCrease, args, kwargs)


def polyCreaseCtx(*args, **kwargs):  # noqa
    """Create a new context to crease components on polygonal objects.

    polyCreaseCtx([createSet=string], [exists=boolean], [extendSelection=boolean],
    [image1=string], [image2=string], [image3=string], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCreaseCtx.html
    """
    return _wrapCommand(cmds.polyCreaseCtx, args, kwargs)


def polyCreateFacet(*args, **kwargs):  # noqa
    """Create a new polygonal object with the specified face, which will be closed.

    polyCreateFacet([constructionHistory=boolean], [hole=boolean], [name=string], [point=[[,
    float, float, float, ]]], [subdivision=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCreateFacet.html
    """
    return _wrapCommand(cmds.polyCreateFacet, args, kwargs)


def polyCreateFacetCtx(*args, **kwargs):  # noqa
    """Create a new context to create polygonal objects.

    polyCreateFacetCtx([append=boolean], [exists=boolean], [image1=string], [image2=string],
    [image3=string], [maximumNumberOfPoints=int], [planarConstraint=boolean],
    [subdivision=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCreateFacetCtx.html
    """
    return _wrapCommand(cmds.polyCreateFacetCtx, args, kwargs)


def polyCube(*args, **kwargs):  # noqa
    """The cube command creates a new polygonal cube.

    polyCube([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [depth=linear], [height=linear],
    [name=string], [nodeState=int], [object=boolean], [subdivisionsDepth=int],
    [subdivisionsHeight=int], [subdivisionsWidth=int], [subdivisionsX=int],
    [subdivisionsY=int], [subdivisionsZ=int], [texture=int], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCube.html
    """
    return _wrapCommand(cmds.polyCube, args, kwargs)


def polyCut(*args, **kwargs):  # noqa
    """This command splits a mesh, or a set of poly faces, along a plane.

    polyCut([caching=boolean], [constructionHistory=boolean], [cutPlaneCenter=[linear, linear,
    linear]], [cutPlaneCenterX=linear], [cutPlaneCenterY=linear],
    [cutPlaneCenterZ=linear], [cutPlaneHeight=linear], [cutPlaneRotate=[angle, angle,
    angle]], [cutPlaneRotateX=angle], [cutPlaneRotateY=angle], [cutPlaneRotateZ=angle],
    [cutPlaneSize=[linear, linear]], [cutPlaneWidth=linear], [cuttingDirection=string],
    [deleteFaces=boolean], [extractFaces=boolean], [extractOffset=[linear, linear,
    linear]], [extractOffsetX=linear], [extractOffsetY=linear], [extractOffsetZ=linear],
    [name=string], [nodeState=int], [onObject=boolean], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCut.html
    """
    return _wrapCommand(cmds.polyCut, args, kwargs)


def polyCutCtx(*args, **kwargs):  # noqa
    """Create a new context to cut facets on polygonal objects.

    polyCutCtx([deleteFaces=boolean], [exists=boolean], [extractFaces=boolean],
    [extractOffset=[linear, linear, linear]], [image1=string], [image2=string],
    [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCutCtx.html
    """
    return _wrapCommand(cmds.polyCutCtx, args, kwargs)


def polyCutUVCtx(*args, **kwargs):  # noqa
    """Create a new context to cut UVs on polygonal objects.

    polyCutUVCtx( contextName , [loopSpeed=int], [mapBordersColor=[float, float, float]],
    [showCheckerMap=boolean], [showTextureBorders=boolean], [showUVShellColoring=boolean],
    [steadyStroke=boolean], [steadyStrokeDistance=float], [symmetry=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCutUVCtx.html
    """
    return _wrapCommand(cmds.polyCutUVCtx, args, kwargs)


def polyCylinder(*args, **kwargs):  # noqa
    """The cylinder command creates a new polygonal cylinder.

    polyCylinder([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [height=linear], [name=string],
    [nodeState=int], [object=boolean], [radius=linear], [roundCap=boolean],
    [subdivisionsAxis=int], [subdivisionsCaps=int], [subdivisionsHeight=int],
    [subdivisionsX=int], [subdivisionsY=int], [subdivisionsZ=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCylinder.html
    """
    return _wrapCommand(cmds.polyCylinder, args, kwargs)


def polyCylindricalProjection(*args, **kwargs):  # noqa
    """TpolyProjCmdBase is a base class for the command to create a mapping on the selected
    polygonal faces.

    polyCylindricalProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [imageCenter=[float, float]], [imageCenterX=float],
    [imageCenterY=float], [imageScale=[float, float]], [imageScaleU=float],
    [imageScaleV=float], [insertBeforeDeformers=boolean], [keepImageRatio=boolean],
    [mapDirection=string], [name=string], [nodeState=int], [perInstance=boolean],
    [projectionCenter=[linear, linear, linear]], [projectionCenterX=linear],
    [projectionCenterY=linear], [projectionCenterZ=linear], [projectionHeight=linear],
    [projectionHorizontalSweep=linear], [projectionScale=[linear, linear]],
    [projectionScaleU=linear], [projectionScaleV=linear], [radius=linear],
    [rotationAngle=angle], [seamCorrect=boolean], [smartFit=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyCylindricalProjection.html
    """
    return _wrapCommand(cmds.polyCylindricalProjection, args, kwargs)


def polyDelEdge(*args, **kwargs):  # noqa
    """Deletes selected edges, and merges neighboring faces.

    polyDelEdge([caching=boolean], [cleanVertices=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyDelEdge.html
    """
    return _wrapCommand(cmds.polyDelEdge, args, kwargs)


def polyDelFacet(*args, **kwargs):  # noqa
    """Deletes faces.

    polyDelFacet([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyDelFacet.html
    """
    return _wrapCommand(cmds.polyDelFacet, args, kwargs)


def polyDelVertex(*args, **kwargs):  # noqa
    """Deletes vertices.

    polyDelVertex([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyDelVertex.html
    """
    return _wrapCommand(cmds.polyDelVertex, args, kwargs)


def polyDuplicateAndConnect(*args, **kwargs):  # noqa
    """This command duplicates the input polygonal object, connects up the outMesh attribute of
    the original polygonal shape to the inMesh attribute of the newly created duplicate
    shape and copies over the shader assignments from the original shape to the new
    duplicated shape.

    polyDuplicateAndConnect( object , [removeOriginalFromShaders=boolean],
    [renameChildren=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyDuplicateAndConnect.html
    """
    return _wrapCommand(cmds.polyDuplicateAndConnect, args, kwargs)


def polyDuplicateEdge(*args, **kwargs):  # noqa
    """Duplicates a series of connected edges (edgeLoop).

    polyDuplicateEdge([adjustEdgeFlow=float], [caching=boolean],
    [constructionHistory=boolean], [deleteEdge=boolean], [endVertexOffset=float],
    [insertWithEdgeFlow=boolean], [name=string], [nodeState=int], [offset=float],
    [smoothingAngle=angle], [splitType=int], [startVertexOffset=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyDuplicateEdge.html
    """
    return _wrapCommand(cmds.polyDuplicateEdge, args, kwargs)


def polyEditEdgeFlow(*args, **kwargs):  # noqa
    """Edit edges of a polygonal object to respect surface curvature.

    polyEditEdgeFlow([adjustEdgeFlow=float], [caching=boolean], [constructionHistory=boolean],
    [edgeFlow=boolean], [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyEditEdgeFlow.html
    """
    return _wrapCommand(cmds.polyEditEdgeFlow, args, kwargs)


def polyEditUV(*args, **kwargs):  # noqa
    """Command edits uvs on polygonal objects.

    polyEditUV([angle=float], [pivotU=float], [pivotV=float], [relative=boolean],
    [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float],
    [scaleV=float], [uValue=float], [uvSetName=string], [vValue=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyEditUV.html
    """
    return _wrapCommand(cmds.polyEditUV, args, kwargs)


def polyEditUVShell(*args, **kwargs):  # noqa
    """Command edits uv shells on polygonal objects.

    polyEditUVShell([angle=float], [pivotU=float], [pivotV=float], [relative=boolean],
    [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float],
    [scaleV=float], [uValue=float], [uvSetName=string], [vValue=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyEditUVShell.html
    """
    return _wrapCommand(cmds.polyEditUVShell, args, kwargs)


def polyEvaluate(*args, **kwargs):  # noqa
    """Returns the required counts on the specified objects.

    polyEvaluate( [poly poly...] , [accurateEvaluation=boolean], [activeShells=boolean],
    [activeUVShells=boolean], [area=boolean], [boundingBox=boolean],
    [boundingBox2d=boolean], [boundingBoxComponent=boolean],
    [boundingBoxComponent2d=boolean], [displayStats=boolean], [edge=boolean],
    [edgeComponent=boolean], [face=boolean], [faceArea=boolean], [faceComponent=boolean],
    [format=boolean], [shell=boolean], [triangle=boolean], [triangleComponent=boolean],
    [uvArea=boolean], [uvComponent=boolean], [uvEdgePairs=boolean], [uvFaceArea=boolean],
    [uvSetName=string], [uvShell=boolean], [uvShellIds=boolean], [uvcoord=boolean],
    [uvsInShell=int], [vertex=boolean], [vertexComponent=boolean], [worldArea=boolean],
    [worldFaceArea=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyEvaluate.html
    """
    return _wrapCommand(cmds.polyEvaluate, args, kwargs)


def polyExtrudeEdge(*args, **kwargs):  # noqa
    """Extrude edges separately or together.

    polyExtrudeEdge([caching=boolean], [constructionHistory=boolean], [createCurve=boolean],
    [divisions=int], [gain=float], [inputCurve=name], [keepFacesTogether=boolean],
    [localCenter=int], [localDirection=[linear, linear, linear]],
    [localDirectionX=linear], [localDirectionY=linear], [localDirectionZ=linear],
    [localRotate=[angle, angle, angle]], [localRotateX=angle], [localRotateY=angle],
    [localRotateZ=angle], [localScale=[float, float, float]], [localScaleX=float],
    [localScaleY=float], [localScaleZ=float], [localTranslate=[linear, linear, linear]],
    [localTranslateX=linear], [localTranslateY=linear], [localTranslateZ=linear],
    [name=string], [nodeState=int], [offset=float], [pivot=[linear, linear, linear]],
    [pivotX=linear], [pivotY=linear], [pivotZ=linear], [random=float], [rotate=[angle,
    angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle], [scale=[float,
    float, float]], [scaleX=float], [scaleY=float], [scaleZ=float],
    [smoothingAngle=angle], [taper=float], [taperCurve_FloatValue=float],
    [taperCurve_Interp=int], [taperCurve_Position=float], [thickness=float],
    [translate=[linear, linear, linear]], [translateX=linear], [translateY=linear],
    [translateZ=linear], [twist=angle], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeEdge.html
    """
    return _wrapCommand(cmds.polyExtrudeEdge, args, kwargs)


def polyExtrudeFacet(*args, **kwargs):  # noqa
    """Extrude faces.

    polyExtrudeFacet([attraction=float], [caching=boolean], [constructionHistory=boolean],
    [createCurve=boolean], [divisions=int], [gain=float], [gravity=[linear, linear,
    linear]], [gravityX=linear], [gravityY=linear], [gravityZ=linear], [inputCurve=name],
    [keepFacesTogether=boolean], [keepFacetTogether=boolean], [localCenter=int],
    [localDirection=[linear, linear, linear]], [localDirectionX=linear],
    [localDirectionY=linear], [localDirectionZ=linear], [localRotate=[angle, angle,
    angle]], [localRotateX=angle], [localRotateY=angle], [localRotateZ=angle],
    [localScale=[float, float, float]], [localScaleX=float], [localScaleY=float],
    [localScaleZ=float], [localTranslate=[linear, linear, linear]],
    [localTranslateX=linear], [localTranslateY=linear], [localTranslateZ=linear],
    [magnX=linear], [magnY=linear], [magnZ=linear], [magnet=[linear, linear, linear]],
    [name=string], [nodeState=int], [offset=float], [pivot=[linear, linear, linear]],
    [pivotX=linear], [pivotY=linear], [pivotZ=linear], [random=float],
    [reverseAllFaces=boolean], [rotate=[angle, angle, angle]], [rotateX=angle],
    [rotateY=angle], [rotateZ=angle], [scale=[float, float, float]], [scaleX=float],
    [scaleY=float], [scaleZ=float], [smoothingAngle=angle], [taper=float],
    [taperCurve_FloatValue=float], [taperCurve_Interp=int], [taperCurve_Position=float],
    [thickness=float], [translate=[linear, linear, linear]], [translateX=linear],
    [translateY=linear], [translateZ=linear], [twist=angle], [weight=float],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeFacet.html
    """
    return _wrapCommand(cmds.polyExtrudeFacet, args, kwargs)


def polyExtrudeVertex(*args, **kwargs):  # noqa
    """Command that extrudes selected vertices outwards.

    polyExtrudeVertex([caching=boolean], [constructionHistory=boolean], [divisions=int],
    [length=float], [name=string], [nodeState=int], [width=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyExtrudeVertex.html
    """
    return _wrapCommand(cmds.polyExtrudeVertex, args, kwargs)


def polyFlipEdge(*args, **kwargs):  # noqa
    """Command to flip the edges shared by 2 adjacent triangles.

    polyFlipEdge()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyFlipEdge.html
    """
    return _wrapCommand(cmds.polyFlipEdge, args, kwargs)


def polyFlipUV(*args, **kwargs):  # noqa
    """Flip (mirror) the UVs (in texture space) of input polyFaces, about either the U or V axis.

    polyFlipUV([caching=boolean], [constructionHistory=boolean], [createNewMap=boolean],
    [cutUV=boolean], [flipType=int], [insertBeforeDeformers=boolean], [local=boolean],
    [name=string], [nodeState=int], [pivotU=float], [pivotV=float], [usePivot=boolean],
    [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyFlipUV.html
    """
    return _wrapCommand(cmds.polyFlipUV, args, kwargs)


def polyForceUV(*args, **kwargs):  # noqa
    """A set of functionalities can be called through this command.

    polyForceUV([cameraProjection=boolean], [createNewMap=boolean], [flipHorizontal=boolean],
    [flipVertical=boolean], [g=boolean], [local=boolean], [normalize=string],
    [numItems=uint], [preserveAspectRatio=boolean], [unitize=boolean], [unshare=boolean],
    [uvSetName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyForceUV.html
    """
    return _wrapCommand(cmds.polyForceUV, args, kwargs)


def polyGeoSampler(*args, **kwargs):  # noqa
    """This command performs a render sampling of surface color and transparency for each
    selected vertex or face and stores the sampled data as either the color value, or uses
    the sampled data to displace the affected vertices or faces by a sampled data value.

    polyGeoSampler([alphaBlend=string], [averageColor=boolean], [clampAlphaMax=float],
    [clampAlphaMin=float], [clampRGBMax=[float, float, float]], [clampRGBMin=[float,
    float, float]], [colorBlend=string], [colorDisplayOption=boolean],
    [computeShadows=boolean], [displaceGeometry=boolean], [flatShading=boolean],
    [ignoreDoubleSided=boolean], [lightingOnly=boolean], [reuseShadows=boolean],
    [sampleByFace=boolean], [scaleFactor=float], [shareUV=boolean],
    [useLightShadows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyGeoSampler.html
    """
    return _wrapCommand(cmds.polyGeoSampler, args, kwargs)


def polyHelix(*args, **kwargs):  # noqa
    """The polyHelix command creates a new polygonal helix.

    polyHelix([caching=boolean], [coils=float], [constructionHistory=boolean],
    [createUVs=int], [direction=int], [height=linear], [name=string], [nodeState=int],
    [object=boolean], [radius=linear], [roundCap=boolean], [subdivisionsAxis=int],
    [subdivisionsCaps=int], [subdivisionsCoil=int], [texture=int],
    [useOldInitBehaviour=boolean], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyHelix.html
    """
    return _wrapCommand(cmds.polyHelix, args, kwargs)


def polyHole(*args, **kwargs):  # noqa
    """Command to set and clear holes on given faces.

    polyHole([assignHole=boolean], [createHistory=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyHole.html
    """
    return _wrapCommand(cmds.polyHole, args, kwargs)


def polyInfo(*args, **kwargs):  # noqa
    """Command queries topological information on polygonal objects and components.

    polyInfo([edgeToFace=boolean], [edgeToVertex=boolean], [faceNormals=boolean],
    [faceToEdge=boolean], [faceToVertex=boolean], [invalidEdges=boolean],
    [invalidVertices=boolean], [laminaFaces=boolean], [nonManifoldEdges=boolean],
    [nonManifoldUVEdges=boolean], [nonManifoldUVs=boolean], [nonManifoldVertices=boolean],
    [vertexToEdge=boolean], [vertexToFace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyInfo.html
    """
    return _wrapCommand(cmds.polyInfo, args, kwargs)


def polyInstallAction(*args, **kwargs):  # noqa
    """Installs/uninstalls several things to help the user to perform the specified action :

    - Pickmask
    - Internal selection constraints
    - Display attributes.

    polyInstallAction( name , [commandName=boolean], [convertSelection=boolean],
    [installConstraint=boolean], [installDisplay=boolean], [keepInstances=boolean],
    [uninstallConstraint=boolean], [uninstallDisplay=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyInstallAction.html
    """
    return _wrapCommand(cmds.polyInstallAction, args, kwargs)


def polyLayoutUV(*args, **kwargs):  # noqa
    """Move UVs in the texture plane to avoid overlaps.

    polyLayoutUV([caching=boolean], [constructionHistory=boolean], [flipReversed=boolean],
    [layout=int], [layoutMethod=int], [name=string], [nodeState=int],
    [percentageSpace=float], [rotateForBestFit=int], [scale=int], [separate=int],
    [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyLayoutUV.html
    """
    return _wrapCommand(cmds.polyLayoutUV, args, kwargs)


def polyListComponentConversion(*args, **kwargs):  # noqa
    """This command converts poly components from one or more types to another one or more types,
    and returns the list of the conversion.

    polyListComponentConversion( selectionItem[] , [border=boolean], [fromEdge=boolean],
    [fromFace=boolean], [fromUV=boolean], [fromVertex=boolean], [fromVertexFace=boolean],
    [internal=boolean], [toEdge=boolean], [toFace=boolean], [toUV=boolean],
    [toVertex=boolean], [toVertexFace=boolean], [uvShell=boolean],
    [vertexFaceAllEdges=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyListComponentConversion.html
    """
    return _wrapCommand(cmds.polyListComponentConversion, args, kwargs)


def polyMapCut(*args, **kwargs):  # noqa
    """Cut along edges of the texture mapping.

    polyMapCut([caching=boolean], [constructionHistory=boolean], [moveratio=float],
    [name=string], [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMapCut.html
    """
    return _wrapCommand(cmds.polyMapCut, args, kwargs)


def polyMapDel(*args, **kwargs):  # noqa
    """Deletes texture coordinates (UVs) from selected faces.

    polyMapDel([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMapDel.html
    """
    return _wrapCommand(cmds.polyMapDel, args, kwargs)


def polyMapSew(*args, **kwargs):  # noqa
    """Sew border edges in texture space.

    polyMapSew([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMapSew.html
    """
    return _wrapCommand(cmds.polyMapSew, args, kwargs)


def polyMapSewMove(*args, **kwargs):  # noqa
    """This command can be used to Move and Sew together separate UV pieces along geometric
    edges.

    polyMapSewMove([caching=boolean], [constructionHistory=boolean], [limitPieceSize=boolean],
    [name=string], [nodeState=int], [numberFaces=int], [uvSetName=string],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMapSewMove.html
    """
    return _wrapCommand(cmds.polyMapSewMove, args, kwargs)


def polyMergeEdge(*args, **kwargs):  # noqa
    """Sews two border edges together.

    polyMergeEdge([caching=boolean], [constructionHistory=boolean], [firstEdge=int],
    [mergeMode=int], [mergeTexture=boolean], [name=string], [nodeState=int],
    [secondEdge=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeEdge.html
    """
    return _wrapCommand(cmds.polyMergeEdge, args, kwargs)


def polyMergeEdgeCtx(*args, **kwargs):  # noqa
    """Sews two border edges together.

    polyMergeEdgeCtx([activeNodes=boolean], [caching=boolean], [constructionHistory=boolean],
    [exists=boolean], [firstEdge=int], [image1=string], [image2=string], [image3=string],
    [immediate=boolean], [mergeMode=int], [mergeTexture=boolean], [name=string],
    [nodeState=int], [previous=boolean], [reset=boolean], [secondEdge=int],
    [toolNode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeEdgeCtx.html
    """
    return _wrapCommand(cmds.polyMergeEdgeCtx, args, kwargs)


def polyMergeFacet(*args, **kwargs):  # noqa
    """The second face becomes a hole in the first face.

    polyMergeFacet([caching=boolean], [constructionHistory=boolean], [firstFacet=int],
    [mergeMode=int], [name=string], [nodeState=int], [secondFacet=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeFacet.html
    """
    return _wrapCommand(cmds.polyMergeFacet, args, kwargs)


def polyMergeFacetCtx(*args, **kwargs):  # noqa
    """The second face becomes a hole in the first face.

    polyMergeFacetCtx([activeNodes=boolean], [caching=boolean], [constructionHistory=boolean],
    [exists=boolean], [firstFacet=int], [image1=string], [image2=string], [image3=string],
    [immediate=boolean], [mergeMode=int], [name=string], [nodeState=int],
    [previous=boolean], [reset=boolean], [secondFacet=int], [toolNode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeFacetCtx.html
    """
    return _wrapCommand(cmds.polyMergeFacetCtx, args, kwargs)


def polyMergeUV(*args, **kwargs):  # noqa
    """Merge UVs of an object based on their distance.

    polyMergeUV([caching=boolean], [constructionHistory=boolean], [distance=float],
    [name=string], [nodeState=int], [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeUV.html
    """
    return _wrapCommand(cmds.polyMergeUV, args, kwargs)


def polyMergeVertex(*args, **kwargs):  # noqa
    """Merge vertices within a given threshold.

    polyMergeVertex([alwaysMergeTwoVertices=boolean], [caching=boolean],
    [constructionHistory=boolean], [distance=linear], [mergeToComponents=string],
    [name=string], [nodeState=int], [texture=boolean], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMergeVertex.html
    """
    return _wrapCommand(cmds.polyMergeVertex, args, kwargs)


def polyMirrorFace(*args, **kwargs):  # noqa
    """Mirror all the faces of the selected object.

    polyMirrorFace([axis=int], [axisDirection=int], [caching=boolean],
    [constructionHistory=boolean], [direction=int], [mergeMode=int],
    [mergeThreshold=linear], [mergeThresholdType=int], [mirrorAxis=int],
    [mirrorPosition=linear], [name=string], [nodeState=int], [pivot=[linear, linear,
    linear]], [pivotX=linear], [pivotY=linear], [pivotZ=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMirrorFace.html
    """
    return _wrapCommand(cmds.polyMirrorFace, args, kwargs)


def polyMoveEdge(*args, **kwargs):  # noqa
    """Modifies edges of a polygonal object.

    polyMoveEdge([caching=boolean], [constructionHistory=boolean], [gain=float],
    [localCenter=int], [localDirection=[linear, linear, linear]],
    [localDirectionX=linear], [localDirectionY=linear], [localDirectionZ=linear],
    [localRotate=[angle, angle, angle]], [localRotateX=angle], [localRotateY=angle],
    [localRotateZ=angle], [localScale=[float, float, float]], [localScaleX=float],
    [localScaleY=float], [localScaleZ=float], [localTranslate=[linear, linear, linear]],
    [localTranslateX=linear], [localTranslateY=linear], [localTranslateZ=linear],
    [name=string], [nodeState=int], [pivot=[linear, linear, linear]], [pivotX=linear],
    [pivotY=linear], [pivotZ=linear], [random=float], [rotate=[angle, angle, angle]],
    [rotateX=angle], [rotateY=angle], [rotateZ=angle], [scale=[float, float, float]],
    [scaleX=float], [scaleY=float], [scaleZ=float], [translate=[linear, linear, linear]],
    [translateX=linear], [translateY=linear], [translateZ=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMoveEdge.html
    """
    return _wrapCommand(cmds.polyMoveEdge, args, kwargs)


def polyMoveFacet(*args, **kwargs):  # noqa
    """Modifies facet of a polygonal object.

    polyMoveFacet([attraction=float], [caching=boolean], [constructionHistory=boolean],
    [gain=float], [gravity=[linear, linear, linear]], [gravityX=linear],
    [gravityY=linear], [gravityZ=linear], [localCenter=int], [localDirection=[linear,
    linear, linear]], [localDirectionX=linear], [localDirectionY=linear],
    [localDirectionZ=linear], [localRotate=[angle, angle, angle]], [localRotateX=angle],
    [localRotateY=angle], [localRotateZ=angle], [localScale=[float, float, float]],
    [localScaleX=float], [localScaleY=float], [localScaleZ=float],
    [localTranslate=[linear, linear, linear]], [localTranslateX=linear],
    [localTranslateY=linear], [localTranslateZ=linear], [magnX=linear], [magnY=linear],
    [magnZ=linear], [magnet=[linear, linear, linear]], [name=string], [nodeState=int],
    [offset=float], [pivot=[linear, linear, linear]], [pivotX=linear], [pivotY=linear],
    [pivotZ=linear], [random=float], [rotate=[angle, angle, angle]], [rotateX=angle],
    [rotateY=angle], [rotateZ=angle], [scale=[float, float, float]], [scaleX=float],
    [scaleY=float], [scaleZ=float], [translate=[linear, linear, linear]],
    [translateX=linear], [translateY=linear], [translateZ=linear], [weight=float],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMoveFacet.html
    """
    return _wrapCommand(cmds.polyMoveFacet, args, kwargs)


def polyMoveFacetUV(*args, **kwargs):  # noqa
    """Modifies the map by moving all UV values associated with the selected face(s).

    polyMoveFacetUV([axisLen=[float, float]], [axisLenX=float], [axisLenY=float],
    [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int],
    [pivot=[float, float]], [pivotU=float], [pivotV=float], [random=float],
    [rotationAngle=angle], [scale=[float, float]], [scaleU=float], [scaleV=float],
    [translate=[float, float]], [translateU=float], [translateV=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMoveFacetUV.html
    """
    return _wrapCommand(cmds.polyMoveFacetUV, args, kwargs)


def polyMoveUV(*args, **kwargs):  # noqa
    """Moves selected UV coordinates in 2D space.

    polyMoveUV([axisLen=[float, float]], [axisLenX=float], [axisLenY=float],
    [caching=boolean], [constructionHistory=boolean], [name=string], [nodeState=int],
    [pivot=[float, float]], [pivotU=float], [pivotV=float], [random=float],
    [rotationAngle=angle], [scale=[float, float]], [scaleU=float], [scaleV=float],
    [translate=[float, float]], [translateU=float], [translateV=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMoveUV.html
    """
    return _wrapCommand(cmds.polyMoveUV, args, kwargs)


def polyMoveVertex(*args, **kwargs):  # noqa
    """Modifies vertices of a polygonal object.

    polyMoveVertex([caching=boolean], [constructionHistory=boolean], [gain=float],
    [localDirection=[linear, linear, linear]], [localDirectionX=linear],
    [localDirectionY=linear], [localDirectionZ=linear], [localTranslate=[linear, linear,
    linear]], [localTranslateX=linear], [localTranslateY=linear],
    [localTranslateZ=linear], [name=string], [nodeState=int], [pivot=[linear, linear,
    linear]], [pivotX=linear], [pivotY=linear], [pivotZ=linear], [random=float],
    [rotate=[angle, angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle],
    [scale=[float, float, float]], [scaleX=float], [scaleY=float], [scaleZ=float],
    [translate=[linear, linear, linear]], [translateX=linear], [translateY=linear],
    [translateZ=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMoveVertex.html
    """
    return _wrapCommand(cmds.polyMoveVertex, args, kwargs)


def polyMultiLayoutUV(*args, **kwargs):  # noqa
    """place the UVs of the selected polygonal objects so that they do not overlap.

    polyMultiLayoutUV([flipReversed=boolean], [gridU=int], [gridV=int], [layout=int],
    [layoutMethod=int], [offsetU=float], [offsetV=float], [percentageSpace=float],
    [prescale=int], [rotateForBestFit=int], [scale=int], [sizeU=float], [sizeV=float],
    [uvSetName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyMultiLayoutUV.html
    """
    return _wrapCommand(cmds.polyMultiLayoutUV, args, kwargs)


def polyNormal(*args, **kwargs):  # noqa
    """Control the normals of an object.

    polyNormal([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [normalMode=int], [userNormalMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyNormal.html
    """
    return _wrapCommand(cmds.polyNormal, args, kwargs)


def polyNormalizeUV(*args, **kwargs):  # noqa
    """Normalizes the UVs of input polyFaces.

    polyNormalizeUV([caching=boolean], [centerOnTile=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [insertBeforeDeformers=boolean], [name=string],
    [nodeState=int], [normalizeDirection=int], [normalizeType=int],
    [preserveAspectRatio=boolean], [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyNormalizeUV.html
    """
    return _wrapCommand(cmds.polyNormalizeUV, args, kwargs)


def polyNormalPerVertex(*args, **kwargs):  # noqa
    """Command associates normal(x, y, z) with vertices on polygonal objects.

    polyNormalPerVertex([allLocked=boolean], [deformable=boolean], [freezeNormal=boolean],
    [normalX=float], [normalXYZ=[float, float, float]], [normalY=float], [normalZ=float],
    [relative=boolean], [unFreezeNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyNormalPerVertex.html
    """
    return _wrapCommand(cmds.polyNormalPerVertex, args, kwargs)


def polyOptions(*args, **kwargs):  # noqa
    """Changes the global display polygonal attributes.

    polyOptions([activeObjects=boolean], [allEdges=boolean], [backCullVertex=boolean],
    [backCulling=boolean], [colorMaterialChannel=string], [colorShadedDisplay=boolean],
    [displayAlphaAsGreyScale=boolean], [displayBlueChannel=boolean],
    [displayBorder=boolean], [displayCenter=boolean], [displayColorAsGreyScale=boolean],
    [displayCreaseEdge=boolean], [displayCreaseVertex=boolean], [displayGeometry=boolean],
    [displayGreenChannel=boolean], [displayInvisibleFaces=boolean],
    [displayItemNumbers=[boolean, boolean, boolean, boolean]], [displayMapBorder=boolean],
    [displayMetadata=[boolean, boolean, boolean]], [displayNormal=boolean],
    [displayRedChannel=boolean], [displaySubdComps=boolean], [displayTangent=boolean],
    [displayTriangle=boolean], [displayUVTopology=boolean], [displayUVs=boolean],
    [displayVertex=boolean], [displayWarp=boolean], [facet=boolean], [fullBack=boolean],
    [gl=boolean], [hardBack=boolean], [hardEdge=boolean], [hardEdgeColor=boolean],
    [materialBlend=string], [newPolymesh=boolean], [point=boolean], [pointFacet=boolean],
    [relative=boolean], [reuseTriangles=boolean], [sizeBorder=float], [sizeNormal=float],
    [sizeUV=float], [sizeVertex=float], [smoothDrawType=int], [softEdge=boolean],
    [vertexNormalMethod=int], [wireBackCulling=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyOptions.html
    """
    return _wrapCommand(cmds.polyOptions, args, kwargs)


def polyOptUvs(*args, **kwargs):  # noqa
    """Optimizes selected UVs.

    polyOptUvs( selectionList , [applyToShell=boolean], [areaWeight=float], [caching=boolean],
    [constructionHistory=boolean], [globalBlend=float], [globalMethodBlend=float],
    [iterations=int], [name=string], [nodeState=int], [optimizeAxis=int],
    [pinSelected=boolean], [pinUvBorder=boolean], [scale=float],
    [stoppingThreshold=float], [useScale=boolean], [uvSetName=string],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyOptUvs.html
    """
    return _wrapCommand(cmds.polyOptUvs, args, kwargs)


def polyOutput(*args, **kwargs):  # noqa
    """Dumps a description of internal memory representation of poly objects.

    polyOutput( poly poly... , [allValues=boolean], [color=boolean], [colorDesc=boolean],
    [edge=boolean], [edgeFace=boolean], [face=boolean], [faceNorm=boolean],
    [force=boolean], [group=boolean], [noOutput=boolean], [normDesc=boolean],
    [outputFile=string], [triangle=boolean], [uvDesc=boolean], [uvValue=boolean],
    [vert=boolean], [vertEdge=boolean], [vertNorm=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyOutput.html
    """
    return _wrapCommand(cmds.polyOutput, args, kwargs)


def polyPinUV(*args, **kwargs):  # noqa
    """This command is used to pin and unpin UVs.

    polyPinUV([createHistory=boolean], [operation=uint], [unpinned=boolean],
    [uvSetName=string], [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPinUV.html
    """
    return _wrapCommand(cmds.polyPinUV, args, kwargs)


def polyPipe(*args, **kwargs):  # noqa
    """The polyPipe command creates a new polygonal pipe.

    polyPipe([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=boolean], [height=linear], [name=string],
    [nodeState=int], [object=boolean], [radius=linear], [roundCap=boolean],
    [subdivisionsAxis=int], [subdivisionsCaps=int], [subdivisionsHeight=int],
    [texture=boolean], [thickness=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPipe.html
    """
    return _wrapCommand(cmds.polyPipe, args, kwargs)


def polyPlanarProjection(*args, **kwargs):  # noqa
    """TpolyProjCmdBase is a base class for the command to create a mapping on the selected
    polygonal faces.

    polyPlanarProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [imageCenter=[float, float]], [imageCenterX=float],
    [imageCenterY=float], [imageScale=[float, float]], [imageScaleU=float],
    [imageScaleV=float], [insertBeforeDeformers=boolean], [keepImageRatio=boolean],
    [mapDirection=string], [name=string], [nodeState=int], [perInstance=boolean],
    [projectionCenter=[linear, linear, linear]], [projectionCenterX=linear],
    [projectionCenterY=linear], [projectionCenterZ=linear], [projectionHeight=linear],
    [projectionHorizontalSweep=linear], [projectionScale=[linear, linear]],
    [rotate=[angle, angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle],
    [rotationAngle=angle], [seamCorrect=boolean], [smartFit=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPlanarProjection.html
    """
    return _wrapCommand(cmds.polyPlanarProjection, args, kwargs)


def polyPlane(*args, **kwargs):  # noqa
    """Create a new polygonal plane.

    polyPlane([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [height=linear], [name=string],
    [nodeState=int], [object=boolean], [subdivisionsHeight=int], [subdivisionsWidth=int],
    [subdivisionsX=int], [subdivisionsY=int], [texture=int], [width=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPlane.html
    """
    return _wrapCommand(cmds.polyPlane, args, kwargs)


def polyPlatonicSolid(*args, **kwargs):  # noqa
    """The polyPlatonicSolid command creates a new polygonal platonic solid.

    polyPlatonicSolid([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [name=string], [nodeState=int],
    [object=boolean], [radius=linear], [sideLength=linear], [solidType=int],
    [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPlatonicSolid.html
    """
    return _wrapCommand(cmds.polyPlatonicSolid, args, kwargs)


def polyPoke(*args, **kwargs):  # noqa
    """Introduces a new vertex in the middle of the selected face, and connects it to the rest of
    the vertices of the face.

    polyPoke( selectionList , [caching=boolean], [constructionHistory=boolean],
    [localTranslate=[linear, linear, linear]], [localTranslateX=linear],
    [localTranslateY=linear], [localTranslateZ=linear], [name=string], [nodeState=int],
    [translate=[linear, linear, linear]], [translateX=linear], [translateY=linear],
    [translateZ=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPoke.html
    """
    return _wrapCommand(cmds.polyPoke, args, kwargs)


def polyPrimitive(*args, **kwargs):  # noqa
    """Create a polygon primative.

    polyPrimitive([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [name=string], [nodeState=int],
    [object=boolean], [polyType=int], [radius=linear], [sideLength=linear], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPrimitive.html
    """
    return _wrapCommand(cmds.polyPrimitive, args, kwargs)


def polyPrism(*args, **kwargs):  # noqa
    """The prism command creates a new polygonal prism.

    polyPrism([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [length=linear], [name=string],
    [nodeState=int], [numberOfSides=int], [numderOfSides=int], [object=boolean],
    [sideLength=linear], [subdivisionsCaps=int], [subdivisionsHeight=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPrism.html
    """
    return _wrapCommand(cmds.polyPrism, args, kwargs)


def polyProjectCurve(*args, **kwargs):  # noqa
    """The polyProjectCurve command creates curves by projecting a selected curve onto a selected
    poly mesh.

    polyProjectCurve( curve poly , [addUnderTransform=boolean], [caching=boolean],
    [direction=[linear, linear, linear]], [directionX=linear], [directionY=linear],
    [directionZ=linear], [nodeState=int], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyProjectCurve.html
    """
    return _wrapCommand(cmds.polyProjectCurve, args, kwargs)


def polyProjection(*args, **kwargs):  # noqa
    """Creates a mapping on the selected polygonal faces.

    polyProjection([constructionHistory=boolean], [createNewMap=boolean],
    [imageCenterX=float], [imageCenterY=float], [imageScaleU=float], [imageScaleV=float],
    [insertBeforeDeformers=boolean], [keepImageRatio=boolean], [mapDirection=string],
    [projectionCenterX=float], [projectionCenterY=float], [projectionCenterZ=float],
    [projectionScaleU=float], [projectionScaleV=float], [rotateX=float], [rotateY=float],
    [rotateZ=float], [rotationAngle=float], [seamCorrect=boolean], [smartFit=boolean],
    [type=string], [uvSetName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyProjection.html
    """
    return _wrapCommand(cmds.polyProjection, args, kwargs)


def polyPyramid(*args, **kwargs):  # noqa
    """The pyramid command creates a new polygonal pyramid.

    polyPyramid([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [name=string], [nodeState=int],
    [numberOfSides=int], [numderOfSides=int], [object=boolean], [sideLength=linear],
    [subdivisionsCaps=int], [subdivisionsHeight=int], [texture=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyPyramid.html
    """
    return _wrapCommand(cmds.polyPyramid, args, kwargs)


def polyQuad(*args, **kwargs):  # noqa
    """Merges selected triangles of a polygonal object into four-sided faces.

    polyQuad([angle=angle], [caching=boolean], [constructionHistory=boolean],
    [keepGroupBorder=boolean], [keepHardEdges=boolean], [keepTextureBorders=boolean],
    [name=string], [nodeState=int], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyQuad.html
    """
    return _wrapCommand(cmds.polyQuad, args, kwargs)


def polyQueryBlindData(*args, **kwargs):  # noqa
    """Command query's blindData associated with particular polygonal components.

    polyQueryBlindData([associationType=string], [binaryData=string], [booleanData=boolean],
    [doubleData=float], [intData=int], [longDataName=string], [maxValue=float],
    [minValue=float], [shortDataName=string], [showComp=boolean], [stringData=string],
    [subString=string], [typeId=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyQueryBlindData.html
    """
    return _wrapCommand(cmds.polyQueryBlindData, args, kwargs)


def polyReduce(*args, **kwargs):  # noqa
    """Simplify a polygonal object by reducing geometry while preserving the overall shape of the
    mesh.

    polyReduce([caching=boolean], [cachingReduce=boolean], [colorWeights=float],
    [compactness=float], [constructionHistory=boolean], [geomWeights=float],
    [invertVertexWeights=boolean], [keepBorder=boolean], [keepBorderWeight=float],
    [keepColorBorder=boolean], [keepColorBorderWeight=float], [keepCreaseEdge=boolean],
    [keepCreaseEdgeWeight=float], [keepFaceGroupBorder=boolean],
    [keepFaceGroupBorderWeight=float], [keepHardEdge=boolean], [keepHardEdgeWeight=float],
    [keepMapBorder=boolean], [keepMapBorderWeight=float], [keepOriginalVertices=boolean],
    [keepQuadsWeight=float], [name=string], [nodeState=int], [percentage=float],
    [preserveLocation=boolean], [preserveTopology=boolean], [replaceOriginal=boolean],
    [sharpness=float], [symmetryPlaneW=float], [symmetryPlaneX=float],
    [symmetryPlaneY=float], [symmetryPlaneZ=float], [symmetryTolerance=float],
    [termination=int], [triangleCount=int], [triangulate=boolean],
    [useVirtualSymmetry=int], [uvWeights=float], [version=int], [vertexCount=int],
    [vertexMapName=string], [vertexWeightCoefficient=float], [weightCoefficient=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyReduce.html
    """
    return _wrapCommand(cmds.polyReduce, args, kwargs)


def polyRemesh(*args, **kwargs):  # noqa
    """Triangulates, then remeshes the given mesh through edge splitting and collapsing.

    polyRemesh([caching=boolean], [collapseThreshold=float], [constructionHistory=boolean],
    [interpolationType=int], [maxEdgeLength=float], [name=string], [nodeState=int],
    [smoothStrength=float], [tessellateBorders=boolean], [useRelativeValues=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyRemesh.html
    """
    return _wrapCommand(cmds.polyRemesh, args, kwargs)


def polyRetopo(*args, **kwargs):  # noqa
    """Retopologize a polygonial surface.

    polyRetopo()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyRetopo.html
    """
    return _wrapCommand(cmds.polyRetopo, args, kwargs)


def polySelect(*args, **kwargs):  # noqa
    """This command makes different types of poly component selections.

    polySelect([add=boolean], [addFirst=boolean], [asSelectString=boolean],
    [deselect=boolean], [edgeBorder=uint], [edgeBorderPath=[int, int]],
    [edgeBorderPattern=[int, int]], [edgeLoop=uint], [edgeLoopOrBorder=uint],
    [edgeLoopOrBorderPattern=[int, int]], [edgeLoopPath=[int, int]],
    [edgeLoopPattern=[int, int]], [edgeRing=uint], [edgeRingPath=[int, int]],
    [edgeRingPattern=[int, int]], [edgeUVLoopOrBorder=uint], [everyN=uint],
    [extendToShell=uint], [noSelection=boolean], [replace=boolean],
    [shortestEdgePath=[int, int]], [shortestEdgePathUV=[int, int]],
    [shortestFacePath=[int, int]], [toggle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySelect.html
    """
    return _wrapCommand(cmds.polySelect, args, kwargs)


def polySelectConstraint(*args, **kwargs):  # noqa
    """Changes the global polygonal selection constraints.

    polySelectConstraint([angle=int], [anglePropagation=boolean], [angleTolerance=float],
    [anglebound=[angle, angle]], [border=boolean], [borderPropagation=boolean],
    [convexity=int], [crease=boolean], [disable=boolean], [dist=int], [distaxis=[float,
    float, float]], [distbound=[float, float]], [distpoint=[float, float, float]],
    [edgeDistance=uint], [geometricarea=int], [geometricareabound=[float, float]],
    [holes=int], [length=int], [lengthbound=[float, float]], [loopPropagation=boolean],
    [max2dAngle=float], [max3dAngle=float], [mode=int], [nonmanifold=int],
    [oppositeEdges=boolean], [order=int], [orderbound=[int, int]], [orient=int],
    [orientaxis=[float, float, float]], [orientbound=[float, float]], [planarity=int],
    [propagate=int], [random=int], [randomratio=float], [returnSelection=boolean],
    [ringPropagation=boolean], [shell=boolean], [size=int], [smoothness=int],
    [stateString=boolean], [textured=int], [texturedarea=int], [texturedareabound=[float,
    float]], [textureshared=int], [topology=int], [type=int], [uvBorderSelection=boolean],
    [uvConstraint=boolean], [uvEdgeLoopPropagation=boolean],
    [uvEdgeRingPropagation=boolean], [uvFaceOrientation=int], [uvShell=boolean],
    [visibility=int], [visibilityangle=angle], [visibilitypoint=[float, float, float]],
    [where=int], [wholeSensitive=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySelectConstraint.html
    """
    return _wrapCommand(cmds.polySelectConstraint, args, kwargs)


def polySelectConstraintMonitor(*args, **kwargs):  # noqa
    """Manage the window to display/edit the polygonal selection constraint parameters.

    polySelectConstraintMonitor( string , [changeCommand=[string, string]], [create=boolean],
    [delete=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySelectConstraintMonitor.html
    """
    return _wrapCommand(cmds.polySelectConstraintMonitor, args, kwargs)


def polySelectCtx(*args, **kwargs):  # noqa
    """Create a new context to select polygon components.

    polySelectCtx([exists=boolean], [image1=string], [image2=string], [image3=string],
    [mode=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySelectCtx.html
    """
    return _wrapCommand(cmds.polySelectCtx, args, kwargs)


def polySelectEditCtx(*args, **kwargs):  # noqa
    """Create a new context to select and edit polygonal objects.

    polySelectEditCtx([absoluteOffset=boolean], [adjustEdgeFlow=float],
    [autoComplete=boolean], [deleteEdge=boolean], [divisions=int],
    [endVertexOffset=float], [exists=boolean], [fixQuads=boolean], [image1=string],
    [image2=string], [image3=string], [insertWithEdgeFlow=boolean], [mode=int],
    [smoothingAngle=angle], [splitType=int], [startVertexOffset=float],
    [useEqualMultiplier=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySelectEditCtx.html
    """
    return _wrapCommand(cmds.polySelectEditCtx, args, kwargs)


def polySeparate(*args, **kwargs):  # noqa
    """This command creates new objects from the given poly.

    polySeparate( [poly] , [caching=boolean], [nodeState=int], [removeShells=boolean],
    [separateSpecificShell=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySeparate.html
    """
    return _wrapCommand(cmds.polySeparate, args, kwargs)


def polySetToFaceNormal(*args, **kwargs):  # noqa
    """This command takes selected polygonal vertices or vertex-faces and changes their normals.

    polySetToFaceNormal([setUserNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySetToFaceNormal.html
    """
    return _wrapCommand(cmds.polySetToFaceNormal, args, kwargs)


def polySewEdge(*args, **kwargs):  # noqa
    """Merge border edges within a given threshold.

    polySewEdge([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [texture=boolean], [tolerance=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySewEdge.html
    """
    return _wrapCommand(cmds.polySewEdge, args, kwargs)


def polyShortestPathCtx(*args, **kwargs):  # noqa
    """Creates a new context to select shortest edge path between two vertices or UVs in the 3d
    viewport.

    polyShortestPathCtx([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyShortestPathCtx.html
    """
    return _wrapCommand(cmds.polyShortestPathCtx, args, kwargs)


def polySlideEdge(*args, **kwargs):  # noqa
    """Moves an edge loop selection along the edges connected to the sides of its vertices.

    polySlideEdge([absolute=boolean], [direction=uint], [edgeDirection=float],
    [symmetry=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySlideEdge.html
    """
    return _wrapCommand(cmds.polySlideEdge, args, kwargs)


def polySmooth(*args, **kwargs):  # noqa
    """Smooth a polygonal object.

    polySmooth([caching=boolean], [constructionHistory=boolean], [continuity=float],
    [degree=int], [divisions=int], [divisionsPerEdge=int], [keepBorder=boolean],
    [keepHardEdge=boolean], [keepMapBorders=int], [keepSelectionBorder=boolean],
    [keepTesselation=boolean], [keepTessellation=boolean], [method=int], [name=string],
    [nodeState=int], [osdCreaseMethod=int], [osdFvarBoundary=int],
    [osdFvarPropagateCorners=boolean], [osdSmoothTriangles=boolean],
    [osdVertBoundary=int], [propagateEdgeHardness=boolean], [pushStrength=float],
    [roundness=float], [smoothUVs=boolean], [subdivisionLevels=int],
    [subdivisionType=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySmooth.html
    """
    return _wrapCommand(cmds.polySmooth, args, kwargs)


def polySoftEdge(*args, **kwargs):  # noqa
    """Selectively makes edges soft or hard.

    polySoftEdge([angle=angle], [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySoftEdge.html
    """
    return _wrapCommand(cmds.polySoftEdge, args, kwargs)


def polySphere(*args, **kwargs):  # noqa
    """The sphere command creates a new polygonal sphere.

    polySphere([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=int], [name=string], [nodeState=int],
    [object=boolean], [radius=linear], [subdivisionsAxis=int], [subdivisionsHeight=int],
    [subdivisionsX=int], [subdivisionsY=int], [texture=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySphere.html
    """
    return _wrapCommand(cmds.polySphere, args, kwargs)


def polySphericalProjection(*args, **kwargs):  # noqa
    """TpolyProjCmdBase is a base class for the command to create a mapping on the selected
    polygonal faces.

    polySphericalProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [imageCenter=[float, float]], [imageCenterX=float],
    [imageCenterY=float], [imageScale=[float, float]], [imageScaleU=float],
    [imageScaleV=float], [insertBeforeDeformers=boolean], [keepImageRatio=boolean],
    [mapDirection=string], [name=string], [nodeState=int], [perInstance=boolean],
    [projectionCenter=[linear, linear, linear]], [projectionCenterX=linear],
    [projectionCenterY=linear], [projectionCenterZ=linear],
    [projectionHorizontalSweep=linear], [projectionScale=[linear, linear]],
    [projectionScaleU=linear], [projectionScaleV=linear], [radius=linear], [rotate=[angle,
    angle, angle]], [rotateX=angle], [rotateY=angle], [rotateZ=angle],
    [rotationAngle=angle], [seamCorrect=boolean], [smartFit=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySphericalProjection.html
    """
    return _wrapCommand(cmds.polySphericalProjection, args, kwargs)


def polySplit(*args, **kwargs):  # noqa
    """Split facets/edges of a polygonal object.

    polySplit([adjustEdgeFlow=float], [constructionHistory=boolean], [detachEdges=boolean],
    [edgepoint=[int, float]], [facepoint=[int, float, float, float]],
    [insertWithEdgeFlow=boolean], [insertpoint=[int, float, [, float, float, ]]],
    [name=string], [projectedCurve=name], [projectedCurveTolerance=float],
    [smoothingangle=angle], [subdivision=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplit.html
    """
    return _wrapCommand(cmds.polySplit, args, kwargs)


def polySplitCtx(*args, **kwargs):  # noqa
    """Create a new context to split facets on polygonal objects.

    polySplitCtx([enablesnap=boolean], [exists=boolean], [image1=string], [image2=string],
    [image3=string], [magnetsnap=int], [precsnap=float], [smoothingangle=angle],
    [snaptoedge=boolean], [subdivision=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplitCtx.html
    """
    return _wrapCommand(cmds.polySplitCtx, args, kwargs)


def polySplitCtx2(*args, **kwargs):  # noqa
    """Create a new context to split facets on polygonal objects.

    polySplitCtx2([adjustEdgeFlow=float], [constrainToEdges=boolean], [edgeMagnets=int],
    [exists=boolean], [image1=string], [image2=string], [image3=string],
    [insertWithEdgeFlow=boolean], [snapTolerance=float], [snappedToEdgeColor=[float,
    float, float]], [snappedToFaceColor=[float, float, float]],
    [snappedToMagnetColor=[float, float, float]], [snappedToVertexColor=[float, float,
    float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplitCtx2.html
    """
    return _wrapCommand(cmds.polySplitCtx2, args, kwargs)


def polySplitEdge(*args, **kwargs):  # noqa
    """Split Edges.

    polySplitEdge([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [operation=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplitEdge.html
    """
    return _wrapCommand(cmds.polySplitEdge, args, kwargs)


def polySplitRing(*args, **kwargs):  # noqa
    """Splits a series of ring edges of connected quads and inserts connecting edges between
    them.

    polySplitRing([adjustEdgeFlow=float], [caching=boolean], [constructionHistory=boolean],
    [direction=boolean], [divisions=int], [enableProfileCurve=boolean],
    [fixQuads=boolean], [insertWithEdgeFlow=boolean], [name=string], [nodeState=int],
    [profileCurveInputOffset=float], [profileCurveInputScale=float],
    [profileCurve_FloatValue=float], [profileCurve_Interp=int],
    [profileCurve_Position=float], [rootEdge=int], [smoothingAngle=angle],
    [splitType=int], [useEqualMultiplier=boolean], [useFaceNormalsAtEnds=boolean],
    [weight=float], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplitRing.html
    """
    return _wrapCommand(cmds.polySplitRing, args, kwargs)


def polySplitVertex(*args, **kwargs):  # noqa
    """Use this command to split one or more vertices.

    polySplitVertex([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySplitVertex.html
    """
    return _wrapCommand(cmds.polySplitVertex, args, kwargs)


def polyStraightenUVBorder(*args, **kwargs):  # noqa
    """Move border UVs along a simple curve.

    polyStraightenUVBorder( selectionList , [blendOriginal=float], [caching=boolean],
    [constructionHistory=boolean], [curvature=float], [gapTolerance=int], [name=string],
    [nodeState=int], [preserveLength=float], [uvSetName=string], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyStraightenUVBorder.html
    """
    return _wrapCommand(cmds.polyStraightenUVBorder, args, kwargs)


def polySubdivideEdge(*args, **kwargs):  # noqa
    """Subdivides an edge into two or more subedges.

    polySubdivideEdge([caching=boolean], [constructionHistory=boolean], [divisions=int],
    [name=string], [nodeState=int], [size=linear], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySubdivideEdge.html
    """
    return _wrapCommand(cmds.polySubdivideEdge, args, kwargs)


def polySubdivideFacet(*args, **kwargs):  # noqa
    """Subdivides a face into quads or triangles.

    polySubdivideFacet([caching=boolean], [constructionHistory=boolean], [divisions=int],
    [divisionsU=int], [divisionsV=int], [mode=int], [name=string], [nodeState=int],
    [subdMethod=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polySubdivideFacet.html
    """
    return _wrapCommand(cmds.polySubdivideFacet, args, kwargs)


def polyTorus(*args, **kwargs):  # noqa
    """The torus command creates a new polygonal torus.

    polyTorus([axis=[linear, linear, linear]], [caching=boolean],
    [constructionHistory=boolean], [createUVs=boolean], [name=string], [nodeState=int],
    [object=boolean], [radius=linear], [sectionRadius=linear], [subdivisionsAxis=int],
    [subdivisionsHeight=int], [subdivisionsX=int], [subdivisionsY=int], [texture=boolean],
    [twist=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyTorus.html
    """
    return _wrapCommand(cmds.polyTorus, args, kwargs)


def polyToSubdiv(*args, **kwargs):  # noqa
    """This command converts a polygon and produces a subd surface.

    polyToSubdiv( [poly] , [absolutePosition=boolean], [addUnderTransform=boolean],
    [applyMatrixToResult=boolean], [caching=boolean], [constructionHistory=boolean],
    [maxEdgesPerVert=int], [maxPolyCount=int], [name=string], [nodeState=int],
    [object=boolean], [preserveVertexOrdering=boolean], [quickConvert=boolean],
    [uvPoints=[float, float]], [uvPointsU=float], [uvPointsV=float], [uvTreatment=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyToSubdiv.html
    """
    return _wrapCommand(cmds.polyToSubdiv, args, kwargs)


def polyTransfer(*args, **kwargs):  # noqa
    """Transfer information from one polygonal object to another one.

    polyTransfer([alternateObject=string], [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [uvSets=boolean], [vertexColor=boolean],
    [vertices=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyTransfer.html
    """
    return _wrapCommand(cmds.polyTransfer, args, kwargs)


def polyTriangulate(*args, **kwargs):  # noqa
    """Triangulation breaks polygons down into triangles, ensuring that all faces are planar and
    non-holed.

    polyTriangulate([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyTriangulate.html
    """
    return _wrapCommand(cmds.polyTriangulate, args, kwargs)


def polyUnite(*args, **kwargs):  # noqa
    """This command creates a new poly as an union of a list of polys If no objects are specified
    in the command line, then the objects from the active list are used.

    polyUnite( poly poly [poly ...] , [caching=boolean], [centerPivot=boolean],
    [mergeUVSets=int], [nodeState=int], [objectPivot=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUnite.html
    """
    return _wrapCommand(cmds.polyUnite, args, kwargs)


def polyUniteSkinned(*args, **kwargs):  # noqa
    """Command to combine poly mesh objects (as polyUnite) while retaining the smooth skinning
    setup on the combined object.

    polyUniteSkinned([centerPivot=boolean], [constructionHistory=boolean], [mergeUVSets=int],
    [objectPivot=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUniteSkinned.html
    """
    return _wrapCommand(cmds.polyUniteSkinned, args, kwargs)


def polyUVCoverage(*args, **kwargs):  # noqa
    """Return the UV space coverage of the specified components.

    polyUVCoverage( selectionItem[] , [uvRange=[float, float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUVCoverage.html
    """
    return _wrapCommand(cmds.polyUVCoverage, args, kwargs)


def polyUVOverlap(*args, **kwargs):  # noqa
    """Return the required result on the specified components.

    polyUVOverlap( selectionItem[] , [nonOverlappingComponents=boolean],
    [overlappingComponents=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUVOverlap.html
    """
    return _wrapCommand(cmds.polyUVOverlap, args, kwargs)


def polyUVRectangle(*args, **kwargs):  # noqa
    """Given two vertices, does one of the following: 1) If the vertices define opposite corners
    of a rectangular area of quads, assigns a grid of UVs spanning the 0-1 area to that
    rectangle.

    polyUVRectangle([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUVRectangle.html
    """
    return _wrapCommand(cmds.polyUVRectangle, args, kwargs)


def polyUVSet(*args, **kwargs):  # noqa
    """Command to do the following to uv sets: - delete an existing uv set.

    polyUVSet([allUVSets=boolean], [allUVSetsIndices=boolean], [allUVSetsWithCount=boolean],
    [copy=boolean], [create=boolean], [currentLastUVSet=boolean],
    [currentPerInstanceUVSet=boolean], [currentUVSet=boolean], [delete=boolean],
    [genNewUVSet=boolean], [newUVSet=string], [perInstance=boolean],
    [projections=boolean], [rename=boolean], [reorder=boolean], [shareInstances=boolean],
    [unshared=boolean], [uvSet=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUVSet.html
    """
    return _wrapCommand(cmds.polyUVSet, args, kwargs)


def polyUVStackSimilarShells(*args, **kwargs):  # noqa
    """Stack Similar UV Shells.

    polyUVStackSimilarShells( selectionItem[] , [onlyMatch=boolean], [tolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyUVStackSimilarShells.html
    """
    return _wrapCommand(cmds.polyUVStackSimilarShells, args, kwargs)


def polyWedgeFace(*args, **kwargs):  # noqa
    """Extrude faces about an axis.

    polyWedgeFace([axis=[float, float, float]], [caching=boolean], [center=[float, float,
    float]], [constructionHistory=boolean], [divisions=int], [edge=int], [name=string],
    [nodeState=int], [wedgeAngle=angle], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/polyWedgeFace.html
    """
    return _wrapCommand(cmds.polyWedgeFace, args, kwargs)


def popupMenu(*args, **kwargs):  # noqa
    """This command creates a popup menu and attaches it to the current control if no parent is
    specified.

    popupMenu( string , [allowOptionBoxes=boolean], [altModifier=boolean], [button=int],
    [ctrlModifier=boolean], [defineTemplate=string], [deleteAllItems=boolean],
    [exists=boolean], [itemArray=boolean], [markingMenu=boolean], [numberOfItems=boolean],
    [parent=string], [postMenuCommand=script], [postMenuCommandOnce=boolean],
    [shiftModifier=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/popupMenu.html
    """
    return _wrapCommand(cmds.popupMenu, args, kwargs)


def pose(*args, **kwargs):  # noqa
    """This command is used to create character poses.

    pose([allPoses=boolean], [apply=boolean], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/pose.html
    """
    return _wrapCommand(cmds.pose, args, kwargs)


def poseEditor(*args, **kwargs):  # noqa
    """This command creates an editor that derives from the base editor class that has controls
    for deformer and control nodes.

    poseEditor( string , [control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string],
    [selectionConnection=string], [stateString=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/poseEditor.html
    """
    return _wrapCommand(cmds.poseEditor, args, kwargs)


def posePanel(*args, **kwargs):  # noqa
    """This command creates a panel that derives from the base panel class that houses a
    poseEditor.

    posePanel( string , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [poseEditor=boolean], [replacePanel=string],
    [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/posePanel.html
    """
    return _wrapCommand(cmds.posePanel, args, kwargs)


def preferredRenderer(*args, **kwargs):  # noqa
    """Command to set the preferred renderer.

    preferredRenderer([string], [fallback=string], [makeCurrent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/preferredRenderer.html
    """
    return _wrapCommand(cmds.preferredRenderer, args, kwargs)


def preloadRefEd(*args, **kwargs):  # noqa
    """This creates an editor for managing which references will be read in (loaded) and which
    deferred (unloaded) upon opening a file.

    preloadRefEd([control=boolean], [defineTemplate=string], [docTag=string],
    [exists=boolean], [filter=string], [forceMainConnection=string],
    [highlightConnection=string], [lockMainConnection=boolean],
    [mainListConnection=string], [panel=string], [parent=string], [selectCommand=script],
    [selectFileNode=boolean], [selectionConnection=string], [stateString=boolean],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/preloadRefEd.html
    """
    return _wrapCommand(cmds.preloadRefEd, args, kwargs)


def prepareRender(*args, **kwargs):  # noqa
    """This command is used to register, manage and invoke render traversals.

    prepareRender([defaultTraversalSet=string], [deregister=string],
    [invokePostRender=boolean], [invokePostRenderFrame=boolean],
    [invokePostRenderLayer=boolean], [invokePreRender=boolean],
    [invokePreRenderFrame=boolean], [invokePreRenderLayer=boolean],
    [invokeSettingsUI=boolean], [label=string], [listTraversalSets=boolean],
    [postRender=script], [postRenderFrame=script], [postRenderLayer=script],
    [preRender=script], [preRenderFrame=script], [preRenderLayer=script],
    [restore=boolean], [saveAssemblyConfig=boolean], [settingsUI=script], [setup=boolean],
    [traversalSet=string], [traversalSetInit=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/prepareRender.html
    """
    return _wrapCommand(cmds.prepareRender, args, kwargs)


def profiler(*args, **kwargs):  # noqa
    """The profiler is used to record timing information from key events within Maya, as an aid
    in tuning the performance of scenes, scripts and plug-ins.

    profiler([addCategory=string], [allCategories=boolean], [bufferSize=int],
    [categoryIndex=int], [categoryIndexToName=int], [categoryInfo=string],
    [categoryName=string], [categoryNameToIndex=string], [categoryRecording=boolean],
    [clearAllMelInstrumentation=boolean], [colorIndex=int], [eventCPUId=boolean],
    [eventCategory=boolean], [eventColor=boolean], [eventCount=boolean],
    [eventDescription=boolean], [eventDuration=boolean], [eventIndex=int],
    [eventName=boolean], [eventStartTime=boolean], [eventThreadId=boolean],
    [instrumentMel=boolean], [load=string], [output=string],
    [procedureDescription=string], [procedureName=string], [removeCategory=string],
    [reset=boolean], [sampling=boolean], [signalEvent=boolean], [signalMelEvent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/profiler.html
    """
    return _wrapCommand(cmds.profiler, args, kwargs)


def profilerTool(*args, **kwargs):  # noqa
    """This script is intended to be used by the profilerPanel to interact with the profiler
    tool's view (draw region).

    profilerTool([categoryView=boolean], [collapseSelectedEvents=boolean],
    [collapseSelectedEventsRepetition=boolean], [cpuView=boolean], [destroy=boolean],
    [eventTypes=boolean], [exists=boolean], [expandSelectedEvents=boolean],
    [expandSelectedEventsRepetition=boolean], [findNext=boolean], [findPrevious=boolean],
    [frameAll=boolean], [frameSelected=boolean], [isolateSegment=int], [make=boolean],
    [matchWholeWord=boolean], [searchEvent=string], [segmentCount=boolean],
    [showAllEvent=boolean], [showCriticalPath=boolean], [showHotspot=boolean],
    [showSelectedEvents=boolean], [showSelectedEventsRepetition=boolean],
    [threadView=boolean], [unisolateSegment=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/profilerTool.html
    """
    return _wrapCommand(cmds.profilerTool, args, kwargs)


def progressBar(*args, **kwargs):  # noqa
    """Creates a progress bar control that graphically fills in as its progress value increases.

    progressBar( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [beginProgress=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [endProgress=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [isCancelled=boolean], [isInterruptable=boolean],
    [isMainProgressBar=boolean], [isObscured=boolean], [manage=boolean], [maxValue=int],
    [minValue=int], [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [progress=int], [status=string],
    [statusBarMessage=string], [step=int], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/progressBar.html
    """
    return _wrapCommand(cmds.progressBar, args, kwargs)


def progressWindow(*args, **kwargs):  # noqa
    """The progressWindow command creates a window containing a status message, a graphical
    progress gauge, and optionally a "Hit ESC to Cancel" label for interruptable
    operations.

    progressWindow([endProgress=boolean], [isCancelled=boolean], [isInterruptable=boolean],
    [maxValue=int], [minValue=int], [progress=int], [status=string], [step=int],
    [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/progressWindow.html
    """
    return _wrapCommand(cmds.progressWindow, args, kwargs)


def projectCurve(*args, **kwargs):  # noqa
    """The projectCurve command creates curves on surface where all selected curves project onto
    the selected surfaces.

    projectCurve( [curve] [surface] , [caching=boolean], [constructionHistory=boolean],
    [direction=[linear, linear, linear]], [directionX=linear], [directionY=linear],
    [directionZ=linear], [name=string], [nodeState=int], [object=boolean],
    [range=boolean], [tolerance=linear], [useNormal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/projectCurve.html
    """
    return _wrapCommand(cmds.projectCurve, args, kwargs)


def projectionContext(*args, **kwargs):  # noqa
    """Set the context for projection manips.

    projectionContext([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/projectionContext.html
    """
    return _wrapCommand(cmds.projectionContext, args, kwargs)


def projectionManip(*args, **kwargs):  # noqa
    """Various commands to set the manipulator to interesting positions.

    projectionManip([fitBBox=boolean], [projType=int], [switchType=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/projectionManip.html
    """
    return _wrapCommand(cmds.projectionManip, args, kwargs)


def projectTangent(*args, **kwargs):  # noqa
    """The project tangent command is used to align (for tangents) a curve to two other curves or
    a surface.

    projectTangent( [curve] [[curve] [curve] | [surface]] , [caching=boolean],
    [constructionHistory=boolean], [curvature=boolean], [curvatureScale=linear],
    [ignoreEdges=boolean], [name=string], [nodeState=int], [object=boolean],
    [replaceOriginal=boolean], [reverseTangent=boolean], [rotate=angle],
    [tangentDirection=int], [tangentScale=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/projectTangent.html
    """
    return _wrapCommand(cmds.projectTangent, args, kwargs)


def promptDialog(*args, **kwargs):  # noqa
    """The promptDialog command creates a modal dialog with a message to the user, a text field
    in which the user may enter a response, and a variable number of buttons to dismiss
    the dialog.

    promptDialog([backgroundColor=[float, float, float]], [button=string],
    [cancelButton=string], [defaultButton=string], [dismissString=string],
    [message=string], [messageAlign=string], [parent=string], [scrollableField=boolean],
    [style=string], [text=string], [title=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/promptDialog.html
    """
    return _wrapCommand(cmds.promptDialog, args, kwargs)


def propModCtx(*args, **kwargs):  # noqa
    """Controls the proportional move context.

    propModCtx( string , [animCurve=string], [animCurveFalloff=[float, float]],
    [animCurveParam=string], [direction=[float, float, float]], [exists=boolean],
    [image1=string], [image2=string], [image3=string], [linear=float],
    [linearParam=[float, float]], [nurbsCurve=string], [powerCutoff=float],
    [powerCutoffParam=[float, float]], [powerDegree=float], [powerDegreeParam=float],
    [script=string], [scriptParam=string], [type=int], [worldspace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/propModCtx.html
    """
    return _wrapCommand(cmds.propModCtx, args, kwargs)


def propMove(*args, **kwargs):  # noqa
    """Performs a proportional translate, scale or rotate operation on any number of objects.

    propMove( [objects] , [percent=float], [percentX=float], [percentY=float],
    [percentZ=float], [pivot=[float, float, float]], [rotate=[angle, angle, angle]],
    [scale=[float, float, float]], [translate=[linear, linear, linear]],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/propMove.html
    """
    return _wrapCommand(cmds.propMove, args, kwargs)


def proximityWrap(*args, **kwargs):  # noqa
    """This command creates a proximityWrap deformer, which deforms geometry based on the
    distance from its drivers.

    proximityWrap( [objects] , [addDrivers=string], [applyUserDefaults=boolean],
    [canBeAdded=string], [driverIndices=boolean], [dumpInfo=boolean],
    [freeDriverIndex=boolean], [removeDrivers=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/proximityWrap.html
    """
    return _wrapCommand(cmds.proximityWrap, args, kwargs)


def psdChannelOutliner(*args, **kwargs):  # noqa
    """Create a psdChannelOutliner control which is capable of displaying a tree structure upto
    one level.

    psdChannelOutliner( string , [addChild=[string, string]], [allItems=boolean],
    [annotation=string], [backgroundColor=[float, float, float]], [defineTemplate=string],
    [docTag=string], [doubleClickCommand=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfItems=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [psdParent=string], [removeAll=boolean], [removeChild=string], [select=string],
    [selectCommand=string], [selectItem=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/psdChannelOutliner.html
    """
    return _wrapCommand(cmds.psdChannelOutliner, args, kwargs)


def psdEditTextureFile(*args, **kwargs):  # noqa
    """Edits the existing PSD file.

    psdEditTextureFile([addChannel=string], [addChannelColor=[string, float, float, float]],
    [addChannelImage=[string, string]], [deleteChannel=string], [psdFileName=string],
    [snapShotImage=string], [uvSnapPostionTop=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/psdEditTextureFile.html
    """
    return _wrapCommand(cmds.psdEditTextureFile, args, kwargs)


def psdExport(*args, **kwargs):  # noqa
    """Writes the Photoshop file layer set into different formats.

    psdExport([alphaChannelIdx=int], [bytesPerChannel=int], [emptyLayerSet=boolean],
    [format=string], [layerName=string], [layerSetName=string], [outFileName=string],
    [preMultiplyAlpha=boolean], [psdFileName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/psdExport.html
    """
    return _wrapCommand(cmds.psdExport, args, kwargs)


def psdTextureFile(*args, **kwargs):  # noqa
    """Creates a Photoshop file with UVSnap shot image and the layer set names as the input.

    psdTextureFile([channelRGB=[string, uint, uint, uint, uint]], [channels=[string, uint,
    boolean]], [imageFileName=[string, string, uint]], [psdFileName=string],
    [snapShotImageName=string], [uvSnapPostionTop=boolean], [xResolution=uint],
    [yResolution=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/psdTextureFile.html
    """
    return _wrapCommand(cmds.psdTextureFile, args, kwargs)


def querySubdiv(*args, **kwargs):  # noqa
    """Queries a subdivision surface based on a set of query parameters and updates the selection
    list with the results.

    querySubdiv([action=int], [level=int], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/querySubdiv.html
    """
    return _wrapCommand(cmds.querySubdiv, args, kwargs)


def quit(*args, **kwargs):  # noqa
    """This command is used to exit the application.

    quit([abort=boolean], [exitCode=uint], [force=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/quit.html
    """
    return _wrapCommand(cmds.quit, args, kwargs)


def radial(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    radial( selectionList , [attenuation=float], [magnitude=float], [maxDistance=linear],
    [name=string], [perVertex=boolean], [position=[linear, linear, linear]],
    [torusSectionRadius=linear], [type=float], [volumeExclusion=boolean],
    [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/radial.html
    """
    return _wrapCommand(cmds.radial, args, kwargs)


def radioButton(*args, **kwargs):  # noqa
    """This command creates a radio button that is added to the most recently created radio
    collection if the `-cl/collection` flag is not used.

    radioButton( [string] , [align=string], [annotation=string], [backgroundColor=[float,
    float, float]], [changeCommand=script], [collection=string], [data=int],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [editable=boolean], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [recomputeSize=boolean], [select=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/radioButton.html
    """
    return _wrapCommand(cmds.radioButton, args, kwargs)


def radioButtonGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    radioButtonGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [annotation1=string],
    [annotation2=string], [annotation3=string], [annotation4=string],
    [backgroundColor=[float, float, float]], [changeCommand=script],
    [changeCommand1=script], [changeCommand2=script], [changeCommand3=script],
    [changeCommand4=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [data1=int], [data2=int], [data3=int],
    [data4=int], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [editable=boolean], [enable=boolean], [enable1=boolean],
    [enable2=boolean], [enable3=boolean], [enable4=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [label1=string], [label2=string], [label3=string], [label4=string],
    [labelAnnotation=string], [labelArray2=[string, string]], [labelArray3=[string,
    string, string]], [labelArray4=[string, string, string, string]], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [numberOfRadioButtons=int],
    [offCommand=script], [offCommand1=script], [offCommand2=script], [offCommand3=script],
    [offCommand4=script], [onCommand=script], [onCommand1=script], [onCommand2=script],
    [onCommand3=script], [onCommand4=script], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [select=int],
    [shareCollection=string], [statusBarMessage=string], [useTemplate=string],
    [vertical=boolean], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/radioButtonGrp.html
    """
    return _wrapCommand(cmds.radioButtonGrp, args, kwargs)


def radioCollection(*args, **kwargs):  # noqa
    """This command creates a radio button collection.

    radioCollection( [string] , [collectionItemArray=boolean], [defineTemplate=string],
    [exists=boolean], [gl=boolean], [numberOfCollectionItems=boolean], [parent=string],
    [select=string], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/radioCollection.html
    """
    return _wrapCommand(cmds.radioCollection, args, kwargs)


def radioMenuItemCollection(*args, **kwargs):  # noqa
    """This command creates a radioMenuItemCollection.

    radioMenuItemCollection( [string] , [defineTemplate=string], [exists=boolean],
    [gl=boolean], [parent=string], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/radioMenuItemCollection.html
    """
    return _wrapCommand(cmds.radioMenuItemCollection, args, kwargs)


def rampColorPort(*args, **kwargs):  # noqa
    """This command creates a control that displays an image representing the ramp node
    specified, and supports editing of that node.

    rampColorPort( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [node=name], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [selectedColorControl=string],
    [selectedInterpControl=string], [selectedPositionControl=string],
    [statusBarMessage=string], [useTemplate=string], [verticalLayout=boolean],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rampColorPort.html
    """
    return _wrapCommand(cmds.rampColorPort, args, kwargs)


def rangeControl(*args, **kwargs):  # noqa
    """This command creates a control used for displaying and modifying the current playback
    range.

    rangeControl( name , [annotation=string], [backgroundColor=[float, float, float]],
    [changedCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [maxRange=time], [minRange=time],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int],
    [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rangeControl.html
    """
    return _wrapCommand(cmds.rangeControl, args, kwargs)


def readTake(*args, **kwargs):  # noqa
    """This action reads a take (.

    readTake([angle=string], [device=string], [frequency=float], [linear=string],
    [noTime=boolean], [take=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/readTake.html
    """
    return _wrapCommand(cmds.readTake, args, kwargs)


def rebuildCurve(*args, **kwargs):  # noqa
    """This command rebuilds a curve by modifying its parameterization.

    rebuildCurve( curve [curve] , [caching=boolean], [constructionHistory=boolean],
    [degree=int], [endKnots=int], [fitRebuild=boolean], [keepControlPoints=boolean],
    [keepEndPoints=boolean], [keepRange=int], [keepTangents=boolean], [name=string],
    [nodeState=int], [object=boolean], [range=boolean], [rebuildType=int],
    [replaceOriginal=boolean], [smartSurfaceCurveRebuild=boolean], [spans=int],
    [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rebuildCurve.html
    """
    return _wrapCommand(cmds.rebuildCurve, args, kwargs)


def rebuildSurface(*args, **kwargs):  # noqa
    """This command rebuilds a surface by modifying its parameterization.

    rebuildSurface( surface [surface] , [caching=boolean], [constructionHistory=boolean],
    [degreeU=int], [degreeV=int], [direction=int], [endKnots=int], [fitRebuild=int],
    [keepControlPoints=boolean], [keepCorners=boolean], [keepRange=int], [name=string],
    [nodeState=int], [object=boolean], [polygon=int], [rebuildType=int],
    [replaceOriginal=boolean], [spansU=int], [spansV=int], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rebuildSurface.html
    """
    return _wrapCommand(cmds.rebuildSurface, args, kwargs)


def recordAttr(*args, **kwargs):  # noqa
    """This command sets up an attribute to be recorded.

    recordAttr([attribute=string], [delete=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/recordAttr.html
    """
    return _wrapCommand(cmds.recordAttr, args, kwargs)


def recordDevice(*args, **kwargs):  # noqa
    """Starts and stops server side device recording.

    recordDevice([cleanup=boolean], [data=boolean], [device=string], [duration=int],
    [playback=boolean], [state=boolean], [wait=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/recordDevice.html
    """
    return _wrapCommand(cmds.recordDevice, args, kwargs)


def redo(*args, **kwargs):  # noqa
    """Takes the most recently undone command from the undo list and redoes it.

    redo()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/redo.html
    """
    return _wrapCommand(cmds.redo, args, kwargs)


def referenceEdit(*args, **kwargs):  # noqa
    """Use this command to remove and change the modifications which have been applied to
    references.

    referenceEdit([applyFailedEdits=boolean], [changeEditTarget=[string, string]],
    [editCommand=string], [failedEdits=boolean], [onReferenceNode=string],
    [removeEdits=boolean], [successfulEdits=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/referenceEdit.html
    """
    return _wrapCommand(cmds.referenceEdit, args, kwargs)


def referenceQuery(*args, **kwargs):  # noqa
    """Use this command to find out information about references and referenced nodes.

    referenceQuery([child=boolean], [dagPath=boolean], [editAttrs=boolean],
    [editCommand=string], [editNodes=boolean], [editStrings=boolean],
    [failedEdits=boolean], [filename=boolean], [isExportEdits=boolean],
    [isLoaded=boolean], [isNodeReferenced=boolean], [isPreviewOnly=boolean],
    [liveEdits=boolean], [namespace=boolean], [nodes=boolean], [onReferenceNode=string],
    [parent=boolean], [parentNamespace=boolean], [referenceNode=boolean],
    [shortName=boolean], [showDagPath=boolean], [showFullPath=boolean],
    [showNamespace=boolean], [successfulEdits=boolean], [topReference=boolean],
    [unresolvedName=boolean], [withoutCopyNumber=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/referenceQuery.html
    """
    return _wrapCommand(cmds.referenceQuery, args, kwargs)


def refineSubdivSelectionList(*args, **kwargs):  # noqa
    """Refines a subdivision surface set of components based on the selection list.

    refineSubdivSelectionList()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/refineSubdivSelectionList.html
    """
    return _wrapCommand(cmds.refineSubdivSelectionList, args, kwargs)


def refresh(*args, **kwargs):  # noqa
    """This command is used to force a redraw during script execution.

    refresh([currentView=boolean], [fileExtension=string], [filename=string], [force=boolean],
    [suspend=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/refresh.html
    """
    return _wrapCommand(cmds.refresh, args, kwargs)


def refreshEditorTemplates(*args, **kwargs):  # noqa
    """This command refreshes all cached attribute editor templates, including those copied from
    the standard AE.

    refreshEditorTemplates()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/refreshEditorTemplates.html
    """
    return _wrapCommand(cmds.refreshEditorTemplates, args, kwargs)


def regionSelectKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to scale keyframes within the graph
    editor using the region select tool.

    regionSelectKeyCtx( contextName , [bottomManip=float], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [leftManip=float], [name=string], [rightManip=float], [topManip=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/regionSelectKeyCtx.html
    """
    return _wrapCommand(cmds.regionSelectKeyCtx, args, kwargs)


def relationship(*args, **kwargs):  # noqa
    """This is primarily for use with file IO.

    relationship([b=boolean], [relationshipData=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/relationship.html
    """
    return _wrapCommand(cmds.relationship, args, kwargs)


def reloadImage(*args, **kwargs):  # noqa
    """This command reloads an xpm image from disk.

    reloadImage( string string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reloadImage.html
    """
    return _wrapCommand(cmds.reloadImage, args, kwargs)


def rememberCtxSettings(*args, **kwargs):  # noqa
    """This command restores a tool to its saved settings.

    rememberCtxSettings( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rememberCtxSettings.html
    """
    return _wrapCommand(cmds.rememberCtxSettings, args, kwargs)


def removeJoint(*args, **kwargs):  # noqa
    """This command will remove the selected joint or the joint given at the command line from
    the skeleton.

    removeJoint( [object] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/removeJoint.html
    """
    return _wrapCommand(cmds.removeJoint, args, kwargs)


def removeMultiInstance(*args, **kwargs):  # noqa
    """Removes a particular instance of a multiElement.

    removeMultiInstance( attribute , [allChildren=boolean], [b=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/removeMultiInstance.html
    """
    return _wrapCommand(cmds.removeMultiInstance, args, kwargs)


def rename(*args, **kwargs):  # noqa
    """Renames the given object to have the new name.

    rename( [object] string , [ignoreShape=boolean], [uuid=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rename.html
    """
    return _wrapCommand(cmds.rename, args, kwargs)


def renameAttr(*args, **kwargs):  # noqa
    """Renames the given user-defined attribute to the name given in the string argument.

    renameAttr()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renameAttr.html
    """
    return _wrapCommand(cmds.renameAttr, args, kwargs)


def renameUI(*args, **kwargs):  # noqa
    """This command renames the UI object passed as first arument to the new name specified as
    second argument.

    renameUI( string string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renameUI.html
    """
    return _wrapCommand(cmds.renameUI, args, kwargs)


def render(*args, **kwargs):  # noqa
    """The render command is used to start off a MayaSoftware rendering session of the currently
    active camera.

    render( [camera] , [abortMissingTexture=boolean], [batch=boolean], [keepPreImage=boolean],
    [layer=string], [nglowpass=boolean], [nshadows=boolean], [replace=boolean],
    [xresolution=int], [yresolution=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/render.html
    """
    return _wrapCommand(cmds.render, args, kwargs)


def renderer(*args, **kwargs):  # noqa
    """Command to register renders.

    renderer([string], [addGlobalsNode=string], [addGlobalsTab=[string, string, string]],
    [batchRenderOptionsProcedure=string], [batchRenderOptionsStringProcedure=string],
    [batchRenderProcedure=string], [cancelBatchRenderProcedure=string],
    [changeIprRegionProcedure=string], [commandRenderProcedure=string], [exists=boolean],
    [globalsNodes=boolean], [globalsTabCreateProcNames=boolean],
    [globalsTabLabels=boolean], [globalsTabUpdateProcNames=boolean],
    [iprOptionsMenuLabel=string], [iprOptionsProcedure=string],
    [iprOptionsSubMenuProcedure=string], [iprRenderProcedure=string],
    [iprRenderSubMenuProcedure=string], [isRunningIprProcedure=string],
    [logoCallbackProcedure=string], [logoImageName=string],
    [materialViewRendererList=boolean], [materialViewRendererPause=boolean],
    [materialViewRendererSuspend=boolean], [namesOfAvailableRenderers=boolean],
    [pauseIprRenderProcedure=string], [polyPrelightProcedure=string],
    [refreshIprRenderProcedure=string], [renderDiagnosticsProcedure=string],
    [renderGlobalsProcedure=string], [renderMenuProcedure=string],
    [renderOptionsProcedure=string], [renderProcedure=string],
    [renderRegionProcedure=string], [renderSequenceProcedure=string],
    [rendererUIName=string], [renderingEditorsSubMenuProcedure=string],
    [showBatchRenderLogProcedure=string], [showBatchRenderProcedure=string],
    [showRenderLogProcedure=string], [startIprRenderProcedure=string],
    [stopIprRenderProcedure=string], [supportColorManagement=boolean],
    [textureBakingProcedure=string], [unregisterRenderer=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderer.html
    """
    return _wrapCommand(cmds.renderer, args, kwargs)


def renderGlobalsNode(*args, **kwargs):  # noqa
    """This command creates a new node in the dependency graph of the specified type.

    renderGlobalsNode( string , [name=string], [parent=string], [renderQuality=string],
    [renderResolution=string], [shared=boolean], [skipSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderGlobalsNode.html
    """
    return _wrapCommand(cmds.renderGlobalsNode, args, kwargs)


def renderInfo(*args, **kwargs):  # noqa
    """The renderInfo commands sets geometric properties of surfaces of the selected object.

    renderInfo([castShadows=boolean], [chordHeight=float], [chordHeightRatio=float],
    [doubleSided=boolean], [edgeSwap=boolean], [minScreen=float], [name=string],
    [opposite=boolean], [smoothShading=boolean], [unum=int], [useChordHeight=boolean],
    [useChordHeightRatio=boolean], [useDefaultLights=boolean], [useMinScreen=boolean],
    [utype=int], [vnum=int], [vtype=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderInfo.html
    """
    return _wrapCommand(cmds.renderInfo, args, kwargs)


def renderLayerPostProcess(*args, **kwargs):  # noqa
    """Post process the results when rendering is done with.

    renderLayerPostProcess([keepImages=boolean], [sceneName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderLayerPostProcess.html
    """
    return _wrapCommand(cmds.renderLayerPostProcess, args, kwargs)


def renderManip(*args, **kwargs):  # noqa
    """This command creates manipulators for cameras or lights.

    renderManip( object , [camera=[boolean, boolean, boolean, boolean, boolean]],
    [light=[boolean, boolean, boolean]], [spotLight=[boolean, boolean, boolean, boolean,
    boolean, boolean, boolean]], [state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderManip.html
    """
    return _wrapCommand(cmds.renderManip, args, kwargs)


def renderPartition(*args, **kwargs):  # noqa
    """Set or query the model's current partition.

    renderPartition( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderPartition.html
    """
    return _wrapCommand(cmds.renderPartition, args, kwargs)


def renderPassRegistry(*args, **kwargs):  # noqa
    """query information related with render passes.

    renderPassRegistry([channels=int], [isPassSupported=boolean], [passID=string],
    [passName=boolean], [renderer=string], [supportedChannelCounts=boolean],
    [supportedDataTypes=boolean], [supportedPassSemantics=boolean],
    [supportedRenderPassNames=boolean], [supportedRenderPasses=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderPassRegistry.html
    """
    return _wrapCommand(cmds.renderPassRegistry, args, kwargs)


def renderQualityNode(*args, **kwargs):  # noqa
    """This command creates a new node in the dependency graph of the specified type.

    renderQualityNode( string , [name=string], [parent=string], [shared=boolean],
    [skipSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderQualityNode.html
    """
    return _wrapCommand(cmds.renderQualityNode, args, kwargs)


def renderSettings(*args, **kwargs):  # noqa
    """Query interface to the common tab of the render settings.

    renderSettings([camera=string], [customTokenString=string], [firstImageName=boolean],
    [fullPath=boolean], [fullPathTemp=boolean], [genericFrameImageName=string],
    [imageGenericName=boolean], [lastImageName=boolean], [layer=string],
    [leaveUnmatchedTokens=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderSettings.html
    """
    return _wrapCommand(cmds.renderSettings, args, kwargs)


def renderThumbnailUpdate(*args, **kwargs):  # noqa
    """Toggle the updating of object thumbnails.

    renderThumbnailUpdate( boolean , [forceUpdate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderThumbnailUpdate.html
    """
    return _wrapCommand(cmds.renderThumbnailUpdate, args, kwargs)


def renderWindowEditor(*args, **kwargs):  # noqa
    """Create a editor window that can receive the result of the rendering process.

    renderWindowEditor( editorName , [autoResize=boolean], [blendMode=int], [caption=string],
    [changeCommand=[string, string, string, string]], [clear=[int, int, float, float,
    float]], [cmEnabled=boolean], [colorManage=boolean], [compDisplay=int],
    [compImageFile=string], [control=boolean], [currentCamera=string],
    [currentCameraRig=string], [defineTemplate=string], [displayImage=int],
    [displayImageViewCount=int], [displayStyle=string], [docTag=string],
    [doubleBuffer=boolean], [drawAxis=boolean], [editorName=boolean], [exists=boolean],
    [exposure=float], [filter=string], [forceMainConnection=string], [frameImage=boolean],
    [frameRegion=boolean], [gamma=float], [highlightConnection=string],
    [loadImage=string], [lockMainConnection=boolean], [mainListConnection=string],
    [marquee=[float, float, float, float]], [nbImages=boolean], [nextViewImage=boolean],
    [outputColorManage=boolean], [panel=string], [parent=string], [pcaption=string],
    [realSize=boolean], [refresh=boolean], [removeAllImages=boolean],
    [removeImage=boolean], [resetRegion=boolean], [resetViewImage=boolean],
    [saveImage=boolean], [scaleBlue=float], [scaleGreen=float], [scaleRed=float],
    [selectionConnection=string], [showRegion=[int, int]], [singleBuffer=boolean],
    [snapshot=[string, int, int]], [snapshotMode=boolean], [stateString=boolean],
    [stereo=int], [stereoImageOrientation=[string, string]], [stereoMode=string],
    [toggle=boolean], [unParent=boolean], [unlockMainConnection=boolean],
    [updateMainConnection=boolean], [useTemplate=string], [viewImageCount=int],
    [viewTransformName=string], [writeImage=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderWindowEditor.html
    """
    return _wrapCommand(cmds.renderWindowEditor, args, kwargs)


def renderWindowSelectContext(*args, **kwargs):  # noqa
    """Set the selection context for the render view panel.

    renderWindowSelectContext([exists=boolean], [image1=string], [image2=string],
    [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/renderWindowSelectContext.html
    """
    return _wrapCommand(cmds.renderWindowSelectContext, args, kwargs)


def reorder(*args, **kwargs):  # noqa
    """This command reorders (moves) objects relative to their siblings.

    reorder( [objects...] , [back=boolean], [front=boolean], [relative=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reorder.html
    """
    return _wrapCommand(cmds.reorder, args, kwargs)


def reorderContainer(*args, **kwargs):  # noqa
    """This command reorders (moves) objects relative to their siblings in a container.

    reorderContainer([back=boolean], [front=boolean], [relative=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reorderContainer.html
    """
    return _wrapCommand(cmds.reorderContainer, args, kwargs)


def reorderDeformers(*args, **kwargs):  # noqa
    """This command changes the order in which 2 deformation nodes affect the output geometry.

    reorderDeformers( string string selectionList , [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reorderDeformers.html
    """
    return _wrapCommand(cmds.reorderDeformers, args, kwargs)


def requires(*args, **kwargs):  # noqa
    """This command is used during file I/O to specify the requirements needed to load the given
    file.

    requires( string string , [dataType=string], [nodeType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/requires.html
    """
    return _wrapCommand(cmds.requires, args, kwargs)


def reroot(*args, **kwargs):  # noqa
    """This command will reroot a skeleton.

    reroot( [object] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reroot.html
    """
    return _wrapCommand(cmds.reroot, args, kwargs)


def resampleFluid(*args, **kwargs):  # noqa
    """A command to extend the fluid grid, keeping the voxels the same size, and keeping the
    existing contents of the fluid in the same place.

    resampleFluid([resampleDepth=int], [resampleHeight=int], [resampleWidth=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/resampleFluid.html
    """
    return _wrapCommand(cmds.resampleFluid, args, kwargs)


def resetTool(*args, **kwargs):  # noqa
    """This command resets a tool back to its "factory settings".

    resetTool( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/resetTool.html
    """
    return _wrapCommand(cmds.resetTool, args, kwargs)


def resolutionNode(*args, **kwargs):  # noqa
    """This command creates a new node in the dependency graph of the specified type.

    resolutionNode( string , [name=string], [parent=string], [shared=boolean],
    [skipSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/resolutionNode.html
    """
    return _wrapCommand(cmds.resolutionNode, args, kwargs)


def resourceManager(*args, **kwargs):  # noqa
    """List resources matching certain properties.

    resourceManager([nameFilter=string], [saveAs=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/resourceManager.html
    """
    return _wrapCommand(cmds.resourceManager, args, kwargs)


def retimeKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to scale keyframes within the graph
    editor using the retime tool.

    retimeKeyCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [moveByFrame=int], [name=string],
    [snapOnFrame=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/retimeKeyCtx.html
    """
    return _wrapCommand(cmds.retimeKeyCtx, args, kwargs)


def reverseCurve(*args, **kwargs):  # noqa
    """The reverseCurve command reverses the direction of a curve or curve-on-surface.

    reverseCurve( curve , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [name=string], [nodeState=int], [object=boolean],
    [range=boolean], [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reverseCurve.html
    """
    return _wrapCommand(cmds.reverseCurve, args, kwargs)


def reverseSurface(*args, **kwargs):  # noqa
    """The reverseSurface command reverses one or both directions of a surface or can be used to
    "swap" the U and V directions (this creates the effect of reversing the surface
    normal).

    reverseSurface( surface , [caching=boolean], [constructionHistory=boolean],
    [direction=int], [name=string], [nodeState=int], [object=boolean],
    [replaceOriginal=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/reverseSurface.html
    """
    return _wrapCommand(cmds.reverseSurface, args, kwargs)


def revolve(*args, **kwargs):  # noqa
    """This command creates a revolved surface by revolving the given profile curve about an
    axis.

    revolve( curve , [autoCorrectNormal=boolean], [axis=[linear, linear, linear]],
    [axisChoice=int], [axisX=linear], [axisY=linear], [axisZ=linear], [bridge=boolean],
    [caching=boolean], [computePivotAndAxis=int], [constructionHistory=boolean],
    [degree=int], [endSweep=angle], [name=string], [nodeState=int], [object=boolean],
    [pivot=[linear, linear, linear]], [pivotX=linear], [pivotY=linear], [pivotZ=linear],
    [polygon=int], [radius=linear], [radiusAnchor=float], [range=boolean],
    [rebuild=boolean], [sections=int], [startSweep=angle], [tolerance=linear],
    [useLocalPivot=boolean], [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/revolve.html
    """
    return _wrapCommand(cmds.revolve, args, kwargs)


def rigidBody(*args, **kwargs):  # noqa
    """This command creates a rigid body from a polygonal or nurbs surface.

    rigidBody([active=boolean], [angularVelocity=boolean], [applyForceAt=string],
    [bounciness=float], [cache=boolean], [centerOfMass=[float, float, float]],
    [collisions=boolean], [contactCount=boolean], [contactName=boolean],
    [contactPosition=boolean], [damping=float], [deleteCache=boolean],
    [dynamicFriction=float], [force=boolean], [ignore=boolean], [impulse=[float, float,
    float]], [impulsePosition=[float, float, float]], [initialAngularVelocity=[float,
    float, float]], [initialVelocity=[float, float, float]], [layer=int],
    [lockCenterOfMass=boolean], [mass=float], [name=string], [orientation=[float, float,
    float]], [particleCollision=boolean], [passive=boolean], [position=[float, float,
    float]], [removeShape=string], [solver=string], [spinImpulse=[float, float, float]],
    [standInObject=string], [staticFriction=float], [tesselationFactor=int],
    [velocity=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rigidBody.html
    """
    return _wrapCommand(cmds.rigidBody, args, kwargs)


def rigidSolver(*args, **kwargs):  # noqa
    """This command sets the attributes for the rigid solver.

    rigidSolver([autoTolerances=boolean], [bounciness=boolean], [cacheData=boolean],
    [collide=boolean], [collisionTolerance=float], [contactData=boolean],
    [create=boolean], [current=boolean], [deleteCache=boolean],
    [displayCenterOfMass=boolean], [displayConstraint=boolean], [displayVelocity=boolean],
    [dynamics=boolean], [friction=boolean], [interpenetrate=boolean],
    [interpenetrationCheck=boolean], [name=string], [rigidBodies=boolean],
    [rigidBodyCount=boolean], [showCollision=boolean], [showInterpenetration=boolean],
    [solverMethod=int], [startTime=float], [state=boolean], [statistics=boolean],
    [stepSize=float], [velocityVectorScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rigidSolver.html
    """
    return _wrapCommand(cmds.rigidSolver, args, kwargs)


def roll(*args, **kwargs):  # noqa
    """The roll command rotates a camera about its viewing direction, a positive angle produces
    clockwise camera rotation, while a negative angle produces counter-clockwise camera
    rotation.

    roll( [camera] , [absolute=boolean], [degree=angle], [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/roll.html
    """
    return _wrapCommand(cmds.roll, args, kwargs)


def rollCtx(*args, **kwargs):  # noqa
    """Create, edit, or query a roll context.

    rollCtx( [context] , [alternateContext=boolean], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string], [rollScale=float],
    [toolName=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rollCtx.html
    """
    return _wrapCommand(cmds.rollCtx, args, kwargs)


def rotate(*args, **kwargs):  # noqa
    """The rotate command is used to change the rotation of geometric objects.

    rotate( float float float [objects] , [absolute=boolean], [centerPivot=boolean],
    [componentSpace=boolean], [constrainAlongNormal=boolean],
    [deletePriorHistory=boolean], [euler=boolean], [forceOrderXYZ=boolean],
    [objectCenterPivot=boolean], [objectSpace=boolean], [orientAxes=[angle, angle,
    angle]], [pivot=[linear, linear, linear]], [preserveChildPosition=boolean],
    [preserveGeometryPosition=boolean], [preserveUV=boolean], [reflection=boolean],
    [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean],
    [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean],
    [reflectionTolerance=float], [relative=boolean], [rotateX=boolean],
    [rotateXY=boolean], [rotateXYZ=boolean], [rotateXZ=boolean], [rotateY=boolean],
    [rotateYZ=boolean], [rotateZ=boolean], [symNegative=boolean], [translate=boolean],
    [worldSpace=boolean], [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rotate.html
    """
    return _wrapCommand(cmds.rotate, args, kwargs)


def rotationInterpolation(*args, **kwargs):  # noqa
    """The rotationInterpolation command converts the rotation curves to the desired rotation
    interpolation representation.

    rotationInterpolation([convert=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rotationInterpolation.html
    """
    return _wrapCommand(cmds.rotationInterpolation, args, kwargs)


def roundConstantRadius(*args, **kwargs):  # noqa
    """This command generates constant radius NURBS fillets and NURBS corner surfaces for
    matching edge pairs on NURBS surfaces.

    roundConstantRadius( string string [string string] , [append=boolean],
    [constructionHistory=boolean], [name=string], [object=boolean], [radiuss=linear],
    [side=[string, int]], [sidea=int], [sideb=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/roundConstantRadius.html
    """
    return _wrapCommand(cmds.roundConstantRadius, args, kwargs)


def rowColumnLayout(*args, **kwargs):  # noqa
    """This command creates a rowColumn layout.

    rowColumnLayout( [string] , [adjustableColumn=int], [annotation=string],
    [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=[int,
    string]], [columnAttach=[int, string, int]], [columnOffset=[int, string, int]],
    [columnSpacing=[int, int]], [columnWidth=[int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfColumns=int], [numberOfPopupMenus=boolean],
    [numberOfRows=int], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAlign=[int, string]], [rowAttach=[int, string, int]],
    [rowHeight=[int, int]], [rowOffset=[int, string, int]], [rowSpacing=[int, int]],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rowColumnLayout.html
    """
    return _wrapCommand(cmds.rowColumnLayout, args, kwargs)


def rowLayout(*args, **kwargs):  # noqa
    """This command creates a layout capable of positioning children into a single horizontal
    row.

    rowLayout( [string] , [adjustableColumn=int], [adjustableColumn1=int],
    [adjustableColumn2=int], [adjustableColumn3=int], [adjustableColumn4=int],
    [adjustableColumn5=int], [adjustableColumn6=int], [annotation=string],
    [backgroundColor=[float, float, float]], [childArray=boolean], [columnAlign=[int,
    string]], [columnAlign1=string], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach1=string], [columnAttach2=[string, string]],
    [columnAttach3=[string, string, string]], [columnAttach4=[string, string, string,
    string]], [columnAttach5=[string, string, string, string, string]],
    [columnAttach6=[string, string, string, string, string, string]], [columnOffset1=int],
    [columnOffset2=[int, int]], [columnOffset3=[int, int, int]], [columnOffset4=[int, int,
    int, int]], [columnOffset5=[int, int, int, int, int]], [columnOffset6=[int, int, int,
    int, int, int]], [columnWidth=[int, int]], [columnWidth1=int], [columnWidth2=[int,
    int]], [columnWidth3=[int, int, int]], [columnWidth4=[int, int, int, int]],
    [columnWidth5=[int, int, int, int, int]], [columnWidth6=[int, int, int, int, int,
    int]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfColumns=int],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/rowLayout.html
    """
    return _wrapCommand(cmds.rowLayout, args, kwargs)


def runTimeCommand(*args, **kwargs):  # noqa
    """Create a MEL command given the specified name.

    runTimeCommand( name , [addKeyword=string], [addTag=string], [annotation=string],
    [category=string], [categoryArray=boolean], [command=script], [commandArray=boolean],
    [commandLanguage=string], [default=boolean], [defaultCommandArray=boolean],
    [delete=boolean], [exists=boolean], [helpUrl=string], [hotkeyCtx=string],
    [image=string], [keywords=string], [label=string], [longAnnotation=string],
    [numberOfCommands=boolean], [numberOfDefaultCommands=boolean],
    [numberOfUserCommands=boolean], [plugin=string], [save=boolean],
    [showInHotkeyEditor=boolean], [tags=string], [userCommandArray=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/runTimeCommand.html
    """
    return _wrapCommand(cmds.runTimeCommand, args, kwargs)


def runup(*args, **kwargs):  # noqa
    """runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it
    does so.

    runup([cache=boolean], [fromPreviousFrame=boolean], [fromStartFrame=boolean],
    [maxFrame=time], [state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/runup.html
    """
    return _wrapCommand(cmds.runup, args, kwargs)


def sampleImage(*args, **kwargs):  # noqa
    """The sampleImage command is used to control parameters of sample images, such as swatches
    in the multilister.

    sampleImage([fastSample=boolean], [resolution=[int, name]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sampleImage.html
    """
    return _wrapCommand(cmds.sampleImage, args, kwargs)


def saveAllShelves(*args, **kwargs):  # noqa
    """This command writes all shelves that are immediate children of the specified control
    layout to the prefs directory.

    saveAllShelves( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveAllShelves.html
    """
    return _wrapCommand(cmds.saveAllShelves, args, kwargs)


def saveFluid(*args, **kwargs):  # noqa
    """A command to save the current state of the fluid to the initial state cache.

    saveFluid([currentTime=int], [endTime=int], [startTime=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveFluid.html
    """
    return _wrapCommand(cmds.saveFluid, args, kwargs)


def saveImage(*args, **kwargs):  # noqa
    """This command creates a static image for non-xpm files.

    saveImage( [imageName] [imageName] , [annotation=string], [backgroundColor=[float, float,
    float]], [currentView=boolean], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [image=string], [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [objectThumbnail=string], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [sceneFile=string],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveImage.html
    """
    return _wrapCommand(cmds.saveImage, args, kwargs)


def saveInitialState(*args, **kwargs):  # noqa
    """saveInitialState saves the current state of dynamics objects as the initial state.

    saveInitialState( selectionList , [attribute=string], [saveall=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveInitialState.html
    """
    return _wrapCommand(cmds.saveInitialState, args, kwargs)


def saveMenu(*args, **kwargs):  # noqa
    """This command is used for saving the contents of a menu, so that another instance of the
    menu may be recreated later.

    saveMenu( string string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveMenu.html
    """
    return _wrapCommand(cmds.saveMenu, args, kwargs)


def savePrefObjects(*args, **kwargs):  # noqa
    """This command saves preference dependency nodes to "userPrefObjects.

    savePrefObjects()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/savePrefObjects.html
    """
    return _wrapCommand(cmds.savePrefObjects, args, kwargs)


def savePrefs(*args, **kwargs):  # noqa
    """This command saves preferences to disk.

    savePrefs([colors=boolean], [file=string], [general=boolean], [hotkeys=boolean],
    [menuSets=boolean], [plugins=boolean], [uiLayout=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/savePrefs.html
    """
    return _wrapCommand(cmds.savePrefs, args, kwargs)


def saveShelf(*args, **kwargs):  # noqa
    """This command saves the specified shelf (first argument) to the specified file (second
    argument).

    saveShelf( string string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveShelf.html
    """
    return _wrapCommand(cmds.saveShelf, args, kwargs)


def saveToolSettings(*args, **kwargs):  # noqa
    """This command causes all the tools not on the shelf to save their settings as optionVars.

    saveToolSettings()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveToolSettings.html
    """
    return _wrapCommand(cmds.saveToolSettings, args, kwargs)


def saveViewportSettings(*args, **kwargs):  # noqa
    """This command causes all the 3d views to save their settings as optionVar's.

    saveViewportSettings()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/saveViewportSettings.html
    """
    return _wrapCommand(cmds.saveViewportSettings, args, kwargs)


def scale(*args, **kwargs):  # noqa
    """The scale command is used to change the sizes of geometric objects.

    scale( float float float [objects] , [absolute=boolean], [centerPivot=boolean],
    [componentSpace=boolean], [constrainAlongNormal=boolean],
    [deletePriorHistory=boolean], [distanceOnly=boolean], [localSpace=boolean],
    [objectCenterPivot=boolean], [objectSpace=boolean], [orientAxes=[angle, angle,
    angle]], [pivot=[linear, linear, linear]], [preserveChildPosition=boolean],
    [preserveGeometryPosition=boolean], [preserveUV=boolean], [reflection=boolean],
    [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean],
    [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean],
    [reflectionTolerance=float], [relative=boolean], [scaleX=boolean], [scaleXY=boolean],
    [scaleXYZ=boolean], [scaleXZ=boolean], [scaleY=boolean], [scaleYZ=boolean],
    [scaleZ=boolean], [symNegative=boolean], [worldSpace=boolean],
    [xformConstraint=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scale.html
    """
    return _wrapCommand(cmds.scale, args, kwargs)


def scaleComponents(*args, **kwargs):  # noqa
    """This is a limited version of the scale command.

    scaleComponents( float float float [objects] , [pivot=[linear, linear, linear]],
    [rotation=[angle, angle, angle]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scaleComponents.html
    """
    return _wrapCommand(cmds.scaleComponents, args, kwargs)


def scaleConstraint(*args, **kwargs):  # noqa
    """Constrain an object's scale to the scale of the target object or to the average scale of a
    number of targets.

    scaleConstraint( [target...] [object] , [layer=string], [maintainOffset=boolean],
    [name=string], [offset=[float, float, float]], [remove=boolean],
    [scaleCompensate=boolean], [skip=string], [targetList=boolean], [weight=float],
    [weightAliasList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scaleConstraint.html
    """
    return _wrapCommand(cmds.scaleConstraint, args, kwargs)


def scaleKey(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    scaleKey( objects , [animation=string], [attribute=string], [autoSnap=boolean],
    [controlPoints=boolean], [float=floatrange], [floatPivot=float], [floatScale=float],
    [hierarchy=string], [includeUpperBound=boolean], [index=uint], [newEndFloat=float],
    [newEndTime=time], [newStartFloat=float], [newStartTime=time],
    [scaleSpecifiedKeys=boolean], [shape=boolean], [time=timerange], [timePivot=time],
    [timeScale=float], [valuePivot=float], [valueScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scaleKey.html
    """
    return _wrapCommand(cmds.scaleKey, args, kwargs)


def scaleKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to scale keyframes within the graph
    editor.

    scaleKeyCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [scaleSpecifiedKeys=boolean],
    [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scaleKeyCtx.html
    """
    return _wrapCommand(cmds.scaleKeyCtx, args, kwargs)


def sceneEditor(*args, **kwargs):  # noqa
    """This creates an editor for managing the files in a scene.

    sceneEditor([control=boolean], [defineTemplate=string], [docTag=string], [exists=boolean],
    [filter=string], [forceMainConnection=string], [highlightConnection=string],
    [lockMainConnection=boolean], [mainListConnection=string], [onlyParents=boolean],
    [panel=string], [parent=string], [refreshReferences=boolean], [selectCommand=script],
    [selectItem=int], [selectReference=string], [selectionConnection=string],
    [shortName=boolean], [stateString=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [unresolvedName=boolean],
    [updateMainConnection=boolean], [useTemplate=string], [withoutCopyNumber=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sceneEditor.html
    """
    return _wrapCommand(cmds.sceneEditor, args, kwargs)


def sceneLint(*args, **kwargs):  # noqa
    """{ "sceneLint" : { "ISSUE_CODE" : { "description" : "DETAILED_DESCRIPTION_OF_ISSUE",
    "mitigation" : [ // List of mitigations that can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }.

    sceneLint([issueType=string], [verbose=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sceneLint.html
    """
    return _wrapCommand(cmds.sceneLint, args, kwargs)


def sceneUIReplacement(*args, **kwargs):  # noqa
    """This command returns existing scene based UI that can be utilized by the scene that is
    being loaded.

    sceneUIReplacement([clear=boolean], [deleteRemaining=boolean], [getNextFilter=[string,
    string]], [getNextPanel=[string, string]], [getNextScriptedPanel=[string, string]],
    [update=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sceneUIReplacement.html
    """
    return _wrapCommand(cmds.sceneUIReplacement, args, kwargs)


def scmh(*args, **kwargs):  # noqa
    """Set the current manipulator handle value(s).

    scmh( float [float...] , [absolute=boolean], [ignore=uint], [quiet=boolean],
    [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scmh.html
    """
    return _wrapCommand(cmds.scmh, args, kwargs)


def scriptCtx(*args, **kwargs):  # noqa
    """This command allows a user to create their own tools based on the selection tool.

    scriptCtx( string , [allComponents=boolean], [allObjects=boolean],
    [animBreakdown=boolean], [animCurve=boolean], [animInTangent=boolean],
    [animKeyframe=boolean], [animOutTangent=boolean], [baseClassName=string],
    [camera=boolean], [cluster=boolean], [collisionModel=boolean],
    [controlVertex=boolean], [cumulativeLists=boolean], [curve=boolean],
    [curveKnot=boolean], [curveOnSurface=boolean], [curveParameterPoint=boolean],
    [dimension=boolean], [dynamicConstraint=boolean], [edge=boolean], [editPoint=boolean],
    [emitter=boolean], [enableRootSelection=boolean], [escToQuit=boolean],
    [exists=boolean], [exitUponCompletion=boolean], [expandSelectionList=boolean],
    [facet=boolean], [field=boolean], [finalCommandScript=script], [fluid=boolean],
    [follicle=boolean], [forceAddSelect=boolean], [hairSystem=boolean], [handle=boolean],
    [history=boolean], [hull=boolean], [ignoreInvalidItems=boolean],
    [ikEndEffector=boolean], [ikHandle=boolean], [image1=string], [image2=string],
    [image3=string], [imagePlane=boolean], [implicitGeometry=boolean], [isoparm=boolean],
    [joint=boolean], [jointPivot=boolean], [lastAutoComplete=boolean], [lattice=boolean],
    [latticePoint=boolean], [light=boolean], [localRotationAxis=boolean],
    [locator=boolean], [locatorUV=boolean], [locatorXYZ=boolean], [nCloth=boolean],
    [nParticle=boolean], [nParticleShape=boolean], [nRigid=boolean], [name=string],
    [nonlinear=boolean], [nurbsCurve=boolean], [nurbsSurface=boolean],
    [objectComponent=boolean], [orientationLocator=boolean], [particle=boolean],
    [particleShape=boolean], [plane=boolean], [polymesh=boolean], [polymeshEdge=boolean],
    [polymeshFace=boolean], [polymeshFreeEdge=boolean], [polymeshUV=boolean],
    [polymeshVertex=boolean], [polymeshVtxFace=boolean], [rigidBody=boolean],
    [rigidConstraint=boolean], [rotatePivot=boolean], [scalePivot=boolean],
    [sculpt=boolean], [selectHandle=boolean], [setAllowExcessCount=boolean],
    [setAutoComplete=boolean], [setAutoToggleSelection=boolean],
    [setDoneSelectionPrompt=string], [setNoSelectionHeadsUp=string],
    [setNoSelectionPrompt=string], [setSelectionCount=int], [setSelectionHeadsUp=string],
    [setSelectionPrompt=string], [showManipulators=boolean], [spring=boolean],
    [springComponent=boolean], [stroke=boolean], [subdiv=boolean],
    [subdivMeshEdge=boolean], [subdivMeshFace=boolean], [subdivMeshPoint=boolean],
    [subdivMeshUV=boolean], [surfaceEdge=boolean], [surfaceFace=boolean],
    [surfaceKnot=boolean], [surfaceParameterPoint=boolean], [surfaceRange=boolean],
    [surfaceUV=boolean], [texture=boolean], [title=string], [toolCursorType=string],
    [toolFinish=script], [toolStart=script], [totalSelectionSets=int], [vertex=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptCtx.html
    """
    return _wrapCommand(cmds.scriptCtx, args, kwargs)


def scriptEditorInfo(*args, **kwargs):  # noqa
    """Use this command to directly manipulate and query the contents of the Command Window
    window.

    scriptEditorInfo([clearHistory=boolean], [clearHistoryFile=boolean],
    [historyFilename=string], [input=string], [suppressErrors=boolean],
    [suppressInfo=boolean], [suppressResults=boolean], [suppressStackWindow=boolean],
    [suppressWarnings=boolean], [writeHistory=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptEditorInfo.html
    """
    return _wrapCommand(cmds.scriptEditorInfo, args, kwargs)


def scriptedPanel(*args, **kwargs):  # noqa
    """This command will create an instance of the specified scriptedPanelType.

    scriptedPanel( [panelName] , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [tearOff=boolean],
    [tearOffCopy=string], [tearOffRestore=boolean], [type=string], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptedPanel.html
    """
    return _wrapCommand(cmds.scriptedPanel, args, kwargs)


def scriptedPanelType(*args, **kwargs):  # noqa
    """This command defines the callbacks for a type of scripted panel.

    scriptedPanelType( [string] , [addCallback=string], [copyStateCallback=string],
    [createCallback=string], [customView=boolean], [defineTemplate=string],
    [deleteCallback=string], [exists=boolean], [hotkeyCtxClient=string],
    [initCallback=string], [label=string], [obsolete=boolean], [removeCallback=string],
    [retainOnFileOpen=boolean], [saveStateCallback=string], [unique=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptedPanelType.html
    """
    return _wrapCommand(cmds.scriptedPanelType, args, kwargs)


def scriptJob(*args, **kwargs):  # noqa
    """This command creates a "script job", which is a MEL command or script.

    scriptJob([allChildren=boolean], [attributeAdded=[string, script]],
    [attributeChange=[string, script]], [attributeDeleted=[string, script]],
    [compressUndo=boolean], [conditionChange=[string, script]], [conditionFalse=[string,
    script]], [conditionTrue=[string, script]], [connectionChange=[string, script]],
    [disregardIndex=boolean], [event=[string, script]], [exists=int], [force=boolean],
    [idleEvent=script], [kill=int], [killAll=boolean], [killWithScene=boolean],
    [listConditions=boolean], [listEvents=boolean], [listJobs=boolean],
    [nodeDeleted=[string, script]], [nodeNameChanged=[string, script]],
    [optionVarChanged=[string, script]], [parent=string], [permanent=boolean],
    [protected=boolean], [replacePrevious=boolean], [runOnce=boolean],
    [timeChange=script], [uiDeleted=[string, script]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptJob.html
    """
    return _wrapCommand(cmds.scriptJob, args, kwargs)


def scriptNode(*args, **kwargs):  # noqa
    """scriptNodes contain scripts that are executed when a file is loaded or when the script
    node is deleted.

    scriptNode( [attributeList] , [afterScript=string], [beforeScript=string],
    [executeAfter=boolean], [executeBefore=boolean], [ignoreReferenceEdits=boolean],
    [name=string], [scriptType=int], [sourceType=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptNode.html
    """
    return _wrapCommand(cmds.scriptNode, args, kwargs)


def scriptTable(*args, **kwargs):  # noqa
    """This command creates/edits/queries the script table control.

    scriptTable( [name] , [afterCellChangedCmd=script], [annotation=string],
    [backgroundColor=[float, float, float]], [cellBackgroundColorCommand=script],
    [cellChangedCmd=script], [cellForegroundColorCommand=script], [cellIndex=[int, int]],
    [cellValue=string], [clearRow=int], [clearTable=boolean], [columnFilter=[int,
    string]], [columnWidth=[int, int]], [columns=int], [defineTemplate=string],
    [deleteRow=int], [docTag=string], [dragCallback=script], [dropCallback=script],
    [editable=boolean], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [excludingHeaders=boolean], [exists=boolean],
    [fullPathName=boolean], [getCellCmd=script], [height=int], [highlightColor=[float,
    float, float]], [insertRow=int], [isObscured=boolean], [label=[int, string]],
    [manage=boolean], [multiEditEnabled=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowHeight=int], [rows=int], [rowsRemovedCmd=script],
    [rowsToBeRemovedCmd=script], [selectedCells=int[]], [selectedColumns=int[]],
    [selectedRow=boolean], [selectedRows=int[]], [selectionBehavior=int],
    [selectionChangedCmd=script], [selectionMode=int], [sortEnabled=boolean],
    [statusBarMessage=string], [underPointerColumn=boolean], [underPointerRow=boolean],
    [useDoubleClickEdit=boolean], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scriptTable.html
    """
    return _wrapCommand(cmds.scriptTable, args, kwargs)


def scrollField(*args, **kwargs):  # noqa
    """This command creates a scrolling field that handles multiple lines of text.

    scrollField( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [clear=boolean], [command=string], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [enterCommand=script], [exists=boolean], [font=string], [fontPointSize=int],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [insertText=string], [insertionPosition=int], [isObscured=boolean],
    [keyPressCommand=script], [manage=boolean], [noBackground=boolean],
    [numberOfLines=int], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [selection=boolean],
    [statusBarMessage=string], [text=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int], [wordWrap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scrollField.html
    """
    return _wrapCommand(cmds.scrollField, args, kwargs)


def scrollLayout(*args, **kwargs):  # noqa
    """This command creates a scroll layout.

    scrollLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [borderVisible=boolean], [childArray=boolean], [childResizable=boolean],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [horizontalScrollBarThickness=int],
    [isObscured=boolean], [manage=boolean], [minChildWidth=int], [noBackground=boolean],
    [numberOfChildren=boolean], [numberOfPopupMenus=boolean], [panEnabled=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [resizeCommand=script], [scrollAreaHeight=boolean], [scrollAreaValue=boolean],
    [scrollAreaWidth=boolean], [scrollByPixel=[string, int]], [scrollPage=string],
    [statusBarMessage=string], [useTemplate=string],
    [verticalScrollBarAlwaysVisible=boolean], [verticalScrollBarThickness=int],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/scrollLayout.html
    """
    return _wrapCommand(cmds.scrollLayout, args, kwargs)


def sculpt(*args, **kwargs):  # noqa
    """This command creates/edits/queries a sculpt object deformer.

    sculpt( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [deformerTools=boolean], [dropoffDistance=linear],
    [dropoffType=string], [exclusive=string], [frontOfChain=boolean], [geometry=string],
    [geometryIndices=boolean], [groupWithLocator=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [insideMode=string], [maxDisplacement=linear],
    [mode=string], [name=string], [objectCentered=boolean], [parallel=boolean],
    [prune=boolean], [remove=boolean], [sculptTool=string], [selectedComponents=boolean],
    [split=boolean], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sculpt.html
    """
    return _wrapCommand(cmds.sculpt, args, kwargs)


def sculptMeshCacheChangeCloneSource(*args, **kwargs):  # noqa
    """This command changes the source blend shape and target for the clone target tool.

    sculptMeshCacheChangeCloneSource([blendShape=string], [target=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheChangeCloneSource.html
    """
    return _wrapCommand(cmds.sculptMeshCacheChangeCloneSource, args, kwargs)


def sculptMeshCacheCtx(*args, **kwargs):  # noqa
    """This is a tool context command for mesh cache sculpting tool.

    sculptMeshCacheCtx([adjustSize=boolean], [adjustStrength=boolean],
    [affectAllLayers=boolean], [brushDirection=int], [brushSize=float],
    [brushStrength=float], [buildUpRate=float], [cloneHideSource=boolean],
    [cloneMethod=int], [cloneShapeSource=string], [cloneTargetSource=string],
    [constrainToSurface=boolean], [direction=int], [displayFrozen=boolean],
    [displayMask=boolean], [displayWireframe=boolean], [falloffType=int], [flood=float],
    [floodFreeze=float], [frame=boolean], [freezeSelection=boolean],
    [grabFollowPath=boolean], [grabSilhouette=boolean], [grabTwist=boolean],
    [inverted=boolean], [lastMode=string], [lockShellBorder=boolean], [makeStroke=[uint,
    uint, uint, float, float]], [minSize=float], [minStrength=float], [mirror=int],
    [mode=string], [orientToSurface=boolean], [recordStroke=boolean],
    [sculptFalloffCurve=string], [size=float], [stampDistance=float], [stampFile=string],
    [stampFlipX=boolean], [stampFlipY=boolean], [stampOrientToStroke=boolean],
    [stampPlacement=int], [stampRandomization=boolean], [stampRandomizationSeed=int],
    [stampRandomizeFlipX=boolean], [stampRandomizeFlipY=boolean],
    [stampRandomizePosX=float], [stampRandomizePosY=float],
    [stampRandomizeRotation=float], [stampRandomizeScale=float],
    [stampRandomizeStrength=float], [stampRotation=float], [steadyStrokeDistance=float],
    [strength=float], [updatePlane=boolean], [useGlobalSize=boolean],
    [useScreenSpace=boolean], [useStampDistance=boolean], [useStampImage=boolean],
    [useSteadyStroke=boolean], [wholeStroke=boolean], [wireframeAlpha=float],
    [wireframeColor=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sculptMeshCacheCtx.html
    """
    return _wrapCommand(cmds.sculptMeshCacheCtx, args, kwargs)


def sculptTarget(*args, **kwargs):  # noqa
    """This command is used to specify the blend shape target to be modified by the sculpting
    tools and transform manipulators.

    sculptTarget( int , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [deformerTools=boolean], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [inbetweenWeight=float], [includeHiddenSelections=boolean],
    [name=string], [parallel=boolean], [prune=boolean], [regenerate=boolean],
    [remove=boolean], [selectedComponents=boolean], [snapshot=int], [split=boolean],
    [target=int], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sculptTarget.html
    """
    return _wrapCommand(cmds.sculptTarget, args, kwargs)


def select(*args, **kwargs):  # noqa
    """This command is used to put objects onto or off of the active list.

    select( [objects...] , [add=boolean], [addFirst=boolean], [all=boolean],
    [allDagObjects=boolean], [allDependencyNodes=boolean], [clear=boolean],
    [containerCentric=boolean], [deselect=boolean], [hierarchy=boolean],
    [noExpand=boolean], [replace=boolean], [symmetry=boolean], [symmetrySide=int],
    [toggle=boolean], [visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/select.html
    """
    return _wrapCommand(cmds.select, args, kwargs)


def selectContext(*args, **kwargs):  # noqa
    """Creates a context to perform selection.

    selectContext( string , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectContext.html
    """
    return _wrapCommand(cmds.selectContext, args, kwargs)


def selectionConnection(*args, **kwargs):  # noqa
    """This command creates a named selectionConnection object.

    selectionConnection( string , [activeCacheList=boolean], [activeCharacterList=boolean],
    [activeList=boolean], [addScript=script], [addTo=string], [characterList=boolean],
    [clear=boolean], [connectionList=boolean], [defineTemplate=string], [deselect=name],
    [editor=string], [exists=boolean], [filter=string], [findObject=name], [g=boolean],
    [highlightList=boolean], [identify=boolean], [keyframeList=boolean], [lock=boolean],
    [modelList=boolean], [object=name], [parent=string], [remove=string],
    [removeScript=script], [select=name], [setList=boolean], [switch=boolean],
    [useTemplate=string], [worldList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectionConnection.html
    """
    return _wrapCommand(cmds.selectionConnection, args, kwargs)


def selectKey(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    selectKey( [targetList] , [addTo=boolean], [animation=string], [attribute=string],
    [clear=boolean], [controlPoints=boolean], [float=floatrange], [hierarchy=string],
    [inTangent=boolean], [includeUpperBound=boolean], [index=uint], [keyframe=boolean],
    [outTangent=boolean], [remove=boolean], [replace=boolean], [shape=boolean],
    [time=timerange], [toggle=boolean], [unsnappedKeys=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectKey.html
    """
    return _wrapCommand(cmds.selectKey, args, kwargs)


def selectKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to select keyframes within the graph
    editor.

    selectKeyCtx( contextName , [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectKeyCtx.html
    """
    return _wrapCommand(cmds.selectKeyCtx, args, kwargs)


def selectKeyframeRegionCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to select keyframes within the keyframe
    region of the dope sheet editor.

    selectKeyframeRegionCtx( contextName , [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectKeyframeRegionCtx.html
    """
    return _wrapCommand(cmds.selectKeyframeRegionCtx, args, kwargs)


def selectMode(*args, **kwargs):  # noqa
    """The `selectMode` command is used to change the selection mode.

    selectMode([component=boolean], [hierarchical=boolean], [leaf=boolean], [object=boolean],
    [preset=boolean], [root=boolean], [template=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectMode.html
    """
    return _wrapCommand(cmds.selectMode, args, kwargs)


def selectPref(*args, **kwargs):  # noqa
    """This command controls state variables used to selection UI behavior.

    selectPref([affectsActive=boolean], [allowHiliteSelection=boolean],
    [autoSelectContainer=boolean], [autoSelectOutlinerSetMembers=boolean],
    [autoUseDepth=boolean], [clickBoxSize=uint], [clickDrag=boolean],
    [containerCentricSelection=boolean], [disableComponentPopups=boolean],
    [expandPopupList=boolean], [ignoreSelectionPriority=boolean],
    [manipClickBoxSize=uint], [paintSelect=boolean], [paintSelectWithDepth=boolean],
    [popupMenuSelection=boolean], [preSelectBackfacing=boolean],
    [preSelectClosest=boolean], [preSelectDeadSpace=uint], [preSelectHilite=boolean],
    [preSelectHiliteSize=float], [preSelectTweakDeadSpace=uint],
    [selectTypeChangeAffectsActive=boolean], [selectionChildHighlightMode=int],
    [singleBoxSelection=boolean], [straightLineDistance=boolean],
    [trackSelectionOrder=boolean], [useDepth=boolean], [xformNoSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectPref.html
    """
    return _wrapCommand(cmds.selectPref, args, kwargs)


def selectPriority(*args, **kwargs):  # noqa
    """The `selectPriority` command is used to change the selection priority of particular types
    of objects that can be selected when using the select tool.

    selectPriority([allComponents=uint], [allObjects=uint], [animBreakdown=uint],
    [animCurve=uint], [animInTangent=uint], [animKeyframe=uint], [animOutTangent=uint],
    [byName=[string, boolean]], [camera=uint], [cluster=uint], [collisionModel=uint],
    [controlVertex=uint], [curve=uint], [curveKnot=uint], [curveOnSurface=uint],
    [curveParameterPoint=uint], [dimension=uint], [dynamicConstraint=uint], [edge=uint],
    [editPoint=uint], [emitter=uint], [facet=uint], [field=uint], [fluid=uint],
    [follicle=uint], [hairSystem=uint], [handle=uint], [hull=uint], [ikEndEffector=uint],
    [ikHandle=uint], [imagePlane=uint], [implicitGeometry=uint], [isoparm=uint],
    [joint=uint], [jointPivot=uint], [lattice=uint], [latticePoint=uint], [light=uint],
    [localRotationAxis=uint], [locator=uint], [locatorUV=uint], [locatorXYZ=uint],
    [meshUVShell=uint], [motionTrailPoint=uint], [motionTrailTangent=uint], [nCloth=uint],
    [nParticle=uint], [nParticleShape=uint], [nRigid=uint], [nonlinear=uint],
    [nurbsCurve=uint], [nurbsSurface=uint], [orientationLocator=uint], [particle=uint],
    [particleShape=uint], [plane=uint], [polymesh=uint], [polymeshEdge=uint],
    [polymeshFace=uint], [polymeshFreeEdge=uint], [polymeshUV=uint],
    [polymeshVertex=uint], [polymeshVtxFace=uint], [queryByName=string], [rigidBody=uint],
    [rigidConstraint=uint], [rotatePivot=uint], [scalePivot=uint], [sculpt=uint],
    [selectHandle=uint], [spring=uint], [springComponent=uint], [stroke=uint],
    [subdiv=uint], [subdivMeshEdge=uint], [subdivMeshFace=uint], [subdivMeshPoint=uint],
    [subdivMeshUV=uint], [surfaceEdge=uint], [surfaceFace=uint], [surfaceKnot=uint],
    [surfaceParameterPoint=uint], [surfaceRange=uint], [texture=uint], [vertex=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectPriority.html
    """
    return _wrapCommand(cmds.selectPriority, args, kwargs)


def selectType(*args, **kwargs):  # noqa
    """The `selectType` command is used to change the set of allowable types of objects that can
    be selected when using the select tool.

    selectType([allComponents=boolean], [allObjects=boolean], [animBreakdown=boolean],
    [animCurve=boolean], [animInTangent=boolean], [animKeyframe=boolean],
    [animOutTangent=boolean], [byName=[string, boolean]], [camera=boolean],
    [cluster=boolean], [collisionModel=boolean], [controlVertex=boolean], [curve=boolean],
    [curveKnot=boolean], [curveOnSurface=boolean], [curveParameterPoint=boolean],
    [dimension=boolean], [dynamicConstraint=boolean], [edge=boolean], [editPoint=boolean],
    [emitter=boolean], [facet=boolean], [field=boolean], [fluid=boolean],
    [follicle=boolean], [hairSystem=boolean], [handle=boolean], [hull=boolean],
    [ikEndEffector=boolean], [ikHandle=boolean], [imagePlane=boolean],
    [implicitGeometry=boolean], [isoparm=boolean], [joint=boolean], [jointPivot=boolean],
    [lattice=boolean], [latticePoint=boolean], [light=boolean],
    [localRotationAxis=boolean], [locator=boolean], [locatorUV=boolean],
    [locatorXYZ=boolean], [meshUVShell=boolean], [motionTrailPoint=boolean],
    [motionTrailTangent=boolean], [nCloth=boolean], [nParticle=boolean],
    [nParticleShape=boolean], [nRigid=boolean], [nonlinear=boolean], [nurbsCurve=boolean],
    [nurbsSurface=boolean], [objectComponent=boolean], [orientationLocator=boolean],
    [particle=boolean], [particleShape=boolean], [plane=boolean], [polymesh=boolean],
    [polymeshEdge=boolean], [polymeshFace=boolean], [polymeshFreeEdge=boolean],
    [polymeshUV=boolean], [polymeshVertex=boolean], [polymeshVtxFace=boolean],
    [queryByName=string], [rigidBody=boolean], [rigidConstraint=boolean],
    [rotatePivot=boolean], [scalePivot=boolean], [sculpt=boolean], [selectHandle=boolean],
    [spring=boolean], [springComponent=boolean], [stroke=boolean], [subdiv=boolean],
    [subdivMeshEdge=boolean], [subdivMeshFace=boolean], [subdivMeshPoint=boolean],
    [subdivMeshUV=boolean], [surfaceEdge=boolean], [surfaceFace=boolean],
    [surfaceKnot=boolean], [surfaceParameterPoint=boolean], [surfaceRange=boolean],
    [surfaceUV=boolean], [texture=boolean], [vertex=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selectType.html
    """
    return _wrapCommand(cmds.selectType, args, kwargs)


def selLoadSettings(*args, **kwargs):  # noqa
    """This command is used to edit and query information about the implicit load settings.

    selLoadSettings([activeProxy=string], [deferReference=boolean], [fileName=string],
    [numSettings=uint], [proxyManager=string], [proxySetFiles=string],
    [proxySetTags=string], [proxyTag=string], [referenceNode=string], [shortName=boolean],
    [unresolvedName=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/selLoadSettings.html
    """
    return _wrapCommand(cmds.selLoadSettings, args, kwargs)


def separator(*args, **kwargs):  # noqa
    """This command creates a separator widget in a variety of drawing styles.

    separator( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [style=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/separator.html
    """
    return _wrapCommand(cmds.separator, args, kwargs)


def sequenceManager(*args, **kwargs):  # noqa
    """The sequenceManager command manages sequences, shots, and their related scenes.

    sequenceManager([addSequencerAudio=string], [attachSequencerAudio=string],
    [currentShot=string], [currentTime=time], [listSequencerAudio=string],
    [listShots=boolean], [modelPanel=string], [node=string], [writableSequencer=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sequenceManager.html
    """
    return _wrapCommand(cmds.sequenceManager, args, kwargs)


def setAttr(*args, **kwargs):  # noqa
    """Sets the value of a dependency node attribute.

    setAttr( attribute Any [Any...] , [alteredValue=boolean], [caching=boolean],
    [capacityHint=uint], [channelBox=boolean], [clamp=boolean], [keyable=boolean],
    [lock=boolean], [size=uint], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html
    """
    return _wrapCommand(cmds.setAttr, args, kwargs)


def setAttrMapping(*args, **kwargs):  # noqa
    """This command applies an offset and scale to a specified device attachment.

    setAttrMapping([absolute=boolean], [attribute=string], [axis=string], [clutch=string],
    [device=string], [offset=float], [relative=boolean], [scale=float],
    [selection=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setAttrMapping.html
    """
    return _wrapCommand(cmds.setAttrMapping, args, kwargs)


def setDefaultShadingGroup(*args, **kwargs):  # noqa
    """The setDefaultShadingGroup command is used to change which shading group is considered the
    current default shading group.

    setDefaultShadingGroup( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setDefaultShadingGroup.html
    """
    return _wrapCommand(cmds.setDefaultShadingGroup, args, kwargs)


def setDrivenKeyframe(*args, **kwargs):  # noqa
    """This command sets a driven keyframe.

    setDrivenKeyframe( [objects] , [attribute=string], [controlPoints=boolean],
    [count=boolean], [currentDriver=string], [driven=boolean], [driver=boolean],
    [driverValue=float], [hierarchy=string], [inTangentType=string], [insert=boolean],
    [insertBlend=boolean], [outTangentType=string], [shape=boolean], [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setDrivenKeyframe.html
    """
    return _wrapCommand(cmds.setDrivenKeyframe, args, kwargs)


def setDynamic(*args, **kwargs):  # noqa
    """setDynamic sets the isDynamic attribute of particle objects on or off.

    setDynamic( selectionList , [allOnWhenRun=boolean], [disableAllOnWhenRun=boolean],
    [setAll=boolean], [setOff=boolean], [setOn=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setDynamic.html
    """
    return _wrapCommand(cmds.setDynamic, args, kwargs)


def setEditCtx(*args, **kwargs):  # noqa
    """This command creates a tool that can be used to modify set membership.

    setEditCtx( name , [exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setEditCtx.html
    """
    return _wrapCommand(cmds.setEditCtx, args, kwargs)


def setFluidAttr(*args, **kwargs):  # noqa
    """Sets values of built-in fluid attributes such as density, velocity, etc.

    setFluidAttr([addValue=boolean], [attribute=string], [clear=boolean], [floatRandom=float],
    [floatValue=float], [lowerFace=boolean], [reset=boolean], [vectorRandom=[float, float,
    float]], [vectorValue=[float, float, float]], [xIndex=int], [xvalue=boolean],
    [yIndex=int], [yvalue=boolean], [zIndex=int], [zvalue=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setFluidAttr.html
    """
    return _wrapCommand(cmds.setFluidAttr, args, kwargs)


def setFocus(*args, **kwargs):  # noqa
    """Give keyboard focus to a specific control or panel, passed as an argument.

    setFocus( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setFocus.html
    """
    return _wrapCommand(cmds.setFocus, args, kwargs)


def setInfinity(*args, **kwargs):  # noqa
    """Set the infinity type before (after) a paramCurve's first (last) keyframe.

    setInfinity( objects , [attribute=string], [controlPoints=boolean], [hierarchy=string],
    [postInfinite=string], [preInfinite=string], [shape=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setInfinity.html
    """
    return _wrapCommand(cmds.setInfinity, args, kwargs)


def setInputDeviceMapping(*args, **kwargs):  # noqa
    """The command sets a scale and offset for all attachments made to a specified device axis.

    setInputDeviceMapping([absolute=boolean], [axis=string], [device=string], [offset=float],
    [relative=boolean], [scale=float], [view=boolean], [world=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setInputDeviceMapping.html
    """
    return _wrapCommand(cmds.setInputDeviceMapping, args, kwargs)


def setKeyCtx(*args, **kwargs):  # noqa
    """This command creates a context which may be used to set keys within the graph editor.

    setKeyCtx( contextName , [breakdown=boolean], [exists=boolean], [history=boolean],
    [image1=string], [image2=string], [image3=string], [name=string],
    [preserveTangent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setKeyCtx.html
    """
    return _wrapCommand(cmds.setKeyCtx, args, kwargs)


def setKeyframe(*args, **kwargs):  # noqa
    """This command creates keyframes for the specified objects, or the active objects if none
    are specified on the command line.

    setKeyframe( [objects] , [adjustTangent=boolean], [animLayer=string], [animated=boolean],
    [attribute=string], [breakdown=boolean], [clip=string], [controlPoints=boolean],
    [dirtyDG=boolean], [float=float], [hierarchy=string], [identity=boolean],
    [inTangentType=string], [insert=boolean], [insertBlend=boolean],
    [minimizeRotation=boolean], [noResolve=boolean], [outTangentType=string],
    [preserveCurveShape=boolean], [respectKeyable=boolean], [shape=boolean], [time=time],
    [useCurrentLockedWeights=boolean], [value=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setKeyframe.html
    """
    return _wrapCommand(cmds.setKeyframe, args, kwargs)


def setKeyframeBlendshapeTargetWts(*args, **kwargs):  # noqa
    """This command can be used to keyframe per-point blendshape target weights.

    setKeyframeBlendshapeTargetWts()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setKeyframeBlendshapeTargetWts.html
    """
    return _wrapCommand(cmds.setKeyframeBlendshapeTargetWts, args, kwargs)


def setKeyPath(*args, **kwargs):  # noqa
    """The setKeyPath command either creates or edits the path (a nurbs curve) based on the
    current position of the selected object at the current time.

    setKeyPath( [object] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setKeyPath.html
    """
    return _wrapCommand(cmds.setKeyPath, args, kwargs)


def setMenuMode(*args, **kwargs):  # noqa
    """Optionally sets a new Menu Mode for the menu bar in the main Maya window.

    setMenuMode([string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setMenuMode.html
    """
    return _wrapCommand(cmds.setMenuMode, args, kwargs)


def setNodeTypeFlag(*args, **kwargs):  # noqa
    """This command sets static data on the specified node type.

    setNodeTypeFlag( [string] , [display=boolean], [threadSafe=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setNodeTypeFlag.html
    """
    return _wrapCommand(cmds.setNodeTypeFlag, args, kwargs)


def setParent(*args, **kwargs):  # noqa
    """This command changes the default parent to be the specified parent.

    setParent( [string] , [defineTemplate=string], [menu=boolean], [topLevel=boolean],
    [upLevel=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setParent.html
    """
    return _wrapCommand(cmds.setParent, args, kwargs)


def setParticleAttr(*args, **kwargs):  # noqa
    """This action will set the value of the chosen attribute for every particle or selected
    component in the selected or passed particle object.

    setParticleAttr( selectionList , [attribute=string], [floatValue=float], [object=string],
    [randomFloat=float], [randomVector=[float, float, float]], [relative=boolean],
    [vectorValue=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setParticleAttr.html
    """
    return _wrapCommand(cmds.setParticleAttr, args, kwargs)


def setRenderPassType(*args, **kwargs):  # noqa
    """This command will set the passID of a renderPass node and create the custom attributes
    specified by the corresponding render pass definition.

    setRenderPassType([defaultDataType=boolean], [numChannels=int], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setRenderPassType.html
    """
    return _wrapCommand(cmds.setRenderPassType, args, kwargs)


def sets(*args, **kwargs):  # noqa
    """This command is used to create a set, query some state of a set, or perform operations to
    update the membership of a set.

    sets( selectionList , [addElement=name], [afterFilters=boolean], [anyMember=name],
    [clear=name], [color=int], [copy=name], [edges=boolean], [editPoints=boolean],
    [empty=boolean], [facets=boolean], [flatten=name], [forceElement=name],
    [include=name], [intersection=name], [isIntersecting=name], [isMember=name],
    [layer=boolean], [name=string], [noIntermediate=boolean], [noSurfaceShader=boolean],
    [noWarnings=boolean], [nodesOnly=boolean], [remove=name], [renderable=boolean],
    [size=boolean], [split=name], [subtract=name], [text=string], [union=name],
    [vertices=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sets.html
    """
    return _wrapCommand(cmds.sets, args, kwargs)


def setStartupMessage(*args, **kwargs):  # noqa
    """Update the startup window message.

    setStartupMessage( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setStartupMessage.html
    """
    return _wrapCommand(cmds.setStartupMessage, args, kwargs)


def setToolTo(*args, **kwargs):  # noqa
    """This command switches control to the named context.

    setToolTo( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setToolTo.html
    """
    return _wrapCommand(cmds.setToolTo, args, kwargs)


def setUITemplate(*args, **kwargs):  # noqa
    """This command sets the current(default) command template for the ELF commands.

    setUITemplate( [string] , [popTemplate=boolean], [pushTemplate=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setUITemplate.html
    """
    return _wrapCommand(cmds.setUITemplate, args, kwargs)


def setXformManip(*args, **kwargs):  # noqa
    """This command changes some of the settings of the xform manip, to control its appearance.

    setXformManip([showUnits=boolean], [suppress=boolean], [useRotatePivot=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/setXformManip.html
    """
    return _wrapCommand(cmds.setXformManip, args, kwargs)


def shadingConnection(*args, **kwargs):  # noqa
    """Sets the connection state of a connection between nodes that are used in shading.

    shadingConnection( attribute , [connectionState=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shadingConnection.html
    """
    return _wrapCommand(cmds.shadingConnection, args, kwargs)


def shadingGeometryRelCtx(*args, **kwargs):  # noqa
    """This command creates a context that can be used for associating geometry to shading
    groups.

    shadingGeometryRelCtx([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [offCommand=string],
    [onCommand=string], [shadingCentric=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shadingGeometryRelCtx.html
    """
    return _wrapCommand(cmds.shadingGeometryRelCtx, args, kwargs)


def shadingLightRelCtx(*args, **kwargs):  # noqa
    """This command creates a context that can be used for associating lights to shading groups.

    shadingLightRelCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string], [offCommand=string], [onCommand=string],
    [shadingCentric=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shadingLightRelCtx.html
    """
    return _wrapCommand(cmds.shadingLightRelCtx, args, kwargs)


def shadingNetworkCompare(*args, **kwargs):  # noqa
    """This command allows you to compare two shading networks.

    shadingNetworkCompare([byName=boolean], [byValue=boolean], [delete=boolean],
    [equivalent=boolean], [network1=boolean], [network2=boolean], [upstreamOnly=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shadingNetworkCompare.html
    """
    return _wrapCommand(cmds.shadingNetworkCompare, args, kwargs)


def shadingNode(*args, **kwargs):  # noqa
    """This command creates a new node in the dependency graph of the specified type.

    shadingNode( node string , [asLight=boolean], [asPostProcess=boolean],
    [asRendering=boolean], [asShader=boolean], [asTexture=boolean], [asUtility=boolean],
    [isColorManaged=boolean], [name=string], [parent=string], [shared=boolean],
    [skipSelect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shadingNode.html
    """
    return _wrapCommand(cmds.shadingNode, args, kwargs)


def shapeCompare(*args, **kwargs):  # noqa
    """Compares two shapes.

    shapeCompare( [object object] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shapeCompare.html
    """
    return _wrapCommand(cmds.shapeCompare, args, kwargs)


def shapeEditor(*args, **kwargs):  # noqa
    """This command creates an editor that derives from the base editor class that has controls
    for deformer, control nodes.

    shapeEditor( string , [clearSelection=boolean], [control=boolean],
    [defineTemplate=string], [docTag=string], [exists=boolean], [filter=string],
    [forceMainConnection=string], [highlightConnection=string],
    [lockMainConnection=boolean], [lowestSelection=boolean], [mainListConnection=string],
    [panel=string], [parent=string], [selectionConnection=string], [stateString=boolean],
    [targetControlList=boolean], [targetList=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string],
    [verticalSliders=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shapeEditor.html
    """
    return _wrapCommand(cmds.shapeEditor, args, kwargs)


def shapePanel(*args, **kwargs):  # noqa
    """This command creates a panel that derives from the base panel class that houses a
    shapeEditor.

    shapePanel( string , [control=boolean], [copy=string], [createString=boolean],
    [defineTemplate=string], [docTag=string], [editString=boolean], [exists=boolean],
    [init=boolean], [isUnique=boolean], [label=string], [menuBarRepeatLast=boolean],
    [menuBarVisible=boolean], [needsInit=boolean], [parent=string],
    [popupMenuProcedure=script], [replacePanel=string], [shapeEditor=boolean],
    [tearOff=boolean], [tearOffCopy=string], [tearOffRestore=boolean], [unParent=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shapePanel.html
    """
    return _wrapCommand(cmds.shapePanel, args, kwargs)


def shelfButton(*args, **kwargs):  # noqa
    """This control supports up to 3 icon images and 4 different display styles.

    shelfButton( [string] , [align=string], [annotation=string], [backgroundColor=[float,
    float, float]], [command=script], [commandRepeatable=boolean],
    [defineTemplate=string], [disabledImage=string], [docTag=string],
    [doubleClickCommand=script], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableCommandRepeat=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [flat=boolean],
    [flexibleWidthType=int], [flexibleWidthValue=int], [flipX=boolean], [flipY=boolean],
    [font=string], [fullPathName=boolean], [handleNodeDropCallback=script], [height=int],
    [highlightColor=[float, float, float]], [highlightImage=string], [image=string],
    [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string],
    [isObscured=boolean], [label=string], [labelEditingCallback=script],
    [labelOffset=int], [manage=boolean], [marginHeight=uint], [marginWidth=uint],
    [menuItem=[string, string]], [menuItemPython=int], [menuItemWithOptionBox=[string,
    string, string]], [noBackground=boolean], [noDefaultPopup=boolean],
    [numberOfPopupMenus=boolean], [overlayLabelBackColor=[float, float, float, float]],
    [overlayLabelColor=[float, float, float]], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rotation=float], [scaleIcon=boolean],
    [selectionImage=string], [sourceType=string], [statusBarMessage=string],
    [style=string], [useAlpha=boolean], [useTemplate=string], [version=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shelfButton.html
    """
    return _wrapCommand(cmds.shelfButton, args, kwargs)


def shelfLayout(*args, **kwargs):  # noqa
    """This command creates a new empty shelf layout.

    shelfLayout( [string] , [alignment=string], [annotation=string], [backgroundColor=[float,
    float, float]], [cellHeight=int], [cellWidth=int], [cellWidthHeight=[int, int]],
    [childArray=boolean], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [horizontal=boolean], [isObscured=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfChildren=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [position=[string, int]], [preventOverride=boolean], [spacing=int],
    [statusBarMessage=string], [style=string], [useTemplate=string], [version=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shelfLayout.html
    """
    return _wrapCommand(cmds.shelfLayout, args, kwargs)


def shelfTabLayout(*args, **kwargs):  # noqa
    """This command creates/edits/queries a shelf tab group which is essentially a normal
    tabLayout with some drop behaviour in the tab bar.

    shelfTabLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [borderStyle=string], [changeCommand=script], [childArray=boolean],
    [childResizable=boolean], [closeTab=int], [closeTabCommand=script],
    [defineTemplate=string], [docTag=string], [doubleClickCommand=script],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontalScrollBarThickness=int], [image=string], [imageVisible=boolean],
    [innerMarginHeight=int], [innerMarginWidth=int], [isObscured=boolean],
    [manage=boolean], [minChildWidth=int], [moveTab=[int, int]], [newTabCommand=script],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [postMenuCommand=script],
    [preSelectCommand=script], [preventOverride=boolean], [scrollable=boolean],
    [scrollableTabs=boolean], [selectCommand=script], [selectTab=string],
    [selectTabIndex=int], [showNewTab=boolean], [statusBarMessage=string],
    [tabIcon=[string, string]], [tabIconIndex=[int, string]], [tabLabel=[string, string]],
    [tabLabelIndex=[int, string]], [tabPosition=string], [tabTooltip=[string, string]],
    [tabTooltipIndex=[int, string]], [tabsClosable=boolean], [tabsVisible=boolean],
    [useTemplate=string], [verticalScrollBarThickness=int], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shelfTabLayout.html
    """
    return _wrapCommand(cmds.shelfTabLayout, args, kwargs)


def shot(*args, **kwargs):  # noqa
    """Use this command to create a shot node or manipulate that node.

    shot([audio=string], [clip=string], [clipDuration=time], [clipOpacity=float],
    [clipSyncState=boolean], [clipZeroOffset=time], [copy=boolean],
    [createCustomAnim=boolean], [currentCamera=string], [customAnim=boolean],
    [deleteCustomAnim=boolean], [determineTrack=boolean], [endTime=time],
    [favorite=boolean], [flag1=boolean], [flag10=boolean], [flag11=boolean],
    [flag12=boolean], [flag2=boolean], [flag3=boolean], [flag4=boolean], [flag5=boolean],
    [flag6=boolean], [flag7=boolean], [flag8=boolean], [flag9=boolean],
    [hasCameraSet=boolean], [hasStereoCamera=boolean], [imagePlaneVisibility=boolean],
    [linkAudio=string], [lock=boolean], [mute=boolean], [paste=boolean],
    [pasteInstance=boolean], [postHoldTime=time], [preHoldTime=time], [scale=float],
    [selfmute=boolean], [sequenceDuration=time], [sequenceEndTime=time],
    [sequenceStartTime=time], [shotName=string], [sourceDuration=time], [startTime=time],
    [track=int], [transitionInLength=time], [transitionInType=int],
    [transitionOutLength=time], [transitionOutType=int], [unlinkAudio=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shot.html
    """
    return _wrapCommand(cmds.shot, args, kwargs)


def shotRipple(*args, **kwargs):  # noqa
    """When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated are
    moved in sequence time to either make way or close up gaps corresponding to that
    node's editing.

    shotRipple([deleted=boolean], [endDelta=time], [endTime=time], [startDelta=time],
    [startTime=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shotRipple.html
    """
    return _wrapCommand(cmds.shotRipple, args, kwargs)


def shotTrack(*args, **kwargs):  # noqa
    """This command is used for inserting and removing tracks related to the shots displayed in
    the Sequencer.

    shotTrack([insertTrack=uint], [lock=boolean], [mute=boolean], [numTracks=uint],
    [removeEmptyTracks=boolean], [removeTrack=uint], [selfmute=boolean], [solo=boolean],
    [swapTracks=[uint, uint]], [title=string], [track=uint], [unsolo=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/shotTrack.html
    """
    return _wrapCommand(cmds.shotTrack, args, kwargs)


def showHelp(*args, **kwargs):  # noqa
    """Invokes a web browser to open the on-line documentation and help files.

    showHelp([string], [absolute=boolean], [docs=boolean], [helpTable=boolean],
    [version=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showHelp.html
    """
    return _wrapCommand(cmds.showHelp, args, kwargs)


def showHidden(*args, **kwargs):  # noqa
    """The `showHidden` command is used to make invisible objects visible.

    showHidden( [objects...] , [above=boolean], [allObjects=boolean], [below=boolean],
    [lastHidden=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showHidden.html
    """
    return _wrapCommand(cmds.showHidden, args, kwargs)


def showManipCtx(*args, **kwargs):  # noqa
    """This command can be used to create a show manip context.

    showManipCtx( string , [addAttr=string], [currentNodeName=boolean], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [incSnap=[uint,
    boolean]], [incSnapRelative=[uint, boolean]], [incSnapUI=boolean],
    [incSnapValue=[uint, float]], [iveVisible=boolean], [lockSelection=boolean],
    [moveActiveAttrDown=boolean], [moveActiveAttrToTop=boolean],
    [moveActiveAttrUp=boolean], [name=string], [removeAttr=string],
    [resetActiveAttr=boolean], [selectedAttributes=boolean], [setAttrActive=string],
    [setNextAttrActive=boolean], [setPreviousAttrActive=boolean], [toggleIncSnap=boolean],
    [toolFinish=script], [toolStart=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showManipCtx.html
    """
    return _wrapCommand(cmds.showManipCtx, args, kwargs)


def showMetadata(*args, **kwargs):  # noqa
    """This command is used to show metadata values which is in the specified channels "vertex",
    "edge", "face", and "vertexFace" in the viewport.

    showMetadata([auto=boolean], [dataType=string], [interpolation=boolean],
    [isActivated=boolean], [listAllStreams=boolean], [listMembers=boolean],
    [listValidMethods=boolean], [listVisibleStreams=boolean], [member=string],
    [method=string], [off=boolean], [range=[float, float]], [rayScale=float],
    [stream=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showMetadata.html
    """
    return _wrapCommand(cmds.showMetadata, args, kwargs)


def showSelectionInTitle(*args, **kwargs):  # noqa
    """This command causes the title of the window specified as an argument to be linked to the
    current file and selection.

    showSelectionInTitle( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showSelectionInTitle.html
    """
    return _wrapCommand(cmds.showSelectionInTitle, args, kwargs)


def showShadingGroupAttrEditor(*args, **kwargs):  # noqa
    """The showShadingGroupAttrEditor command opens up the attribute editor for the current
    object's shading-group information.

    showShadingGroupAttrEditor()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showShadingGroupAttrEditor.html
    """
    return _wrapCommand(cmds.showShadingGroupAttrEditor, args, kwargs)


def showWindow(*args, **kwargs):  # noqa
    """Make a window visible.

    showWindow( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/showWindow.html
    """
    return _wrapCommand(cmds.showWindow, args, kwargs)


def simplify(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    simplify( animatedObject , [animation=string], [attribute=string],
    [controlPoints=boolean], [float=floatrange], [floatTolerance=float],
    [hierarchy=string], [includeUpperBound=boolean], [index=uint], [shape=boolean],
    [time=timerange], [timeTolerance=time], [valueTolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/simplify.html
    """
    return _wrapCommand(cmds.simplify, args, kwargs)


def singleProfileBirailSurface(*args, **kwargs):  # noqa
    """This cmd creates a railed surface by sweeping the profile curve along the two rail curves.

    singleProfileBirailSurface( curve curve curve , [caching=boolean],
    [constructionHistory=boolean], [name=string], [nodeState=int], [object=boolean],
    [polygon=int], [tangentContinuityProfile1=boolean], [transformMode=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/singleProfileBirailSurface.html
    """
    return _wrapCommand(cmds.singleProfileBirailSurface, args, kwargs)


def skeletonEmbed(*args, **kwargs):  # noqa
    """This command is used to embed a skeleton inside meshes.

    skeletonEmbed([mergedMesh=boolean], [segmentationMethod=uint],
    [segmentationResolution=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/skeletonEmbed.html
    """
    return _wrapCommand(cmds.skeletonEmbed, args, kwargs)


def skinBindCtx(*args, **kwargs):  # noqa
    """This command creates a tool that can be used to edit volumes from an interactive bind.

    skinBindCtx( string , [about=string], [axis=string], [colorRamp=string],
    [currentInfluence=string], [displayInactiveMode=int], [displayNormalized=boolean],
    [exists=boolean], [falloffCurve=string], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [symmetry=boolean],
    [tolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/skinBindCtx.html
    """
    return _wrapCommand(cmds.skinBindCtx, args, kwargs)


def skinCluster(*args, **kwargs):  # noqa
    """The skinCluster command is used for smooth skinning in maya.

    skinCluster( objects , [addInfluence=string], [addToSelection=boolean], [after=boolean],
    [afterReference=boolean], [baseShape=string], [before=boolean], [bindMethod=int],
    [components=boolean], [deformerTools=boolean], [dropoffRate=float],
    [exclusive=string], [forceNormalizeWeights=boolean], [frontOfChain=boolean],
    [geometry=string], [geometryIndices=boolean], [heatmapFalloff=float],
    [ignoreBindPose=boolean], [ignoreHierarchy=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [influence=string], [lockWeights=boolean],
    [maximumInfluences=int], [moveJointsMode=boolean], [name=string],
    [normalizeWeights=int], [nurbsSamples=int], [obeyMaxInfluences=boolean],
    [parallel=boolean], [polySmoothness=float], [prune=boolean],
    [recacheBindMatrices=boolean], [remove=boolean], [removeFromSelection=boolean],
    [removeInfluence=string], [removeUnusedInfluence=boolean],
    [selectInfluenceVerts=string], [selectedComponents=boolean], [skinMethod=int],
    [smoothWeights=float], [smoothWeightsMaxIterations=int], [split=boolean],
    [toSelectedBones=boolean], [toSkeletonAndTransforms=boolean], [unbind=boolean],
    [unbindKeepHistory=boolean], [useComponentTags=boolean], [useGeometry=boolean],
    [volumeBind=float], [volumeType=int], [weight=float], [weightDistribution=int],
    [weightedInfluence=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/skinCluster.html
    """
    return _wrapCommand(cmds.skinCluster, args, kwargs)


def skinPercent(*args, **kwargs):  # noqa
    """This command edits and queries the weight values on members of a skinCluster node, given
    as the first argument.

    skinPercent( [object] [selectionList] , [ignoreBelow=float], [normalize=boolean],
    [pruneWeights=float], [relative=boolean], [resetToDefault=boolean],
    [transform=string], [transformMoveWeights=string], [transformValue=[string, float]],
    [value=boolean], [zeroRemainingInfluences=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/skinPercent.html
    """
    return _wrapCommand(cmds.skinPercent, args, kwargs)


def smoothCurve(*args, **kwargs):  # noqa
    """The smooth command smooths the curve at the given control points.

    smoothCurve( selectionList , [caching=boolean], [constructionHistory=boolean],
    [name=string], [nodeState=int], [object=boolean], [replaceOriginal=boolean],
    [smoothness=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/smoothCurve.html
    """
    return _wrapCommand(cmds.smoothCurve, args, kwargs)


def smoothTangentSurface(*args, **kwargs):  # noqa
    """The smoothTangentSurface command smooths the surface along an isoparm at each parameter
    value.

    smoothTangentSurface( surface , [caching=boolean], [constructionHistory=boolean],
    [direction=int], [name=string], [nodeState=int], [object=boolean], [parameter=float],
    [replaceOriginal=boolean], [smoothness=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/smoothTangentSurface.html
    """
    return _wrapCommand(cmds.smoothTangentSurface, args, kwargs)


def snapKey(*args, **kwargs):  # noqa
    """This command operates on a keyset.

    snapKey( animatedObject , [animation=string], [attribute=string], [controlPoints=boolean],
    [float=floatrange], [hierarchy=string], [includeUpperBound=boolean], [index=uint],
    [mergeDuplicate=boolean], [shape=boolean], [time=timerange], [timeMultiple=float],
    [valueMultiple=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapKey.html
    """
    return _wrapCommand(cmds.snapKey, args, kwargs)


def snapMode(*args, **kwargs):  # noqa
    """The snapMode command is used to control snapping.

    snapMode([curve=boolean], [distanceIncrement=linear], [edgeMagnet=uint],
    [edgeMagnetTolerance=float], [grid=boolean], [liveFaceCenter=boolean],
    [livePoint=boolean], [meshCenter=boolean], [pixelCenter=boolean], [pixelSnap=boolean],
    [point=boolean], [tolerance=uint], [useTolerance=boolean], [uvTolerance=uint],
    [viewPlane=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapMode.html
    """
    return _wrapCommand(cmds.snapMode, args, kwargs)


def snapshot(*args, **kwargs):  # noqa
    """This command can be used to create either a series of surfaces evaluated at the times
    specified by the command flags, or a motion trail displaying the trajectory of the
    object's pivot point at the times specified.

    snapshot( [objects] , [constructionHistory=boolean], [endTime=time], [increment=time],
    [motionTrail=boolean], [name=string], [startTime=time], [update=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapshot.html
    """
    return _wrapCommand(cmds.snapshot, args, kwargs)


def snapshotBeadCtx(*args, **kwargs):  # noqa
    """Creates a context for manipulating in and/or out tangent beads on the motion trail.

    snapshotBeadCtx([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [inTangent=boolean], [name=string], [outTangent=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapshotBeadCtx.html
    """
    return _wrapCommand(cmds.snapshotBeadCtx, args, kwargs)


def snapshotModifyKeyCtx(*args, **kwargs):  # noqa
    """Creates a context for inserting/delete keys on an editable motion trail.

    snapshotModifyKeyCtx([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapshotModifyKeyCtx.html
    """
    return _wrapCommand(cmds.snapshotModifyKeyCtx, args, kwargs)


def snapTogetherCtx(*args, **kwargs):  # noqa
    """The snapTogetherCtx command creates a tool for snapping surfaces together.

    snapTogetherCtx( [contextName] , [clearSelection=boolean], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string],
    [setOrientation=boolean], [snapPolygonFace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/snapTogetherCtx.html
    """
    return _wrapCommand(cmds.snapTogetherCtx, args, kwargs)


def soft(*args, **kwargs):  # noqa
    """Makes a soft body from the object(s) passed on the command line or in the selection list.

    soft( selectionList , [convert=boolean], [duplicate=boolean], [duplicateHistory=boolean],
    [goal=float], [hideOriginal=boolean], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/soft.html
    """
    return _wrapCommand(cmds.soft, args, kwargs)


def softMod(*args, **kwargs):  # noqa
    """The softMod command creates a softMod or edits the membership of an existing softMod.

    softMod( [objects] , [after=boolean], [afterReference=boolean], [before=boolean],
    [bindState=boolean], [components=boolean], [curveInterpolation=int],
    [curvePoint=float], [curveValue=float], [deformerTools=boolean], [envelope=float],
    [exclusive=string], [falloffAroundSelection=boolean], [falloffBasedOnX=boolean],
    [falloffBasedOnY=boolean], [falloffBasedOnZ=boolean], [falloffCenter=[float, float,
    float]], [falloffMasking=boolean], [falloffMode=int], [falloffRadius=float],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [name=string],
    [parallel=boolean], [prune=boolean], [relative=boolean], [remove=boolean],
    [resetGeometry=boolean], [selectedComponents=boolean], [split=boolean],
    [useComponentTags=boolean], [weightedNode=[string, string]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/softMod.html
    """
    return _wrapCommand(cmds.softMod, args, kwargs)


def softModCtx(*args, **kwargs):  # noqa
    """Controls the softMod context.

    softModCtx( string , [dragSlider=string], [exists=boolean], [falseColor=boolean],
    [image1=string], [image2=string], [image3=string], [reset=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/softModCtx.html
    """
    return _wrapCommand(cmds.softModCtx, args, kwargs)


def softSelect(*args, **kwargs):  # noqa
    """This command allows you to change the soft modelling options.

    softSelect([compressUndo=int], [enableFalseColor=int], [softSelectColorCurve=string],
    [softSelectCurve=string], [softSelectDistance=float], [softSelectEnabled=int],
    [softSelectFalloff=int], [softSelectReset=boolean], [softSelectUVDistance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/softSelect.html
    """
    return _wrapCommand(cmds.softSelect, args, kwargs)


def soloMaterial(*args, **kwargs):  # noqa
    """Shows a preview of a specified material node output attribute.

    soloMaterial([attr=string], [last=boolean], [node=string], [unsolo=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/soloMaterial.html
    """
    return _wrapCommand(cmds.soloMaterial, args, kwargs)


def sortCaseInsensitive(*args, **kwargs):  # noqa
    """This command sorts all the strings of an array in a case insensitive way.

    sortCaseInsensitive()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sortCaseInsensitive.html
    """
    return _wrapCommand(cmds.sortCaseInsensitive, args, kwargs)


def sound(*args, **kwargs):  # noqa
    """Creates an audio node which can be used with UI commands such as soundControl or
    timeControl which support sound scrubbing and sound during playback.

    sound( [objects] , [endTime=time], [file=string], [length=boolean], [mute=boolean],
    [name=string], [offset=time], [sourceEnd=time], [sourceStart=time])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sound.html
    """
    return _wrapCommand(cmds.sound, args, kwargs)


def soundControl(*args, **kwargs):  # noqa
    """This command creates a control used for changing current time and scratching/scrubbing
    through sound files.

    soundControl( string , [annotation=string], [backgroundColor=[float, float, float]],
    [beginScrub=boolean], [defineTemplate=string], [displaySound=boolean],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [endScrub=boolean],
    [exists=boolean], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [isObscured=boolean], [manage=boolean], [maxTime=time], [minTime=time],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [pressCommand=string], [preventOverride=boolean],
    [releaseCommand=string], [repeatChunkSize=float], [repeatOnHold=boolean],
    [resample=boolean], [sound=string], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [waveform=string], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/soundControl.html
    """
    return _wrapCommand(cmds.soundControl, args, kwargs)


def soundPopup(*args, **kwargs):  # noqa
    """Create a poup with sound slider control that accepts only float values and is bound by a
    minimum and maximum value.

    soundPopup( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/soundPopup.html
    """
    return _wrapCommand(cmds.soundPopup, args, kwargs)


def spaceLocator(*args, **kwargs):  # noqa
    """The command creates a locator at the specified position in space.

    spaceLocator([absolute=boolean], [name=string], [position=[linear, linear, linear]],
    [relative=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/spaceLocator.html
    """
    return _wrapCommand(cmds.spaceLocator, args, kwargs)


def sphere(*args, **kwargs):  # noqa
    """The sphere command creates a new sphere.

    sphere([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean],
    [degree=int], [endSweep=angle], [heightRatio=float], [name=string], [nodeState=int],
    [object=boolean], [pivot=[linear, linear, linear]], [polygon=int], [radius=linear],
    [sections=int], [spans=int], [startSweep=angle], [tolerance=linear],
    [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sphere.html
    """
    return _wrapCommand(cmds.sphere, args, kwargs)


def spotLight(*args, **kwargs):  # noqa
    """TlightCmd is the base class for other light commands.

    spotLight([barnDoors=boolean], [bottomBarnDoorAngle=angle], [coneAngle=angle],
    [decayRate=int], [discRadius=linear], [dropOff=float], [exclusive=boolean],
    [intensity=float], [leftBarnDoorAngle=angle], [name=string], [penumbra=angle],
    [position=[linear, linear, linear]], [rgb=[float, float, float]],
    [rightBarnDoorAngle=angle], [rotation=[angle, angle, angle]], [shadowColor=[float,
    float, float]], [shadowDither=float], [shadowSamples=int], [softShadow=boolean],
    [topBarnDoorAngle=angle], [useRayTraceShadows=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/spotLight.html
    """
    return _wrapCommand(cmds.spotLight, args, kwargs)


def spotLightPreviewPort(*args, **kwargs):  # noqa
    """This command creates a 3dPort that displays an image representing the illumination
    provided by the spotLight.

    spotLightPreviewPort( [string] , [annotation=string], [backgroundColor=[float, float,
    float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [spotLight=name],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int], [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/spotLightPreviewPort.html
    """
    return _wrapCommand(cmds.spotLightPreviewPort, args, kwargs)


def spreadSheetEditor(*args, **kwargs):  # noqa
    """This command creates a new spread sheet editor in the current layout.

    spreadSheetEditor( [name] , [allAttr=boolean], [attrRegExp=string], [control=boolean],
    [defineTemplate=string], [docTag=string], [execute=string], [exists=boolean],
    [filter=string], [fixedAttrList=string[]], [forceMainConnection=string],
    [highlightConnection=string], [keyableOnly=boolean], [lockMainConnection=boolean],
    [longNames=boolean], [mainListConnection=string], [niceNames=boolean], [panel=string],
    [parent=string], [precision=int], [selectedAttr=boolean],
    [selectionConnection=string], [showShapes=boolean], [stateString=boolean],
    [unParent=boolean], [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/spreadSheetEditor.html
    """
    return _wrapCommand(cmds.spreadSheetEditor, args, kwargs)


def spring(*args, **kwargs):  # noqa
    """The spring command can do any of the following:.

    spring( objects , [addSprings=boolean], [allPoints=boolean], [count=boolean],
    [damping=float], [dampingPS=float], [endForceWeight=float], [exclusive=boolean],
    [length=float], [maxDistance=float], [minDistance=float], [minMax=boolean],
    [name=string], [noDuplicate=boolean], [restLength=float], [restLengthPS=float],
    [startForceWeight=float], [stiffness=float], [stiffnessPS=float],
    [useDampingPS=boolean], [useRestLengthPS=boolean], [useStiffnessPS=boolean],
    [walkLength=uint], [wireframe=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/spring.html
    """
    return _wrapCommand(cmds.spring, args, kwargs)


def squareSurface(*args, **kwargs):  # noqa
    """This command produces a square surface given 3 or 4 curves.

    squareSurface( string string string [string] , [caching=boolean],
    [constructionHistory=boolean], [continuityType1=int], [continuityType2=int],
    [continuityType3=int], [continuityType4=int], [curveFitCheckpoints=int],
    [endPointTolerance=linear], [name=string], [nodeState=int], [object=boolean],
    [polygon=int], [rebuildCurve1=boolean], [rebuildCurve2=boolean],
    [rebuildCurve3=boolean], [rebuildCurve4=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/squareSurface.html
    """
    return _wrapCommand(cmds.squareSurface, args, kwargs)


def srtContext(*args, **kwargs):  # noqa
    """This command can be used to create a combined transform (translate/scale/rotate) context.

    srtContext([exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/srtContext.html
    """
    return _wrapCommand(cmds.srtContext, args, kwargs)


def stereoCameraView(*args, **kwargs):  # noqa
    """Create, edit or query a model editor.

    stereoCameraView( objects [editorName] , [activeComponentsXray=boolean],
    [activeCustomEnvironment=string], [activeCustomGeometry=string],
    [activeCustomLighSet=string], [activeCustomOverrideGeometry=string],
    [activeCustomRenderer=string], [activeOnly=boolean], [activeShadingGraph=string],
    [activeSupported=boolean], [activeView=boolean], [addObjects=string],
    [addSelected=boolean], [allObjects=boolean], [backfaceCulling=boolean],
    [bufferMode=string], [bumpResolution=[uint, uint]], [camera=string],
    [cameraName=string], [cameraSet=string], [cameraSetup=boolean], [cameras=boolean],
    [capture=string], [captureSequenceNumber=int], [centerCamera=string],
    [colorMap=boolean], [colorResolution=[uint, uint]], [control=boolean],
    [controlVertices=boolean], [cullingOverride=string], [default=boolean],
    [defineTemplate=string], [deformers=boolean], [dimensions=boolean],
    [displayAppearance=string], [displayLights=string], [displayMode=string],
    [displayTextures=boolean], [docTag=string], [dynamicConstraints=boolean],
    [dynamics=boolean], [editorChanged=script], [exists=boolean], [filter=string],
    [filteredObjectList=boolean], [fluids=boolean], [fogColor=[float, float, float,
    float]], [fogDensity=float], [fogEnd=float], [fogMode=string], [fogSource=string],
    [fogStart=float], [fogging=boolean], [follicles=boolean],
    [forceMainConnection=string], [grid=boolean], [hairSystems=boolean],
    [handles=boolean], [headsUpDisplay=boolean], [height=boolean],
    [highlightConnection=string], [hulls=boolean], [ignorePanZoom=boolean],
    [ikHandles=boolean], [imagePlane=boolean], [interactive=boolean],
    [interactiveBackFaceCull=boolean], [interactiveDisableShadows=boolean],
    [isFiltered=boolean], [jointXray=boolean], [joints=boolean], [leftCamera=string],
    [lights=boolean], [lineWidth=float], [locators=boolean], [lockMainConnection=boolean],
    [lowQualityLighting=boolean], [mainListConnection=string], [manipulators=boolean],
    [maxConstantTransparency=float], [maximumNumHardwareLights=boolean],
    [modelPanel=string], [motionTrails=boolean], [nCloths=boolean], [nParticles=boolean],
    [nRigids=boolean], [noUndo=boolean], [nurbsCurves=boolean], [nurbsSurfaces=boolean],
    [objectFilter=script], [objectFilterList=script], [objectFilterListUI=script],
    [objectFilterShowInHUD=boolean], [objectFilterUI=script], [occlusionCulling=boolean],
    [panel=string], [parent=string], [pivots=boolean], [planes=boolean],
    [pluginObjects=[string, boolean]], [pluginShapes=boolean], [polymeshes=boolean],
    [queryPluginObjects=string], [removeSelected=boolean], [rendererDeviceName=boolean],
    [rendererList=boolean], [rendererListUI=boolean], [rendererName=string],
    [rendererOverrideList=boolean], [rendererOverrideListUI=boolean],
    [rendererOverrideName=string], [resetCustomCamera=boolean], [rigRoot=string],
    [rightCamera=string], [sceneRenderFilter=string], [selectionConnection=string],
    [selectionHiliteDisplay=boolean], [setSelected=boolean], [shadingModel=int],
    [shadows=boolean], [smallObjectCulling=boolean], [smallObjectThreshold=float],
    [smoothWireframe=boolean], [sortTransparent=boolean], [stateString=boolean],
    [stereoDrawMode=boolean], [strokes=boolean], [subdivSurfaces=boolean],
    [swapEyes=boolean], [textureAnisotropic=boolean], [textureCompression=boolean],
    [textureDisplay=string], [textureEnvironmentMap=boolean], [textureHilight=boolean],
    [textureMaxSize=int], [textureMemoryUsed=boolean], [textureSampling=int],
    [textures=boolean], [transpInShadows=boolean], [transparencyAlgorithm=string],
    [twoSidedLighting=boolean], [unParent=boolean], [unlockMainConnection=boolean],
    [updateColorMode=boolean], [updateMainConnection=boolean], [useBaseRenderer=boolean],
    [useColorIndex=boolean], [useCustomBackground=boolean], [useDefaultMaterial=boolean],
    [useInteractiveMode=boolean], [useRGBImagePlane=boolean],
    [useReducedRenderer=boolean], [useTemplate=string], [userNode=string],
    [viewColor=[float, float, float, float]], [viewObjects=boolean],
    [viewSelected=boolean], [viewType=boolean], [width=boolean],
    [wireframeBackingStore=boolean], [wireframeOnShaded=boolean], [xray=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stereoCameraView.html
    """
    return _wrapCommand(cmds.stereoCameraView, args, kwargs)


def stereoRigManager(*args, **kwargs):  # noqa
    """This command manages the set of stereo rig tools.

    stereoRigManager( objects , [addRig=[string, string, string]], [cameraSetFunc=[string,
    string]], [creationProcedure=[string, string]], [defaultRig=string], [delete=string],
    [language=[string, string]], [listRigs=boolean], [rigDefinition=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stereoRigManager.html
    """
    return _wrapCommand(cmds.stereoRigManager, args, kwargs)


def stitchSurface(*args, **kwargs):  # noqa
    """The stitchSurface command aligns two surfaces together to be G(0) and/or G(1) continuous
    by ajusting only the Control Vertices of the surfaces.

    stitchSurface( [surfaceIsoparm] [surfaceIsoparm] , [bias=float], [caching=boolean],
    [cascade=boolean], [constructionHistory=boolean], [cvIthIndex=int], [cvJthIndex=int],
    [fixBoundary=boolean], [keepG0Continuity=boolean], [keepG1Continuity=boolean],
    [name=string], [nodeState=int], [numberOfSamples=int], [object=boolean],
    [parameterU=float], [parameterV=float], [positionalContinuity=boolean],
    [replaceOriginal=boolean], [stepCount=int], [tangentialContinuity=boolean],
    [togglePointNormals=boolean], [togglePointPosition=boolean],
    [toggleTolerance=boolean], [tolerance=linear], [weight0=float], [weight1=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stitchSurface.html
    """
    return _wrapCommand(cmds.stitchSurface, args, kwargs)


def stitchSurfacePoints(*args, **kwargs):  # noqa
    """The stitchSurfacePoints command aligns two or more surface points along the boundaries
    together to a single point.

    stitchSurfacePoints( selectionList , [bias=float], [caching=boolean], [cascade=boolean],
    [constructionHistory=boolean], [cvIthIndex=int], [cvJthIndex=int],
    [equalWeight=boolean], [fixBoundary=boolean], [keepG0Continuity=boolean],
    [keepG1Continuity=boolean], [name=string], [nodeState=int], [object=boolean],
    [parameterU=float], [parameterV=float], [positionalContinuity=boolean],
    [replaceOriginal=boolean], [stepCount=int], [tangentialContinuity=boolean],
    [togglePointNormals=boolean], [togglePointPosition=boolean],
    [toggleTolerance=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stitchSurfacePoints.html
    """
    return _wrapCommand(cmds.stitchSurfacePoints, args, kwargs)


def stringArrayIntersector(*args, **kwargs):  # noqa
    """The stringArrayIntersector command creates and edits an object which is able to
    efficiently intersect large string arrays.

    stringArrayIntersector( string , [allowDuplicates=boolean], [defineTemplate=string],
    [exists=boolean], [intersect=string[]], [reset=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stringArrayIntersector.html
    """
    return _wrapCommand(cmds.stringArrayIntersector, args, kwargs)


def stroke(*args, **kwargs):  # noqa
    """The stroke command creates a new Paint Effects stroke node.

    stroke( [string] , [name=string], [pressure=boolean], [seed=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/stroke.html
    """
    return _wrapCommand(cmds.stroke, args, kwargs)


def subdAutoProjection(*args, **kwargs):  # noqa
    """Projects a texture map onto an object, using several orthogonal projections
    simultaneously.

    subdAutoProjection( selectionList , [caching=boolean], [constructionHistory=boolean],
    [layout=int], [layoutMethod=int], [name=string], [nodeState=int], [optimize=int],
    [percentageSpace=float], [planes=int], [scale=int], [skipIntersect=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdAutoProjection.html
    """
    return _wrapCommand(cmds.subdAutoProjection, args, kwargs)


def subdCleanTopology(*args, **kwargs):  # noqa
    """Command cleans topology of subdiv surfaces - at all levels.

    subdCleanTopology()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdCleanTopology.html
    """
    return _wrapCommand(cmds.subdCleanTopology, args, kwargs)


def subdCollapse(*args, **kwargs):  # noqa
    """This command converts a takes a subdivision surface, passed as the argument, and produces
    a subdivision surface with a number of hierarchy levels "removed".

    subdCollapse( [string] , [caching=boolean], [constructionHistory=boolean], [level=int],
    [name=string], [nodeState=int], [object=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdCollapse.html
    """
    return _wrapCommand(cmds.subdCollapse, args, kwargs)


def subdDuplicateAndConnect(*args, **kwargs):  # noqa
    """This command duplicates the input subdivision surface object, connects up the outSubdiv
    attribute of the original subd shape to the create attribute of the newly created
    duplicate shape and copies over the shader assignments from the original shape to the
    new duplicated shape.

    subdDuplicateAndConnect( object )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdDuplicateAndConnect.html
    """
    return _wrapCommand(cmds.subdDuplicateAndConnect, args, kwargs)


def subdEditUV(*args, **kwargs):  # noqa
    """Command edits uvs on subdivision surfaces.

    subdEditUV([angle=float], [pivotU=float], [pivotV=float], [relative=boolean],
    [rotateRatio=float], [rotation=boolean], [scale=boolean], [scaleU=float],
    [scaleV=float], [uValue=float], [uvSetName=string], [vValue=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdEditUV.html
    """
    return _wrapCommand(cmds.subdEditUV, args, kwargs)


def subdiv(*args, **kwargs):  # noqa
    """Provides useful information about the selected subdiv or components, such as the deepest
    subdivided level, the children or parents of the currently selected components, etc.

    subdiv([currentLevel=boolean], [currentSubdLevel=boolean], [deepestLevel=int],
    [displayLoad=boolean], [edgeStats=boolean], [faceStats=boolean],
    [maxPossibleLevel=int], [proxyMode=int], [smallOffsets=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdiv.html
    """
    return _wrapCommand(cmds.subdiv, args, kwargs)


def subdivCrease(*args, **kwargs):  # noqa
    """Set the creasing on subdivision mesh edges or mesh points that are on the selection list.

    subdivCrease([sharpness=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdivCrease.html
    """
    return _wrapCommand(cmds.subdivCrease, args, kwargs)


def subdivDisplaySmoothness(*args, **kwargs):  # noqa
    """Sets or querys the display smoothness of subdivision surfaces on the selection list or of
    all subdivision surfaces if the -all option is set.

    subdivDisplaySmoothness([all=boolean], [smoothness=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdivDisplaySmoothness.html
    """
    return _wrapCommand(cmds.subdivDisplaySmoothness, args, kwargs)


def subdLayoutUV(*args, **kwargs):  # noqa
    """Move UVs in the texture plane to avoid overlaps.

    subdLayoutUV([caching=boolean], [constructionHistory=boolean], [flipReversed=boolean],
    [layout=int], [layoutMethod=int], [name=string], [nodeState=int],
    [percentageSpace=float], [rotateForBestFit=int], [scale=int], [separate=int],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdLayoutUV.html
    """
    return _wrapCommand(cmds.subdLayoutUV, args, kwargs)


def subdListComponentConversion(*args, **kwargs):  # noqa
    """This command converts subdivision surface components from one or more types to another one
    or more types, and returns the list of the conversion.

    subdListComponentConversion( [objects...] , [border=boolean], [fromEdge=boolean],
    [fromFace=boolean], [fromUV=boolean], [fromVertex=boolean], [internal=boolean],
    [toEdge=boolean], [toFace=boolean], [toUV=boolean], [toVertex=boolean],
    [uvShell=boolean], [uvShellBorder=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdListComponentConversion.html
    """
    return _wrapCommand(cmds.subdListComponentConversion, args, kwargs)


def subdMapCut(*args, **kwargs):  # noqa
    """Cut along edges of the texture mapping.

    subdMapCut([caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdMapCut.html
    """
    return _wrapCommand(cmds.subdMapCut, args, kwargs)


def subdMapSewMove(*args, **kwargs):  # noqa
    """This command can be used to Move and Sew together separate UV pieces along geometric
    edges.

    subdMapSewMove( selectionList , [caching=boolean], [constructionHistory=boolean],
    [limitPieceSize=boolean], [name=string], [nodeState=int], [numberFaces=int],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdMapSewMove.html
    """
    return _wrapCommand(cmds.subdMapSewMove, args, kwargs)


def subdMatchTopology(*args, **kwargs):  # noqa
    """Command matches topology across multiple subdiv surfaces - at all levels.

    subdMatchTopology([frontOfChain=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdMatchTopology.html
    """
    return _wrapCommand(cmds.subdMatchTopology, args, kwargs)


def subdMirror(*args, **kwargs):  # noqa
    """This command takes a subdivision surface, passed as the argument, and produces a
    subdivision surface that is a mirror.

    subdMirror( [string] , [caching=boolean], [constructionHistory=boolean], [name=string],
    [nodeState=int], [object=boolean], [xMirror=boolean], [yMirror=boolean],
    [zMirror=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdMirror.html
    """
    return _wrapCommand(cmds.subdMirror, args, kwargs)


def subdPlanarProjection(*args, **kwargs):  # noqa
    """TsubProjCmdBase is a base class for the command to create a mapping on the selected
    subdivision faces.

    subdPlanarProjection([caching=boolean], [constructionHistory=boolean],
    [createNewMap=boolean], [imageCenter=[float, float]], [imageCenterX=float],
    [imageCenterY=float], [imageScale=[float, float]], [imageScaleU=float],
    [imageScaleV=float], [insertBeforeDeformers=boolean], [keepImageRatio=boolean],
    [mapDirection=string], [name=string], [nodeState=int], [projectionCenter=[linear,
    linear, linear]], [projectionCenterX=linear], [projectionCenterY=linear],
    [projectionCenterZ=linear], [projectionHeight=linear], [projectionScale=[linear,
    linear]], [projectionWidth=linear], [rotate=[angle, angle, angle]], [rotateX=angle],
    [rotateY=angle], [rotateZ=angle], [rotationAngle=angle], [smartFit=boolean],
    [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdPlanarProjection.html
    """
    return _wrapCommand(cmds.subdPlanarProjection, args, kwargs)


def subdToBlind(*args, **kwargs):  # noqa
    """The subdivision surface hierarchical edits will get copied into blind data on the given
    polygon.

    subdToBlind([absolutePosition=boolean], [includeCreases=boolean],
    [includeZeroOffsets=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdToBlind.html
    """
    return _wrapCommand(cmds.subdToBlind, args, kwargs)


def subdToPoly(*args, **kwargs):  # noqa
    """This command tessellates a subdivision surface and produces polygon.

    subdToPoly( [subd] , [addUnderTransform=boolean], [applyMatrixToResult=boolean],
    [caching=boolean], [connectShaders=boolean], [constructionHistory=boolean],
    [copyUVTopology=boolean], [depth=int], [extractPointPosition=boolean], [format=int],
    [inSubdCVId=[int, int]], [inSubdCVIdLeft=int], [inSubdCVIdRight=int], [maxPolys=int],
    [name=string], [nodeState=int], [object=boolean], [outSubdCVId=[int, int]],
    [outSubdCVIdLeft=int], [outSubdCVIdRight=int], [outv=int],
    [preserveVertexOrdering=boolean], [sampleCount=int], [shareUVs=boolean],
    [subdNormals=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdToPoly.html
    """
    return _wrapCommand(cmds.subdToPoly, args, kwargs)


def subdTransferUVsToCache(*args, **kwargs):  # noqa
    """The subdivision surface finer level uvs will get copied to the polygonToSubd node sent in
    as argument.

    subdTransferUVsToCache()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/subdTransferUVsToCache.html
    """
    return _wrapCommand(cmds.subdTransferUVsToCache, args, kwargs)


def substituteGeometry(*args, **kwargs):  # noqa
    """This command can be used to replace the geometry which is already connected to deformers
    with a new geometry.

    substituteGeometry([disableNonSkinDeformers=boolean], [newGeometryToLayer=boolean],
    [oldGeometryToLayer=boolean], [reWeightDistTolerance=float],
    [retainOldGeometry=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/substituteGeometry.html
    """
    return _wrapCommand(cmds.substituteGeometry, args, kwargs)


def suitePrefs(*args, **kwargs):  # noqa
    """This command sets the mouse and keyboard interaction mode for Maya and other Suites
    applications (if Maya is part of a Suites install).

    suitePrefs([applyToSuite=string], [installedAsSuite=boolean], [isCompleteSuite=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/suitePrefs.html
    """
    return _wrapCommand(cmds.suitePrefs, args, kwargs)


def surface(*args, **kwargs):  # noqa
    """The cmd creates a NURBS spline surface (rational or non rational).

    surface([degreeU=int], [degreeV=int], [formU=string], [formV=string], [knotU=float],
    [knotV=float], [name=string], [objectSpace=boolean], [point=[linear, linear, linear]],
    [pointWeight=[linear, linear, linear, linear]], [worldSpace=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/surface.html
    """
    return _wrapCommand(cmds.surface, args, kwargs)


def surfaceSampler(*args, **kwargs):  # noqa
    """Maps surface detail from a source surface to a new texture map on a target surface.

    surfaceSampler([camera=name], [fileFormat=string], [filename=string], [filterSize=float],
    [filterType=uint], [flipU=boolean], [flipV=boolean], [ignoreMirroredFaces=boolean],
    [ignoreTransforms=boolean], [mapHeight=uint], [mapMaterials=boolean],
    [mapOutput=string], [mapSpace=string], [mapWidth=uint], [maxSearchDistance=linear],
    [maximumValue=linear], [overscan=uint], [searchCage=string], [searchMethod=uint],
    [searchOffset=linear], [shadows=boolean], [source=string], [sourceUVSpace=string],
    [superSampling=uint], [target=string], [targetUVSpace=string],
    [useGeometryNormals=boolean], [uvSet=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/surfaceSampler.html
    """
    return _wrapCommand(cmds.surfaceSampler, args, kwargs)


def surfaceShaderList(*args, **kwargs):  # noqa
    """Add/Remove a relationship between an object and the current shading group.

    surfaceShaderList([add=name], [remove=name])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/surfaceShaderList.html
    """
    return _wrapCommand(cmds.surfaceShaderList, args, kwargs)


def swatchDisplayPort(*args, **kwargs):  # noqa
    """This command creates a 3dPort that displays a swatch representing the shading node.

    swatchDisplayPort( [string] , [annotation=string], [backgroundColor=[float, float,
    float]], [borderColor=[float, float, float]], [borderWidth=int],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [pressCommand=script], [preventOverride=boolean],
    [renderPriority=int], [renderSize=int], [shadingNode=name], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int],
    [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/swatchDisplayPort.html
    """
    return _wrapCommand(cmds.swatchDisplayPort, args, kwargs)


def swatchRefresh(*args, **kwargs):  # noqa
    """The `swatchRefresh` command causes image source node swatches to be refreshed on screen.

    swatchRefresh()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/swatchRefresh.html
    """
    return _wrapCommand(cmds.swatchRefresh, args, kwargs)


def switchTable(*args, **kwargs):  # noqa
    """This command creates/edits/queries the switch table control.

    switchTable( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label1=string],
    [label2=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [selectedRow=boolean], [statusBarMessage=string],
    [switchNode=name], [underPointerRow=boolean], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/switchTable.html
    """
    return _wrapCommand(cmds.switchTable, args, kwargs)


def symbolButton(*args, **kwargs):  # noqa
    """This command creates a symbol button.

    symbolButton( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [command=script], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [isObscured=boolean],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/symbolButton.html
    """
    return _wrapCommand(cmds.symbolButton, args, kwargs)


def symbolCheckBox(*args, **kwargs):  # noqa
    """This command creates a symbol check box.

    symbolCheckBox( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [disableOffImage=string],
    [disableOnImage=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [image=string], [innerMargin=boolean],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [offCommand=script], [offImage=string],
    [onCommand=script], [onImage=string], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [value=boolean], [version=string], [visible=boolean], [visibleChangeCommand=script],
    [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/symbolCheckBox.html
    """
    return _wrapCommand(cmds.symbolCheckBox, args, kwargs)


def symmetricModelling(*args, **kwargs):  # noqa
    """This command allows you to change the symmetric modelling options.

    symmetricModelling([about=string], [allowPartial=boolean], [axis=string],
    [preserveSeam=int], [reset=boolean], [seamFalloffCurve=string], [seamTolerance=float],
    [symmetry=int], [tolerance=float], [topoSymmetry=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/symmetricModelling.html
    """
    return _wrapCommand(cmds.symmetricModelling, args, kwargs)


def sysFile(*args, **kwargs):  # noqa
    """This command provides a system independent way to create a directory or to rename or
    delete a file.

    sysFile( string , [copy=string], [delete=boolean], [makeDir=boolean], [move=string],
    [removeEmptyDir=boolean], [rename=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/sysFile.html
    """
    return _wrapCommand(cmds.sysFile, args, kwargs)


def tabLayout(*args, **kwargs):  # noqa
    """This command creates a tab group.

    tabLayout( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [borderStyle=string], [changeCommand=script], [childArray=boolean],
    [childResizable=boolean], [closeTab=int], [closeTabCommand=script],
    [defineTemplate=string], [docTag=string], [doubleClickCommand=script],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [horizontalScrollBarThickness=int], [image=string], [imageVisible=boolean],
    [innerMarginHeight=int], [innerMarginWidth=int], [isObscured=boolean],
    [manage=boolean], [minChildWidth=int], [moveTab=[int, int]], [newTabCommand=script],
    [noBackground=boolean], [numberOfChildren=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [popupMenuArray=boolean], [postMenuCommand=script],
    [preSelectCommand=script], [preventOverride=boolean], [scrollable=boolean],
    [scrollableTabs=boolean], [selectCommand=script], [selectTab=string],
    [selectTabIndex=int], [showNewTab=boolean], [statusBarMessage=string],
    [tabIcon=[string, string]], [tabIconIndex=[int, string]], [tabLabel=[string, string]],
    [tabLabelIndex=[int, string]], [tabPosition=string], [tabTooltip=[string, string]],
    [tabTooltipIndex=[int, string]], [tabsClosable=boolean], [tabsVisible=boolean],
    [useTemplate=string], [verticalScrollBarThickness=int], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tabLayout.html
    """
    return _wrapCommand(cmds.tabLayout, args, kwargs)


def tangentConstraint(*args, **kwargs):  # noqa
    """Constrain an object's orientation based on the tangent of the target curve[s] at the
    closest point[s] to the object.

    tangentConstraint( [target...] object , [aimVector=[float, float, float]], [layer=string],
    [name=string], [remove=boolean], [targetList=boolean], [upVector=[float, float,
    float]], [weight=float], [weightAliasList=boolean], [worldUpObject=name],
    [worldUpType=string], [worldUpVector=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tangentConstraint.html
    """
    return _wrapCommand(cmds.tangentConstraint, args, kwargs)


def targetWeldCtx(*args, **kwargs):  # noqa
    """Create a new context to weld vertices together on a poly object.

    targetWeldCtx([exists=boolean], [image1=string], [image2=string], [image3=string],
    [mergeToCenter=boolean], [preserveUV=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/targetWeldCtx.html
    """
    return _wrapCommand(cmds.targetWeldCtx, args, kwargs)


def tension(*args, **kwargs):  # noqa
    """This command is used to create, edit and query tension nodes.

    tension( selectionList , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [deformerTools=boolean], [envelope=float], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [ignoreSelected=boolean], [includeHiddenSelections=boolean], [inwardConstraint=float],
    [name=string], [outwardConstraint=float], [parallel=boolean],
    [pinBorderVertices=boolean], [prune=boolean], [remove=boolean],
    [selectedComponents=boolean], [smoothingIterations=uint], [smoothingStep=float],
    [split=boolean], [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tension.html
    """
    return _wrapCommand(cmds.tension, args, kwargs)


def texCutContext(*args, **kwargs):  # noqa
    """This command creates a context for cut uv tool.

    texCutContext( contextName , [adjustSize=boolean], [displayShellBorders=boolean],
    [edgeSelectSensitive=float], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [mode=string], [moveRatio=float], [name=string],
    [size=float], [steadyStroke=boolean], [steadyStrokeDistance=float],
    [touchToSew=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texCutContext.html
    """
    return _wrapCommand(cmds.texCutContext, args, kwargs)


def texLatticeDeformContext(*args, **kwargs):  # noqa
    """This command creates a context which may be used to deform UV maps with lattice
    manipulator.

    texLatticeDeformContext( contextName , [envelope=float], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string],
    [latticeColumns=uint], [latticeRows=uint], [name=string],
    [showMoveManipulator=boolean], [snapPixelMode=boolean], [useBoundingRect=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texLatticeDeformContext.html
    """
    return _wrapCommand(cmds.texLatticeDeformContext, args, kwargs)


def texManipContext(*args, **kwargs):  # noqa
    """Command used to register the texSelectCtx tool.

    texManipContext([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texManipContext.html
    """
    return _wrapCommand(cmds.texManipContext, args, kwargs)


def texMoveContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a texture editor move manip context.

    texMoveContext( [object] , [editPivotMode=boolean], [exists=boolean], [image1=string],
    [image2=string], [image3=string], [position=boolean], [snap=boolean],
    [snapComponentsRelative=boolean], [snapPixelMode=int], [snapValue=float],
    [tweakMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texMoveContext.html
    """
    return _wrapCommand(cmds.texMoveContext, args, kwargs)


def texMoveUVShellContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a texture editor move manip context.

    texMoveUVShellContext( [object] , [exists=boolean], [image1=string], [image2=string],
    [image3=string], [iterations=int], [mask=boolean], [position=boolean],
    [shellBorder=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texMoveUVShellContext.html
    """
    return _wrapCommand(cmds.texMoveUVShellContext, args, kwargs)


def texRotateContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a rotate context for the UV Editor.

    texRotateContext([editPivotMode=boolean], [exists=boolean], [image1=string],
    [image2=string], [image3=string], [position=boolean], [snap=boolean],
    [snapRelative=boolean], [snapValue=float], [tweakMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texRotateContext.html
    """
    return _wrapCommand(cmds.texRotateContext, args, kwargs)


def texScaleContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a scale context for the UV Editor.

    texScaleContext([editPivotMode=boolean], [exists=boolean], [image1=string],
    [image2=string], [image3=string], [position=boolean], [preventNegativeScale=boolean],
    [snap=boolean], [snapRelative=boolean], [snapValue=float], [tweakMode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texScaleContext.html
    """
    return _wrapCommand(cmds.texScaleContext, args, kwargs)


def texSculptCacheContext(*args, **kwargs):  # noqa
    """This is a tool context command for uv cache sculpting tool.

    texSculptCacheContext([adjustSize=boolean], [adjustStrength=boolean], [direction=int],
    [falloffType=int], [floodPin=float], [grabTwist=boolean], [inverted=boolean],
    [mode=string], [sculptFalloffCurve=string], [showBrushRingDuringStroke=boolean],
    [size=float], [strength=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texSculptCacheContext.html
    """
    return _wrapCommand(cmds.texSculptCacheContext, args, kwargs)


def texSelectContext(*args, **kwargs):  # noqa
    """Command used to register the texSelectCtx tool.

    texSelectContext([exists=boolean], [image1=string], [image2=string], [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texSelectContext.html
    """
    return _wrapCommand(cmds.texSelectContext, args, kwargs)


def texSelectShortestPathCtx(*args, **kwargs):  # noqa
    """Creates a new context to select shortest edge path between two vertices or UVs in the
    texture editor window.

    texSelectShortestPathCtx([exists=boolean], [image1=string], [image2=string],
    [image3=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texSelectShortestPathCtx.html
    """
    return _wrapCommand(cmds.texSelectShortestPathCtx, args, kwargs)


def texSmudgeUVContext(*args, **kwargs):  # noqa
    """This command creates a context for smudge UV tool.

    texSmudgeUVContext( contextName , [dragSlider=string], [effectType=string],
    [exists=boolean], [functionType=string], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [pressure=float], [radius=float],
    [smudgeIsMiddle=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texSmudgeUVContext.html
    """
    return _wrapCommand(cmds.texSmudgeUVContext, args, kwargs)


def text(*args, **kwargs):  # noqa
    """Create a simple text label control.

    text( [string] , [align=string], [annotation=string], [backgroundColor=[float, float,
    float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [dropRectCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [font=string], [fullPathName=boolean], [height=int], [highlightColor=[float, float,
    float]], [hyperlink=boolean], [isObscured=boolean], [label=string], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [recomputeSize=boolean],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int], [wordWrap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/text.html
    """
    return _wrapCommand(cmds.text, args, kwargs)


def textCurves(*args, **kwargs):  # noqa
    """The textCurves command creates NURBS curves from a text string using the specified font.

    textCurves( [string] , [font=string], [name=string], [object=boolean], [text=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textCurves.html
    """
    return _wrapCommand(cmds.textCurves, args, kwargs)


def textField(*args, **kwargs):  # noqa
    """Create a text field control.

    textField( [string] , [alwaysInvokeEnterCommandOnReturn=boolean], [annotation=string],
    [backgroundColor=[float, float, float]], [changeCommand=script],
    [defineTemplate=string], [disableButtons=boolean], [disableClearButton=boolean],
    [disableHistoryButton=boolean], [docTag=string], [dragCallback=script],
    [drawInactiveFrame=boolean], [dropCallback=script], [editable=boolean],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [enterCommand=script], [exists=boolean], [fileName=string], [font=string],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [insertText=string], [insertionPosition=int], [isObscured=boolean], [manage=boolean],
    [noBackground=boolean], [numberOfPopupMenus=boolean], [parent=string],
    [placeholderText=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [receiveFocusCommand=script], [searchField=boolean], [statusBarMessage=string],
    [text=string], [textChangedCommand=script], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textField.html
    """
    return _wrapCommand(cmds.textField, args, kwargs)


def textFieldButtonGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    textFieldButtonGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [buttonCommand=script], [buttonLabel=string], [changeCommand=script],
    [columnAlign=[int, string]], [columnAlign2=[string, string]], [columnAlign3=[string,
    string, string]], [columnAlign4=[string, string, string, string]],
    [columnAlign5=[string, string, string, string, string]], [columnAlign6=[string,
    string, string, string, string, string]], [columnAttach=[int, string, int]],
    [columnAttach2=[string, string]], [columnAttach3=[string, string, string]],
    [columnAttach4=[string, string, string, string]], [columnAttach5=[string, string,
    string, string, string]], [columnAttach6=[string, string, string, string, string,
    string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean],
    [enable=boolean], [enableBackground=boolean], [enableButton=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fileName=string],
    [forceChangeCommand=boolean], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [insertText=string], [insertionPosition=int],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [placeholderText=string],
    [popupMenuArray=boolean], [preventOverride=boolean], [rowAttach=[int, string, int]],
    [statusBarMessage=string], [text=string], [textChangedCommand=script],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textFieldButtonGrp.html
    """
    return _wrapCommand(cmds.textFieldButtonGrp, args, kwargs)


def textFieldGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    textFieldGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [editable=boolean],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [fileName=string], [forceChangeCommand=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [insertText=string], [insertionPosition=int], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [parent=string], [placeholderText=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [rowAttach=[int, string, int]], [statusBarMessage=string],
    [text=string], [textChangedCommand=script], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textFieldGrp.html
    """
    return _wrapCommand(cmds.textFieldGrp, args, kwargs)


def textManip(*args, **kwargs):  # noqa
    """Shows/hides the text manip.

    textManip([visible=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textManip.html
    """
    return _wrapCommand(cmds.textManip, args, kwargs)


def textScrollList(*args, **kwargs):  # noqa
    """This command creates/edits/queries a text scrolling list.

    textScrollList( [string] , [allItems=boolean], [allowAutomaticSelection=boolean],
    [allowMultiSelection=boolean], [annotation=string], [append=string],
    [appendPosition=[int, string]], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [deleteKeyCommand=script], [deselectAll=boolean],
    [deselectIndexedItem=int], [deselectItem=string], [docTag=string],
    [doubleClickCommand=script], [dragCallback=script], [dropCallback=script],
    [enable=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [font=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [lineFont=[int,
    string]], [manage=boolean], [noBackground=boolean], [numberOfItems=boolean],
    [numberOfPopupMenus=boolean], [numberOfRows=int], [numberOfSelectedItems=boolean],
    [parent=string], [popupMenuArray=boolean], [preventOverride=boolean],
    [removeAll=boolean], [removeIndexedItem=int], [removeItem=string],
    [selectCommand=script], [selectIndexedItem=int], [selectItem=string],
    [selectUniqueTagItem=string], [showIndexedItem=int], [statusBarMessage=string],
    [uniqueTag=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textScrollList.html
    """
    return _wrapCommand(cmds.textScrollList, args, kwargs)


def textureDeformer(*args, **kwargs):  # noqa
    """This command creates a texture deformer for the object.

    textureDeformer( selectionList , [after=boolean], [afterReference=boolean],
    [before=boolean], [components=boolean], [deformerTools=boolean], [direction=string],
    [envelope=float], [exclusive=string], [frontOfChain=boolean], [geometry=string],
    [geometryIndices=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [name=string], [offset=float], [parallel=boolean],
    [pointSpace=string], [prune=boolean], [remove=boolean], [selectedComponents=boolean],
    [split=boolean], [strength=float], [useComponentTags=boolean], [vectorOffset=[float,
    float, float]], [vectorSpace=string], [vectorStrength=[float, float, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textureDeformer.html
    """
    return _wrapCommand(cmds.textureDeformer, args, kwargs)


def texturePlacementContext(*args, **kwargs):  # noqa
    """Create a command for creating new texture placement contexts.

    texturePlacementContext([exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [labelMapping=boolean], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texturePlacementContext.html
    """
    return _wrapCommand(cmds.texturePlacementContext, args, kwargs)


def textureWindow(*args, **kwargs):  # noqa
    """This command is used to create a UV Editor and to query or edit the texture editor
    settings.

    textureWindow( string , [activeSelectionOnTop=boolean], [axesColor=[float, float, float]],
    [backFacingColor=[float, float, float, float]], [capture=string],
    [captureSequenceNumber=int], [changeCommand=[string, string, string, string]],
    [checkerColor1=[float, float, float]], [checkerColor2=[float, float, float]],
    [checkerColorMode=int], [checkerDensity=int], [checkerDrawTileLabels=boolean],
    [checkerGradient1=[float, float, float]], [checkerGradient2=[float, float, float]],
    [checkerGradientOverlay=boolean], [checkerTileLabelColor=[float, float, float]],
    [clearImage=boolean], [cmEnabled=boolean], [control=boolean], [defineTemplate=string],
    [displayAxes=boolean], [displayCheckered=boolean], [displayDistortion=boolean],
    [displayDivisionLines=boolean], [displayGridLines=boolean], [displayImage=int],
    [displayIsolateSelectHUD=boolean], [displayLabels=boolean],
    [displayOverlappingUVCountHUD=boolean], [displayPreselection=boolean],
    [displayReversedUVCountHUD=boolean], [displaySolidMap=boolean], [displayStyle=string],
    [displayTextureBorder=boolean], [displayUVPositionHUD=boolean],
    [displayUVShellCountHUD=boolean], [displayUVStatisticsHUD=boolean],
    [displayUsedPercentageHUD=boolean], [distortionAlpha=float],
    [distortionPerObject=boolean], [divisions=int], [docTag=string],
    [doubleBuffer=boolean], [drawAxis=boolean], [drawSubregions=boolean],
    [exists=boolean], [exposure=float], [filter=string], [forceMainConnection=string],
    [forceRebake=boolean], [frameAll=boolean], [frameSelected=boolean],
    [frontFacingColor=[float, float, float, float]], [gamma=float],
    [gridLinesColor=[float, float, float]], [gridNumbersColor=[float, float, float]],
    [highlightConnection=string], [imageBaseColor=[float, float, float]],
    [imageDim=boolean], [imageDisplay=boolean], [imageNames=boolean], [imageNumber=int],
    [imagePixelSnap=boolean], [imageRatio=boolean], [imageRatioValue=float],
    [imageSize=boolean], [imageTileRange=[float, float, float, float]],
    [imageUnfiltered=boolean], [internalFaces=boolean], [labelPosition=string],
    [loadImage=string], [lockMainConnection=boolean], [mainListConnection=string],
    [maxResolution=int], [multiColorAlpha=float], [nbImages=boolean], [nextView=boolean],
    [numUvSets=boolean], [numberOfImages=int], [numberOfTextures=int], [panel=string],
    [parent=string], [previousView=boolean], [realSize=boolean], [refresh=boolean],
    [relatedFaces=boolean], [removeAllImages=boolean], [removeImage=boolean],
    [rendererString=string], [reset=boolean], [saveImage=boolean], [scaleBlue=float],
    [scaleGreen=float], [scaleRed=float], [selectInternalFaces=boolean],
    [selectRelatedFaces=boolean], [selectionConnection=string], [setUvSet=int],
    [singleBuffer=boolean], [size=float], [solidMap3dView=boolean],
    [solidMapColorSeed=int], [solidMapPerShell=boolean], [spacing=float],
    [stateString=boolean], [style=int], [subdivisionLinesColor=[float, float, float]],
    [textureBorder3dView=boolean], [textureBorderColor=[float, float, float]],
    [textureBorderWidth=int], [textureNames=boolean], [textureNumber=int],
    [tileLabels=boolean], [tileLinesColor=[float, float, float]], [toggle=boolean],
    [toggleExposure=boolean], [toggleGamma=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean],
    [useFaceGroup=boolean], [useTemplate=string], [usedPercentageHUDRange=[float, float,
    float, float]], [uvSets=boolean], [viewPortImage=boolean], [viewTransformName=string],
    [wireframeComponentColor=[float, float, float, float]], [wireframeObjectColor=[float,
    float, float, float]], [writeImage=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/textureWindow.html
    """
    return _wrapCommand(cmds.textureWindow, args, kwargs)


def texTweakUVContext(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a texture editor move manip context.

    texTweakUVContext( [object] , [exists=boolean], [image1=string], [image2=string],
    [image3=string], [position=boolean], [tolerance=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texTweakUVContext.html
    """
    return _wrapCommand(cmds.texTweakUVContext, args, kwargs)


def texWinToolCtx(*args, **kwargs):  # noqa
    """This class creates a context for the View Tools "track", "dolly", and "box zoom" in the
    texture window.

    texWinToolCtx([alternateContext=boolean], [boxzoom=boolean], [dolly=boolean],
    [exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string], [toolName=string], [track=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/texWinToolCtx.html
    """
    return _wrapCommand(cmds.texWinToolCtx, args, kwargs)


def threadCount(*args, **kwargs):  # noqa
    """This command sets the number of threads to be used by Maya in regions of code that are
    multithreaded.

    threadCount([numberOfThreads=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/threadCount.html
    """
    return _wrapCommand(cmds.threadCount, args, kwargs)


def threePointArcCtx(*args, **kwargs):  # noqa
    """The threePointArcCtx command creates a new context for creating 3 point arcs.

    threePointArcCtx([degree=uint], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [spans=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/threePointArcCtx.html
    """
    return _wrapCommand(cmds.threePointArcCtx, args, kwargs)


def thumbnailCaptureComponent(*args, **kwargs):  # noqa
    """This command is used to generate a thumbnail/playblast sequence from the scene.

    thumbnailCaptureComponent( [string] , [capture=boolean], [capturedFrameCount=boolean],
    [closeCurrentSession=boolean], [delete=boolean], [endFrame=int],
    [fileDialogCallback=string], [isSessionOpened=boolean],
    [launchedFromOptionsBox=boolean], [previewPath=boolean],
    [removeProjectThumbnail=string], [save=string], [startFrame=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/thumbnailCaptureComponent.html
    """
    return _wrapCommand(cmds.thumbnailCaptureComponent, args, kwargs)


def timeCode(*args, **kwargs):  # noqa
    """Use this command to query and set the time code information in the file.

    timeCode([mayaStartFrame=float], [productionStartFrame=float],
    [productionStartHour=float], [productionStartMinute=float],
    [productionStartSecond=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeCode.html
    """
    return _wrapCommand(cmds.timeCode, args, kwargs)


def timeControl(*args, **kwargs):  # noqa
    """This command creates a control that can be used for changing current time,
    displaying/editing keys, and displaying/scrubbing sound.

    timeControl( string , [animCurveNames=boolean], [animLayerFilterOptions=string],
    [animLayerShowWeight=boolean], [annotation=string], [backgroundColor=[float, float,
    float]], [beginScrub=boolean], [currentFrameColor=[float, float, float, float]],
    [defineTemplate=string], [displaySound=boolean], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [endScrub=boolean],
    [exists=boolean], [forceRedraw=boolean], [forceRefresh=boolean],
    [foregroundColor=[float, float, float]], [fullPathName=boolean], [globalTime=boolean],
    [height=int], [highlightColor=[float, float, float]], [isObscured=boolean],
    [mainListConnection=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [pressCommand=script], [preventOverride=boolean], [range=boolean],
    [rangeArray=boolean], [rangeVisible=boolean], [releaseCommand=script],
    [repeatChunkSize=float], [repeatOnHold=boolean], [resample=boolean],
    [showKeys=string], [showKeysCombined=boolean], [snap=boolean], [sound=string],
    [statusBarMessage=string], [tickSize=int], [tickSpan=int], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [waveform=string], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeControl.html
    """
    return _wrapCommand(cmds.timeControl, args, kwargs)


def timeEditor(*args, **kwargs):  # noqa
    """General Time Editor commands.

    timeEditor([allClips=string], [clipId=int], [commonParentTrack=boolean],
    [composition=string], [drivingClipsForAttr=string], [drivingClipsForObj=[string,
    int]], [includeParent=boolean], [mute=boolean], [selectedClips=string],
    [topLevelClips=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditor.html
    """
    return _wrapCommand(cmds.timeEditor, args, kwargs)


def timeEditorAnimSource(*args, **kwargs):  # noqa
    """Commands for managing animation sources.

    timeEditorAnimSource([addObjects=string], [addRelatedKG=boolean],
    [addSelectedObjects=boolean], [addSource=string], [apply=boolean], [attribute=string],
    [bakeToAnimSource=string], [calculateTiming=boolean], [copyAnimation=boolean],
    [drivenClips=boolean], [exclusive=boolean], [export=string],
    [importAllFbxTakes=boolean], [importFbx=string], [importFbxTakes=string],
    [importMayaFile=string], [importOption=string], [importPopulateOption=string],
    [importedContainerNames=string], [includeRoot=boolean], [isUnique=boolean],
    [populateImportedAnimSources=string], [poseClip=boolean], [recursively=boolean],
    [removeSceneAnimation=boolean], [removeSource=string],
    [showAnimSourceRemapping=boolean], [takeList=string], [takesToImport=string],
    [targetIndex=string], [targets=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorAnimSource.html
    """
    return _wrapCommand(cmds.timeEditorAnimSource, args, kwargs)


def timeEditorBakeClips(*args, **kwargs):  # noqa
    """This command is used to bake Time Editor clips and to blend them into a single clip.

    timeEditorBakeClips( objects , [bakeToAnimSource=string], [bakeToClip=string],
    [clipId=int], [combineLayers=boolean], [forceSampling=boolean],
    [keepOriginalClip=boolean], [path=string], [sampleBy=time], [targetTrackIndex=int],
    [targetTracksNode=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorBakeClips.html
    """
    return _wrapCommand(cmds.timeEditorBakeClips, args, kwargs)


def timeEditorClip(*args, **kwargs):  # noqa
    """This command edits/queries Time Editor clips.

    timeEditorClip([absolute=boolean], [addAttribute=string], [addObjects=string],
    [addRelatedKG=boolean], [addSelectedObjects=boolean], [allowShrinking=boolean],
    [animSource=string], [attribute=string], [audio=string], [blendMode=int],
    [children=int], [clipAfter=boolean], [clipBefore=boolean], [clipDataType=boolean],
    [clipId=int], [clipIdFromNodeName=int], [clipIdFromPath=boolean], [clipNode=boolean],
    [clipPath=boolean], [copyClip=boolean], [crossfadeMode=int], [crossfadePlug=boolean],
    [curveTime=time], [defaultGhostRoot=boolean], [drivenAttributes=boolean],
    [drivenClipsBySource=string], [drivenObjects=boolean], [drivenRootObjects=boolean],
    [drivingSources=string], [duplicateClip=boolean], [duration=time],
    [emptySource=boolean], [endTime=time], [exclusive=boolean], [existingOnly=boolean],
    [exists=boolean], [explode=int], [exportAllClips=boolean], [exportFbx=string],
    [extend=boolean], [extendParent=boolean], [ghost=boolean], [ghostRootAdd=string],
    [ghostRootRemove=string], [group=boolean], [holdEnd=time], [holdStart=time],
    [importAllFbxTakes=boolean], [importFbx=string], [importFbxTakes=string],
    [importMayaFile=string], [importOption=string], [importPopulateOption=string],
    [importTakeDestination=int], [importedContainerNames=string], [includeRoot=boolean],
    [isContainer=boolean], [listUserGhostRoot=boolean], [loopEnd=time], [loopStart=time],
    [minClipDuration=boolean], [modifyAnimSource=boolean], [moveClip=time],
    [mute=boolean], [name=string], [parent=int], [parentClipId=int],
    [parentGroupId=boolean], [pasteClip=time], [path=string],
    [populateImportedAnimSources=string], [poseClip=boolean],
    [preserveAnimationTiming=boolean], [razorClip=time], [recursively=boolean],
    [remap=[string, string]], [remapNamespace=[string, string]], [remapSource=[string,
    string]], [remappedSourceAttrs=boolean], [remappedTargetAttrs=boolean],
    [removeAttribute=string], [removeClip=boolean], [removeCrossfade=boolean],
    [removeSceneAnimation=boolean], [removeWeightCurve=boolean], [resetTiming=boolean],
    [resetTransition=boolean], [ripple=boolean], [rootClipId=int], [rootPath=string],
    [scaleEnd=time], [scalePivot=time], [scaleStart=time], [setKeyframe=string],
    [showAnimSourceRemapping=boolean], [speedRamping=int], [startTime=time],
    [takeList=string], [takesToImport=string], [timeWarp=boolean],
    [timeWarpCurve=boolean], [timeWarpType=int], [track=string], [tracksNode=boolean],
    [transition=boolean], [trimEnd=time], [trimStart=time], [truncated=boolean],
    [type=string], [uniqueAnimSource=boolean], [userGhostRoot=boolean],
    [weightCurve=boolean], [zeroKeying=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClip.html
    """
    return _wrapCommand(cmds.timeEditorClip, args, kwargs)


def timeEditorClipLayer(*args, **kwargs):  # noqa
    """Time Editor clip layers commands.

    timeEditorClipLayer([addAttribute=string], [addLayer=string], [addObject=string],
    [allLayers=boolean], [attribute=string], [attributeKeyable=string], [clipId=int],
    [index=int], [keySiblings=boolean], [layerId=int], [layerName=string], [mode=int],
    [mute=boolean], [name=boolean], [path=string], [removeAttribute=string],
    [removeLayer=boolean], [removeObject=string], [resetSolo=boolean],
    [setKeyframe=boolean], [solo=boolean], [zeroKeying=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipLayer.html
    """
    return _wrapCommand(cmds.timeEditorClipLayer, args, kwargs)


def timeEditorClipOffset(*args, **kwargs):  # noqa
    """This command is used to compute an offset to apply on a source clip in order to
    automatically align it to a destination clip at a specified match element.

    timeEditorClipOffset([applyToAllRoots=boolean], [clipId=int], [matchClipId=int],
    [matchDstTime=time], [matchObj=name], [matchOffsetRot=boolean],
    [matchOffsetTrans=boolean], [matchPath=string], [matchRotOp=int], [matchSrcTime=time],
    [matchTransOp=int], [offsetTransform=boolean], [path=string], [resetMatch=int],
    [resetMatchPath=string], [rootObj=string], [upVectorX=float], [upVectorY=float],
    [upVectorZ=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorClipOffset.html
    """
    return _wrapCommand(cmds.timeEditorClipOffset, args, kwargs)


def timeEditorComposition(*args, **kwargs):  # noqa
    """Commands related to composition management inside Time Editor.

    timeEditorComposition([active=boolean], [allCompositions=boolean], [createTrack=boolean],
    [delete=boolean], [duplicateFrom=string], [rename=[string, string]],
    [tracksNode=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorComposition.html
    """
    return _wrapCommand(cmds.timeEditorComposition, args, kwargs)


def timeEditorPanel(*args, **kwargs):  # noqa
    """Time Editor - non-linear animation editor.

    timeEditorPanel( editorName , [activeClipEditMode=int], [activeTabRootClipId=boolean],
    [activeTabTime=boolean], [activeTabView=int], [autoFit=string], [autoFitTime=string],
    [control=boolean], [defineTemplate=string], [displayActiveKeyTangents=string],
    [displayActiveKeys=string], [displayInfinities=string], [displayKeys=string],
    [displayTangents=string], [displayValues=string], [docTag=string], [exists=boolean],
    [filter=string], [forceMainConnection=string], [groupIdForTabView=int],
    [highlightConnection=string], [keyingTarget=int], [layerId=int],
    [lockMainConnection=boolean], [lookAt=string], [mainListConnection=string],
    [menu=script], [minClipWidth=int], [panel=string], [parent=string],
    [selectionConnection=string], [setToPrevClipEditMode=boolean], [snapTime=string],
    [snapToClip=boolean], [snapToFrame=boolean], [snapTolerance=int], [snapValue=string],
    [stateString=boolean], [tabView=int], [timeCursor=boolean], [unParent=boolean],
    [unlockMainConnection=boolean], [updateMainConnection=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorPanel.html
    """
    return _wrapCommand(cmds.timeEditorPanel, args, kwargs)


def timeEditorTracks(*args, **kwargs):  # noqa
    """Time Editor tracks commands.

    timeEditorTracks([activeClipWeight=time], [activeClipWeightId=time], [addTrack=int],
    [allClips=boolean], [allTracks=boolean], [allTracksRecursive=boolean],
    [composition=boolean], [path=string], [plugIndex=int], [removeTrack=int],
    [removeTrackByPath=string], [reorderTrack=[int, int]], [resetMute=boolean],
    [resetSolo=boolean], [selectedTracks=boolean], [trackGhost=boolean], [trackIndex=int],
    [trackMuted=boolean], [trackName=string], [trackSolo=boolean], [trackType=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeEditorTracks.html
    """
    return _wrapCommand(cmds.timeEditorTracks, args, kwargs)


def timeField(*args, **kwargs):  # noqa
    """Create a field control that accepts only time values.

    timeField( [string] , [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [editable=boolean], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [enterCommand=script], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [precision=int], [preventOverride=boolean], [receiveFocusCommand=script],
    [statusBarMessage=string], [step=time], [useTemplate=string], [value=time],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeField.html
    """
    return _wrapCommand(cmds.timeField, args, kwargs)


def timeFieldGrp(*args, **kwargs):  # noqa
    """All of the group commands position their individual controls in columns starting at column
    1.

    timeFieldGrp( [groupName] , [adjustableColumn=int], [adjustableColumn2=int],
    [adjustableColumn3=int], [adjustableColumn4=int], [adjustableColumn5=int],
    [adjustableColumn6=int], [annotation=string], [backgroundColor=[float, float, float]],
    [changeCommand=script], [columnAlign=[int, string]], [columnAlign2=[string, string]],
    [columnAlign3=[string, string, string]], [columnAlign4=[string, string, string,
    string]], [columnAlign5=[string, string, string, string, string]],
    [columnAlign6=[string, string, string, string, string, string]], [columnAttach=[int,
    string, int]], [columnAttach2=[string, string]], [columnAttach3=[string, string,
    string]], [columnAttach4=[string, string, string, string]], [columnAttach5=[string,
    string, string, string, string]], [columnAttach6=[string, string, string, string,
    string, string]], [columnOffset2=[int, int]], [columnOffset3=[int, int, int]],
    [columnOffset4=[int, int, int, int]], [columnOffset5=[int, int, int, int, int]],
    [columnOffset6=[int, int, int, int, int, int]], [columnWidth=[int, int]],
    [columnWidth1=int], [columnWidth2=[int, int]], [columnWidth3=[int, int, int]],
    [columnWidth4=[int, int, int, int]], [columnWidth5=[int, int, int, int, int]],
    [columnWidth6=[int, int, int, int, int, int]], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dragCommand=script], [dropCallback=script],
    [enable=boolean], [enable1=boolean], [enable2=boolean], [enable3=boolean],
    [enable4=boolean], [enableBackground=boolean], [enableKeyboardFocus=boolean],
    [exists=boolean], [extraLabel=string], [fullPathName=boolean], [height=int],
    [highlightColor=[float, float, float]], [isObscured=boolean], [label=string],
    [manage=boolean], [noBackground=boolean], [numberOfFields=int],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [precision=int], [preventOverride=boolean], [rowAttach=[int, string, int]],
    [statusBarMessage=string], [step=time], [useTemplate=string], [value=[time, time,
    time, time]], [value1=time], [value2=time], [value3=time], [value4=time],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeFieldGrp.html
    """
    return _wrapCommand(cmds.timeFieldGrp, args, kwargs)


def timePort(*args, **kwargs):  # noqa
    """This command creates a simple time control widget.

    timePort( name , [annotation=string], [backgroundColor=[float, float, float]],
    [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [fullPathName=boolean],
    [globalTime=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [snap=boolean], [statusBarMessage=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timePort.html
    """
    return _wrapCommand(cmds.timePort, args, kwargs)


def timer(*args, **kwargs):  # noqa
    """Allow simple timing of scripts and commands.

    timer([endTimer=boolean], [lapTime=boolean], [name=string], [startTimer=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timer.html
    """
    return _wrapCommand(cmds.timer, args, kwargs)


def timerX(*args, **kwargs):  # noqa
    """Used to calculate elapsed time.

    timerX([startTime=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timerX.html
    """
    return _wrapCommand(cmds.timerX, args, kwargs)


def timeWarp(*args, **kwargs):  # noqa
    """This command is used to create a time warp input to a set of animation curves.

    timeWarp([deleteFrame=int], [frame=float], [g=boolean], [interpType=[int, string]],
    [moveFrame=[int, float]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/timeWarp.html
    """
    return _wrapCommand(cmds.timeWarp, args, kwargs)


def toggle(*args, **kwargs):  # noqa
    """The toggle command is used to toggle the display of various object features for objects
    which have these components.

    toggle( [objects] , [above=boolean], [below=boolean], [boundary=boolean],
    [boundingBox=boolean], [controlVertex=boolean], [doNotWrite=boolean],
    [editPoint=boolean], [extent=boolean], [facet=boolean], [geometry=boolean],
    [gl=boolean], [highPrecisionNurbs=boolean], [hull=boolean], [latticePoint=boolean],
    [latticeShape=boolean], [localAxis=boolean], [newCurve=boolean],
    [newPolymesh=boolean], [newSurface=boolean], [normal=boolean], [origin=boolean],
    [point=boolean], [pointDisplay=boolean], [pointFacet=boolean], [rotatePivot=boolean],
    [scalePivot=boolean], [selectHandle=boolean], [state=boolean], [surfaceFace=boolean],
    [template=boolean], [uvCoords=boolean], [vertex=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toggle.html
    """
    return _wrapCommand(cmds.toggle, args, kwargs)


def toggleAxis(*args, **kwargs):  # noqa
    """Toggles the state of the display axis.

    toggleAxis([origin=boolean], [view=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toggleAxis.html
    """
    return _wrapCommand(cmds.toggleAxis, args, kwargs)


def toggleDisplacement(*args, **kwargs):  # noqa
    """This command toggles the displacement preview of the polygon.

    toggleDisplacement( [objects] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toggleDisplacement.html
    """
    return _wrapCommand(cmds.toggleDisplacement, args, kwargs)


def toggleWindowVisibility(*args, **kwargs):  # noqa
    """Toggle the visibility of a window.

    toggleWindowVisibility( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toggleWindowVisibility.html
    """
    return _wrapCommand(cmds.toggleWindowVisibility, args, kwargs)


def tolerance(*args, **kwargs):  # noqa
    """This command sets tolerances used by modelling operations that require a tolerance, such
    as surface fillet.

    tolerance([angular=angle], [linear=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tolerance.html
    """
    return _wrapCommand(cmds.tolerance, args, kwargs)


def toolBar(*args, **kwargs):  # noqa
    """Create a toolbar.

    toolBar( [name] , [allowedArea=string], [annotation=string], [area=string],
    [backgroundColor=[float, float, float]], [content=string], [defineTemplate=string],
    [docTag=string], [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [isObscured=boolean], [label=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [statusBarMessage=string], [useTemplate=string],
    [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolBar.html
    """
    return _wrapCommand(cmds.toolBar, args, kwargs)


def toolButton(*args, **kwargs):  # noqa
    """This command creates a toolButton that is added to the most recently created tool button
    collection unless the `cl/collection` flag is used.

    toolButton( [string] , [allowMultipleTools=boolean], [annotation=string],
    [backgroundColor=[float, float, float]], [changeCommand=script], [collection=string],
    [defineTemplate=string], [docTag=string], [doubleClickCommand=script],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [exists=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [image1=string], [image2=string], [image3=string], [imageOverlayLabel=string],
    [isObscured=boolean], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [offCommand=script], [onCommand=script],
    [parent=string], [popupIndicatorVisible=boolean], [popupMenuArray=boolean],
    [preventOverride=boolean], [select=boolean], [statusBarMessage=string],
    [style=string], [tool=string], [toolArray=boolean], [toolCount=boolean],
    [toolImage1=[string, string]], [toolImage2=[string, string]], [toolImage3=[string,
    string]], [useTemplate=string], [version=string], [visible=boolean],
    [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolButton.html
    """
    return _wrapCommand(cmds.toolButton, args, kwargs)


def toolCollection(*args, **kwargs):  # noqa
    """This command creates a tool button collection.

    toolCollection( [string] , [collectionItemArray=boolean], [defineTemplate=string],
    [exists=boolean], [gl=boolean], [numberOfCollectionItems=boolean], [parent=string],
    [select=string], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolCollection.html
    """
    return _wrapCommand(cmds.toolCollection, args, kwargs)


def toolDropped(*args, **kwargs):  # noqa
    """This command builds and executes the commands necessary to recreate the specified tool
    button.

    toolDropped( [string] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolDropped.html
    """
    return _wrapCommand(cmds.toolDropped, args, kwargs)


def toolHasOptions(*args, **kwargs):  # noqa
    """This command queries a tool to see if it has options.

    toolHasOptions( string )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolHasOptions.html
    """
    return _wrapCommand(cmds.toolHasOptions, args, kwargs)


def toolPropertyWindow(*args, **kwargs):  # noqa
    """End users should only call this command as 1.

    toolPropertyWindow([field=string], [helpButton=string], [icon=string],
    [inMainWindow=boolean], [location=string], [noviceMode=boolean], [resetButton=string],
    [restore=boolean], [selectCommand=string], [showCommand=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/toolPropertyWindow.html
    """
    return _wrapCommand(cmds.toolPropertyWindow, args, kwargs)


def torus(*args, **kwargs):  # noqa
    """The torus command creates a new torus and/or a dependency node that creates one, and
    returns their names.

    torus([axis=[linear, linear, linear]], [caching=boolean], [constructionHistory=boolean],
    [degree=int], [endSweep=angle], [heightRatio=float], [minorSweep=angle],
    [name=string], [nodeState=int], [object=boolean], [pivot=[linear, linear, linear]],
    [polygon=int], [radius=linear], [sections=int], [spans=int], [startSweep=angle],
    [tolerance=linear], [useTolerance=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/torus.html
    """
    return _wrapCommand(cmds.torus, args, kwargs)


def track(*args, **kwargs):  # noqa
    """The track command translates a camera horizontally or vertically in the world space.

    track( [camera] , [down=linear], [left=linear], [right=linear], [upDistance01=linear],
    [upDistance02=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/track.html
    """
    return _wrapCommand(cmds.track, args, kwargs)


def trackCtx(*args, **kwargs):  # noqa
    """This command can be used to create a track context.

    trackCtx([alternateContext=boolean], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [toolName=string],
    [trackGeometry=boolean], [trackScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/trackCtx.html
    """
    return _wrapCommand(cmds.trackCtx, args, kwargs)


def transferAttributes(*args, **kwargs):  # noqa
    """Samples the attributes of a source surface (first argument) and transfers them onto a
    target surface (second argument).

    transferAttributes( object object , [after=boolean], [afterReference=boolean],
    [before=boolean], [colorBorders=uint], [components=boolean], [deformerTools=boolean],
    [exclusive=string], [flipUVs=uint], [frontOfChain=boolean], [geometry=string],
    [geometryIndices=boolean], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [matchChoice=uint], [name=string],
    [parallel=boolean], [prune=boolean], [remove=boolean], [sampleSpace=uint],
    [searchMethod=uint], [searchScaleX=float], [searchScaleY=float], [searchScaleZ=float],
    [selectedComponents=boolean], [sourceColorSet=string], [sourceUvSet=string],
    [sourceUvSpace=string], [split=boolean], [targetColorSet=string],
    [targetUvSet=string], [targetUvSpace=string], [transferColors=uint],
    [transferNormals=uint], [transferPositions=uint], [transferUVs=uint],
    [useComponentTags=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/transferAttributes.html
    """
    return _wrapCommand(cmds.transferAttributes, args, kwargs)


def transferShadingSets(*args, **kwargs):  # noqa
    """Command to transfer shading set assignments between meshes.

    transferShadingSets([sampleSpace=uint], [searchMethod=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/transferShadingSets.html
    """
    return _wrapCommand(cmds.transferShadingSets, args, kwargs)


def transformCompare(*args, **kwargs):  # noqa
    """Compares two transforms passed as arguments.

    transformCompare( [dagObject dagObject] , [root=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/transformCompare.html
    """
    return _wrapCommand(cmds.transformCompare, args, kwargs)


def transformLimits(*args, **kwargs):  # noqa
    """The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.

    transformLimits( [object] , [enableRotationX=[boolean, boolean]],
    [enableRotationY=[boolean, boolean]], [enableRotationZ=[boolean, boolean]],
    [enableScaleX=[boolean, boolean]], [enableScaleY=[boolean, boolean]],
    [enableScaleZ=[boolean, boolean]], [enableTranslationX=[boolean, boolean]],
    [enableTranslationY=[boolean, boolean]], [enableTranslationZ=[boolean, boolean]],
    [remove=boolean], [rotationX=[angle, angle]], [rotationY=[angle, angle]],
    [rotationZ=[angle, angle]], [scaleX=[float, float]], [scaleY=[float, float]],
    [scaleZ=[float, float]], [translationX=[linear, linear]], [translationY=[linear,
    linear]], [translationZ=[linear, linear]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/transformLimits.html
    """
    return _wrapCommand(cmds.transformLimits, args, kwargs)


def translator(*args, **kwargs):  # noqa
    """Set or query parameters associated with the file translators specified in as the argument.

    translator( [string] , [defaultFileRule=boolean], [defaultOptions=string],
    [extension=boolean], [fileCompression=string], [filter=boolean], [list=boolean],
    [loaded=boolean], [objectType=boolean], [optionsScript=boolean],
    [readSupport=boolean], [writeSupport=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/translator.html
    """
    return _wrapCommand(cmds.translator, args, kwargs)


def treeLister(*args, **kwargs):  # noqa
    """This command creates/edits/queries the tree lister control.

    treeLister( [string] , [addFavorite=string], [addItem=[string, string, script]],
    [addVnnItem=[string, string, string, string]], [annotation=string],
    [backgroundColor=[float, float, float]], [clearContents=boolean],
    [collapsePath=string], [defineTemplate=string], [docTag=string],
    [dragCallback=script], [dropCallback=script], [enable=boolean],
    [enableBackground=boolean], [enableKeyboardFocus=boolean], [executeItem=string],
    [exists=boolean], [expandPath=string], [expandToDepth=int],
    [favoritesCallback=script], [favoritesList=boolean], [fullPathName=boolean],
    [height=int], [highlightColor=[float, float, float]], [isObscured=boolean],
    [itemScript=string], [manage=boolean], [noBackground=boolean],
    [numberOfPopupMenus=boolean], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [refreshCommand=script], [removeFavorite=string],
    [removeItem=string], [resultsPathUnderCursor=boolean], [selectPath=string],
    [statusBarMessage=string], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [vnnString=boolean], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/treeLister.html
    """
    return _wrapCommand(cmds.treeLister, args, kwargs)


def treeView(*args, **kwargs):  # noqa
    """This command creates a custom control.

    treeView( [string] , [addItem=[string, string]], [allowDragAndDrop=boolean],
    [allowHiddenParents=boolean], [allowMultiSelection=boolean],
    [allowReparenting=boolean], [annotation=string], [attachButtonRight=int],
    [backgroundColor=[float, float, float]], [borderHighlite=[string, boolean]],
    [borderHighliteColor=[string, float, float, float]], [buttonErase=[string, boolean]],
    [buttonState=[string, int, string]], [buttonStyle=[string, int, string]],
    [buttonTextIcon=[string, int, string]], [buttonTooltip=[string, int, string]],
    [buttonTransparencyColor=[string, int, float, float, float]],
    [buttonTransparencyOverride=[string, int, boolean]], [buttonVisible=[string, int,
    boolean]], [children=string], [clearSelection=boolean], [contextMenuCommand=script],
    [defineTemplate=string], [displayLabel=[string, string]], [displayLabelSuffix=[string,
    string]], [docTag=string], [dragAndDropCommand=script], [dragCallback=script],
    [dropCallback=script], [editLabelCommand=script], [enable=boolean],
    [enableBackground=boolean], [enableButton=[string, int, int]],
    [enableKeyboardFocus=boolean], [enableKeys=boolean], [enableLabel=[string, int]],
    [exists=boolean], [expandCollapseCommand=script], [expandItem=[string, boolean]],
    [flatButton=int], [font=[string, string]], [fontFace=[string, int]],
    [fullPathName=boolean], [height=int], [hideButtons=boolean], [highlightColor=[float,
    float, float]], [highlite=[string, boolean]], [highliteColor=[string, float, float,
    float]], [ignoreButtonClick=[string, int, int]], [image=[string, int, string]],
    [insertItem=[string, string, int]], [isItemExpanded=string], [isLeaf=string],
    [isObscured=boolean], [item=string], [itemAnnotation=[string, string]],
    [itemDblClickCommand=script], [itemDblClickCommand2=script], [itemExists=string],
    [itemIndex=string], [itemParent=string], [itemRenamedCommand=script],
    [itemSelected=string], [itemVisible=[string, boolean]], [labelBackgroundColor=[string,
    float, float, float]], [manage=boolean], [noBackground=boolean],
    [numberOfButtons=int], [numberOfPopupMenus=boolean], [ornament=[string, int, int,
    int]], [ornamentColor=[string, float, float, float]], [parent=string],
    [popupMenuArray=boolean], [pressCommand=[int, script]], [preventOverride=boolean],
    [removeAll=boolean], [removeItem=string], [reverseTreeOrder=boolean],
    [rightPressCommand=[int, script]], [select=[string, int]], [selectCommand=script],
    [selectItem=[string, boolean]], [selectionChangedCommand=script],
    [selectionColor=[string, float, float, float]], [showItem=string],
    [statusBarMessage=string], [textColor=[string, float, float, float]],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/treeView.html
    """
    return _wrapCommand(cmds.treeView, args, kwargs)


def trim(*args, **kwargs):  # noqa
    """This command trims a surface to its curves on surface by first splitting the surface and
    then selecting which regions to keep or discard.

    trim( objects , [caching=boolean], [constructionHistory=boolean], [locatorU=float],
    [locatorV=float], [name=string], [nodeState=int], [object=boolean], [selected=int],
    [shrink=boolean], [tolerance=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/trim.html
    """
    return _wrapCommand(cmds.trim, args, kwargs)


def truncateFluidCache(*args, **kwargs):  # noqa
    """This command sets the end time of a fluid cache to the current time.

    truncateFluidCache()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/truncateFluidCache.html
    """
    return _wrapCommand(cmds.truncateFluidCache, args, kwargs)


def truncateHairCache(*args, **kwargs):  # noqa
    """This command sets the end time of a hair cache to the current time.

    truncateHairCache()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/truncateHairCache.html
    """
    return _wrapCommand(cmds.truncateHairCache, args, kwargs)


def tumble(*args, **kwargs):  # noqa
    """The tumble command revolves the camera(s) by varying the azimuth and elevation angles in
    the perspective window.

    tumble( [camera] , [azimuthAngle=angle], [elevationAngle=angle], [localTumble=int],
    [pivotPoint=[linear, linear, linear]], [rotationAngles=[angle, angle]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tumble.html
    """
    return _wrapCommand(cmds.tumble, args, kwargs)


def tumbleCtx(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a tumble context.

    tumbleCtx([alternateContext=boolean], [autoOrthoConstrain=boolean],
    [autoSetPivot=boolean], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [localTumble=int], [name=string],
    [objectTumble=boolean], [orthoLock=boolean], [orthoStep=angle], [toolName=string],
    [tumbleScale=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/tumbleCtx.html
    """
    return _wrapCommand(cmds.tumbleCtx, args, kwargs)


def turbulence(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    turbulence( selectionList , [attenuation=float], [frequency=float], [magnitude=float],
    [maxDistance=linear], [name=string], [noiseLevel=int], [noiseRatio=float],
    [perVertex=boolean], [phase=float], [phaseX=float], [phaseY=float], [phaseZ=float],
    [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]],
    [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/turbulence.html
    """
    return _wrapCommand(cmds.turbulence, args, kwargs)


def twoPointArcCtx(*args, **kwargs):  # noqa
    """The twoPointArcCtx command creates a new context for creating two point circular arcs.

    twoPointArcCtx([degree=uint], [exists=boolean], [history=boolean], [image1=string],
    [image2=string], [image3=string], [name=string], [spans=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/twoPointArcCtx.html
    """
    return _wrapCommand(cmds.twoPointArcCtx, args, kwargs)


def ubercam(*args, **kwargs):  # noqa
    """Use this command to create a "ubercam" with equivalent behavior to all cameras used by
    shots in the sequencer.

    ubercam([string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ubercam.html
    """
    return _wrapCommand(cmds.ubercam, args, kwargs)


def uiTemplate(*args, **kwargs):  # noqa
    """This command creates a new command template object.

    uiTemplate( [string] , [defineTemplate=string], [exists=boolean], [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/uiTemplate.html
    """
    return _wrapCommand(cmds.uiTemplate, args, kwargs)


def unassignInputDevice(*args, **kwargs):  # noqa
    """This command deletes all command strings associated with this device.

    unassignInputDevice([clutch=string], [device=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/unassignInputDevice.html
    """
    return _wrapCommand(cmds.unassignInputDevice, args, kwargs)


def undo(*args, **kwargs):  # noqa
    """Takes the most recent command from the undo list and undoes it.

    undo()

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/undo.html
    """
    return _wrapCommand(cmds.undo, args, kwargs)


def undoInfo(*args, **kwargs):  # noqa
    """This command controls the undo/redo parameters.

    undoInfo([chunkName=string], [closeChunk=boolean], [infinity=boolean], [length=uint],
    [openChunk=boolean], [printQueue=boolean], [printRedoQueue=boolean],
    [redoName=string], [redoQueueEmpty=boolean], [state=boolean],
    [stateWithoutFlush=boolean], [undoName=string], [undoQueueEmpty=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/undoInfo.html
    """
    return _wrapCommand(cmds.undoInfo, args, kwargs)


def unfold(*args, **kwargs):  # noqa
    """None.

    unfold([applyToShell=boolean], [areaWeight=float], [globalBlend=float],
    [globalMethodBlend=float], [iterations=int], [optimizeAxis=int],
    [pinSelected=boolean], [pinUvBorder=boolean], [scale=float],
    [stoppingThreshold=float], [useScale=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/unfold.html
    """
    return _wrapCommand(cmds.unfold, args, kwargs)


def ungroup(*args, **kwargs):  # noqa
    """This command ungroups the specified objects.

    ungroup( [objects...] , [absolute=boolean], [parent=string], [relative=boolean],
    [world=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/ungroup.html
    """
    return _wrapCommand(cmds.ungroup, args, kwargs)


def uniform(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    uniform( selectionList , [attenuation=float], [directionX=float], [directionY=float],
    [directionZ=float], [magnitude=float], [maxDistance=linear], [name=string],
    [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]],
    [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/uniform.html
    """
    return _wrapCommand(cmds.uniform, args, kwargs)


def unknownNode(*args, **kwargs):  # noqa
    """Allows querying of the data stored for unknown nodes (nodes that are defined by a plug-in
    that Maya could not load when loading a scene file).

    unknownNode([plugin=boolean], [realClassName=boolean], [realClassTag=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/unknownNode.html
    """
    return _wrapCommand(cmds.unknownNode, args, kwargs)


def unknownPlugin(*args, **kwargs):  # noqa
    """Allows querying of the unknown plug-ins used by the scene, and provides a means to remove
    them.

    unknownPlugin([dataTypes=boolean], [list=boolean], [nodeTypes=boolean], [remove=boolean],
    [version=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/unknownPlugin.html
    """
    return _wrapCommand(cmds.unknownPlugin, args, kwargs)


def unloadPlugin(*args, **kwargs):  # noqa
    """Unload plug-ins from Maya.

    unloadPlugin( string [string...] , [addCallback=script], [force=boolean],
    [removeCallback=script])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/unloadPlugin.html
    """
    return _wrapCommand(cmds.unloadPlugin, args, kwargs)


def untangleUV(*args, **kwargs):  # noqa
    """This command will aid in the creation of non-overlapping regions (i.

    untangleUV([mapBorder=string], [maxRelaxIterations=int], [pinBorder=boolean],
    [pinSelected=boolean], [pinUnselected=boolean], [relax=string],
    [relaxTolerance=float], [shapeDetail=float])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/untangleUV.html
    """
    return _wrapCommand(cmds.untangleUV, args, kwargs)


def untrim(*args, **kwargs):  # noqa
    """Untrim the surface.

    untrim( surface , [caching=boolean], [constructionHistory=boolean],
    [curveOnSurface=boolean], [name=string], [noChanges=boolean], [nodeState=int],
    [object=boolean], [replaceOriginal=boolean], [untrimAll=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/untrim.html
    """
    return _wrapCommand(cmds.untrim, args, kwargs)


def upAxis(*args, **kwargs):  # noqa
    """The upAxis command changes the world up direction.

    upAxis([axis=string], [rotateView=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/upAxis.html
    """
    return _wrapCommand(cmds.upAxis, args, kwargs)


def uvLink(*args, **kwargs):  # noqa
    """This command is used to make, break and query UV linking relationships between UV sets on
    objects and textures that use those UV sets.

    uvLink( [objects] , [b=boolean], [isValid=boolean], [make=boolean], [queryObject=name],
    [texture=name], [uvSet=name])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/uvLink.html
    """
    return _wrapCommand(cmds.uvLink, args, kwargs)


def uvSnapshot(*args, **kwargs):  # noqa
    """Builds an image containg the UVs of the selected objects.

    uvSnapshot([antiAliased=boolean], [blueColor=int], [entireUVRange=boolean],
    [fileFormat=string], [greenColor=int], [name=string], [overwrite=boolean],
    [redColor=int], [uMax=float], [uMin=float], [uvSetName=string], [vMax=float],
    [vMin=float], [xResolution=int], [yResolution=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/uvSnapshot.html
    """
    return _wrapCommand(cmds.uvSnapshot, args, kwargs)


def vectorize(*args, **kwargs):  # noqa
    """This command renders Maya scenes to various vector and raster formats using the Maya
    Vector renderer.

    vectorize([browserView=boolean], [byFrame=float], [camera=string],
    [combineFillsEdges=boolean], [currentFrame=boolean], [curveTolerance=float],
    [customExtension=string], [detailLevel=int], [edgeColor=[int, int, int]],
    [edgeDetail=boolean], [edgeStyle=string], [edgeWeight=float], [endFrame=float],
    [filenameFormat=string], [fillStyle=string], [flashVersion=int], [frameRate=int],
    [height=int], [hiddenEdges=boolean], [highlightLevel=int], [highlights=boolean],
    [imageFormat=string], [layer=name], [minEdgeAngle=float],
    [outlinesAtIntersections=boolean], [outputFileName=string], [pixelAspectRatio=float],
    [reflectionDepth=int], [reflections=boolean], [renderLayers=boolean],
    [renderOptimization=string], [renderView=boolean], [secondaryCurveFitting=boolean],
    [shadows=boolean], [showBackFaces=boolean], [startFrame=float], [svgAnimation=string],
    [svgCompression=boolean], [width=int])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/vectorize.html
    """
    return _wrapCommand(cmds.vectorize, args, kwargs)


def view2dToolCtx(*args, **kwargs):  # noqa
    """This class creates a context for the View Tools "track", "dolly", and "box zoom" in the
    Hypergraph.

    view2dToolCtx([alternateContext=boolean], [boxzoom=boolean], [dolly=boolean],
    [exists=boolean], [history=boolean], [image1=string], [image2=string],
    [image3=string], [name=string], [toolName=string], [track=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/view2dToolCtx.html
    """
    return _wrapCommand(cmds.view2dToolCtx, args, kwargs)


def viewCamera(*args, **kwargs):  # noqa
    """The viewCamera command is used to position a camera to look directly at the side or top of
    another camera.

    viewCamera( [camera] , [move=name], [sideView=boolean], [topView=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewCamera.html
    """
    return _wrapCommand(cmds.viewCamera, args, kwargs)


def viewClipPlane(*args, **kwargs):  # noqa
    """The viewClipPlane command can be used to query or set a camera's clip planes.

    viewClipPlane( [camera] , [autoClipPlane=boolean], [farClipPlane=linear],
    [nearClipPlane=linear], [surfacesOnly=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewClipPlane.html
    """
    return _wrapCommand(cmds.viewClipPlane, args, kwargs)


def viewFit(*args, **kwargs):  # noqa
    """The viewFit command positions the specified camera so its point-of-view contains all
    selected objects other than itself.

    viewFit( [camera...] , [allObjects=boolean], [animate=boolean], [center=boolean],
    [fitFactor=float], [namespace=string], [noChildren=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewFit.html
    """
    return _wrapCommand(cmds.viewFit, args, kwargs)


def viewHeadOn(*args, **kwargs):  # noqa
    """The viewHeadOn command positions the specified camera so it is looking "down" the normal
    of the live object, and fitted to the live object.

    viewHeadOn( [camera] )

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewHeadOn.html
    """
    return _wrapCommand(cmds.viewHeadOn, args, kwargs)


def viewLookAt(*args, **kwargs):  # noqa
    """The viewLookAt command positions the specified camera so it is looking at the centroid of
    all selected objects.

    viewLookAt( [camera] , [position=[linear, linear, linear]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewLookAt.html
    """
    return _wrapCommand(cmds.viewLookAt, args, kwargs)


def viewManip(*args, **kwargs):  # noqa
    """Mel access to the view cube manipulator.

    viewManip([bottomLeft=boolean], [bottomRight=boolean], [compassAngle=float],
    [dragSnap=boolean], [drawCompass=boolean], [fitToView=boolean],
    [frontParameters=string], [goDefault=boolean], [goHome=boolean],
    [homeParameters=string], [levelCamera=boolean], [minOpacity=float],
    [namespace=string], [postCommand=string], [preCommand=string],
    [preserveSceneUp=boolean], [resetFront=boolean], [resetHome=boolean],
    [restoreCenter=boolean], [selectionLockParameters=string], [setFront=boolean],
    [setHome=boolean], [size=string], [toggleSelectionLock=boolean], [topLeft=boolean],
    [topRight=boolean], [visible=boolean], [zoomToFitScene=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewManip.html
    """
    return _wrapCommand(cmds.viewManip, args, kwargs)


def viewPlace(*args, **kwargs):  # noqa
    """This command positions the camera as specified.

    viewPlace( [camera] , [animate=boolean], [eyePoint=[linear, linear, linear]],
    [fieldOfView=angle], [lookAt=[linear, linear, linear]], [ortho=boolean],
    [perspective=boolean], [upDirection=[linear, linear, linear]], [viewDirection=[linear,
    linear, linear]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewPlace.html
    """
    return _wrapCommand(cmds.viewPlace, args, kwargs)


def viewSet(*args, **kwargs):  # noqa
    """This command positions the camera to one of the pre-defined positions.

    viewSet( [camera] , [animate=boolean], [back=boolean], [bottom=boolean], [fit=boolean],
    [fitFactor=float], [front=boolean], [home=boolean], [keepRenderSettings=boolean],
    [leftSide=boolean], [namespace=string], [nextView=boolean], [persp=boolean],
    [previousView=boolean], [rightSide=boolean], [side=boolean], [top=boolean],
    [viewNegativeX=boolean], [viewNegativeY=boolean], [viewNegativeZ=boolean],
    [viewX=boolean], [viewY=boolean], [viewZ=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/viewSet.html
    """
    return _wrapCommand(cmds.viewSet, args, kwargs)


def visor(*args, **kwargs):  # noqa
    """Command for the creation and manipulation of a Visor UI element.

    visor([addFolder=boolean], [addNodes=string], [allowPanningInX=boolean],
    [allowPanningInY=boolean], [allowZooming=boolean], [command=string],
    [deleteFolder=string], [editFolder=string], [folderList=string], [menu=string],
    [name=string], [nodeType=string], [openDirectories=boolean], [openFolder=boolean],
    [parent=string], [path=string], [popupMenuScript=string], [rebuild=boolean],
    [refreshAllSwatches=boolean], [refreshSelectedSwatches=boolean],
    [refreshSwatch=string], [reset=boolean], [restrictPanAndZoom=boolean],
    [saveSwatches=boolean], [scrollBar=string], [scrollPercent=float],
    [selectedGadgets=string], [showDividers=boolean], [showFiles=boolean],
    [showFolders=boolean], [showNodes=boolean], [stateString=boolean], [style=string],
    [transform=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/visor.html
    """
    return _wrapCommand(cmds.visor, args, kwargs)


def volumeAxis(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    volumeAxis( selectionList , [alongAxis=float], [aroundAxis=float], [attenuation=float],
    [awayFromAxis=float], [awayFromCenter=float], [detailTurbulence=float],
    [directionX=float], [directionY=float], [directionZ=float], [directionalSpeed=float],
    [invertAttenuation=boolean], [magnitude=float], [maxDistance=linear], [name=string],
    [perVertex=boolean], [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [turbulence=float], [turbulenceFrequencyX=float], [turbulenceFrequencyY=float],
    [turbulenceFrequencyZ=float], [turbulenceOffsetX=float], [turbulenceOffsetY=float],
    [turbulenceOffsetZ=float], [turbulenceSpeed=float], [volumeExclusion=boolean],
    [volumeOffset=[linear, linear, linear]], [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/volumeAxis.html
    """
    return _wrapCommand(cmds.volumeAxis, args, kwargs)


def volumeBind(*args, **kwargs):  # noqa
    """Command for creating and editing volume binding nodes.

    volumeBind( objects , [influence=string], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/volumeBind.html
    """
    return _wrapCommand(cmds.volumeBind, args, kwargs)


def vortex(*args, **kwargs):  # noqa
    """For each listed object, the command creates a new field.

    vortex( selectionList , [attenuation=float], [axisX=float], [axisY=float], [axisZ=float],
    [magnitude=float], [maxDistance=linear], [name=string], [perVertex=boolean],
    [position=[linear, linear, linear]], [torusSectionRadius=linear],
    [volumeExclusion=boolean], [volumeOffset=[linear, linear, linear]],
    [volumeShape=string], [volumeSweep=angle])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/vortex.html
    """
    return _wrapCommand(cmds.vortex, args, kwargs)


def waitCursor(*args, **kwargs):  # noqa
    """This command sets/resets a wait cursor for the entire Maya application.

    waitCursor([state=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/waitCursor.html
    """
    return _wrapCommand(cmds.waitCursor, args, kwargs)


def walkCtx(*args, **kwargs):  # noqa
    """This command can be used to create, edit, or query a walk context.

    walkCtx([alternateContext=boolean], [crouchCount=float], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string],
    [toolName=string], [walkHeight=float], [walkSensitivity=float], [walkSpeed=float],
    [walkToolHud=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/walkCtx.html
    """
    return _wrapCommand(cmds.walkCtx, args, kwargs)


def warning(*args, **kwargs):  # noqa
    """The warning command is provided so that the user can issue warning messages from his/her
    scripts.

    warning([noContext=boolean], [showLineNumber=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/warning.html
    """
    return _wrapCommand(cmds.warning, args, kwargs)


def webBrowser(*args, **kwargs):  # noqa
    """This command is obsolete and will be removed in next version of Maya.

    webBrowser( [string] , [annotation=string], [back=boolean], [backgroundColor=[float,
    float, float]], [defineTemplate=string], [docTag=string], [dragCallback=script],
    [dropCallback=script], [enable=boolean], [enableBackground=boolean],
    [enableKeyboardFocus=boolean], [exists=boolean], [find=string], [forward=boolean],
    [fullPathName=boolean], [height=int], [highlightColor=[float, float, float]],
    [home=boolean], [isObscured=boolean], [manage=boolean], [matchCase=boolean],
    [matchWholeWorld=boolean], [noBackground=boolean], [numberOfPopupMenus=boolean],
    [openURL=string], [parent=string], [popupMenuArray=boolean],
    [preventOverride=boolean], [reload=boolean], [searchForward=boolean],
    [statusBarMessage=string], [stop=boolean], [urlChangedCb=string],
    [useTemplate=string], [visible=boolean], [visibleChangeCommand=script], [width=int],
    [wrap=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/webBrowser.html
    """
    return _wrapCommand(cmds.webBrowser, args, kwargs)


def weightsColor(*args, **kwargs):  # noqa
    """Controls the coloring of deformer weights.

    weightsColor( [objects...] , [colorRamp=string], [deformer=string], [falseColor=boolean],
    [outOfRangeColor=[float, float, float]], [rampMaxColor=[float, float, float]],
    [rampMinColor=[float, float, float]], [useColorRamp=boolean],
    [useMaxMinColor=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/weightsColor.html
    """
    return _wrapCommand(cmds.weightsColor, args, kwargs)


def whatsNewHighlight(*args, **kwargs):  # noqa
    """This command is used to toggle the What's New highlighting feature, and the display of the
    settings dialog for the feature that appears on startup.

    whatsNewHighlight([highlightColor=[float, float, float]], [highlightOn=boolean],
    [showStartupDialog=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/whatsNewHighlight.html
    """
    return _wrapCommand(cmds.whatsNewHighlight, args, kwargs)


def window(*args, **kwargs):  # noqa
    """This command creates a new window but leaves it invisible.

    window( [string] , [backgroundColor=[float, float, float]], [closeCommand=script],
    [defineTemplate=string], [docTag=string], [dockCorner=[string, string]],
    [dockStation=boolean], [dockingLayout=string], [exists=boolean],
    [frontWindow=boolean], [height=int], [iconName=string], [iconify=boolean],
    [interactivePlacement=boolean], [leftEdge=int], [mainMenuBar=boolean],
    [mainWindow=boolean], [maximizeButton=boolean], [menuArray=boolean],
    [menuBar=boolean], [menuBarCornerWidget=[string, string]], [menuBarResize=boolean],
    [menuBarVisible=boolean], [menuIndex=[string, uint]], [minimizeButton=boolean],
    [minimizeCommand=script], [nestedDockingEnabled=boolean], [numberOfMenus=boolean],
    [parent=string], [resizeToFitChildren=boolean], [restoreCommand=script],
    [retain=boolean], [sizeable=boolean], [state=string], [title=string],
    [titleBar=boolean], [titleBarMenu=boolean], [toolbox=boolean], [topEdge=int],
    [topLeftCorner=[int, int]], [useTemplate=string], [visible=boolean], [width=int],
    [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/window.html
    """
    return _wrapCommand(cmds.window, args, kwargs)


def windowPref(*args, **kwargs):  # noqa
    """Create or modify preferred window attributes.

    windowPref( string , [enableAll=boolean], [exists=boolean], [height=int], [leftEdge=int],
    [loadAll=boolean], [maximized=boolean], [parentMain=boolean], [remove=boolean],
    [removeAll=boolean], [restoreMainWindowState=string], [saveAll=boolean],
    [saveMainWindowState=string], [topEdge=int], [topLeftCorner=[int, int]], [width=int],
    [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/windowPref.html
    """
    return _wrapCommand(cmds.windowPref, args, kwargs)


def wire(*args, **kwargs):  # noqa
    """This command creates a wire deformer.

    wire( [objects] , [after=boolean], [afterReference=boolean], [before=boolean],
    [components=boolean], [crossingEffect=float], [deformerTools=boolean],
    [dropoffDistance=[uint, linear]], [envelope=float], [exclusive=string],
    [frontOfChain=boolean], [geometry=string], [geometryIndices=boolean],
    [groupWithBase=boolean], [holder=[uint, string]], [ignoreSelected=boolean],
    [includeHiddenSelections=boolean], [localInfluence=float], [name=string],
    [parallel=boolean], [prune=boolean], [remove=boolean], [selectedComponents=boolean],
    [split=boolean], [useComponentTags=boolean], [wire=string], [wireCount=uint])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/wire.html
    """
    return _wrapCommand(cmds.wire, args, kwargs)


def wireContext(*args, **kwargs):  # noqa
    """This command creates a tool that can be used to create a wire deformer.

    wireContext( string , [crossingEffect=linear], [deformationOrder=string],
    [dropoffDistance=linear], [envelope=linear], [exclusive=boolean],
    [exclusivePartition=string], [exists=boolean], [groupWithBase=boolean],
    [history=boolean], [holder=boolean], [image1=string], [image2=string],
    [image3=string], [localInfluence=linear], [name=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/wireContext.html
    """
    return _wrapCommand(cmds.wireContext, args, kwargs)


def workspace(*args, **kwargs):  # noqa
    """Create, open, or edit a workspace associated with a given workspace file.

    workspace( [string] , [active=boolean], [baseWorkspace=string], [create=string],
    [directory=string], [expandName=string], [fileRule=[string, string]],
    [fileRuleEntry=string], [fileRuleList=boolean], [filter=boolean], [fullName=boolean],
    [list=boolean], [listFullWorkspaces=boolean], [listWorkspaces=boolean],
    [newWorkspace=boolean], [objectType=[string, string]], [objectTypeEntry=string],
    [objectTypeList=boolean], [openWorkspace=boolean], [projectPath=string],
    [removeFileRuleEntry=string], [removeVariableEntry=string], [renderType=[string,
    string]], [renderTypeEntry=string], [renderTypeList=boolean], [rootDirectory=boolean],
    [saveWorkspace=boolean], [shortName=boolean], [update=boolean], [updateAll=boolean],
    [variable=[string, string]], [variableEntry=string], [variableList=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/workspace.html
    """
    return _wrapCommand(cmds.workspace, args, kwargs)


def workspaceControl(*args, **kwargs):  # noqa
    """Creates and manages the widget used to host windows in a layout that enables docking and
    stacking windows together.

    workspaceControl( [name] , [actLikeMayaUIElement=boolean], [checksPlugins=boolean],
    [close=boolean], [closeCommand=script], [collapse=boolean], [defineTemplate=string],
    [dockToControl=[string, string]], [dockToMainWindow=[string, boolean]],
    [dockToPanel=[string, string, boolean]], [duplicatable=boolean], [exists=boolean],
    [floating=boolean], [height=boolean], [heightProperty=string], [horizontal=boolean],
    [initCallback=string], [initialHeight=int], [initialWidth=int], [label=string],
    [layoutDirectionCallback=string], [loadImmediately=boolean], [minimumHeight=int],
    [minimumWidth=int], [r=boolean], [requiredControl=string], [requiredPlugin=string],
    [resizeHeight=int], [resizeWidth=int], [restore=boolean], [retain=boolean],
    [stateString=string], [tabPosition=[string, boolean]], [tabToControl=[string, int]],
    [uiScript=script], [useTemplate=string], [visible=boolean],
    [visibleChangeCommand=script], [width=boolean], [widthProperty=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/workspaceControl.html
    """
    return _wrapCommand(cmds.workspaceControl, args, kwargs)


def workspaceControlState(*args, **kwargs):  # noqa
    """Create or modify preferred window attributes for workspace controls.

    workspaceControlState( string , [defaultTopLeftCorner=[int, int]],
    [defaultWidthHeight=[int, int]], [exists=boolean], [height=int], [leftEdge=int],
    [maximized=boolean], [remove=boolean], [topEdge=int], [topLeftCorner=[int, int]],
    [width=int], [widthHeight=[int, int]])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/workspaceControlState.html
    """
    return _wrapCommand(cmds.workspaceControlState, args, kwargs)


def workspaceLayoutManager(*args, **kwargs):  # noqa
    """The Workspace Layout Manager loads and saves the layout of the various toolbars and
    windows in the user interface.

    workspaceLayoutManager( [name] , [collapseMainWindowControls=[string, boolean]],
    [current=boolean], [delete=string], [i=string], [listLayouts=boolean],
    [listModuleLayouts=boolean], [listUserLayouts=boolean], [modified=string],
    [parentWorkspaceControl=string], [reset=boolean], [restoreMainWindowControls=boolean],
    [save=boolean], [saveAs=string], [setCurrent=string], [setCurrentCallback=string],
    [setModifiedCallback=string], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/workspaceLayoutManager.html
    """
    return _wrapCommand(cmds.workspaceLayoutManager, args, kwargs)


def workspacePanel(*args, **kwargs):  # noqa
    """Workspace panel.

    workspacePanel([defineTemplate=string], [exists=boolean], [mainWindow=boolean],
    [useTemplate=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/workspacePanel.html
    """
    return _wrapCommand(cmds.workspacePanel, args, kwargs)


def wrinkle(*args, **kwargs):  # noqa
    """The wrinkle command is used to create a network of wrinkles on a surface.

    wrinkle( objects , [axis=[linear, linear, linear]], [branchCount=uint],
    [branchDepth=uint], [center=[linear, linear, linear]], [crease=string],
    [dropoffDistance=linear], [envelope=linear], [randomness=linear], [style=string],
    [thickness=linear], [uvSpace=[linear, linear, linear, linear, linear]],
    [wrinkleCount=uint], [wrinkleIntensity=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/wrinkle.html
    """
    return _wrapCommand(cmds.wrinkle, args, kwargs)


def wrinkleContext(*args, **kwargs):  # noqa
    """This command creates a context that creates wrinkles.

    wrinkleContext( string , [branchCount=uint], [branchDepth=uint], [exists=boolean],
    [history=boolean], [image1=string], [image2=string], [image3=string], [name=string],
    [randomness=linear], [style=string], [thickness=linear], [wrinkleCount=uint],
    [wrinkleIntensity=linear])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/wrinkleContext.html
    """
    return _wrapCommand(cmds.wrinkleContext, args, kwargs)


def writeTake(*args, **kwargs):  # noqa
    """This action writes a take from a device with recorded data to a take (.

    writeTake([angle=string], [device=string], [linear=string], [noTime=boolean],
    [precision=int], [take=string], [virtualDevice=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/writeTake.html
    """
    return _wrapCommand(cmds.writeTake, args, kwargs)


def xform(*args, **kwargs):  # noqa
    """This command can be used query/set any element in a transformation node.

    xform( [objects...] , [absolute=boolean], [boundingBox=boolean],
    [boundingBoxInvisible=boolean], [centerPivots=boolean],
    [centerPivotsOnComponents=boolean], [deletePriorHistory=boolean], [euler=boolean],
    [matrix=[float, float, float, float, float, float, float, float, float, float, float,
    float, float, float, float, float]], [objectSpace=boolean], [pivots=[linear, linear,
    linear]], [preserve=boolean], [preserveUV=boolean], [reflection=boolean],
    [reflectionAboutBBox=boolean], [reflectionAboutOrigin=boolean],
    [reflectionAboutX=boolean], [reflectionAboutY=boolean], [reflectionAboutZ=boolean],
    [reflectionTolerance=float], [relative=boolean], [rotateAxis=[angle, angle, angle]],
    [rotateOrder=string], [rotatePivot=[linear, linear, linear]],
    [rotateTranslation=[linear, linear, linear]], [rotation=[angle, angle, angle]],
    [scale=[float, float, float]], [scalePivot=[linear, linear, linear]],
    [scaleTranslation=[linear, linear, linear]], [shear=[float, float, float]],
    [translation=[linear, linear, linear]], [worldSpace=boolean],
    [worldSpaceDistance=boolean], [zeroTransformPivots=boolean])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/xform.html
    """
    return _wrapCommand(cmds.xform, args, kwargs)


def xformConstraint(*args, **kwargs):  # noqa
    """This command allows you to change the transform constraint used by the transform tools
    during component transforms.

    xformConstraint([alongNormal=int], [live=boolean], [type=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/xformConstraint.html
    """
    return _wrapCommand(cmds.xformConstraint, args, kwargs)


def xpmPicker(*args, **kwargs):  # noqa
    """Open a dialog and ask you to choose a xpm file.

    xpmPicker([fileName=string], [parent=string])

    http://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/xpmPicker.html
    """
    return _wrapCommand(cmds.xpmPicker, args, kwargs)
