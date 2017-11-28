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


class V1MigrationSpec(object):
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
        'node_selector': 'object',
        'selector': 'V1VMSelector'
    }

    attribute_map = {
        'node_selector': 'nodeSelector',
        'selector': 'selector'
    }

    def __init__(self, node_selector=None, selector=None):
        """
        V1MigrationSpec - a model defined in Swagger
        """

        self._node_selector = None
        self._selector = None

        if node_selector is not None:
          self.node_selector = node_selector
        self.selector = selector

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1MigrationSpec.
        Criteria to use when selecting the destination for the migration for example, to select by the hostname, specify `kubernetes.io/hostname: master` other possible choices include the hardware required to run the vm or or lableing of the nodes to indicate their roles in larger applications. examples: disktype: ssd, randomGenerator: /dev/random, randomGenerator: superfastdevice, app: mysql, licensedForServiceX: true Note that these selectors are additions to the node selectors on the VM itself and they must not exist on the VM. If they are conflicting with the VM, no migration will be started.

        :return: The node_selector of this V1MigrationSpec.
        :rtype: object
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1MigrationSpec.
        Criteria to use when selecting the destination for the migration for example, to select by the hostname, specify `kubernetes.io/hostname: master` other possible choices include the hardware required to run the vm or or lableing of the nodes to indicate their roles in larger applications. examples: disktype: ssd, randomGenerator: /dev/random, randomGenerator: superfastdevice, app: mysql, licensedForServiceX: true Note that these selectors are additions to the node selectors on the VM itself and they must not exist on the VM. If they are conflicting with the VM, no migration will be started.

        :param node_selector: The node_selector of this V1MigrationSpec.
        :type: object
        """

        self._node_selector = node_selector

    @property
    def selector(self):
        """
        Gets the selector of this V1MigrationSpec.
        Criterias for selecting the VM to migrate. For example selector:   name: testvm will select the VM `testvm` for migration

        :return: The selector of this V1MigrationSpec.
        :rtype: V1VMSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1MigrationSpec.
        Criterias for selecting the VM to migrate. For example selector:   name: testvm will select the VM `testvm` for migration

        :param selector: The selector of this V1MigrationSpec.
        :type: V1VMSelector
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
        if not isinstance(other, V1MigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other