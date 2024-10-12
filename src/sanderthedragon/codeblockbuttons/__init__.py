# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

import json

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from sphinx.util import fileutil

import sanderthedragon as common


def add_js(app: Sphinx, path: Path) -> None:
    source = Path(__file__).parent / '_static' / path
    destination = Path(app.builder.outdir) / '_static' / path

    destination.parent.mkdir(exist_ok=True, parents=True)
    fileutil.copy_asset_file(str(source), str(destination))
    app.add_js_file(str(path))


def add_js_option(app: Sphinx, option: str) -> None:
    # Append it to a file, since adding it inline was adding it twice
    filename = 'cb_options.js'
    path = Path(app.builder.outdir) / '_static' / filename
    with open(path, 'a', encoding='utf-8') as js_file:
        js_file.write(f'const {option} = {json.dumps(app.config[option])};\n')

    app.add_js_file(filename)


def add_css(app: Sphinx, path: Path) -> None:
    source = Path(__file__).parent / '_static' / path
    destination = Path(app.builder.outdir) / '_static' / path

    destination.parent.mkdir(exist_ok=True, parents=True)
    fileutil.copy_asset_file(str(source), str(destination))
    app.add_css_file(str(path))


def add_static(app: Sphinx) -> None:
    if app.builder.format != 'html':
        return

    add_js(app, Path('clipboard.min.js'))

    add_css(app, Path('codeblock.css'))
    add_js(app, Path('codeblock.js'))

    add_js_option(app, 'cb_default')
    add_js_option(app, 'cb_hidden')
    add_js_option(app, 'cb_transitions')


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value('cb_default', 'cbd-copy', 'html', [ str ])
    app.add_config_value('cb_hidden', False, 'html', [ bool ])
    app.add_config_value('cb_transitions', True, 'html', [ bool ])

    app.connect('builder-inited', add_static)

    return { 'version': common.__version__, 'parallel_read_safe': True }
