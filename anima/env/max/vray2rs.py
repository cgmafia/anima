# -*- coding: utf-8 -*-
# Copyright (c) 2012-2017, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import pymxs
import MaxPlus
from anima.render.mat_converter import ConversionManagerBase, NodeCreatorBase


CONVERSION_SPEC_SHEET = {
    'VRayMtl': {
        'node_type': MaxPlus.Mtl,
        'secondary_type': 'Redshift Material',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'diffuse': 'diffuse_color',
            'diffuse_roughness': 'diffuse_roughness',
            'selfIllumination': 'emission_color',
            # 'selfIllumination_gi': '',
            'selfIllumination_multiplier': 'emission_weight',
            'reflection': 'refl_color',
            'reflection_glossiness': 'refl_roughness',
            # 'hilight_glossiness': '',
            # 'reflection_subdivs': {
            #     'refl_samples': lambda x: 16,
            # },

            # 'reflection_fresnel': '',

            'reflection_maxDepth': 'refl_depth',
            # 'reflection_exitColor': '',

            # 'reflection_useInterpolation': '',
            'reflection_ior': 'refl_ior',
            # 'reflection_lockGlossiness': '',
            # 'reflection_lockIOR': '',

            # 'reflection_dimDistance': '',
            # 'reflection_dimDistance_on': '',
            # 'reflection_dimDistance_falloff': '',

            # 'reflection_affectAlpha': '',

            'refraction': 'refr_color',
            'refraction_glossiness': {
                'refr_roughness': lambda x: x,
                'refr_isGlossiness': True,
            },
            # 'refraction_subdivs': '',
            'refraction_ior': 'refr_ior',

            # 'refraction_fogColor': '',
            # 'refraction_fogMult': '',
            # 'refraction_fogBias': '',
            # 'refraction_affectShadows': '',
            # 'refraction_affectAlpha': '',

            'refraction_maxDepth': 'refr_depth',
            # 'refraction_exitColor': '',
            # 'refraction_useExitColor': '',
            # 'refraction_useInterpolation': '',

            # 'refraction_dispersion': 'refr_abbe',
            'refraction_dispersion_on': {
                'refr_abbe': lambda x, y:
                y.ParameterBlock.refraction_dispersion.Value
                if ((x - 1.0) / 149.0) else 0  # VRay uses a value between 1-150
                                               # fit it in to 0-100 range
            },

            # 'translucency_on': '',
            # 'translucency_thickness': '',
            # 'translucency_scatterCoeff': '',
            # 'translucency_fbCoeff': '',

            'translucency_scatterCoeff': {
                'transl_weight': lambda x, y: \
                    (1 if y.ParameterBlock.translucency_on.Value else 0) * x
            },
            'translucency_color': 'transl_color',

            'brdf_type': {
                'refl_brdf': lambda x: {0: 0, 1: 0, 2: 2, 4: 1}[x],
            },

            'anisotropy': 'refl_aniso',
            'anisotropy_rotation': 'refl_aniso_rotation',

            # 'anisotropy_derivation': '',
            # 'anisotropy_axis': '',
            # 'anisotropy_channel': '',

            # 'soften': '',  # Couldn't find it in the UI

            # 'brdf_fixDarkEdges': '',
            # 'gtr_gamma': '',
            # 'gtr_oldGamma': '',

            'brdf_useRoughness': {
                'refl_isGlossiness': lambda x: not x,
            },

            # 'option_traceDiffuse': '',
            # 'option_traceReflection': '',
            # 'option_traceRefraction': '',
            # 'option_doubleSided': '',
            # 'option_reflectOnBack': '',
            # 'option_useIrradMap': '',

            # 'refraction_fogUnitsScale_on': '',
            # 'option_traceDiffuseAndGlossy': '',
            'option_cutOff': {
                'refl_cutoff': lambda x: x,
                'refr_cutoff': lambda x: x,
            },

            'preservationMode': {
                'energyCompMode': lambda x: 1 - x
            },

            # 'option_environment_priority': '',
            # 'effect_id': '',  # There should have been a material_id but
                                # like the one in Maya, but I couldn't find it
            # 'override_effect_id': '',
            # 'option_clampTextures': '',
            # 'option_opacityMode': '',  # May be related with the
                                         # affects_alpha option

            # 'option_glossyFresnel':,

            'texmap_diffuse': 'diffuse_color_map',
            'texmap_diffuse_on': 'diffuse_color_mapenable',
            'texmap_diffuse_multiplier': 'diffuse_color_mapamount',

            'texmap_reflection': 'refl_color_map',
            'texmap_reflection_on': 'refl_color_mapenable',
            'texmap_reflection_multiplier': 'refl_color_mapamount',

            'texmap_refraction': 'refr_color_map',
            'texmap_refraction_on': 'refr_color_mapenable',
            'texmap_refraction_multiplier': 'refr_color_mapamount',

            'texmap_bump': {
                'bump_input_map': lambda x: create_bump_node(x),
            },
            'texmap_bump_on': 'bump_input_mapenable',
            'texmap_bump_multiplier': 'bump_input_mapamount',

            'texmap_reflectionGlossiness': 'refl_roughness_map',
            'texmap_reflectionGlossiness_on': 'refl_roughness_mapenable',
            'texmap_reflectionGlossiness_multiplier': 'refl_roughness_mapamount',

            'texmap_refractionGlossiness': 'refr_roughness_map',
            'texmap_refractionGlossiness_on': 'refr_roughness_mapenable',
            'texmap_refractionGlossiness_multiplier': 'refr_roughness_mapamount',

            'texmap_refractionIOR': 'refr_ior_map',
            'texmap_refractionIOR_on': 'refr_ior_mapenable',
            'texmap_refractionIOR_multiplier': 'refr_ior_mapamount',

            'texmap_displacement': {
                'displacement_input_map':
                    lambda x: create_displacement_node(x),
            },
            'texmap_displacement_on': 'displacement_input_mapenable',
            'texmap_displacement_multiplier': 'displacement_input_mapamount',

            'texmap_translucent': 'transl_color_map',
            'texmap_translucent_on': 'transl_color_mapenable',
            'texmap_translucent_multiplier': 'transl_color_mapamount',

            # 'texmap_environment': '',
            # 'texmap_environment_on': '',
            #
            # 'texmap_hilightGlossiness': '',
            # 'texmap_hilightGlossiness_on': '',
            # 'texmap_hilightGlossiness_multiplier': '',

            'texmap_reflectionIOR': 'refl_ior_map',
            'texmap_reflectionIOR_on': 'refl_ior_mapenable',
            'texmap_reflectionIOR_multiplier': 'refl_ior_mapamount',

            'texmap_opacity': 'opacity_color_map',
            'texmap_opacity_on': 'opacity_color_mapenable',
            'texmap_opacity_multiplier': 'opacity_color_mapamount',

            'texmap_roughness': 'diffuse_roughness_map',
            'texmap_roughness_on': 'diffuse_roughness_mapenable',
            'texmap_roughness_multiplier': 'diffuse_roughness_mapamount',

            'texmap_anisotropy': 'refl_aniso_map',
            'texmap_anisotropy_on': 'refl_aniso_mapenable',
            'texmap_anisotropy_multiplier': 'refl_aniso_mapamount',

            'texmap_anisotropy_rotation': 'refl_aniso_rotation_map',
            'texmap_anisotropy_rotation_on': 'refl_aniso_rotation_mapenable',
            'texmap_anisotropy_rotation_multiplier':
                'refl_aniso_rotation_mapamount',

            # 'texmap_refraction_fog': '',
            # 'texmap_refraction_fog_on': '',
            # 'texmap_refraction_fog_multiplier': '',

            'texmap_self_illumination': 'emission_color_map',
            'texmap_self_illumination_on': 'emission_color_mapenable',
            'texmap_self_illumination_multiplier': 'emission_color_mapamount',

            # 'reflect_minRate': '',
            # 'reflect_maxRate': '',
            # 'reflect_interpSamples': '',
            # 'reflect_colorThreshold': '',
            # 'reflect_normalThreshold': '',
            # 'refract_minRate': '',
            # 'refract_maxRate': '',
            # 'refract_interpSamples': '',
            # 'refract_colorThreshold': '',
            # 'refract_normalThreshold': '',
        }

    },
    'VRayBlendMtl': {
        'node_type': MaxPlus.Mtl,
        'secondary_type': 'Redshift Material Blender',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'baseMtl': 'baseColor_map',
            'coatMtl_enable': {
                'layerColor1_mapenable': lambda x: x[0],
                'layerColor2_mapenable': lambda x: x[1],
                'layerColor3_mapenable': lambda x: x[2],
                'layerColor4_mapenable': lambda x: x[3],
                'layerColor5_mapenable': lambda x: x[4],
                'layerColor6_mapenable': lambda x: x[5],
            },
            'coatMtl': {
                'layerColor1_map': lambda x: x[0],
                'layerColor2_map': lambda x: x[1],
                'layerColor3_map': lambda x: x[2],
                'layerColor4_map': lambda x: x[3],
                'layerColor5_map': lambda x: x[4],
                'layerColor6_map': lambda x: x[5],
            },
            'blend': {
                'blendColor1': lambda x: x[0],
                'blendColor2': lambda x: x[1],
                'blendColor3': lambda x: x[2],
                'blendColor4': lambda x: x[3],
                'blendColor5': lambda x: x[4],
                'blendColor6': lambda x: x[5],
            },
            'texmap_blend': {
                'blendColor1_map': lambda x: x[0],
                'blendColor2_map': lambda x: x[1],
                'blendColor3_map': lambda x: x[2],
                'blendColor4_map': lambda x: x[3],
                'blendColor5_map': lambda x: x[4],
                'blendColor6_map': lambda x: x[5],
            },
            # 'texmap_blend_multiplier': '',
            'additiveMode': [
                'additiveMode1',
                'additiveMode2',
                'additiveMode3',
                'additiveMode4',
                'additiveMode5',
                'additiveMode6',
            ]
        }
    },

    'VRayColor': {
        # Convert it to 3ds Max's Color Correction node
        'node_type': MaxPlus.Texmap,
        'secondary_type': 'Color Correction',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'red': {
                'lightnessMode': 1,
                'exposureMode': 0,
                'enableR': True,
                'gainR': lambda x: x * 100,
            },
            'green': {
                'lightnessMode': 1,
                'exposureMode': 0,
                'enableG': True,
                'gainG': lambda x: x * 100,
            },
            'blue': {
                'lightnessMode': 1,
                'exposureMode': 0,
                'enableB': True,
                'gainB': lambda x: x * 100,
            },
            'rgb_multiplier': {
                'gammaRGB': lambda x: x * 100,
            },
            # 'alpha', # can do nothing
            'color': 'color',
            'color_gamma': 'gammaRGB'

        }
    },

    'VRayDirt': {
        # Convert it to 3ds Max's Color Correction node
        'node_type': MaxPlus.Texmap,
        'secondary_type': 'Redshift Ambient Occlusion',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'radius': 'maxDistance',
            'occluded_color': 'dark',
            'unoccluded_color': 'bright',
            'distribution': 'spread',
            'falloff': 'fallOff',
            'subdivs': 'numSamples',
            'bias': 'bias',
            'affect_alpha': 'occlusionInAlpha',
            # ignore_for_gi
            'consider_same_object_only': 'sameObjectOnly',
            # double_sided
            'invert_normal': 'invert',
            # work_with_transparency
            # environment_occlusion
            'mode': {
                'reflective': lambda x: min(1, x),
            },
            # reflection_glossiness
            # affect_reflection_elements
            'texmap_radius': 'maxDistance_map',
            'texmap_radius_on': 'maxDistance_mapenable',
            # texmap_radius_multiplier
            'texmap_occluded_color': 'dark_map',
            'texmap_occluded_color_on': 'dark_mapenable',
            # texmap_occluded_color_multiplier
            'texmap_unoccluded_color': 'bright_map',
            'texmap_unoccluded_color_on': 'bright_mapenable',
            # texmap_unoccluded_color_multiplier
            # texmap_reflection_glossiness
            # texmap_reflection_glossiness_on
            # texmap_reflection_glossiness_multiplier
            # subdivs_as_samples
        }
    },

    'VRayLightMtl': {
        # Convert it to 3ds Max's Color Correction node
        'node_type': MaxPlus.Mtl,
        'secondary_type': 'Redshift Incandescent',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'color': 'color',
            'multiplier': 'intensity',
            'texmap': 'color_map',
            'texmap_on': 'color_mapenable',
            'twoSided': 'doublesided',
            'compensate_exposure': 'applyExposureCompensation',
            # 'opacity_multiplyColor'
            'opacity_texmap': 'alpha_map',
            'opacity_texmap_on': 'alpha_mapenable',

            # directLight_on
            # directLight_subdivs
            # directLight_cutoffThreshold

            # displacement_multiplier
            # displacement_texmap
            # displacement_texmap_on

            # texmap_resolution
            # texmap_adaptiveness
        }
    },

    'Normal Bump': {
        # Convert it to 3ds Max's Color Correction node
        'node_type': MaxPlus.Texmap,
        'secondary_type': 'Redshift Normal Map',

        # 'call_after': # write the code here to assign this material to
        # all of the objects that is using the VRayMtl

        'attributes': {
            'mult_spin': 'scale',
            # 'bump_spin': '',
            'normal_map': {
                # write down the code that assigns the bitmap to the path
                # tex0
                # I couldn't find any reasonable method of setting the tex0
                # attribute
                #
                # so instead of setting it by using the code, I'll excuse the
                # the user to do it by hand
                #
                # sorry!
                'tex0': lambda x, y, z: print_out_node_info(
                    x.ParameterBlock.fileName.Value, y.GetName(), z.GetName(),
                    'Please set {target_node}.tex0 -> {source_value}'
                )
            },
            # 'bump_map': '',
            # 'map1on': '',
            # 'map2on': '',
            'method': {
                'tspace_id': lambda x: x + 1,
            },
            # 'flipred': '',
            'flipgreen': 'flipY',
            # 'swap_rg': '',
        }
    },
}


