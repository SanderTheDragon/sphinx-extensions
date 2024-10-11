# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config
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
    js = f'const {option} = "{app.config[option]}";'
    app.add_js_file(None, body=js)


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


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value('cb_default', 'cbd-copy', 'html', [ str ])

    app.connect('builder-inited', add_static)

    return { 'version': common.__version__, 'parallel_read_safe': True }
