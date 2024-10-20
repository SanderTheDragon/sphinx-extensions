.. SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
..
.. SPDX-License-Identifier: CC-BY-SA-4.0

#########
Changelog
#########

******************
1.1.0 - 2024-10-20
******************
- Added new extension :extension:`Inline Code Highlight`.
- Improved extension :extension:`Code Block Buttons`:

  - Added option :extension:`cb_hidden <Code Block Buttons:cb_hidden>` to hide buttons by default.
  - Added CSS transitions, which can be disabled with option :extension:`cb_transition <Code Block Buttons:cb_transition>`.
  - Added MIME type support for the view button, which can be configured using :extension:`cb_mimes <Code Block Buttons:cb_mimes>`.
  - Added option :extension:`cb_icons <Code Block Buttons:cb_icons>` to override the default icons.
  - Changed default value of :extension:`cb_default <Code Block Buttons:cb_default>` to :python:`'cbd-copy'`.
  - Fixed view button icon changing to copy button.
  - Updated :extern:`clipboard.js` to 2.0.11.

- Updated copyright years.
- Improved documentation.

******************
1.0.1 - 2022-03-04
******************
- Added *Special Case* to :extension:`Mapped Link Role`.

******************
1.0.0 - 2022-01-01
******************
- Added the :extension:`cb_default <Code Block Buttons:cb_default>` option to :extension:`Code Block Buttons`.
- Fixed heading characters for the changelog.
- Updated copyright years.

*********************
1.0.0rc1 - 2021-10-29
*********************
- Fixed a missing :javascript:`null` check which caused the console to fill up with errors on every click.

********************
1.0.0b4 - 2021-10-27
********************
- Fixed the view button for :extension:`Code Block Buttons`.

********************
1.0.0b3 - 2021-10-25
********************
- Added a :html:`<span>` to increase the width of the :rst:`code-block` scroll area, this way the buttons will not overlay the code.

********************
1.0.0b2 - 2021-10-10
********************
- Added a warning to :extension:`Mapped Link Role` for when a role defined as :python:`None` has no mapping defined.

********************
1.0.0b1 - 2021-10-10
********************
Initial release.
