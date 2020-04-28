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
#ifndef USDARNOLD_GENERATED_ARNOLDPOLYMESHAPI_H
#define USDARNOLD_GENERATED_ARNOLDPOLYMESHAPI_H

/// \file usdArnold/arnoldPolymeshAPI.h

#include "pxr/pxr.h"
#include ".//api.h"
#include "pxr/usd/usd/apiSchemaBase.h"
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
// ARNOLDPOLYMESHAPI                                                          //
// -------------------------------------------------------------------------- //

/// \class UsdArnoldPolymeshAPI
///
/// For any described attribute \em Fallback \em Value or \em Allowed \em Values below
/// that are text/tokens, the actual token is published and defined in \ref UsdArnoldTokens.
/// So to set an attribute to the value "rightHanded", use UsdArnoldTokens->rightHanded
/// as the value.
///
class UsdArnoldPolymeshAPI : public UsdAPISchemaBase
{
public:
    /// Compile time constant representing what kind of schema this class is.
    ///
    /// \sa UsdSchemaType
    static const UsdSchemaType schemaType = UsdSchemaType::SingleApplyAPI;

    /// Construct a UsdArnoldPolymeshAPI on UsdPrim \p prim .
    /// Equivalent to UsdArnoldPolymeshAPI::Get(prim.GetStage(), prim.GetPath())
    /// for a \em valid \p prim, but will not immediately throw an error for
    /// an invalid \p prim
    explicit UsdArnoldPolymeshAPI(const UsdPrim& prim=UsdPrim())
        : UsdAPISchemaBase(prim)
    {
    }

    /// Construct a UsdArnoldPolymeshAPI on the prim held by \p schemaObj .
    /// Should be preferred over UsdArnoldPolymeshAPI(schemaObj.GetPrim()),
    /// as it preserves SchemaBase state.
    explicit UsdArnoldPolymeshAPI(const UsdSchemaBase& schemaObj)
        : UsdAPISchemaBase(schemaObj)
    {
    }

    /// Destructor.
    USDARNOLD_API
    virtual ~UsdArnoldPolymeshAPI();

    /// Return a vector of names of all pre-declared attributes for this schema
    /// class and all its ancestor classes.  Does not include attributes that
    /// may be authored by custom/extended methods of the schemas involved.
    USDARNOLD_API
    static const TfTokenVector &
    GetSchemaAttributeNames(bool includeInherited=true);

    /// Return a UsdArnoldPolymeshAPI holding the prim adhering to this
    /// schema at \p path on \p stage.  If no prim exists at \p path on
    /// \p stage, or if the prim at that path does not adhere to this schema,
    /// return an invalid schema object.  This is shorthand for the following:
    ///
    /// \code
    /// UsdArnoldPolymeshAPI(stage->GetPrimAtPath(path));
    /// \endcode
    ///
    USDARNOLD_API
    static UsdArnoldPolymeshAPI
    Get(const UsdStagePtr &stage, const SdfPath &path);


    /// Applies this <b>single-apply</b> API schema to the given \p prim.
    /// This information is stored by adding "ArnoldPolymeshAPI" to the 
    /// token-valued, listOp metadata \em apiSchemas on the prim.
    /// 
    /// \return A valid UsdArnoldPolymeshAPI object is returned upon success. 
    /// An invalid (or empty) UsdArnoldPolymeshAPI object is returned upon 
    /// failure. See \ref UsdAPISchemaBase::_ApplyAPISchema() for conditions 
    /// resulting in failure. 
    /// 
    /// \sa UsdPrim::GetAppliedSchemas()
    /// \sa UsdPrim::HasAPI()
    ///
    USDARNOLD_API
    static UsdArnoldPolymeshAPI 
    Apply(const UsdPrim &prim);

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
    // PRIMVARSARNOLDVISIBILITY 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uchar primvars:arnold:visibility = 255` |
    /// | C++ Type | unsigned char |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UChar |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldVisibilityAttr() const;

    /// See GetPrimvarsArnoldVisibilityAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldVisibilityAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSIDEDNESS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uchar primvars:arnold:sidedness = 255` |
    /// | C++ Type | unsigned char |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UChar |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSidednessAttr() const;

    /// See GetPrimvarsArnoldSidednessAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSidednessAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDRECEIVE_SHADOWS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:receive_shadows = 1` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldReceive_shadowsAttr() const;

