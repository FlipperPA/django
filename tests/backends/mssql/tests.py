import unittest

from django.db import connection
from django.utils.version import get_version_tuple
from django.test import (
    TestCase, TransactionTestCase, override_settings, skipIfDBFeature,
)
from ..models import Author, Item, Object, Square


print("VENDOR", connection.vendor)
@unittest.skipUnless(
    connection.vendor == 'mssql', 'Microsoft SQL Server tests'
)
class Tests(TestCase):
    longMessage = True

    def test_check_pyodbc_version(self):
        print("RUNNING CHECK TEST...")
        try:
            from pyodbc import version
        except ImportError:
            self.fail("pyodbc is not installed.")

        pyodbc_version = get_version_tuple(version)
        self.assertTrue(pyodbc_version > (3, 0))
