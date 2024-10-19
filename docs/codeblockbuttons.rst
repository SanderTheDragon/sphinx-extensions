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

Disabled buttons can be enabled for specific blocks by adding the :css:`cb-all`, :css:`cb-copy` or :css:`cb-view` classes.

=========
cb_hidden
=========
:python:`cb_hidden` can be set to :python:`True` to hide the buttons by default, they will then be shown when the user hovers over the code block.
By default it is set to :python:`False`, which will make the buttons always visible.

Hidden buttons can be shown for specific blocks by adding the :css:`cb-visible` class.
Visible buttons can be hidden for specific blocks by adding the :css:`cb-hidden` class.

========
cb_icons
========
The default icons can be overriden using the :python:`cb_icons` option, which should be defined as a :python:`dict`.
The key must be any of :python:`view`, :python:`copy`, :python:`copy-success`, or :python:`copy-error`, the value should be a base64 encoded SVG icon.
It is also possible to use another format than SVG, in which case the value should be the HTML :html:`<img>` encoded as base64.

========
cb_mimes
========
:python:`cb_mimes` can be set to a :python:`dict` to map highlight languages to MIME types which will be used for the view buttons.
The key should be the language as provided to a code block, the value should be the MIME type.
In case a language is not mapped here, then it will automatically select the first one from the :extern:`Pygments` mapping.
If there is no MIME type found in the :extern:`Pygments` mapping, then :python:`'text/plain'` will be used.

=============
cb_transition
=============
:python:`cb_transition` can be set to :python:`True` to enable CSS transitions, this is also the default setting.
Setting it to :python:`False` will disable the CSS transitions.

Transitions are implemented for icon color, tooltip opacity, and button opacity (if the buttons are hidden).

********
Examples
********

================
Button Selection
================
These examples assume :python:`cb_default` is :python:`'cbd-copy'`.

Copy Only
---------
The copy button is enabled by default, so just create a :rst:`code-block`, :rst:`literalinclude`, or something similar.

.. code-block:: rst

   .. code-block:: rst

      I have a copy button!

Copy and View
-------------
The view button can be enabled by adding the :css:`cb-view` class.

.. code-block:: rst
   :class: cb-view

   .. code-block:: rst
      :class: cb-view

      I have copy and view buttons!!

View Only
---------
The copy button can then be disabled by adding the :css:`cb-nocopy` class.

.. code-block:: rst
   :class: cb-view cb-nocopy

   .. code-block:: rst
      :class: cb-view cb-nocopy

      I have a view button!

No Buttons
----------
The copy button can be disabled by adding the :css:`cb-nocopy` class, but if all buttons should be disabled, then :css:`cb-none` class can be used as well.

.. code-block:: rst
   :class: cb-none

   .. code-block:: rst
      :class: cb-none

      I have no buttons. :(

=============
Button Hiding
=============
The buttons can be hidden until the user hovers over the code block, globally this can be set with the :python:`cb_hidden` option.
For a specific code block the buttons can be hidden by adding the :css:`cb-hidden` class.

.. code-block:: rst
   :class: cb-all cb-hidden

   .. code-block:: rst
      :class: cb-all cb-hidden

      My buttons are hidden until hovering.

==========
MIME Types
==========
It is possible to provide a MIME type based on the highlight language, with some MIME types the browser provides extra functionality when viewed.
For instance with HTML the browser can render it if the MIME type is correct, just try the view button in the next code block which uses the :rst:`html` language.

.. code-block:: html
   :class: cb-view cb-nocopy

   <h1>I will be rendered as <i>HTML</i>!</h1>

Aliases
-------
By default the MIME types will be detected from the :extern:`Pygments` mapping, this can be overriden using the :extension:`cb_mimes option <Code Block Buttons:cb_mimes>`.
If it is wished to be able to view HTML rendered and not rendered, then an alias for the lexer can be added.

.. code-block:: python

   from pygments.lexers.html import HtmlLexer
   from sphinx.application import Sphinx

   def setup(app: Sphinx) -> None:
       app.add_lexer('raw_html', HtmlLexer)

The :python:`setup` can be placed in :file:`conf.py`, from here it is possible to add aliases to existing :extern:`Pygments` lexers.
In this example an alias for the HTML lexer called :rst:`raw_html` was added, which does not have a mapped MIME type.
Any code block with :rst:`raw_html` as language will now have the view button show the plain HTML.

.. code-block:: raw_html
   :class: cb-view cb-nocopy

   <h1>I will not be rendered as <i>HTML</i>.</h1>

*********
3rd Party
*********
:extern:`clipboard.js`, licensed under :license:`MIT`, is used for copying code.

Icons are from :extern:`Tabler Icons`, licensed under :license:`MIT`.
