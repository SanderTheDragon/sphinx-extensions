.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

################
Mapped Link Role
################
The *mapped link role* extension adds roles based on a mapping which will create links possibly based on a other mapping.

*****
Usage
*****
The extension can be enabled by adding ``sanderthedragon.mappedlinkrole`` to your extensions in :file:`conf.py`.

The main mapping is done by creating a ``role_mapping`` dictionary in :file:`conf.py`.
The keys of the dictionary can then be used as role in :file:`.rst` files.
The values should be URLs containing at least one ``{}`` which will be replaced based on the value, or ``None``.

Each of the keys of the dictionary can be used to create its own mapping.
The mapping should be called ``{key}_mapping``, where ``{key}`` should be replaced by the key.
The keys are what is used as value in the role, the value is then used to replace the ``{}``, or completely if ``None`` was used.

********
Examples
********

==============
Simple Mapping
==============
The most simple way is to just create a ``role_mapping`` in :file:`conf.py`, like this for Wikipedia.

.. code-block:: py
   :class: cb-none

   role_mapping = {
       'wikipedia': 'https://en.wikipedia.org/wiki/{}'
   }

Now the ``wikipedia`` role is available, and can be used like this.

.. code-block:: rst
   :class: cb-none

   This document is written in :wikipedia:`reStructuredText`.

This document is written in :wikipedia:`reStructuredText`.

=====================
More Advanced Mapping
=====================
Continuing with the previous example, and the same :file:`conf.py`.

.. code-block:: rst
   :class: cb-none

   :wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx`.

.. ...

:wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx <!Sphinx>`.

--------

This will now go to the wrong Sphinx, the right link is ``Sphinx_(documentation_generator)`` so this will work.

.. code-block:: rst
   :class: cb-none

   :wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx_(documentation_generator)`.

:wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx_(documentation_generator)`.

--------

The text is wrong now, the following fixes it.

.. code-block:: rst
   :class: cb-none

   :wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx <Sphinx_(documentation_generator)>`.

:wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx <Sphinx_(documentation_generator)>`.

--------

But that is pretty long to type often, an extra mapping can help, change :file:`conf.py` like this.

.. code-block:: py
   :class: cb-none

   role_mapping = {
       'wikipedia': 'https://en.wikipedia.org/wiki/{}'
   }

   wikipedia_mapping = {
       'Sphinx': 'Sphinx_(documentation_generator)'
   }

And now the first way can be used, only pointing to the correct page now.

.. code-block:: rst
   :class: cb-none

   :wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx`.

:wikipedia:`reStructuredText` can be compiled using :wikipedia:`Sphinx`.

============
None Mapping
============
When setting the value in ``role_mapping`` to ``None``, an extra mapping is required.
This can only be used for complete URLs, and can be used as a nicer way to link to external websites.

.. code-block:: py
   :class: cb-none

   role_mapping = {
       'extern': None
   }

   extern_mapping = {
       'Sphinx': 'https://www.sphinx-doc.org'
   }

Now the ``extern`` role is available, and can be used like this.

.. code-block:: rst
   :class: cb-none

   Sphinx documentation is available :extern:`here <Sphinx>`.

Sphinx documentation is available :extern:`here <Sphinx>`.

=======
Anchors
=======
It is also possible to define an anchor for the URL, for instance with the Wikipedia role.

.. code-block:: rst
   :class: cb-none

   :wikipedia:`Lists in reStructuredText <reStructuredText:Lists>`.

:wikipedia:`Lists in reStructuredText <reStructuredText:Lists>`.

.. note::

   Internal anchors will automatically be converted to :extern:`Sphinx` identifiers.

============
Special Case
============
Since the ``:`` is used to split key and anchor, it will cause problem if your text has a ``:`` in it.
Like when referencing C++ classes or functions.

.. code-block:: rst
   :class: cb-none

   :cppreference:`std::vector` is a container type.

:cppreference:`std::vector` is a container type.

--------

But that will turn into ``https://en.cppreference.com/w/cpp/std:#vector``.
This can be fixed by adding ``<:>``.

.. code-block:: rst
   :class: cb-none

   :cppreference:`std::vector <:>` is a container type.

:cppreference:`std::vector <:>` is a container type.
