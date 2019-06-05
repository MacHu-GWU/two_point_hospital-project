# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import two_point_hospital
    from two_point_hospital.docs import doc_data


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
