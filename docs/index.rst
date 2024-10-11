.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

###################################
SanderTheDragon's Sphinx Extensions
###################################
These are some :extern:`Sphinx` extensions I wrote, feel free to use them.

- :extension:`Code Block Buttons` adds copy and view buttons to code blocks.
- :extension:`Extra Lexers` adds extra lexers to pygments currently only LLVM JSON.
- :extension:`Inline Code Highlight` adds custom roles to be able to highlight inline code.
- :extension:`Mapped Link Role` adds custom roles which can be mapped to links.

************
Installation
************
The extensions can be installed with :program:`pip`.

.. code-block:: sh
   :class: cb-noview

   pip install sanderthedragon-sphinxext

*********
Changelog
*********
Changelog is available :changelog:`here`.

*******
License
*******
These documents are licensed under :license:`CC-BY-SA-4.0`.
Code and examples are licensed under :license:`MIT`.
Other files, like configuration files are licensed under :license:`CC0-1.0`.

.. toctree::
   :caption: Extensions
   :hidden:

   codeblockbuttons.rst
   extralexers.rst
   inlinecodehighlight.rst
   mappedlinkrole.rst

.. toctree::
   :caption: Project
   :hidden:

   changelog.rst

   GitLab Repository <https://gitlab.com/SanderTheDragon/sphinx-extensions>
