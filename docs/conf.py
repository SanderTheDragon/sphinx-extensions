# SPDX-FileCopyrightText: 2021-2022 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

import os
import sys

from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent / 'extensions'))

# Sphinx settings
author = 'SanderTheDragon'
copyright = f'2021-2022, SanderTheDragon'
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

# `mappedlinkrole` settings
role_mapping_root = '/'
if os.environ.get('GITLAB_CI', 'false').lower() == 'true':
    role_mapping_root = '/sphinx-extensions/'

role_mapping = {
    'extension': role_mapping_root + '{}.html',
    'changelog': role_mapping_root + 'changelog.html',

    'license': 'https://spdx.org/licenses/{}.html',
    'wikipedia': 'https://en.wikipedia.org/wiki/{}',
    'cppreference': 'https://en.cppreference.com/w/cpp/{}',

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

cppreference_mapping = {
    'std::vector': 'container/vector'
}

extern_mapping = {
    'clipboard.js': 'https://clipboardjs.com',
    'include-what-you-use': 'https://include-what-you-use.org',
    'REUSE': 'https://reuse.software',
    'Sphinx': 'https://www.sphinx-doc.org',
    'Tabler Icons': 'https://tablericons.com'
}
