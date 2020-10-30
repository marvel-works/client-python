# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NetworkConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_network_interface': 'str',
        'permit_bridge_interface_on_pod_network': 'bool',
        'permit_slirp_interface': 'bool'
    }

    attribute_map = {
        'default_network_interface': 'defaultNetworkInterface',
        'permit_bridge_interface_on_pod_network': 'permitBridgeInterfaceOnPodNetwork',
        'permit_slirp_interface': 'permitSlirpInterface'
    }

    def __init__(self, default_network_interface=None, permit_bridge_interface_on_pod_network=None, permit_slirp_interface=None):
        """
        V1NetworkConfiguration - a model defined in Swagger
        """

        self._default_network_interface = None
        self._permit_bridge_interface_on_pod_network = None
        self._permit_slirp_interface = None

        if default_network_interface is not None:
          self.default_network_interface = default_network_interface
        if permit_bridge_interface_on_pod_network is not None:
          self.permit_bridge_interface_on_pod_network = permit_bridge_interface_on_pod_network
        if permit_slirp_interface is not None:
          self.permit_slirp_interface = permit_slirp_interface

    @property
    def default_network_interface(self):
        """
        Gets the default_network_interface of this V1NetworkConfiguration.

        :return: The default_network_interface of this V1NetworkConfiguration.
        :rtype: str
        """
        return self._default_network_interface

    @default_network_interface.setter
    def default_network_interface(self, default_network_interface):
        """
        Sets the default_network_interface of this V1NetworkConfiguration.

        :param default_network_interface: The default_network_interface of this V1NetworkConfiguration.
        :type: str
        """

        self._default_network_interface = default_network_interface

    @property
    def permit_bridge_interface_on_pod_network(self):
        """
        Gets the permit_bridge_interface_on_pod_network of this V1NetworkConfiguration.

        :return: The permit_bridge_interface_on_pod_network of this V1NetworkConfiguration.
        :rtype: bool
        """
        return self._permit_bridge_interface_on_pod_network

    @permit_bridge_interface_on_pod_network.setter
    def permit_bridge_interface_on_pod_network(self, permit_bridge_interface_on_pod_network):
        """
        Sets the permit_bridge_interface_on_pod_network of this V1NetworkConfiguration.

        :param permit_bridge_interface_on_pod_network: The permit_bridge_interface_on_pod_network of this V1NetworkConfiguration.
        :type: bool
        """

        self._permit_bridge_interface_on_pod_network = permit_bridge_interface_on_pod_network

    @property
    def permit_slirp_interface(self):
        """
        Gets the permit_slirp_interface of this V1NetworkConfiguration.

        :return: The permit_slirp_interface of this V1NetworkConfiguration.
        :rtype: bool
        """
        return self._permit_slirp_interface

    @permit_slirp_interface.setter
    def permit_slirp_interface(self, permit_slirp_interface):
        """
        Sets the permit_slirp_interface of this V1NetworkConfiguration.

        :param permit_slirp_interface: The permit_slirp_interface of this V1NetworkConfiguration.
        :type: bool
        """

        self._permit_slirp_interface = permit_slirp_interface

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
        if not isinstance(other, V1NetworkConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