def create_bump_node(source_value):
    """Creates a bump map

    :param source_value:
    :return:
    """
    try:
        source_value.GetName()
        rs_bump_map = NodeCreator.create_node_by_type(
            MaxPlus.Texmap,
            'Redshift Bump Map'
        )
        rs_bump_map.ParameterBlock.input_map.Value = source_value
        return rs_bump_map
    except RuntimeError:
        return None


def create_displacement_node(source_value):
    """Creates a bump map

    :param source_value:
    :return:
    """
    try:
        source_value.GetName()
        rs_displacement_map = NodeCreator.create_node_by_type(
            MaxPlus.Texmap,
            'Redshift Displacement Map'
        )
        rs_displacement_map.ParameterBlock.texMap_map.Value = source_value
        return rs_displacement_map
    except RuntimeError:
        return None


def print_out_node_info(source_value, source_node, target_node, template=''):
    """prints out node info

    :param source_value:
    :param source_node:
    :param target_node:
    :param str template:
    :return:
    """
    print(
        template.format(
            source_value=source_value,
            source_node=source_node,
            target_node=target_node
        )
    )


class NodeCreator(NodeCreatorBase):
    """Creates nodes according to the given specs
    """

    def create(self):
        """creates the node
        """
        node_class = self.specs.get('node_type')
        secondary_class = self.specs.get('secondary_type')

        new_node = self.create_node_by_type(node_class, secondary_class)

        # add it to Material manager slot
        MaxPlus.MaterialManager.PutMtlToMtlEditor(new_node, 0)
        return new_node

    @classmethod
    def create_node_by_type(cls, node_class, secondary_class_name):
        """Creates nodes by type name

        :param node_class: The MaxPlus class object (ex: MaxPlus.MtlBase)
        :param str secondary_class_name: A string for the node type name
        :return:
        """
        # get the class, its id and its super class id
        class_ = ConversionManager.get_class_by_name(secondary_class_name)

        class_id = class_.ClassId
        super_class_id = class_.SuperClassId

        # create an animatable
        animatable = MaxPlus.Factory.CreateAnimatable(
            super_class_id, class_id, False
        )

        # and cast it to the node_type
        new_node = node_class._CastFrom(animatable)

        return new_node


