import os
import pickle

import pytest

from picklecat import picklecat


@pytest.fixture(params=["dict", "list"])
def pickle_setup(request):
    filenames = ["__a.pkl", "__b.pkl", "__c.pkl"]

    if request.param == "object":
        vals = ["one", "two", "three"]
        concatenated = vals

    elif request.param == "dict":
        vals = [{"a": 1}, {"b": 2}, {"c": 3}]
        concatenated = {"a": 1, "b": 2, "c": 3}

    elif request.param == "list":
        vals = [[1, 2], [3, 4, 5], [6, 7]]
        concatenated = [1, 2, 3, 4, 5, 6, 7]

    for filename, val in zip(filenames, vals):
        with open(filename, "wb") as f:
            pickle.dump(val, f)

    yield filenames, concatenated

    for filename in filenames:
        os.remove(filename)


def test_picklecat(pickle_setup):
    filenames, expected_vals = pickle_setup
    vals = picklecat(*filenames)
    assert vals == expected_vals
