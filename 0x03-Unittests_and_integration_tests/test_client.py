#!/usr/bin/env python3
"""A module for testing the client module"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """a class to test 'GithubOrgClient'"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch(
        "client.get_json", return_value={"payload": True})