    /// See GetPrimvarsArnoldReceive_shadowsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldReceive_shadowsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSELF_SHADOWS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:self_shadows = 1` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSelf_shadowsAttr() const;

    /// See GetPrimvarsArnoldSelf_shadowsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSelf_shadowsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDINVERT_NORMALS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:invert_normals = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldInvert_normalsAttr() const;

    /// See GetPrimvarsArnoldInvert_normalsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldInvert_normalsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDRAY_BIAS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:ray_bias = 0.000001` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldRay_biasAttr() const;

    /// See GetPrimvarsArnoldRay_biasAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldRay_biasAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDTRANSFORM_TYPE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token primvars:arnold:transform_type = "rotate_about_center"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | linear, rotate_about_origin, rotate_about_center |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldTransform_typeAttr() const;

    /// See GetPrimvarsArnoldTransform_typeAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldTransform_typeAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDOPAQUE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:opaque = 1` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldOpaqueAttr() const;

    /// See GetPrimvarsArnoldOpaqueAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldOpaqueAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDMATTE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:matte = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldMatteAttr() const;

    /// See GetPrimvarsArnoldMatteAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldMatteAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDUSE_LIGHT_GROUP 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:use_light_group = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldUse_light_groupAttr() const;

    /// See GetPrimvarsArnoldUse_light_groupAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldUse_light_groupAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDUSE_SHADOW_GROUP 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:use_shadow_group = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldUse_shadow_groupAttr() const;

    /// See GetPrimvarsArnoldUse_shadow_groupAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldUse_shadow_groupAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDTRACE_SETS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `string[] primvars:arnold:trace_sets` |
    /// | C++ Type | VtArray<std::string> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->StringArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldTrace_setsAttr() const;

    /// See GetPrimvarsArnoldTrace_setsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldTrace_setsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDMOTION_START 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:motion_start = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldMotion_startAttr() const;

    /// See GetPrimvarsArnoldMotion_startAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldMotion_startAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDMOTION_END 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:motion_end = 1` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldMotion_endAttr() const;

    /// See GetPrimvarsArnoldMotion_endAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldMotion_endAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDID 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uint primvars:arnold:id = 0` |
    /// | C++ Type | unsigned int |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UInt |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldIdAttr() const;

    /// See GetPrimvarsArnoldIdAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldIdAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDUVIDXS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uint[] primvars:arnold:uvidxs` |
    /// | C++ Type | VtArray<unsigned int> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UIntArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldUvidxsAttr() const;

    /// See GetPrimvarsArnoldUvidxsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldUvidxsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDCREASE_IDXS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uint[] primvars:arnold:crease_idxs` |
    /// | C++ Type | VtArray<unsigned int> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UIntArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldCrease_idxsAttr() const;

    /// See GetPrimvarsArnoldCrease_idxsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldCrease_idxsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDCREASE_SHARPNESS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float[] primvars:arnold:crease_sharpness` |
    /// | C++ Type | VtArray<float> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->FloatArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldCrease_sharpnessAttr() const;

    /// See GetPrimvarsArnoldCrease_sharpnessAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldCrease_sharpnessAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSHIDXS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uchar[] primvars:arnold:shidxs` |
    /// | C++ Type | VtArray<unsigned char> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UCharArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldShidxsAttr() const;

    /// See GetPrimvarsArnoldShidxsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldShidxsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDVLIST 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `vector3f[] primvars:arnold:vlist` |
    /// | C++ Type | VtArray<GfVec3f> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Vector3fArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldVlistAttr() const;

    /// See GetPrimvarsArnoldVlistAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldVlistAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDNLIST 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `vector3f[] primvars:arnold:nlist` |
    /// | C++ Type | VtArray<GfVec3f> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Vector3fArray |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldNlistAttr() const;

    /// See GetPrimvarsArnoldNlistAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldNlistAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDUVLIST 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float2[] primvars:arnold:uvlist` |
    /// | C++ Type | VtArray<GfVec2f> |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float2Array |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldUvlistAttr() const;

    /// See GetPrimvarsArnoldUvlistAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldUvlistAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSMOOTHING 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:smoothing = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSmoothingAttr() const;

    /// See GetPrimvarsArnoldSmoothingAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSmoothingAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_TYPE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token primvars:arnold:subdiv_type = "none"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | none, catclark, linear |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_typeAttr() const;

