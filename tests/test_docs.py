"""Tests from https://github.com/dcmi/dctap-python/tree/main/docs/test_csvs ."""

import os
import pytest
from pathlib import Path
from dctap.csvreader import _get_tapshapes, _get_rows
from dctap.classes import TAPShape, TAPStatementConstraint

NORM_DIR = Path(os.path.dirname(os.path.realpath(__file__))).joinpath("../docs/normalizations")

TESTS_DIR = Path(os.path.dirname(os.path.realpath(__file__))).joinpath("../docs/test_csvs")


def test_propertyID_only_IS_OKAY():
    """Minimal application profile can have propertyID column only."""
    csvfile = Path(TESTS_DIR).joinpath("propertyID_only.csv")
    rows = _get_rows(csvfile)
    assert _get_tapshapes(rows)


def test_propertyID_plus_label_IS_OKAY():
    """Properties can have labels."""
    csvfile = Path(TESTS_DIR).joinpath("propertyID_plus_label.csv")
    rows = _get_rows(csvfile)
    assert _get_tapshapes(rows)


def test_propertyID_plus_nodetype_datatype_IS_OKAY():
    """Properties can have node types and datatypes."""
    csvfile = Path(TESTS_DIR).joinpath("propertyID_plus_nodetype_datatype.csv")
    rows = _get_rows(csvfile)
    assert _get_tapshapes(rows)


def test_propertyID_missing_RAISES_EXCEPTION():
    """Exits if there is no propertyID column - not a valid DCTAP instance."""
    csvfile = Path(TESTS_DIR).joinpath("propertyID_missing.csv")
    with pytest.raises(SystemExit):
        _get_rows(csvfile)


def test_propertyID_before_shapeID_IS_OKAY():
    """Order of columns does not matter."""
    csvfile = Path(TESTS_DIR).joinpath("propertyID_before_shapeID.csv")
    rows_list = _get_rows(csvfile)
    assert _get_tapshapes(rows_list)


def test_karen_twoSameShape_PASSES():
    """shapeID appears more than once, but without intervening shapes."""
    csvfile = Path(NORM_DIR).joinpath("twoSameShape.csv")
    rows_list = _get_rows(csvfile)
    assert _get_tapshapes(rows_list)
    assert len(_get_tapshapes(rows_list)) == 2


def test_karen_mixOfEmptyCells_PASSES():
    """shapeID appears more than once, but with intervening shapes."""
    csvfile = Path(NORM_DIR).joinpath("mixOfEmptyCells.csv")
    rows_list = _get_rows(csvfile)
    assert _get_tapshapes(rows_list)
    assert len(_get_tapshapes(rows_list)) == 2


def test_karen_valueNodeTypeLowercase_PASSES():
    """valueNodeType in lower case."""
    csvfile = Path(NORM_DIR).joinpath("valueNodeTypeLowercase.csv")
    rows_list = _get_rows(csvfile)
    shapes_list = _get_tapshapes(rows_list)
    config_dict = dict()
    config_dict['value_node_types'] = ["URI", "BNode", "literal"]
    assert _get_tapshapes(rows_list)
    for shape in shapes_list:
        for statconstraint in shape.sc_list:
            statconstraint._normalize_value_node_type(config_dict)
            if statconstraint.valueNodeType:
                assert statconstraint.valueNodeType


def test_karen_valueNodeTypeWrong_NORMALIZED_TO_EMPTY_STRING():
    """Exits if value node type is not in enumerated list."""
    csvfile = Path(NORM_DIR).joinpath("valueNodeTypeWrong.csv")
    rows_list = _get_rows(csvfile)
    shapes_list = _get_tapshapes(rows_list)
    config_dict = dict()
    config_dict['value_node_types'] = ["URI", "BNode", "literal"]
    assert _get_tapshapes(rows_list)
    for shape in shapes_list:
        for statconstraint in shape.sc_list:
            statconstraint._normalize_value_node_type(config_dict)
            if statconstraint.valueNodeType:
                assert statconstraint.valueNodeType == "URI"
            else:
                assert not statconstraint.valueNodeType

def test_karen_IRIwithLiteralDatatype_EMITS_WARNING_DELETES_DATATYPE():
    """When valueNodeType=IRI plus any valueDataType, emit warning, drop datatype."""
    csvfile = Path(NORM_DIR).joinpath("IRIwithLiteralDatatype.csv")

def test_karen_bothBlankAndFilledShapeID_SHAPES_EITHER_DECLARED_IN_ROW_OR_CARRIED():
    """Shapes may be declared on each row or carried from previous row."""
    csvfile = Path(NORM_DIR).joinpath("bothBlankAndFilledShapeID.csv")

def test_karen_literalWithoutDatatype_XXX():
    """Literal node but no datatype""" 
    csvfile = Path(NORM_DIR).joinpath("literalWithoutDatatype.csv")

def test_karen_valueDataTypeWrong_XXX():
    """literal not an xsd:literal"""
    csvfile = Path(NORM_DIR).joinpath("valueDataTypeWrong.csv")

def test_karen_shapeNotReferenced_XXX():
    """Shape not referenced in valueShape""" 
    csvfile = Path(NORM_DIR).joinpath("shapeNotReferenced.csv")

def test_karen_shapewithoutShapeID_XXX():
    """Value shape does not match a shape"""
    csvfile = Path(NORM_DIR).joinpath("shapewithoutShapeID.csv")

def test_karen_valueNodeTypeTwice_XXX():
    """Two valueNodeType columns""" 
    csvfile = Path(NORM_DIR).joinpath("valueNodeTypeTwice.csv")
