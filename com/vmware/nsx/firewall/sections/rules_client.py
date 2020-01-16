# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.firewall.sections.rules.
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


class Stats(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Stats.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Stats.get`.

    """
    GET_0_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Stats.get_0`.

    """
    GET_0_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Stats.get_0`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.sections.rules.stats'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatsStub)


    def get(self,
            section_id,
            source=None,
            ):
        """
        Get aggregated statistics for all rules for a given firewall section.
        The API only supports access to cached (source=cached) statistical data
        collected offline in the system. Data includes total number of packets,
        bytes, sessions counters and popularity index for a firewall rule and
        overall session count, max session count and max popularity index for
        all firewall rules on transport nodes or edge nodes. Aggregated
        statistics like maximum popularity index, maximum session count and
        total session count are computed with lower frequency compared to
        individual generic rule statistics, hence they may have a computation
        delay up to 15 minutes to reflect in response to this API.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallStatsList`
        :return: com.vmware.nsx.model.FirewallStatsList
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
                            'section_id': section_id,
                            'source': source,
                            })

    def get_0(self,
              section_id,
              rule_id,
              source=None,
              ):
        """
        Get aggregated statistics for a rule for given firewall section. The
        API only supports access to cached (source=cached) statistical data
        collected offline in the system. Data includes total number of packets,
        bytes, sessions counters and popularity index for a firewall rule and
        overall session count, max session count and max popularity index for
        all firewall rules on transport nodes or edge nodes. Aggregated
        statistics like maximum popularity index, maximum session count and
        total session count are computed with lower frequency compared to
        individual generic rule statistics, hence they may have a computation
        delay up to 15 minutes to reflect in response to this API.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallStats`
        :return: com.vmware.nsx.model.FirewallStats
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
                            'section_id': section_id,
                            'rule_id': rule_id,
                            'source': source,
                            })
class _StatsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/firewall/sections/{section-id}/rules/stats',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'rule_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
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
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/firewall/sections/{section-id}/rules/{rule-id}/stats',
            path_variables={
                'section_id': 'section-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStatsList'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStats'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.firewall.sections.rules.stats',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Stats': Stats,
    }

