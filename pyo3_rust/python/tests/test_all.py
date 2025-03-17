import pytest
import pyo3_rust


def test_sum_as_string():
    assert pyo3_rust.sum_as_string(1, 1) == "2"
