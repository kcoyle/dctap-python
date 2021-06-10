"""Class for Python objects derived from CSV files."""


from dataclasses import dataclass, field
from typing import List


@dataclass
class DCTAPStatementConstraint:
    """Instances hold TAP/CSV elements related to statement constraints."""

    # pylint: disable=too-many-instance-attributes
    # It's a dataclass, right?
    # pylint: disable=invalid-name
    # propertyID, etc, do not conform to snake-case naming style.

    propertyID: str = ""
    propertyLabel: str = ""
    mandatory: str = False
    repeatable: str = False
    valueNodeType: str = ""
    valueDataType: str = ""
    valueConstraint: str = ""
    valueConstraintType: str = ""
    valueShape: str = ""
    note: str = ""

    def normalize(self, config_dict=None):
        """Normalizes values of fields."""
        self._normalize_valueNodeType(config_dict)
        return True

    def _normalize_value_node_type(self, config_dict=None):
        """Take valueNodeType from configurable enumerated list, case-insensitive."""
        valid_types = config_dict['value_node_types']
        if self.valueNodeType:
            if self.valueNodeType.lower not in [v.lower for v in valid_types]:
                print(f"Warning: {self.valueNodeType} is not a recognized node type.")
                self.valueNodeType = ""
        return self

    def emit_warnings(self, config_dict=None):
        """Emit warnings on possible errors."""
        self._warn_about_literal_datatype_used_with_uri(config_dict)
        return True

    def _warn_about_literal_datatype_used_with_uri(self):
        """URIs should usually not be typed as literals."""
        if self.valueDataType == "Literal":
            pass


@dataclass
class DCTAPShape:
    """Instances hold TAP/CSV row elements related to shapes."""

    # pylint: disable=invalid-name
    # True that propertyID, etc, do not conform to snake-case naming style.

    shapeID: str = ""
    shapeLabel: str = ""
    start: bool = False
    sc_list: List[DCTAPStatementConstraint] = field(default_factory=list)

    def normalize(self, config_dict=None):
        """Normalize values where required."""
        self._normalize_default_shapeID(config_dict)
        return True

    def _normalize_default_shapeID(self, config_dict=None):
        """If shapeID not specified, sets default value from config."""
        if not self.shapeID:
            self.shapeID = config_dict['default_shape_name']
        return self


@dataclass
class CSVSchema:
    """List of DCTAPShape instances"""

    csvshapes_list: List[DCTAPShape] = field(default_factory=list)
