.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>

.. SPDX-License-Identifier: CC-BY-SA-4.0

##################
Code Block Buttons
##################
The *code block buttons* extension will add a copy and view button to all code blocks.

*****
Usage
*****
The extension can be enabled by adding ``sanderthedragon.codeblockbuttons`` to your extensions in :file:`conf.py`.

*************
Configuration
*************

==========
cb_default
==========
``cb_default`` can be set to select the default buttons to show, it defaults to ``'cbd-all'``.
Valid values are:

- ``'cbd-all'``: show the copy and view buttons.
- ``'cbd-copy'``: show the copy button only.
- ``'cbd-view'``: show the view button only.
- ``'cbd-none'``: show no buttons.

Disabled buttons can be enabled for specific blocks by adding the ``cb-all``, ``cb-copy`` or ``cb-view`` classes.

********
Examples
********
These examples assume ``cb_default`` is ``'cbd-all'`` (or not defined).

=============
Copy and View
=============
The copy and view buttons are enabled by default, so just create a ``code-block``, ``literalinclude`` or something similar.

.. code-block:: rst

   .. code-block:: rst

      I have copy and view buttons!

=========
Copy only
=========
The view button can be disabled by adding the ``cb-noview`` class.

.. code-block:: rst
   :class: cb-noview

   .. code-block:: rst
      :class: cb-noview

      I only have a copy button.

=========
View only
=========
The copy button can be disabled by adding the ``cb-nocopy`` class.

.. code-block:: rst
   :class: cb-nocopy

   .. code-block:: rst
      :class: cb-nocopy

      I only have a view button.

==========
No buttons
==========
The view and copy buttons can be disabled by adding the ``cb-none`` class, or both ``cb-noview`` and ``cb-nocopy``.

.. code-block:: rst
   :class: cb-none

   .. code-block:: rst
      :class: cb-none

      I have no buttons. :(

*********
3rd Party
*********
:extern:`clipboard.js`, licensed under :license:`MIT`, is used for copying code.

Icons are from :extern:`Tabler Icons`, licensed under :license:`MIT`.
