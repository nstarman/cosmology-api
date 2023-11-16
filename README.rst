Cosmology API
=============

.. container::

    |Actions Status| |ReadTheDocs Status| |PyPI Status| |Conda Status| |GitHub Discussions|

There are a lot of (Python) cosmology libraries out there, from big projects --
including `Astropy <https://docs.astropy.org/en/stable/cosmology/index.html>`_,
`CLASS <http://class-code.net>`_, and `CAMB
<https://camb.readthedocs.io/en/latest/>`_ -- down to small personal scripts.
These libraries perform many of the same tasks, but they all have different
interfaces, and different ways of doing things. This makes it hard to switch
between libraries, and nearly impossible to write code that works with multiple
libraries.

The Cosmology API for Python solves this problem, providing detailed interfaces
for cosmology codes, from individual methods and functions up to fully-featured
cosmology objects, even whole libraries. Best of all, using the Cosmology API
does not require any run-time dependencies, even this library!

With the Cosmology API you can **write code that works with anything that
implements the API**, i.e many different cosmology libraries. We provide the
easy-to-use, well-defined descriptions, you can build functions that work with
any supporting library. For example

.. skip: next
.. code-block:: python

   # No implementation, just a description of the interface!
   from cosmology.api import StandardCosmology


   def flat_angular_diameter_distance(
       cosmo: StandardCosmology[Array, Array], z: Array
   ) -> Array:
       # Do some cosmology with any object that implements the API
       if cosmo.Omega_k != 0:
           raise ValueError("This function only works for flat cosmologies")
       return cosmo.comoving_distance(z) / (1 + z)


.. |Actions Status| image:: https://github.com/cosmology-api/cosmology.api/workflows/CI/badge.svg
    :target: https://github.com/cosmology-api/cosmology.api/actions
    :alt: Astropy's GitHub Actions CI Status

.. |ReadTheDocs Status| image:: https://readthedocs.org/projects/cosmology.api/badge/?version=latest
    :target: https://cosmology.api.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |PyPI Status| image:: https://img.shields.io/pypi/v/cosmology.api
    :target: https://pypi.org/project/cosmology.api/
    :alt: Documentation Status

.. |Conda Status| image:: https://img.shields.io/conda/vn/conda-forge/cosmology.api
    :target: https://github.com/conda-forge/cosmology.api-feedstock
    :alt: Conda Status

.. |GitHub Discussions| image:: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
    :target: https://github.com/orgs/cosmology-api/discussions
    :alt: GitHub Discussions
