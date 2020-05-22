picklecat
=========

A tiny script for concatenating or merging pickled Python 3 object, lists, and dictionaries.

Example usage:

.. code-block:: bash

    # a.pkl pickles "a"
    # b.pkl pickles "b"

    picklecat a.pkl b.pkl > c.pkl

    # c.pkl pickles ["a", "b"]
