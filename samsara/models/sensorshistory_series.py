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

from pprint import pformat
from six import iteritems
import re


class SensorshistorySeries(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, widget_id=None, field=None):
        """
        SensorshistorySeries - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'widget_id': 'int',
            'field': 'str'
        }

        self.attribute_map = {
            'widget_id': 'widgetId',
            'field': 'field'
        }

        self._widget_id = widget_id
        self._field = field

    @property
    def widget_id(self):
        """
        Gets the widget_id of this SensorshistorySeries.


        :return: The widget_id of this SensorshistorySeries.
        :rtype: int
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        """
        Sets the widget_id of this SensorshistorySeries.


        :param widget_id: The widget_id of this SensorshistorySeries.
        :type: int
        """

        self._widget_id = widget_id

    @property
    def field(self):
        """
        Gets the field of this SensorshistorySeries.


        :return: The field of this SensorshistorySeries.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this SensorshistorySeries.


        :param field: The field of this SensorshistorySeries.
        :type: str
        """
        allowed_values = ["ambientTemperature", "probeTemperature", "currentLoop1Raw", "currentLoop1Mapped", "currentLoop2Raw", "currentLoop2Mapped", "pmPowerTotal", "pmPhase1Power", "pmPhase2Power", "pmPhase3Power", "pmPhase1PowerFactor", "pmPhase2PowerFactor", "pmPhase3PowerFactor"]
        if field not in allowed_values:
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"
                .format(field, allowed_values)
            )

        self._field = field

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
