//
// Copyright 2016 Pixar
//
// Licensed under the Apache License, Version 2.0 (the "Apache License")
// with the following modification; you may not use this file except in
// compliance with the Apache License and the following modification to it:
// Section 6. Trademarks. is deleted and replaced with:
//
// 6. Trademarks. This License does not grant permission to use the trade
//    names, trademarks, service marks, or product names of the Licensor
//    and its affiliates, except as required to comply with Section 4(c) of
//    the License and to reproduce the content of the NOTICE file.
//
// You may obtain a copy of the Apache License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the Apache License with the above modification is
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied. See the Apache License for the specific
// language governing permissions and limitations under the Apache License.
//
#ifndef USDARNOLD_GENERATED_ARNOLDPERSPCAMERA_H
#define USDARNOLD_GENERATED_ARNOLDPERSPCAMERA_H

/// \file usdArnold/arnoldPerspCamera.h

#include "pxr/pxr.h"
#include ".//api.h"
#include ".//arnoldCamera.h"
#include "pxr/usd/usd/prim.h"
#include "pxr/usd/usd/stage.h"
#include ".//tokens.h"

#include "pxr/base/vt/value.h"

#include "pxr/base/gf/vec3d.h"
#include "pxr/base/gf/vec3f.h"
#include "pxr/base/gf/matrix4d.h"

#include "pxr/base/tf/token.h"
#include "pxr/base/tf/type.h"

PXR_NAMESPACE_OPEN_SCOPE

class SdfAssetPath;

// -------------------------------------------------------------------------- //
// ARNOLDPERSPCAMERA                                                          //
// -------------------------------------------------------------------------- //

/// \class UsdArnoldPerspCamera
///
/// For any described attribute \em Fallback \em Value or \em Allowed \em Values below
/// that are text/tokens, the actual token is published and defined in \ref UsdArnoldTokens.
/// So to set an attribute to the value "rightHanded", use UsdArnoldTokens->rightHanded
/// as the value.
///
class UsdArnoldPerspCamera : public UsdArnoldCamera
{
public:
    /// Compile time constant representing what kind of schema this class is.
    ///
    /// \sa UsdSchemaType
    static const UsdSchemaType schemaType = UsdSchemaType::ConcreteTyped;

    /// Construct a UsdArnoldPerspCamera on UsdPrim \p prim .
    /// Equivalent to UsdArnoldPerspCamera::Get(prim.GetStage(), prim.GetPath())
    /// for a \em valid \p prim, but will not immediately throw an error for
    /// an invalid \p prim
    explicit UsdArnoldPerspCamera(const UsdPrim& prim=UsdPrim())
        : UsdArnoldCamera(prim)
    {
    }

    /// Construct a UsdArnoldPerspCamera on the prim held by \p schemaObj .
    /// Should be preferred over UsdArnoldPerspCamera(schemaObj.GetPrim()),
    /// as it preserves SchemaBase state.
    explicit UsdArnoldPerspCamera(const UsdSchemaBase& schemaObj)
        : UsdArnoldCamera(schemaObj)
    {
    }

    /// Destructor.
    USDARNOLD_API
    virtual ~UsdArnoldPerspCamera();

    /// Return a vector of names of all pre-declared attributes for this schema
    /// class and all its ancestor classes.  Does not include attributes that
    /// may be authored by custom/extended methods of the schemas involved.
    USDARNOLD_API
    static const TfTokenVector &
    GetSchemaAttributeNames(bool includeInherited=true);

    /// Return a UsdArnoldPerspCamera holding the prim adhering to this
    /// schema at \p path on \p stage.  If no prim exists at \p path on
    /// \p stage, or if the prim at that path does not adhere to this schema,
    /// return an invalid schema object.  This is shorthand for the following:
    ///
    /// \code
    /// UsdArnoldPerspCamera(stage->GetPrimAtPath(path));
    /// \endcode
    ///
    USDARNOLD_API
    static UsdArnoldPerspCamera
    Get(const UsdStagePtr &stage, const SdfPath &path);

