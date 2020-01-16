# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.draas.
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


class ReplicaDiskCollections(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.draas.replica_disk_collections'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReplicaDiskCollectionsStub)


    def get(self,
            org,
            sddc,
            datastore_mo_id=None,
            ):
        """
        Query replica disk collections

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  datastore_mo_id: :class:`str` or ``None``
        :param datastore_mo_id: Represents the datastore moref id to search. (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.draas.model_client.ReplicaDiskCollection`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'datastore_mo_id': datastore_mo_id,
                            })
class SiteRecovery(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.draas.site_recovery'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SiteRecoveryStub)


    def delete(self,
               org,
               sddc,
               force=None,
               deactivate_hcx=None,
               ):
        """
        Deactivate site recovery for the specified sddc

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  force: :class:`bool` or ``None``
        :param force: If = 'true', will deactivate site recovery forcefully. (optional)
        :type  deactivate_hcx: :class:`bool` or ``None``
        :param deactivate_hcx: If = 'true', will deactivate HCX. (optional)
        :rtype: :class:`com.vmware.vmc.draas.model_client.Task`
        :return: com.vmware.vmc.draas.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find site recovery configuration for sddc identifier
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'force': force,
                            'deactivate_hcx': deactivate_hcx,
                            })

    def get(self,
            org,
            sddc,
            ):
        """
        Query site recovery configuration for the specified sddc

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :rtype: :class:`com.vmware.vmc.draas.model_client.SiteRecovery`
        :return: com.vmware.vmc.draas.model.SiteRecovery
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })

    def post(self,
             org,
             sddc,
             activate_site_recovery_config=None,
             ):
        """
        Activate site recovery for the specified sddc

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  activate_site_recovery_config: :class:`com.vmware.vmc.draas.model_client.ActivateSiteRecoveryConfig` or ``None``
        :param activate_site_recovery_config: Customization, for example can specify custom extension key suffix
            for SRM. (optional)
        :rtype: :class:`com.vmware.vmc.draas.model_client.Task`
        :return: com.vmware.vmc.draas.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find site recovery configuration for sddc identifier
        """
        return self._invoke('post',
                            {
                            'org': org,
                            'sddc': sddc,
                            'activate_site_recovery_config': activate_site_recovery_config,
                            })
class SiteRecoverySrmNodes(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.draas.site_recovery_srm_nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SiteRecoverySrmNodesStub)


    def delete(self,
               org,
               sddc,
               srm_node,
               ):
        """
        Delete a SRM server.

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  srm_node: :class:`str`
        :param srm_node: SRM node identifier (required)
        :rtype: :class:`com.vmware.vmc.draas.model_client.Task`
        :return: com.vmware.vmc.draas.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find SDDC or SRM node
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'srm_node': srm_node,
                            })

    def post(self,
             org,
             sddc,
             provision_srm_config=None,
             ):
        """
        Provision an additional SRM server.

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  provision_srm_config: :class:`com.vmware.vmc.draas.model_client.ProvisionSrmConfig` or ``None``
        :param provision_srm_config: Customization, for example can specify custom extension key suffix
            for SRM. (optional)
        :rtype: :class:`com.vmware.vmc.draas.model_client.Task`
        :return: com.vmware.vmc.draas.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find site recovery configuration for sddc identifier
        """
        return self._invoke('post',
                            {
                            'org': org,
                            'sddc': sddc,
                            'provision_srm_config': provision_srm_config,
                            })
class SiteRecoveryVersions(VapiInterface):
    """
    
    """
    GET_VERSION_SOURCE_VAMICLI = "vamicli"
    """
    Possible value for ``versionSource`` of method
    :func:`SiteRecoveryVersions.get`.

    """
    GET_VERSION_SOURCE_LS = "ls"
    """
    Possible value for ``versionSource`` of method
    :func:`SiteRecoveryVersions.get`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.draas.site_recovery_versions'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SiteRecoveryVersionsStub)


    def get(self,
            org,
            sddc,
            version_source=None,
            ):
        """
        Query site recovery versions for the specified sddc

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  sddc: :class:`str`
        :param sddc: sddc identifier (required)
        :type  version_source: :class:`str` or ``None``
        :param version_source: Represents the source for getting the version from. (optional)
        :rtype: :class:`com.vmware.vmc.draas.model_client.SiteRecoveryVersions`
        :return: com.vmware.vmc.draas.model.SiteRecoveryVersions
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find site recovery versions for sddc identifier
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'version_source': version_source,
                            })
class Task(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.draas.task'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TaskStub)


    def get(self,
            org,
            task,
            ):
        """
        Retrieve details of a task.

        :type  org: :class:`str`
        :param org: Organization identifier (required)
        :type  task: :class:`str`
        :param task: task identifier (required)
        :rtype: :class:`com.vmware.vmc.draas.model_client.Task`
        :return: com.vmware.vmc.draas.model.Task
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
class _ReplicaDiskCollectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'datastore_mo_id': type.OptionalType(type.StringType()),
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
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery/replica-disk-collections',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'datastore_mo_id': 'datastore_mo_id',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.draas.model_client', 'ReplicaDiskCollection')),
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
            self, iface_name='com.vmware.vmc.draas.replica_disk_collections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SiteRecoveryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
            'deactivate_hcx': type.OptionalType(type.BooleanType()),
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
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'force': 'force',
                'deactivate_hcx': 'deactivate_hcx',
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
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'activate_site_recovery_config': type.OptionalType(type.ReferenceType('com.vmware.vmc.draas.model_client', 'ActivateSiteRecoveryConfig')),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery',
            request_body_parameter='activate_site_recovery_config',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'SiteRecovery'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'Task'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.draas.site_recovery',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SiteRecoverySrmNodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'srm_node': type.StringType(),
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
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery/srm-nodes/{srmNode}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'srm_node': 'srmNode',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'provision_srm_config': type.OptionalType(type.ReferenceType('com.vmware.vmc.draas.model_client', 'ProvisionSrmConfig')),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery/srm-nodes',
            request_body_parameter='provision_srm_config',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'Task'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.draas.site_recovery_srm_nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SiteRecoveryVersionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'version_source': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/draas/api/orgs/{org}/sddcs/{sddc}/site-recovery/versions',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'version_source': 'version_source',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'SiteRecoveryVersions'),
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
            self, iface_name='com.vmware.vmc.draas.site_recovery_versions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TaskStub(ApiInterfaceStub):
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
            url_template='/vmc/draas/api/orgs/{org}/tasks/{task}',
            path_variables={
                'org': 'org',
                'task': 'task',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.draas.model_client', 'Task'),
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
            self, iface_name='com.vmware.vmc.draas.task',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ReplicaDiskCollections': ReplicaDiskCollections,
        'SiteRecovery': SiteRecovery,
        'SiteRecoverySrmNodes': SiteRecoverySrmNodes,
        'SiteRecoveryVersions': SiteRecoveryVersions,
        'Task': Task,
        'model': 'com.vmware.vmc.draas.model_client.StubFactory',
    }

