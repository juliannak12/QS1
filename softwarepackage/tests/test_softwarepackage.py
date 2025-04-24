"""
Unit and regression test for the softwarepackage package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import softwarepackage


def test_softwarepackage_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "softwarepackage" in sys.modules
