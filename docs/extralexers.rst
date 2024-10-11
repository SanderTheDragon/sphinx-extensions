.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

############
Extra Lexers
############
The *extra lexers* extension adds extra lexers (currently only 1) to :extern:`Pygments`.

*****
Usage
*****
The extension can be enabled by adding :python:`'sanderthedragon.extralexers'` to the :python:`extensions` list in :file:`conf.py`.
After that any of the lexers below can be used as language for a code block.

************
Added Lexers
************

=========
LLVM JSON
=========
The LLVM flavour of JSON slightly differs from JavaScript JSON (therefore it is based on the JavaScript lexer).
The only real difference is that it uses a ``#`` for comments instead of ``//``.
It can be used for :extern:`include-what-you-use` mapping files for instance.

.. table::
   :align: left
   :class: codetable
   :width: 100%

   +---------------------------------+---------------------------------+---------------------------------+
   | ``llvmjson`` lexer              | ``javascript`` lexer  (forced)  | ``json`` lexer (forced)         |
   +=================================+=================================+=================================+
   | .. code-block:: llvmjson        | .. code-block:: javascript      | .. code-block:: json            |
   |    :class: cb-none              |    :class: cb-none              |    :class: cb-none              |
   |                                 |    :force:                      |    :force:                      |
   |                                 |                                 |                                 |
   |    # I'm a comment in LLVM JSON |    # but not in JavaScript JSON |    # or regular JSON            |
   |                                 |                                 |                                 |
   |    {                            |    {                            |    {                            |
   |        "foo": [                 |        "foo": [                 |        "foo": [                 |
   |            "bar",               |            "bar",               |            "bar",               |
   |            "baz"                |            "baz"                |            "baz"                |
   |        ]                        |        ]                        |        ]                        |
   |    }                            |    }                            |    }                            |
   +---------------------------------+---------------------------------+---------------------------------+
