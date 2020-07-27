# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.additional_properties_integer import AdditionalPropertiesInteger


class TestAdditionalPropertiesInteger(unittest.TestCase):
    """AdditionalPropertiesInteger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdditionalPropertiesInteger(self):
        """Test AdditionalPropertiesInteger"""
        # can make model without additional properties
        model = AdditionalPropertiesInteger()

        # can make one with additional properties
        model = AdditionalPropertiesInteger(some_key=3)
        assert model['some_key'] == 3

        # type checking works on additional properties
        with self.assertRaises(petstore_api.ApiTypeError) as exc:
            model = AdditionalPropertiesInteger(some_key=11.3)


if __name__ == '__main__':
    unittest.main()