class ConversionManager(ConversionManagerBase):
    """Manages the conversion from VRay to RedShift
    """

    def __init__(self):
        super(ConversionManager, self).__init__()
        self.conversion_spec_sheet = CONVERSION_SPEC_SHEET
        self.node_creator_factory = NodeCreator

    def rename_node(self, node, new_name):
        """Renames the node

        :param node:
        :param new_name:
        :return:
        """
        node.SetName(MaxPlus.WStr(new_name))

    def get_node_name(self, node):
        """Returns the node name

        :param node:
        :return:
        """
        return node.GetName()

    def get_node_inputs(self, node, attr=None):
        """returns the node inputs

        :param node:
        :param attr:
        :return:
        """
        inputs = []
        if attr is None:
            # return all connected nodes
            for param in node.ParameterBlock.Parameters:
                value = param.GetValue()
                # TODO: This one doesn't consider that the parameter is a multi
                # parameter.
                if isinstance(value, MaxPlus.Animatable) \
                   and str(value) != 'None':
                    inputs.append(value)
        else:
            param = node.ParameterBlock.GetParamByName(attr)
            value = param.GetValue()
            if isinstance(value, MaxPlus.Animatable) and str(value) != 'None':
                inputs.append(value)

        return inputs

    def connect_attr(self, source_node, target_node, target_parameter):
        """creates a connection from source_attr to target_attr target_node

        :param source_node:
        :param target_node:
        :param str target_parameter:
        :return:
        """
        # param = target_node.ParameterBlock.GetParamByName(target_attr)
        # param.Value = source_attr

        # do it with pymxs
        MaxPlus.MaterialManager.PutMtlToMtlEditor(
            source_node, 0
        )
        source_node_pymxs = \
            pymxs.runtime.getMEditMaterial(1)

        # get the parent node
        MaxPlus.MaterialManager.PutMtlToMtlEditor(
            target_node, 1
        )
        target_node_pymxs = \
            pymxs.runtime.getMEditMaterial(2)

        # Then execute the connection script
        exec('target_node_pymxs.%s = source_node_pymxs' % target_parameter)
        # This should've worked!

    @classmethod
    def get_class_by_name(cls, class_name):
        """returns the class_id from the given class_name

        :param str class_name: The class name
        :return MaxPlus.Class_ID:
        """
        for c in MaxPlus.PluginManager.GetClassList().Classes:
            if c.Name == class_name:
                return c

    @classmethod
    def get_class_id_by_name(cls, class_name):
        """returns the class_id from the given class_name

        :param str class_name: The class name
        :return MaxPlus.Class_ID:
        """
        c = cls.get_class_by_name(class_name)
        return c.ClassId

    @classmethod
    def get_super_class_id_by_name(cls, class_name):
        """returns the super class id of the given class

        :param str class_name: Class Name
        :return:
        """
        c = cls.get_class_by_name(class_name)
        return c.SuperClassId

    @classmethod
    def get_class_name(cls, class_id):
        """returns the class_name from the given class_id

        :param class_id:
        :return:
        """
        for cd in MaxPlus.PluginManager.GetClassList().Classes:
            if cd.ClassId == class_id:
                return cd.Name

    def get_node_type(self, node):
        """returns the node type name

        :param node:
        :return:
        """
        return self.get_class_name(node.ClassID)

    def list_nodes(self, type_):
        """list nodes of given type

        :param type_:
        :return:
        """
        # just return materials for now
        mat_lib = MaxPlus.MaterialLibrary.GetSceneMaterialLibrary()

        # nodes_to_return = []
        nodes_to_return = {}

        num_materials = mat_lib.GetNumMaterials()
        for i in range(num_materials):
            mat = mat_lib.GetMaterial(i)
            class_name = mat.GetClassName()
            if class_name == type_:
                nodes_to_return[mat.GetFullName()] = mat

            # try to get it from the material hierarchy
            for parent_mat, param, sub_mat, index in \
                    self.walk_material_hierarchy(mat):
                try:
                    class_name = sub_mat.GetClassName()
                except RuntimeError:
                    pass
                else:
                    if class_name == type_:
                        nodes_to_return[sub_mat.GetFullName()] = sub_mat

        return nodes_to_return.values()

    def get_node_by_name(self, node_name):
        """Finds and returns the node with the given name

        :param node_name:
        :return:
        """
        # just return materials for now
        mat_lib = MaxPlus.MaterialLibrary.GetSceneMaterialLibrary()

        num_materials = mat_lib.GetNumMaterials()
        nodes_to_return = []
        for i in range(num_materials):
            mat = mat_lib.GetMaterial(i)
            if mat.GetName() == node_name:
                nodes_to_return.append(mat)
                return nodes_to_return

            # try to get it from the material hierarchy
            for parent_mat, param, sub_mat, index in \
                    self.walk_material_hierarchy(mat):
                try:
                    sub_mat_name = sub_mat.GetName()
                except RuntimeError:
                    pass
                else:
                    if sub_mat_name == node_name:
                        nodes_to_return.append(sub_mat)
        return nodes_to_return

    def get_node_by_class(self, node_class_name):
        """Finds and returns the node with the given name

        :param string node_class_name:
        :return:
        """
        # just return materials for now
        mat_lib = MaxPlus.MaterialLibrary.GetSceneMaterialLibrary()

        num_materials = mat_lib.GetNumMaterials()
        nodes_to_return = []
        for i in range(num_materials):
            mat = mat_lib.GetMaterial(i)
            if mat.GetClassName() == node_class_name:
                nodes_to_return.append(mat)
                return nodes_to_return

            # try to get it from the material hierarchy
            for parent_mat, param, sub_mat, index in \
                    self.walk_material_hierarchy(mat):
                try:
                    sub_mat_class_name = sub_mat.GetClassName()
                except RuntimeError:
                    pass
                else:
                    if sub_mat_class_name == node_class_name:
                        nodes_to_return.append(sub_mat)
        return nodes_to_return

    def get_attr(self, node, attr):
        """returns node attribute value

        :param node:
        :param attr:
        :return:
        """
        return node.ParameterBlock.GetParamByName(attr).GetValue()

    def set_attr(self, node, attr, value):
        """sets parameter value

        :param node:
        :param attr:
        :param value:
        :return:
        """
        if str(value) != 'None':
            node.ParameterBlock.GetParamByName(attr).SetValue(value)

    def walk_hierarchy(self, node):
        """this is a generator that yields all dag nodes in the current scene
        """
        for c in node.Children:
            yield c
            for gc in self.walk_hierarchy(c):
                yield gc

    @classmethod
    def walk_material_hierarchy(cls, node):
        """Walks through the material hierarchy through their parameters

        :param node:
        :return:
        """
        for p in node.ParameterBlock.Parameters:
            # decide what to do by looking at the parameter type of the p param
            param_type_name = MaxPlus.FPTypeGetName(p.GetParamType())
            value = p.Value
            if param_type_name in ['MtlTab', 'TexmapTab']:
                # it contains multiple materials
                for i, v in enumerate(value):
                    yield (node, p, v, i)
                    try:
                        v.GetName()
                        for pp in cls.walk_material_hierarchy(v):
                            yield pp
                    except (RuntimeError, AttributeError):
                        pass
            else:
                try:
                    value.GetName()
                    yield (node, p, value, -1)
                    if isinstance(value, MaxPlus.MtlBase):
                        for pp in cls.walk_material_hierarchy(value):
                            yield pp
                except (RuntimeError, AttributeError):
                    pass

    # @classmethod
    # def inputs(cls, node):
    #     """return the inputs of the given node
    #     :param node:
    #     :return:
    #     """
    #     # traverse parameters
    #     for p in node.ParameterBlock.Parameters:
    #         if p.GetParamType()

    @classmethod
    def outputs(cls, node):
        """return the node and the parameter that this node is connected to

        :param node:
        :return:
        """
        inode = node.FindDependentNode()
        top_mat = inode.Material
        for parent, param, child, i in cls.walk_material_hierarchy(top_mat):
            try:
                if child.GetFullName() == node.GetFullName():
                    # we found our material but where did we come here
                    yield parent, param, i
            except RuntimeError:
                # This is not what you think it is...
                # so pass
                pass

    def clean_up(self, new_nodes):
        """A clean up stage for assigning materials to objects in the scene

        :param new_nodes: a list of lists of
            [[old_node, new_node], [old_node, new_node]...] style
        :return:
        """
        for old_node, new_node in new_nodes:
            # get the INodes using directly the old_node as material
            # Recursively assign the new material to the objects
            print('cleaning up: %s' % old_node.GetName())
            iteration = 0
            while True:
                iteration += 1
                inode = old_node.FindDependentNode()
                try:
                    inode_name = inode.GetName()
                    inode_mat = inode.GetMaterial()
                    print('updating material of (%i): %s' %
                          (iteration, inode_name))
                except RuntimeError:
                    break
                if inode_mat.GetName() == old_node.GetName():
                    # directly assign the new_node as the material
                    try:
                        inode.SetMaterial(new_node)
                    except (TypeError, ValueError):
                        # the new_node is None
                        pass
                    # and fuck off
                else:
                    # then this node is used in a material network
                    # so update the referencing nodes to use the new node
                    # instead
                    for parent, param, i in self.outputs(old_node):
                        if i == -1:
                            param.Value = new_node
                        else:
                            try:
                                # unless this is is a Multi/Sub-Object node
                                # do it directly
                                if parent.GetClassName() == 'Multi/Sub-Object':
                                    # convert it to a MaxPlus.Mtl object
                                    print('using Mtl instead of MtlBase for '
                                          'Multi/Sub-Object')
                                    # parent = MaxPlus.Mtl._CastFrom(parent)
                                    # # then use the SetSubMtl() method
                                    # parent.SetSubMtl(i, new_node)
                                    self.connect_attr(
                                        new_node, parent,
                                        '%s[%i]' % (param.GetName(), i)
                                    )
                                else:
                                    # do it with pymxs
                                    # I don't know any other way to pass the
                                    # Python material/texture to pymxs
                                    # so the best way I found was to use the
                                    # material editor
                                    print(
                                        'using pymxs for complex connection!'
                                    )
                                    print(
                                        '%s --> %s.%s[%s]' % (
                                            new_node.GetFullName(),
                                            parent.GetName(),
                                            param.GetName(),
                                            i
                                        )
                                    )

                                    self.connect_attr(
                                        new_node, parent,
                                        '%s[%i]' % (param.GetName(), i)
                                    )

                                    # # put the material to slot 1. which is slot
                                    # # 0 in Python by the way
                                    # MaxPlus.MaterialManager.PutMtlToMtlEditor(
                                    #     new_node, 0
                                    # )
                                    # new_node_pymxs = \
                                    #     pymxs.runtime.getMEditMaterial(1)
                                    #
                                    # # get the parent node
                                    # MaxPlus.MaterialManager.PutMtlToMtlEditor(
                                    #     parent, 1
                                    # )
                                    # parent_pymxs = \
                                    #     pymxs.runtime.getMEditMaterial(2)
                                    #
                                    # # Then execute the connection script
                                    # exec(
                                    #     'parent_pymxs.%s[%i] = '
                                    #     'new_node_pymxs' % (param.GetName(), i)
                                    # )
                                    # # This should've worked!

                            except TypeError:
                                print('Could not connect: %s --> %s.%s[%s]' %
                                      (new_node.GetFullName(),
                                       parent.GetName(), param.GetName(), i))
                    # # do this only once
                    # break

    @classmethod
    def get_all_material_types_in_current_scene(cls):
        """returns all the material types in the current scene
        """
        mat_types = {}
        mat_lib = MaxPlus.MaterialLibrary.GetSceneMaterialLibrary()
        mat_count = mat_lib.GetNumMaterials()
        for i in range(mat_count):
            mat = mat_lib.GetMaterial(i)
            mat_class_name = mat.GetClassName()
            if mat_class_name not in mat_types:
                mat_types[mat_class_name] = {
                    'count': 0,
                    'nodes': []
                }
            mat_types[mat_class_name]['count'] += 1
            mat_types[mat_class_name]['nodes'].append(mat)

            for parent, parameter, sub_mat, index in \
                    cls.walk_material_hierarchy(mat):
                try:
                    sub_mat_class_name = sub_mat.GetClassName()
                except RuntimeError:
                    continue
                if sub_mat_class_name not in mat_types:
                    mat_types[sub_mat_class_name] = {
                        'count': 0,
                        'nodes': []
                    }
                mat_types[sub_mat_class_name]['count'] += 1
                mat_types[sub_mat_class_name]['nodes'].append(sub_mat)

        return mat_types

    def export_basic_material_attibutes(self, node):
        """exports basic material attributes to a json file.

        :return:
        """
        import os
        import tempfile
        json_file_path = os.path.join(
            tempfile.gettempdir(),
            'basic_material.json'
        )

        data = {}

        exportable_types = ['Texmap', 'Int', 'PercentFraction', 'Float',
                            'FRgb', 'Rgb', 'Point3', 'BOOL', 'World']
        param_types = []
        for p in node.ParameterBlock.Parameters:
            param_type_name = MaxPlus.FPTypeGetName(p.GetParamType())
            #print(p.GetName(), )
            # data[p.GetName()] = p.Value;
            param_types.append(param_type_name)

        print(set(param_types))
