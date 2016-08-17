# coding: utf-8

"""
    Samsara API


    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_fleet_locations(self, access_token, group_param, **kwargs):
        """
        Get the GPS locations for all vehicles in the group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fleet_locations(access_token, group_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param GroupParam group_param:  (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_fleet_locations_with_http_info(access_token, group_param, **kwargs)
        else:
            (data) = self.get_fleet_locations_with_http_info(access_token, group_param, **kwargs)
            return data

    def get_fleet_locations_with_http_info(self, access_token, group_param, **kwargs):
        """
        Get the GPS locations for all vehicles in the group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fleet_locations_with_http_info(access_token, group_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param GroupParam group_param:  (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'group_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fleet_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_fleet_locations`")
        # verify the required parameter 'group_param' is set
        if ('group_param' not in params) or (params['group_param'] is None):
            raise ValueError("Missing the required parameter `group_param` when calling `get_fleet_locations`")

        resource_path = '/fleet/locations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_param' in params:
            body_params = params['group_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse200',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_fleet_trips(self, access_token, trips_param, **kwargs):
        """
        Get the trips for the specified vehicle.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fleet_trips(access_token, trips_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param TripsParam trips_param:  (required)
        :return: TripResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_fleet_trips_with_http_info(access_token, trips_param, **kwargs)
        else:
            (data) = self.get_fleet_trips_with_http_info(access_token, trips_param, **kwargs)
            return data

    def get_fleet_trips_with_http_info(self, access_token, trips_param, **kwargs):
        """
        Get the trips for the specified vehicle.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fleet_trips_with_http_info(access_token, trips_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param TripsParam trips_param:  (required)
        :return: TripResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'trips_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fleet_trips" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_fleet_trips`")
        # verify the required parameter 'trips_param' is set
        if ('trips_param' not in params) or (params['trips_param'] is None):
            raise ValueError("Missing the required parameter `trips_param` when calling `get_fleet_trips`")

        resource_path = '/fleet/trips'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'trips_param' in params:
            body_params = params['trips_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TripResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sensors(self, access_token, group_param, **kwargs):
        """
        Get the sensors for a group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors(access_token, group_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param GroupParam group_param:  (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sensors_with_http_info(access_token, group_param, **kwargs)
        else:
            (data) = self.get_sensors_with_http_info(access_token, group_param, **kwargs)
            return data

    def get_sensors_with_http_info(self, access_token, group_param, **kwargs):
        """
        Get the sensors for a group.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_with_http_info(access_token, group_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param GroupParam group_param:  (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'group_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_sensors`")
        # verify the required parameter 'group_param' is set
        if ('group_param' not in params) or (params['group_param'] is None):
            raise ValueError("Missing the required parameter `group_param` when calling `get_sensors`")

        resource_path = '/sensors/list'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'group_param' in params:
            body_params = params['group_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sensors_history(self, access_token, history_param, **kwargs):
        """
        Get the historical data for the sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_history(access_token, history_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param HistoryParam history_param:  (required)
        :return: SensorHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sensors_history_with_http_info(access_token, history_param, **kwargs)
        else:
            (data) = self.get_sensors_history_with_http_info(access_token, history_param, **kwargs)
            return data

    def get_sensors_history_with_http_info(self, access_token, history_param, **kwargs):
        """
        Get the historical data for the sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_history_with_http_info(access_token, history_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param HistoryParam history_param:  (required)
        :return: SensorHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'history_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_sensors_history`")
        # verify the required parameter 'history_param' is set
        if ('history_param' not in params) or (params['history_param'] is None):
            raise ValueError("Missing the required parameter `history_param` when calling `get_sensors_history`")

        resource_path = '/sensors/history'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'history_param' in params:
            body_params = params['history_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SensorHistoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sensors_humidity(self, access_token, sensor_param, **kwargs):
        """
        Get the current humidity readings for the specified sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_humidity(access_token, sensor_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param SensorParam sensor_param:  (required)
        :return: HumidityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sensors_humidity_with_http_info(access_token, sensor_param, **kwargs)
        else:
            (data) = self.get_sensors_humidity_with_http_info(access_token, sensor_param, **kwargs)
            return data

    def get_sensors_humidity_with_http_info(self, access_token, sensor_param, **kwargs):
        """
        Get the current humidity readings for the specified sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_humidity_with_http_info(access_token, sensor_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param SensorParam sensor_param:  (required)
        :return: HumidityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'sensor_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_humidity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_sensors_humidity`")
        # verify the required parameter 'sensor_param' is set
        if ('sensor_param' not in params) or (params['sensor_param'] is None):
            raise ValueError("Missing the required parameter `sensor_param` when calling `get_sensors_humidity`")

        resource_path = '/sensors/humidity'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensor_param' in params:
            body_params = params['sensor_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HumidityResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_sensors_temperature(self, access_token, sensor_param, **kwargs):
        """
        Get the current temperature readings for the specified sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_temperature(access_token, sensor_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param SensorParam sensor_param:  (required)
        :return: TemperatureResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sensors_temperature_with_http_info(access_token, sensor_param, **kwargs)
        else:
            (data) = self.get_sensors_temperature_with_http_info(access_token, sensor_param, **kwargs)
            return data

    def get_sensors_temperature_with_http_info(self, access_token, sensor_param, **kwargs):
        """
        Get the current temperature readings for the specified sensors.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sensors_temperature_with_http_info(access_token, sensor_param, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str access_token:  (required)
        :param SensorParam sensor_param:  (required)
        :return: TemperatureResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'sensor_param']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_temperature" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_sensors_temperature`")
        # verify the required parameter 'sensor_param' is set
        if ('sensor_param' not in params) or (params['sensor_param'] is None):
            raise ValueError("Missing the required parameter `sensor_param` when calling `get_sensors_temperature`")

        resource_path = '/sensors/temperature'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'access_token' in params:
            query_params['access_token'] = params['access_token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensor_param' in params:
            body_params = params['sensor_param']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TemperatureResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
