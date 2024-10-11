.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

##################
Code Block Buttons
##################
The *code block buttons* extension will add a copy and/or view button to all code blocks.

*****
Usage
*****
The extension can be enabled by adding :python:`'sanderthedragon.codeblockbuttons'` to the :python:`extensions` list in :file:`conf.py`.

*************
Configuration
*************

==========
cb_default
==========
:python:`cb_default` can be set to select the default buttons to show, it defaults to :python:`'cbd-copy'`.
Valid values are:

- :python:`'cbd-all'`: show the copy and view button.
- :python:`'cbd-copy'`: show the copy button only.
- :python:`'cbd-view'`: show the view button only.
- :python:`'cbd-none'`: do not show either button.

Disabled buttons can be enabled for specific blocks by adding the :rst:`cb-all`, :rst:`cb-copy` or :rst:`cb-view` classes.

********
Examples
********
These examples assume :python:`cb_default` is :python:`'cbd-all'`.

=============
Copy and View
=============
The copy and view buttons are enabled by default, so just create a :rst:`code-block`, :rst:`literalinclude` or something similar.

.. code-block:: rst

   .. code-block:: rst

      I have copy and view buttons!

=========
Copy only
=========
The view button can be disabled by adding the :rst:`cb-noview` class.

.. code-block:: rst
   :class: cb-noview

   .. code-block:: rst
      :class: cb-noview

      I only have a copy button.

=========
View only
=========
The copy button can be disabled by adding the :rst:`cb-nocopy` class.

.. code-block:: rst
   :class: cb-nocopy

   .. code-block:: rst
      :class: cb-nocopy

      I only have a view button.

==========
No buttons
==========
The view and copy buttons can be disabled by adding the :rst:`cb-none` class, or both :rst:`cb-noview` and :rst:`cb-nocopy`.

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