    /// Attempt to ensure a \a UsdPrim adhering to this schema at \p path
    /// is defined (according to UsdPrim::IsDefined()) on this stage.
    ///
    /// If a prim adhering to this schema at \p path is already defined on this
    /// stage, return that prim.  Otherwise author an \a SdfPrimSpec with
    /// \a specifier == \a SdfSpecifierDef and this schema's prim type name for
    /// the prim at \p path at the current EditTarget.  Author \a SdfPrimSpec s
    /// with \p specifier == \a SdfSpecifierDef and empty typeName at the
    /// current EditTarget for any nonexistent, or existing but not \a Defined
    /// ancestors.
    ///
    /// The given \a path must be an absolute prim path that does not contain
    /// any variant selections.
    ///
    /// If it is impossible to author any of the necessary PrimSpecs, (for
    /// example, in case \a path cannot map to the current UsdEditTarget's
    /// namespace) issue an error and return an invalid \a UsdPrim.
    ///
    /// Note that this method may return a defined prim whose typeName does not
    /// specify this schema class, in case a stronger typeName opinion overrides
    /// the opinion at the current EditTarget.
    ///
    USDARNOLD_API
    static UsdArnoldPerspCamera
    Define(const UsdStagePtr &stage, const SdfPath &path);

protected:
    /// Returns the type of schema this class belongs to.
    ///
    /// \sa UsdSchemaType
    USDARNOLD_API
    UsdSchemaType _GetSchemaType() const override;

private:
    // needs to invoke _GetStaticTfType.
    friend class UsdSchemaRegistry;
    USDARNOLD_API
    static const TfType &_GetStaticTfType();

    static bool _IsTypedSchema();

    // override SchemaBase virtuals.
    USDARNOLD_API
    const TfType &_GetTfType() const override;

public:
    // --------------------------------------------------------------------- //
    // FOV 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float[] fov` |
    /// | C++ Type | VtArray<float> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->FloatArray |
    USDARNOLD_API
    UsdAttribute GetFovAttr() const;

    /// See GetFovAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateFovAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PLANE_DISTANCE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool plane_distance = 1` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPlane_distanceAttr() const;

    /// See GetPlane_distanceAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePlane_distanceAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // FOCUS_DISTANCE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float[] focus_distance` |
    /// | C++ Type | VtArray<float> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->FloatArray |
    USDARNOLD_API
    UsdAttribute GetFocus_distanceAttr() const;

    /// See GetFocus_distanceAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateFocus_distanceAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // FLAT_FIELD_FOCUS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool flat_field_focus = 1` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetFlat_field_focusAttr() const;

    /// See GetFlat_field_focusAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateFlat_field_focusAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // APERTURE_SIZE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float[] aperture_size` |
    /// | C++ Type | VtArray<float> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->FloatArray |
    USDARNOLD_API
    UsdAttribute GetAperture_sizeAttr() const;

    /// See GetAperture_sizeAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateAperture_sizeAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // APERTURE_BLADES 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `int aperture_blades = 0` |
    /// | C++ Type | int |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Int |
    USDARNOLD_API
    UsdAttribute GetAperture_bladesAttr() const;

    /// See GetAperture_bladesAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateAperture_bladesAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // APERTURE_ROTATION 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float aperture_rotation = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetAperture_rotationAttr() const;

    /// See GetAperture_rotationAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateAperture_rotationAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // APERTURE_BLADE_CURVATURE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float aperture_blade_curvature = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetAperture_blade_curvatureAttr() const;

    /// See GetAperture_blade_curvatureAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateAperture_blade_curvatureAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // APERTURE_ASPECT_RATIO 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float aperture_aspect_ratio = 1` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetAperture_aspect_ratioAttr() const;

    /// See GetAperture_aspect_ratioAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateAperture_aspect_ratioAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // UV_REMAP 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `color4f uv_remap = (0, 0, 0, 0)` |
    /// | C++ Type | GfVec4f |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Color4f |
    USDARNOLD_API
    UsdAttribute GetUv_remapAttr() const;

    /// See GetUv_remapAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateUv_remapAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // RADIAL_DISTORTION 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float radial_distortion = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetRadial_distortionAttr() const;

    /// See GetRadial_distortionAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateRadial_distortionAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // LENS_TILT_ANGLE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float2[] lens_tilt_angle` |
    /// | C++ Type | VtArray<GfVec2f> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float2Array |
    USDARNOLD_API
    UsdAttribute GetLens_tilt_angleAttr() const;

    /// See GetLens_tilt_angleAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateLens_tilt_angleAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // LENS_SHIFT 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float2[] lens_shift` |
    /// | C++ Type | VtArray<GfVec2f> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float2Array |
    USDARNOLD_API
    UsdAttribute GetLens_shiftAttr() const;

    /// See GetLens_shiftAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateLens_shiftAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // RADIAL_DISTORTION_TYPE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token radial_distortion_type = "cubic"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | cubic, cubic_inverse |
    USDARNOLD_API
    UsdAttribute GetRadial_distortion_typeAttr() const;

    /// See GetRadial_distortion_typeAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreateRadial_distortion_typeAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // ===================================================================== //
    // Feel free to add custom code below this line, it will be preserved by 
    // the code generator. 
    //
    // Just remember to: 
    //  - Close the class declaration with }; 
    //  - Close the namespace with PXR_NAMESPACE_CLOSE_SCOPE
    //  - Close the include guard with #endif
    // ===================================================================== //
    // --(BEGIN CUSTOM CODE)--
};

PXR_NAMESPACE_CLOSE_SCOPE

#endif