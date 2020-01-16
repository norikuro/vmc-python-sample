# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.clusters.
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


class Reconfigure(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.clusters.reconfigure'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReconfigureStub)


    def cluster_reconfig(self,
                         org,
                         sddc,
                         cluster,
                         cluster_reconfigure_params,
                         ):
        """
        This reconfiguration will handle changing both the number of hosts and
        the cluster storage capacity.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  cluster: :class:`str`
        :param cluster: cluster identifier (required)
        :type  cluster_reconfigure_params: :class:`com.vmware.vmc.model_client.ClusterReconfigureParams`
        :param cluster_reconfigure_params: clusterReconfigureParams (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            Bad Request. The SDDC is not in a valid state. , Method not allowed
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the cluster with the given id
        """
        return self._invoke('cluster_reconfig',
                            {
                            'org': org,
                            'sddc': sddc,
                            'cluster': cluster,
                            'cluster_reconfigure_params': cluster_reconfigure_params,
                            })
class _ReconfigureStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cluster_reconfig operation
        cluster_reconfig_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'cluster': type.StringType(),
            'cluster_reconfigure_params': type.ReferenceType('com.vmware.vmc.model_client', 'ClusterReconfigureParams'),
        })
        cluster_reconfig_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        cluster_reconfig_input_value_validator_list = [
        ]
        cluster_reconfig_output_validator_list = [
        ]
        cluster_reconfig_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/clusters/{cluster}/reconfigure',
            request_body_parameter='cluster_reconfigure_params',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'cluster': 'cluster',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'cluster_reconfig': {
                'input_type': cluster_reconfig_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': cluster_reconfig_error_dict,
                'input_value_validator_list': cluster_reconfig_input_value_validator_list,
                'output_validator_list': cluster_reconfig_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'cluster_reconfig': cluster_reconfig_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.clusters.reconfigure',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Reconfigure': Reconfigure,
        'config': 'com.vmware.vmc.orgs.sddcs.clusters.config_client.StubFactory',
    }

