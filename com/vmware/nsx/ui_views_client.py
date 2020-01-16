# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.ui_views.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Widgetconfigurations(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.ui_views.widgetconfigurations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _WidgetconfigurationsStub)


    def create(self,
               view_id,
               widget_configuration,
               ):
        """
        Creates a new Widget Configuration and adds it to the specified view.
        Supported resource_types are LabelValueConfiguration,
        DonutConfiguration, GridConfiguration, StatsConfiguration,
        MultiWidgetConfiguration and ContainerConfiguration. Note: Expressions
        should be given in a single line. If an expression spans multiple
        lines, then form the expression in a single line. For label-value
        pairs, expressions are evaluated as follows: a. First, render
        configurations are evaluated in their order of appearance in the widget
        config. The 'field' is evaluated at the end. b. Second, when render
        configuration is provided then the order of evaluation is 1. If
        expressions provided in 'condition' and 'display value' are well-formed
        and free of runtime-errors such as 'null pointers' and evaluates to
        'true'; Then remaining render configurations are not evaluated, and the
        current render configuration's 'display value' is taken as the final
        value. 2. If expression provided in 'condition' of render configuration
        is false, then next render configuration is evaluated. 3. Finally,
        'field' is evaluated only when every render configuration evaluates to
        false and no error occurs during steps 1 and 2 above. If an error
        occurs during evaluation of render configuration, then an error message
        is shown. The display value corresponding to that label is not shown
        and evaluation of the remaining render configurations continues to
        collect and show all the error messages (marked with the 'Label' for
        identification) as 'Error_Messages: {}'. If during evaluation of
        expressions for any label-value pair an error occurs, then it is marked
        with error. The errors are shown in the report, along with the label
        value pairs that are error-free. Important: For elements that take
        expressions, strings should be provided by escaping them with a
        back-slash. These elements are - condition, field, tooltip text and
        render_configuration's display_value.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  widget_configuration: :class:`vmware.vapi.struct.VapiStruct`
        :param widget_configuration: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.WidgetConfiguration`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.WidgetConfiguration
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.WidgetConfiguration`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'view_id': view_id,
                            'widget_configuration': widget_configuration,
                            })

    def delete(self,
               view_id,
               widgetconfiguration_id,
               ):
        """
        Detaches widget from a given view. If the widget is no longer part of
        any view, then it will be purged.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  widgetconfiguration_id: :class:`str`
        :param widgetconfiguration_id: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('delete',
                            {
                            'view_id': view_id,
                            'widgetconfiguration_id': widgetconfiguration_id,
                            })

    def get(self,
            view_id,
            container=None,
            widget_ids=None,
            ):
        """
        If no query params are specified then all the Widget Configurations of
        the specified view are returned.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  container: :class:`str` or ``None``
        :param container: Id of the container (optional)
        :type  widget_ids: :class:`str` or ``None``
        :param widget_ids: Ids of the WidgetConfigurations (optional)
        :rtype: :class:`com.vmware.nsx.model_client.WidgetConfigurationList`
        :return: com.vmware.nsx.model.WidgetConfigurationList
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'view_id': view_id,
                            'container': container,
                            'widget_ids': widget_ids,
                            })

    def get_0(self,
              view_id,
              widgetconfiguration_id,
              ):
        """
        Returns Information about a specific Widget Configuration.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  widgetconfiguration_id: :class:`str`
        :param widgetconfiguration_id: (required)
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.WidgetConfiguration
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.WidgetConfiguration`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get_0',
                            {
                            'view_id': view_id,
                            'widgetconfiguration_id': widgetconfiguration_id,
                            })

    def update(self,
               view_id,
               widgetconfiguration_id,
               widget_configuration,
               ):
        """
        Updates the widget at the given view. If the widget is referenced by
        other views, then the widget will be updated in all the views that it
        is part of.

        :type  view_id: :class:`str`
        :param view_id: (required)
        :type  widgetconfiguration_id: :class:`str`
        :param widgetconfiguration_id: (required)
        :type  widget_configuration: :class:`vmware.vapi.struct.VapiStruct`
        :param widget_configuration: (required)
            The parameter must contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.WidgetConfiguration`.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: com.vmware.nsx.model.WidgetConfiguration
            The return value will contain all the attributes defined in
            :class:`com.vmware.nsx.model_client.WidgetConfiguration`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'view_id': view_id,
                            'widgetconfiguration_id': widgetconfiguration_id,
                            'widget_configuration': widget_configuration,
                            })
class _WidgetconfigurationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'widget_configuration': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfiguration')]),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/ui-views/{view-id}/widgetconfigurations',
            request_body_parameter='widget_configuration',
            path_variables={
                'view_id': 'view-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'widgetconfiguration_id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id}',
            path_variables={
                'view_id': 'view-id',
                'widgetconfiguration_id': 'widgetconfiguration-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'container': type.OptionalType(type.StringType()),
            'widget_ids': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ui-views/{view-id}/widgetconfigurations',
            path_variables={
                'view_id': 'view-id',
            },
            query_parameters={
                'container': 'container',
                'widget_ids': 'widget_ids',
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'widgetconfiguration_id': type.StringType(),
        })
        get_0_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id}',
            path_variables={
                'view_id': 'view-id',
                'widgetconfiguration_id': 'widgetconfiguration-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'view_id': type.StringType(),
            'widgetconfiguration_id': type.StringType(),
            'widget_configuration': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfiguration')]),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/ui-views/{view-id}/widgetconfigurations/{widgetconfiguration-id}',
            request_body_parameter='widget_configuration',
            path_variables={
                'view_id': 'view-id',
                'widgetconfiguration_id': 'widgetconfiguration-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfiguration')]),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfigurationList'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfiguration')]),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.nsx.model_client', 'WidgetConfiguration')]),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.ui_views.widgetconfigurations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Widgetconfigurations': Widgetconfigurations,
    }

