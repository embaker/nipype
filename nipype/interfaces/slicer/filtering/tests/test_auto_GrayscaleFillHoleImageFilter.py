# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..morphology import GrayscaleFillHoleImageFilter


def test_GrayscaleFillHoleImageFilter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='%s',
    position=-2,
    ),
    outputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = GrayscaleFillHoleImageFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_GrayscaleFillHoleImageFilter_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = GrayscaleFillHoleImageFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
