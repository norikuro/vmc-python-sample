# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.
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


class AccountLink(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.account_link'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AccountLinkStub)


    def get(self,
            org,
            ):
        """
        Gets a link that can be used on a customer's account to start the
        linking process.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
             Generic Error
        """
        return self._invoke('get',
                            {
                            'org': org,
                            })
class Providers(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.providers'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProvidersStub)


    def list(self,
             org,
             ):
        """
        

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.AwsCloudProvider`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Organization doesn't exist
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class Reservations(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.reservations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReservationsStub)


    def list(self,
             org,
             ):
        """
        Get all reservations for this org

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.MaintenanceWindowEntry`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class SddcTemplates(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddc_templates'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcTemplatesStub)


    def delete(self,
               org,
               template_id,
               ):
        """
        Delete SDDC template identified by given id.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  template_id: :class:`str`
        :param template_id: SDDC Template identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'template_id': template_id,
                            })

    def get(self,
            org,
            template_id,
            ):
        """
        Get configuration template by given template id.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  template_id: :class:`str`
        :param template_id: SDDC Template identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.SddcTemplate`
        :return: com.vmware.vmc.model.SddcTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC Template with given identifier
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'template_id': template_id,
                            })

    def list(self,
             org,
             ):
        """
        List all available SDDC configuration templates in an organization

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SddcTemplate`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class Sddcs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcsStub)


    def create(self,
               org,
               sddc_config,
               validate_only=None,
               ):
        """
        Provision an SDDC in target cloud

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc_config: :class:`com.vmware.vmc.model_client.AwsSddcConfig`
        :param sddc_config: sddcConfig (required)
        :type  validate_only: :class:`bool` or ``None``
        :param validate_only: When true, only validates the given sddc configuration without
            provisioning. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc_config': sddc_config,
                            'validate_only': validate_only,
                            })

    def delete(self,
               org,
               sddc,
               retain_configuration=None,
               template_name=None,
               force=None,
               ):
        """
        Delete SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  retain_configuration: :class:`bool` or ``None``
        :param retain_configuration: If = 'true', the SDDC's configuration is retained as a template for
            later use. This flag is applicable only to SDDCs in ACTIVE state.
            (optional)
        :type  template_name: :class:`str` or ``None``
        :param template_name: Only applicable when retainConfiguration is also set to 'true'.
            When set, this value will be used as the name of the SDDC
            configuration template generated. (optional)
        :type  force: :class:`str` or ``None``
        :param force: If = 'true', will delete forcefully. Beware: do not use the force
            flag if there is a chance an active provisioning or deleting task
            is running against this SDDC. This option is restricted. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for deletion
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'retain_configuration': retain_configuration,
                            'template_name': template_name,
                            'force': force,
                            })

    def get(self,
            org,
            sddc,
            ):
        """
        Get SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Sddc`
        :return: com.vmware.vmc.model.Sddc
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })

    def list(self,
             org,
             include_deleted=None,
             ):
        """
        List all the SDDCs of an organization

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  include_deleted: :class:`bool` or ``None``
        :param include_deleted: When true, forces the result to also include deleted SDDCs.
            (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.Sddc`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'include_deleted': include_deleted,
                            })

    def patch(self,
              org,
              sddc,
              sddc_patch_request,
              ):
        """
        Patch SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  sddc_patch_request: :class:`com.vmware.vmc.model_client.SddcPatchRequest`
        :param sddc_patch_request: Patch request for the SDDC (required)
        :rtype: :class:`com.vmware.vmc.model_client.Sddc`
        :return: com.vmware.vmc.model.Sddc
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             SDDC cannot be patched
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        """
        return self._invoke('patch',
                            {
                            'org': org,
                            'sddc': sddc,
                            'sddc_patch_request': sddc_patch_request,
                            })
