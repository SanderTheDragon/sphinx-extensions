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
The extension can be enabled by adding :python:`'sanderthedragon.mappedlinkrole'` to the :python:`extensions` list in :file:`conf.py`.

The main mapping is done by creating a :python:`role_mapping` dictionary in :file:`conf.py`.
The keys of the dictionary can then be used as role in :file:`.rst` files.
The values should be URLs containing at least one :python:`{}` which will be replaced based on the value, or :python:`None`.

Each of the keys of the dictionary can be used to create its own mapping.
The mapping should be called :python:`{key}_mapping`, where :python:`{key}` should be replaced by the key.
The keys are what is used as value in the role, the value is then used to replace the :python:`{}`, or completely if :python:`None` was used.

********
Examples
********

==============
Simple Mapping
==============
The most simple way is to just create a :python:`role_mapping` in :file:`conf.py`, like this for Wikipedia.

.. code-block:: py
   :class: cb-none

   role_mapping = {
       'wikipedia': 'https://en.wikipedia.org/wiki/{}'
   }

Now the :rst:`wikipedia` role is available, and can be used like this.

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
When setting the value in :python:`role_mapping` to :python:`None`, an extra mapping is required.
This can only be used for complete URLs, and can be used as a nicer way to link to external websites.

.. code-block:: py
   :class: cb-none

   role_mapping = {
       'extern': None
   }

   extern_mapping = {
       'Sphinx': 'https://www.sphinx-doc.org'
   }

Now the :rst:`extern` role is available, and can be used like this.

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

Internal Anchors
----------------
Anchors for internal references are automatically converted to :extern:`Sphinx` identifiers.
So it can be directly referred to the by title.

.. code-block:: rst
   :class: cb-none

   :extension:`This will link to this section <Mapped Link Role:Internal Anchors>`

:extension:`This will link to this section <Mapped Link Role:Internal Anchors>`

.. warning::

   If the title is not unique within a document, then this will link to the first occurrence.

============
Special Case
============
Since the ``:`` is used to split key and anchor, it will cause problem if your text has a ``:`` in it.
Like when referencing C++ classes or functions, using a mapping like :python:`'cppreference': 'https://en.cppreference.com/w/cpp/{}'`.

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

Anchors
-------
If an anchor is needed, then the key needs to be repeated.

.. code-block:: rst
   :class: cb-none

   Member functions of :cppreference:`std::vector <std::vector:Member_functions>`.

Member functions of :cppreference:`std::vector <std::vector:Member_functions>`.
