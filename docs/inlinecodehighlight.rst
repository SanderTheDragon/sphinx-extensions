.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

#####################
Inline Code Highlight
#####################
The *inline code highlight* extension adds roles to highlight inline code blocks.

*****
Usage
*****
The extension can be enabled by adding :python:`'sanderthedragon.inlinecodehighlight'` to the :python:`extensions` list in :file:`conf.py`.

To be able to use any of the roles, they first need to be defined.
This can be done with the :python:`inline_codes` option, which can be added to :file:`conf.py`.
The value can be set to either a :python:`dict` or a :python:`list`.

With a :python:`dict`, the key defines name of the new role, and the value the highlight language, for example:

.. code-block:: python

   inline_codes = {
       'python': 'python',
       'bash': 'bash',
       'javascript': 'javascript'
   }

With a :python:`list`, the items define the highlight language, for example:

.. code-block:: python

   inline_codes = [ 'python', 'bash', 'javascript' ]

Both of these configurations will add the same 3 new roles ``python``, ``bash``, and ``javascript``, which can all highlight inline code block with their respective languages.

********
Examples
********
A simple ``Hello, World!`` will look like this for each of the previously defined languages:

+------------+------------------------------------------------+-----------------------------------------+
| Language   | Code (highlighted with a ``rst`` role)         | Result                                  |
+============+================================================+=========================================+
| Python     | :rst:`:python:`print('Hello, World!')``        | :python:`print('Hello, World!')`        |
+------------+------------------------------------------------+-----------------------------------------+
| Bash       | :rst:`:bash:`echo 'Hello, World!'``            | :bash:`echo 'Hello, World!'`            |
+------------+------------------------------------------------+-----------------------------------------+
| Javascript | :rst:`:python:`console.log("Hello, World!");`` | :python:`console.log("Hello, World!");` |
+------------+------------------------------------------------+-----------------------------------------+