    /// See GetPrimvarsArnoldSubdiv_typeAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_typeAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_ITERATIONS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uchar primvars:arnold:subdiv_iterations = 1` |
    /// | C++ Type | unsigned char |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UChar |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_iterationsAttr() const;

    /// See GetPrimvarsArnoldSubdiv_iterationsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_iterationsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_ADAPTIVE_ERROR 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:subdiv_adaptive_error = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_adaptive_errorAttr() const;

    /// See GetPrimvarsArnoldSubdiv_adaptive_errorAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_adaptive_errorAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_ADAPTIVE_METRIC 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token primvars:arnold:subdiv_adaptive_metric = "metric_auto"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | metric_auto, edge_length, flatness |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_adaptive_metricAttr() const;

    /// See GetPrimvarsArnoldSubdiv_adaptive_metricAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_adaptive_metricAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_ADAPTIVE_SPACE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token primvars:arnold:subdiv_adaptive_space = "raster"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | raster, object |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_adaptive_spaceAttr() const;

    /// See GetPrimvarsArnoldSubdiv_adaptive_spaceAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_adaptive_spaceAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_FRUSTUM_IGNORE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:subdiv_frustum_ignore = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_frustum_ignoreAttr() const;

    /// See GetPrimvarsArnoldSubdiv_frustum_ignoreAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_frustum_ignoreAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_UV_SMOOTHING 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `token primvars:arnold:subdiv_uv_smoothing = "pin_corners"` |
    /// | C++ Type | TfToken |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Token |
    /// | \ref UsdArnoldTokens "Allowed Values" | pin_corners, pin_borders, linear, smooth |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_uv_smoothingAttr() const;

    /// See GetPrimvarsArnoldSubdiv_uv_smoothingAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_uv_smoothingAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSUBDIV_SMOOTH_DERIVS 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:subdiv_smooth_derivs = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldSubdiv_smooth_derivsAttr() const;

    /// See GetPrimvarsArnoldSubdiv_smooth_derivsAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldSubdiv_smooth_derivsAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDDISP_PADDING 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:disp_padding = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldDisp_paddingAttr() const;

    /// See GetPrimvarsArnoldDisp_paddingAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldDisp_paddingAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDDISP_HEIGHT 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:disp_height = 1` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldDisp_heightAttr() const;

    /// See GetPrimvarsArnoldDisp_heightAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldDisp_heightAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDDISP_ZERO_VALUE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:disp_zero_value = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldDisp_zero_valueAttr() const;

    /// See GetPrimvarsArnoldDisp_zero_valueAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldDisp_zero_valueAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDDISP_AUTOBUMP 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `bool primvars:arnold:disp_autobump = 0` |
    /// | C++ Type | bool |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Bool |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldDisp_autobumpAttr() const;

    /// See GetPrimvarsArnoldDisp_autobumpAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldDisp_autobumpAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDAUTOBUMP_VISIBILITY 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `uchar primvars:arnold:autobump_visibility = 1` |
    /// | C++ Type | unsigned char |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->UChar |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldAutobump_visibilityAttr() const;

    /// See GetPrimvarsArnoldAutobump_visibilityAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldAutobump_visibilityAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDSTEP_SIZE 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:step_size = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldStep_sizeAttr() const;

    /// See GetPrimvarsArnoldStep_sizeAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldStep_sizeAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

public:
    // --------------------------------------------------------------------- //
    // PRIMVARSARNOLDVOLUME_PADDING 
    // --------------------------------------------------------------------- //
    /// 
    ///
    /// | ||
    /// | -- | -- |
    /// | Declaration | `float primvars:arnold:volume_padding = 0` |
    /// | C++ Type | float |
    /// | \ref Usd_Datatypes "Usd Type" | SdfValueTypeNames->Float |
    USDARNOLD_API
    UsdAttribute GetPrimvarsArnoldVolume_paddingAttr() const;

    /// See GetPrimvarsArnoldVolume_paddingAttr(), and also 
    /// \ref Usd_Create_Or_Get_Property for when to use Get vs Create.
    /// If specified, author \p defaultValue as the attribute's default,
    /// sparsely (when it makes sense to do so) if \p writeSparsely is \c true -
    /// the default for \p writeSparsely is \c false.
    USDARNOLD_API
    UsdAttribute CreatePrimvarsArnoldVolume_paddingAttr(VtValue const &defaultValue = VtValue(), bool writeSparsely=false) const;

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