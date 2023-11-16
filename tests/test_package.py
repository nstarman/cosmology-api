from __future__ import annotations

import importlib.metadata

import cosmology_api as m


def test_version():
    assert importlib.metadata.version("cosmology_api") == m.__version__
