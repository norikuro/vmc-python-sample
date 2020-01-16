# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.traceflows.
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


class Observations(VapiInterface):
    """
    
    """
    LIST_COMPONENT_TYPE_PHYSICAL = "PHYSICAL"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_LR = "LR"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_LS = "LS"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_DFW = "DFW"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_BRIDGE = "BRIDGE"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_EDGE_TUNNEL = "EDGE_TUNNEL"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_EDGE_HOSTSWITCH = "EDGE_HOSTSWITCH"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_COMPONENT_TYPE_UNKNOWN = "UNKNOWN"
    """
    Possible value for ``componentType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONFORWARDED = "TraceflowObservationForwarded"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONDROPPED = "TraceflowObservationDropped"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONDELIVERED = "TraceflowObservationDelivered"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONRECEIVED = "TraceflowObservationReceived"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONFORWARDEDLOGICAL = "TraceflowObservationForwardedLogical"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONDROPPEDLOGICAL = "TraceflowObservationDroppedLogical"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """
    LIST_RESOURCE_TYPE_TRACEFLOWOBSERVATIONRECEIVEDLOGICAL = "TraceflowObservationReceivedLogical"
    """
    Possible value for ``resourceType`` of method :func:`Observations.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.traceflows.observations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ObservationsStub)


    def list(self,
             traceflow_id,
             component_name=None,
             component_type=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             resource_type=None,
             sort_ascending=None,
             sort_by=None,
             transport_node_name=None,
             ):
        """
        Get observations for the Traceflow round

        :type  traceflow_id: :class:`str`
        :param traceflow_id: (required)
        :type  component_name: :class:`str` or ``None``
        :param component_name: Observations having the given component name will be listed.
            (optional)
        :type  component_type: :class:`str` or ``None``
        :param component_type: Observations having the given component type will be listed.
            (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: The type of observations that will be listed. (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  transport_node_name: :class:`str` or ``None``
        :param transport_node_name: Observations having the given transport node name will be listed.
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TraceflowObservationListResult`
        :return: com.vmware.nsx.model.TraceflowObservationListResult
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
        return self._invoke('list',
                            {
                            'traceflow_id': traceflow_id,
                            'component_name': component_name,
                            'component_type': component_type,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'resource_type': resource_type,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'transport_node_name': transport_node_name,
                            })
class _ObservationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'traceflow_id': type.StringType(),
            'component_name': type.OptionalType(type.StringType()),
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'resource_type': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'transport_node_name': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
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
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/traceflows/{traceflow-id}/observations',
            path_variables={
                'traceflow_id': 'traceflow-id',
            },
            query_parameters={
                'component_name': 'component_name',
                'component_type': 'component_type',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'resource_type': 'resource_type',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'transport_node_name': 'transport_node_name',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TraceflowObservationListResult'),
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
            self, iface_name='com.vmware.nsx.traceflows.observations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Observations': Observations,
    }

