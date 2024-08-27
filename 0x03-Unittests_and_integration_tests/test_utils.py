#!/usr/bin/env python3
"""A module for testing the utils module"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """a class to Test the 'access_nested_map' function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """method to test 'access_nested_map''s output"""
        self.assertEqual(access_nested_map(nested_map, path), answer)

    """to test key errors"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """method to test 'access_nested_map''s exception raising"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """a class to test the 'get_json' function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, get_mock):
        """method to test the 'get_json''s output"""
        get_mock.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ a class to test the 'memoize' function"""
    def test_memoize(self):
        """a method to test the 'memoize''s output"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once()