class Subscriptions(VapiInterface):
    """
    
    """
    GET_0_OFFER_TYPE_TERM = "TERM"
    """
    Possible value for ``offerType`` of method :func:`Subscriptions.get_0`.

    """
    GET_0_OFFER_TYPE_ON_DEMAND = "ON_DEMAND"
    """
    Possible value for ``offerType`` of method :func:`Subscriptions.get_0`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.subscriptions'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SubscriptionsStub)


    def create(self,
               org,
               subscription_request,
               ):
        """
        Initiates the creation of a subscription

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  subscription_request: :class:`com.vmware.vmc.model_client.SubscriptionRequest`
        :param subscription_request: subscriptionRequest (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'subscription_request': subscription_request,
                            })

    def get(self,
            org,
            subscription,
            ):
        """
        Get subscription details for a given subscription id

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  subscription: :class:`str`
        :param subscription: SubscriptionId for an sddc. (required)
        :rtype: :class:`com.vmware.vmc.model_client.SubscriptionDetails`
        :return: com.vmware.vmc.model.SubscriptionDetails
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'subscription': subscription,
                            })

    def get_0(self,
              org,
              offer_type=None,
              ):
        """
        Returns all subscriptions for a given org id

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  offer_type: :class:`str` or ``None``
        :param offer_type: Offer Type \* \\\\`ON_DEMAND\\\\` - on-demand subscription \*
            \\\\`TERM\\\\` - term subscription \* All subscriptions if not
            specified (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SubscriptionDetails`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get_0',
                            {
                            'org': org,
                            'offer_type': offer_type,
                            })
class Tasks(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.tasks'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TasksStub)


    def get(self,
            org,
            task,
            ):
        """
        Retrieve details of a task.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  task: :class:`str`
        :param task: Task identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the task with given identifier
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'task': task,
                            })

    def list(self,
             org,
             filter=None,
             ):
        """
        List all tasks with optional filtering.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  filter: :class:`str` or ``None``
        :param filter: Filter expression Binary Operators: 'eq', 'ne', 'lt', 'gt', 'le',
            'ge', 'mul', 'div', 'mod', 'sub', 'add' Unary Operators: 'not', '-'
            (minus) String Operators: 'startswith', 'endswith', 'length',
            'contains', 'tolower', 'toupper', Nested attributes are composed
            using '.' Dates must be formatted as yyyy-MM-dd or
            yyyy-MM-ddTHH:mm:ss[.SSS]Z Strings should enclosed in single
            quotes, escape single quote with two single quotes The special
            literal 'created' will be mapped to the time the resource was first
            created. Examples: - $filter=(updated gt 2016-08-09T13:00:00Z) and
            (org_id eq 278710ff4e-6b6d-4d4e-aefb-ca637f38609e) -
            $filter=(created eq 2016-08-09) - $filter=(created gt 2016-08-09)
            and (sddc.status eq 'READY') (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.Task`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'filter': filter,
                            })

    def update(self,
               org,
               task,
               action=None,
               ):
        """
        Request that a running task be canceled. This is advisory only, some
        tasks may not be cancelable, and some tasks might take an arbitrary
        amount of time to respond to a cancelation request. The task must be
        monitored to determine subsequent status.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  task: :class:`str`
        :param task: Task identifier (required)
        :type  action: :class:`str` or ``None``
        :param action: If = 'cancel', task will be canceled (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the task with given identifier
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'task': task,
                            'action': action,
                            })
class _AccountLinkStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.VoidType(),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ProvidersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/providers',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'AwsCloudProvider')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.providers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ReservationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/reservations',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'MaintenanceWindowEntry')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.reservations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcTemplatesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'template_id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vmc/api/orgs/{org}/sddc-templates/{templateId}',
            path_variables={
                'org': 'org',
                'template_id': 'templateId',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'template_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddc-templates/{templateId}',
            path_variables={
                'org': 'org',
                'template_id': 'templateId',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddc-templates',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SddcTemplate'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SddcTemplate')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddc_templates',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_config': type.ReferenceType('com.vmware.vmc.model_client', 'AwsSddcConfig'),
            'validate_only': type.OptionalType(type.BooleanType()),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs',
            request_body_parameter='sddc_config',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'validate_only': 'validateOnly',
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'retain_configuration': type.OptionalType(type.BooleanType()),
            'template_name': type.OptionalType(type.StringType()),
            'force': type.OptionalType(type.StringType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'retain_configuration': 'retain_configuration',
                'template_name': 'template_name',
                'force': 'force',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'include_deleted': type.OptionalType(type.BooleanType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'include_deleted': 'includeDeleted',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'sddc_patch_request': type.ReferenceType('com.vmware.vmc.model_client', 'SddcPatchRequest'),
        })
        patch_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        patch_input_value_validator_list = [
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}',
            request_body_parameter='sddc_patch_request',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Sddc'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'Sddc')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Sddc'),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SubscriptionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'subscription_request': type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionRequest'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/subscriptions',
            request_body_parameter='subscription_request',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'subscription': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions/{subscription}',
            path_variables={
                'org': 'org',
                'subscription': 'subscription',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'offer_type': type.OptionalType(type.StringType()),
        })
        get_0_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'offer_type': 'offer_type',
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionDetails'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionDetails')),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.subscriptions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TasksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'task': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/tasks/{task}',
            path_variables={
                'org': 'org',
                'task': 'task',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'filter': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/tasks',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'filter': '$filter',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'task': type.StringType(),
            'action': type.OptionalType(type.StringType()),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/tasks/{task}',
            path_variables={
                'org': 'org',
                'task': 'task',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'Task')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.tasks',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'AccountLink': AccountLink,
        'Providers': Providers,
        'Reservations': Reservations,
        'SddcTemplates': SddcTemplates,
        'Sddcs': Sddcs,
        'Subscriptions': Subscriptions,
        'Tasks': Tasks,
        'account_link': 'com.vmware.vmc.orgs.account_link_client.StubFactory',
        'reservations': 'com.vmware.vmc.orgs.reservations_client.StubFactory',
        'sddcs': 'com.vmware.vmc.orgs.sddcs_client.StubFactory',
        'storage': 'com.vmware.vmc.orgs.storage_client.StubFactory',
        'subscriptions': 'com.vmware.vmc.orgs.subscriptions_client.StubFactory',
        'tbrs': 'com.vmware.vmc.orgs.tbrs_client.StubFactory',
    }

