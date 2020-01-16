# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.storage.
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


class ClusterConstraints(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.storage.cluster_constraints'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterConstraintsStub)


    def get(self,
            org,
            provider,
            num_hosts,
            one_node_reduced_capacity=None,
            ):
        """
        Get constraints on cluster storage size for EBS-backed clusters.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  provider: :class:`str`
        :param provider: Cloud storage provider ID (example AWS) (required)
        :type  num_hosts: :class:`long`
        :param num_hosts: Number of hosts in cluster (required)
        :type  one_node_reduced_capacity: :class:`bool` or ``None``
        :param one_node_reduced_capacity: Whether this sddc is reduced capacity 1NODE. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.VsanConfigConstraints`
        :return: com.vmware.vmc.model.VsanConfigConstraints
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid or missing parameters
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'provider': provider,
                            'num_hosts': num_hosts,
                            'one_node_reduced_capacity': one_node_reduced_capacity,
                            })
class _ClusterConstraintsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'provider': type.StringType(),
            'num_hosts': type.IntegerType(),
            'one_node_reduced_capacity': type.OptionalType(type.BooleanType()),
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
            url_template='/vmc/api/orgs/{org}/storage/cluster-constraints',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'provider': 'provider',
                'num_hosts': 'num_hosts',
                'one_node_reduced_capacity': 'one_node_reduced_capacity',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'VsanConfigConstraints'),
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
            self, iface_name='com.vmware.vmc.orgs.storage.cluster_constraints',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ClusterConstraints': ClusterConstraints,
    }

