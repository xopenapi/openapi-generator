# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import petstore_api
from petstore_api.models.map_test import MapTest  # noqa: E501
from petstore_api.rest import ApiException

class TestMapTest(unittest.TestCase):
    """MapTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MapTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = petstore_api.models.map_test.MapTest()  # noqa: E501
        if include_optional :
            return MapTest(
                map_map_of_string = {
                    'key' : {
                        'key' : '0'
                        }
                    }, 
                map_of_enum_string = {
                    'UPPER' : 'UPPER'
                    }, 
                direct_map = {
                    'key' : True
                    }, 
                indirect_map = {
                    'key' : True
                    }
            )
        else :
            return MapTest(
        )

    def testMapTest(self):
        """Test MapTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
