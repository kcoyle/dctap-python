"""Default settings."""

DEFAULT_CONFIGFILE_NAME = "dctap.yml"

DEFAULT_CONFIG_YAML = """# dctap configuration file (in YAML format)
default_shape_name: "default"

value_node_types:
- iri
- literal
- bnode

prefixes:
    ":":        "http://example.org/"
    "dc:":      "http://purl.org/dc/elements/1.1/"
    "dcterms:": "http://purl.org/dc/terms/"
    "dct:":     "http://purl.org/dc/terms/"
    "foaf:":    "http://xmlns.com/foaf/0.1/"
    "owl:":     "http://www.w3.org/2002/07/owl#"
    "rdf:":     "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    "rdfs:":    "http://www.w3.org/2000/01/rdf-schema#"
    "schema:":  "http://schema.org/"
    "skos:":    "http://www.w3.org/2004/02/skos/core#"
    "skosxl:":  "http://www.w3.org/2008/05/skos-xl#"
    "wdt:":     "http://www.wikidata.org/prop/direct/"
    "xsd:":     "http://www.w3.org/2001/XMLSchema#"

# Aliases (case-insensitive) mapped to "official" element names (case-sensitive)
element_aliases:
    "propid": "propertyID"
    "mand": "mandatory"
    "rep": "repeatable"
    "nodetype": "valueNodeType"
    "datatype": "valueDataType"
    "vc": "valueConstraint"
    "vctype": "valueConstraintType"
    "vshape": "valueShape"

# If elements (column headers) are encountered that are not part of the 
# base DCTAP model, they will be ignored - unless they are entered here as
# "extra" elements.
# "Extra" elements must either be "shape" elements or "statement constraint" elements.
# The following "shape" and "statement constraint" elements are merely examples...
extra_shape_elements:
- closed
- start

extra_statement_constraint_elements:
- min
- max

# 
picklist_item_separator: ' '
"""