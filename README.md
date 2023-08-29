# mvr-uuid-shuuffle

Generates new UUIDs inside of a [My Virtual Rig (MVR)](https://gdtf-share.com/help/en/help/mvr/) file.

## Why?

In some show design CAD software, such as [Capture](https://www.capture.se/), fixtures/objects created in a project are given unique identifiers (UUID) under the hood. These persist and in some cases are reflected in model exports, such as in the MVR format. Other software that ingests MVR files (such as [GrandMA3](https://www.malighting.com/grandma3/)) may honor this UUID and treat it with a higher precedence than the user-assignable Fixture ID.

If you, for example, duplicated a CAD project file, made a few changes and wanted to treat the design as a new stage/venue -- as you might do with a "template" project -- importing the MVR, even with non-overlapping fixture IDs, would result in merge conflicts if you previously imported an MVR from another stage made with the same template.

## Requirements

- A UNIX-like environemnt, such as:
  - Linux
  - macOS X
  - Windows running Git Bash
- Python (3.5 or greater)
  - virtualenv support preferred

## Installation

    sh build.sh

    # in Linux/macOS/etc:
    source venv/bin/activate

    # in Windows:
    source venv/Scripts/activate

## Usage

    Usage: mvrUuidShuffle [OPTIONS]

    Options:
    -i, --input-file PATH           [required]
    -o, --output-file PATH          [required]
    --layers / --no-layers
    --fixtures / --no-fixtures
    --classes / --no-classes
    --group-objects / --no-group-objects

## Examples

    cd ~/MALightingTechnology/gma3_library/mvr
    mvrUuidShuffle -i venue1.mvr -o venue1-unique.mvr

## Limitations

Only a few common node types from the [MVR 1.5 spec](https://github.com/mvrdevelopment/spec/blob/main/mvr-spec.md) (layers, fixtures, classes, group-objects) are made unique.
