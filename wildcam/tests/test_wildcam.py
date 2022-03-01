"""
Unit and regression test for the wildcam package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import wildcam


def test_wildcam_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "wildcam" in sys.modules
