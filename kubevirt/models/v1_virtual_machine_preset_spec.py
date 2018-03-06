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


class V1VirtualMachinePresetSpec(object):
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
        'domain': 'V1DomainSpec',
        'selector': 'V1LabelSelector'
    }

    attribute_map = {
        'domain': 'domain',
        'selector': 'selector'
    }

    def __init__(self, domain=None, selector=None):
        """
        V1VirtualMachinePresetSpec - a model defined in Swagger
        """

        self._domain = None
        self._selector = None

        if domain is not None:
          self.domain = domain
        self.selector = selector

    @property
    def domain(self):
        """
        Gets the domain of this V1VirtualMachinePresetSpec.
        Domain is the same object type as contained in VirtualMachineSpec

        :return: The domain of this V1VirtualMachinePresetSpec.
        :rtype: V1DomainSpec
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this V1VirtualMachinePresetSpec.
        Domain is the same object type as contained in VirtualMachineSpec

        :param domain: The domain of this V1VirtualMachinePresetSpec.
        :type: V1DomainSpec
        """

        self._domain = domain

    @property
    def selector(self):
        """
        Gets the selector of this V1VirtualMachinePresetSpec.
        Selector is a label query over a set of VMs. Required.

        :return: The selector of this V1VirtualMachinePresetSpec.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1VirtualMachinePresetSpec.
        Selector is a label query over a set of VMs. Required.

        :param selector: The selector of this V1VirtualMachinePresetSpec.
        :type: V1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")

        self._selector = selector

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
        if not isinstance(other, V1VirtualMachinePresetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other