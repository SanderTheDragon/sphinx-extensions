# SPDX-FileCopyrightText: 2021 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

import os
import sys


sys.path.insert(0, os.path.abspath('./extensions'))

# Sphinx settings
author = 'SanderTheDragon'
copyright = f'2021, SanderTheDragon'
project = f'SanderTheDragon\'s Sphinx Extensions'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sanderthedragon.codeblockbuttons',
    'sanderthedragon.extralexers',
    'sanderthedragon.mappedlinkrole'
]

# HTML settings
html_theme = 'furo'

html_title = project

html_static_path = [ '_static' ]
html_css_files = [ 'css/custom.css' ]

# `autosectionlabel` settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# Role settings
role_mapping = {
    'extension': '/{}.html',

    'license': 'https://spdx.org/licenses/{}.html',
    'wikipedia': 'https://en.wikipedia.org/wiki/{}',

    'extern': None
}

extension_mapping = {
    'Code Block Buttons': 'codeblockbuttons',
    'Extra Lexers': 'extralexers',
    'Mapped Link Role': 'mappedlinkrole'
}

wikipedia_mapping = {
    'Sphinx': 'Sphinx_(documentation_generator)',
    '!Sphinx': 'Sphinx'
}

extern_mapping = {
    'clipboard.js': 'https://clipboardjs.com',
    'include-what-you-use': 'https://include-what-you-use.org',
    'REUSE': 'https://reuse.software',
    'Sphinx': 'https://www.sphinx-doc.org',
    'Tabler Icons': 'https://tablericons.com'
}