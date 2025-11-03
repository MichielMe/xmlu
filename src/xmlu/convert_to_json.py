import json
from pathlib import Path
from typing import Optional, Union

from lxml import etree
from rich import print

source_path = Path(__file__).parent.parent.parent / "_testing_usage" / "source"
source_file = source_path / "SimplePlaylist.sch"

# XML Element structure in lxml:
# - element.tag: the tag name (string)
# - element.text: text content directly inside the element (string or None),
#   only text before any child elements. If element has children, element.text
#   may be None or contain only whitespace.
# - element.attrib: dictionary of attributes {attr_name: attr_value}
# - Child elements: accessed by iterating over element (for child in element)
#
# For JSON conversion:
# - If element has only text content: {element.tag: element.text}
# - If element has children: {element.tag: {child1.tag: ..., child2.tag: ...}}
# - If element has attributes: typically merge with content, e.g.:
#   {element.tag: {"@attrib1": value1, "@attrib2": value2, ...actual content...}}
#   OR keep attributes separate: {element.tag: {"attrs": element.attrib, "content": ...}}

# Conversion strategy:
# {
#   "element.tag": {
#     "text": "element.text",
#     "attrib": {
#       "element.attrib.key": "element.attrib.value"
#     }
#   }
# }


def xml_to_json(source_file: Union[str, Path]) -> str:
    """Convert an XML file to a JSON string."""
    tree = etree.parse(source_file)

    for element in tree.iter():
        parent_element = element.tag
        parent_element_text = element.text.strip() if element.text else None

        print(parent_element)
        if parent_element_text:
            print({"text": parent_element_text})
        elif element.attrib:
            print({"attrib": element.attrib})


print(xml_to_json(source_file))
