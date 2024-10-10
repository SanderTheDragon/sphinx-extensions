# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

import os
import sys

from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Sphinx settings
author = 'SanderTheDragon'
copyright = f'2021-2024, SanderTheDragon'
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
html_theme_options = {
    'footer_icons': [
        {
            'name': 'GitLab',
            'url': 'https://gitlab.com/SanderTheDragon/sphinx-extensions',
            # https://about.gitlab.com/images/press/press-kit-icon.svg
            'html': '''
                <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 92" style="enable-background:new 0 0 100 92;" xml:space="preserve">
                    <style type="text/css">
                        .st0{fill:#E24329;}
                        .st1{fill:#FC6D26;}
                        .st2{fill:#FCA326;}
                    </style>
                    <desc>Created with Sketch.</desc>
                    <g>
                        <path class="st0" d="M95.9,36.5l-0.1-0.3L82.8,2.4c-0.3-0.7-0.7-1.2-1.3-1.6c-0.6-0.4-1.3-0.6-2-0.5c-0.7,0-1.4,0.3-2,0.7   c-0.6,0.4-1,1.1-1.1,1.7l-8.7,26.7H32.3L23.6,2.7C23.4,2.1,23,1.4,22.5,1c-0.6-0.4-1.2-0.7-2-0.7c-0.7,0-1.4,0.1-2,0.5   c-0.6,0.4-1.1,0.9-1.3,1.6L4.2,36.1l-0.1,0.3c-3.8,10-0.6,21.3,8,27.7c0,0,0,0,0,0l0.1,0.1l19.7,14.7l9.7,7.4l5.9,4.5   c1.4,1.1,3.4,1.1,4.8,0l5.9-4.5l9.7-7.4l19.8-14.8c0,0,0,0,0.1,0C96.5,57.8,99.7,46.5,95.9,36.5z"/>
                        <path class="st1" d="M95.9,36.5l-0.1-0.3c-6.4,1.3-12.3,4-17.4,7.8C78.3,44,63,55.6,50,65.4c9.7,7.3,18.1,13.7,18.1,13.7l19.8-14.8   c0,0,0,0,0.1,0C96.5,57.8,99.7,46.5,95.9,36.5z"/>
                        <path class="st2" d="M31.9,79.1l9.7,7.4l5.9,4.5c1.4,1.1,3.4,1.1,4.8,0l5.9-4.5l9.7-7.4c0,0-8.4-6.4-18.1-13.7   C40.3,72.7,31.9,79.1,31.9,79.1z"/>
                        <path class="st1" d="M21.6,43.9c-5.1-3.8-11-6.5-17.4-7.8l-0.1,0.3c-3.8,10-0.6,21.3,8,27.7c0,0,0,0,0,0l0.1,0.1l19.7,14.7   c0,0,8.4-6.4,18.1-13.7C37,55.6,21.7,44,21.6,43.9z"/>
                    </g>
                </svg>
            ''',
            'class': 'grayscale'
        }
    ]
}

html_copy_source = False
html_show_sourcelink = False

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
