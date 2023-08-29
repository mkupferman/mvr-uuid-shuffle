#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import tempfile
import zipfile
import uuid
import xml.etree.ElementTree as ET
import os


@click.command()
@click.option("--input-file", "-i", type=click.Path(exists=True), required=True)
@click.option("--output-file", "-o", type=click.Path(exists=False), required=True)
@click.option("--layers/--no-layers", default=True)
@click.option("--fixtures/--no-fixtures", default=True)
@click.option("--classes/--no-classes", default=True)
@click.option("--group-objects/--no-group-objects", default=True)
def mvrUuidShuffle(**params):
    input_file = params["input_file"]
    output_file = params["output_file"]

    # work in a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        # unzip the input file into the temporary directory
        with zipfile.ZipFile(input_file, "r") as zip_ref:
            zip_ref.extractall(tmpdirname)

        # shuffle the UUIDs in the temporary GeneralSceneDescription.xml:
        tree = ET.parse(tmpdirname + "/GeneralSceneDescription.xml")
        root = tree.getroot()

        if params["layers"]:
            for layer in root.iter("Layer"):
                layer.set("uuid", str(uuid.uuid4()))

        if params["fixtures"]:
            for fixture in root.iter("Fixture"):
                fixture.set("uuid", str(uuid.uuid4()))

        if params["classes"]:
            for layer in root.iter("Class"):
                layer.set("uuid", str(uuid.uuid4()))

        if params["group_objects"]:
            for group_object in root.iter("GroupObject"):
                group_object.set("uuid", str(uuid.uuid4()))

        tree.write(tmpdirname + "/GeneralSceneDescription.xml")

        # re-zip the temporary directory into the output file
        with zipfile.ZipFile(output_file, "w") as zip_ref:
            for root, dirs, files in os.walk(tmpdirname):
                for file in files:
                    if file in [".", ".."]:
                        continue
                    zip_ref.write(
                        os.path.join(root, file),
                        arcname=os.path.relpath(os.path.join(root, file), tmpdirname),
                        compress_type=zipfile.ZIP_DEFLATED,
                    )
