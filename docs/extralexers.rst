.. SPDX-FileCopyrightText: 2021 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

############
Extra Lexers
############
The *extra lexers* extension adds extra lexers to pygments.

*****
Usage
*****
The extension can be enabled by adding ``sanderthedragon.extralexers`` to your extensions in :file:`conf.py`.

************
Added Lexers
************

=========
LLVM JSON
=========
The LLVM flavour of JSON slightly differs from JavaScript JSON (therefore it is based on the JavaScript lexer).
The only real difference is that it uses a ``#`` for comments instead of ``//``.
It is useful for :extern:`include-what-you-use` mapping files.

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
   |    # I'm a comment in LLVM JSON |                                 |                                 |
   |                                 |    # but not in JavaScript JSON |    # or regular JSON            |
   |    {                            |                                 |                                 |
   |        "foo": [                 |    {                            |    {                            |
   |            "bar",               |        "foo": [                 |        "foo": [                 |
   |            "baz"                |            "bar",               |            "bar",               |
   |        ]                        |            "baz"                |            "baz"                |
   |    }                            |        ]                        |        ]                        |
   |                                 |    }                            |    }                            |
   +---------------------------------+---------------------------------+---------------------------------+
