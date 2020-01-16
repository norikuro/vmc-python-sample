# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.
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


class Locale(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.locale'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LocaleStub)


    def set(self,
            vmc_locale,
            ):
        """
        Sets the locale for the session which is used for translating
        responses.

        :type  vmc_locale: :class:`com.vmware.vmc.model_client.VmcLocale`
        :param vmc_locale: The locale to be set. (required)
        :rtype: :class:`com.vmware.vmc.model_client.VmcLocale`
        :return: com.vmware.vmc.model.VmcLocale
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('set',
                            {
                            'vmc_locale': vmc_locale,
                            })
class Orgs(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OrgsStub)


    def get(self,
            org,
            ):
        """
        Get details of organization

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Organization`
        :return: com.vmware.vmc.model.Organization
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Organization doesn't exist
        """
        return self._invoke('get',
                            {
                            'org': org,
                            })

    def list(self):
        """
        Return a list of all organizations the calling user (based on
        credential) is authorized on.


        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.Organization`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list', None)
class _LocaleStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'vmc_locale': type.ReferenceType('com.vmware.vmc.model_client', 'VmcLocale'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/locale',
            request_body_parameter='vmc_locale',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'set': {
                'input_type': set_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'VmcLocale'),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.locale',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _OrgsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
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
            url_template='/vmc/api/orgs/{org}',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/vmc/api/orgs',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Organization'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'Organization')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Locale': Locale,
        'Orgs': Orgs,
        'model': 'com.vmware.vmc.model_client.StubFactory',
        'orgs': 'com.vmware.vmc.orgs_client.StubFactory',
    }

