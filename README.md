# Ensure unique GUID
## Rationale

This add-on corrects the consequences of a bug in add-on [copy note(1566928056)](https://ankiweb.net/shared/info/1566928056). It may also be useful if anything else has the same bug.

This is not a big bug. It only occurs if you copy a note, export a deck containing the original and the copy, and then import the deck into another collection. If you do this, you'll import only the original or the copy note but not both. Therefore, you should use this add-on to correct the bug before exporting cards.

To use this add-on, you simply need to select «Ensure unique GUID» in the main window.

## Technical

For some reason, each note has two identifiers. The note identifier (nid) which is used in most of anki. And a Globally Unique IDentifier (guid), which is used when a note is shared between different collections; i.e. when a deck is shared and imported. The add-on "copy note" did change nid but not guid. This is now changed.

## Version 2.0
None

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-Close-and-lose-current-input-for-sticky-fields
Addon number| [2082040683](https://ankiweb.net/shared/info/2082040683)
