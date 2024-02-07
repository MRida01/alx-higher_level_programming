#!/usr/bin/python3
"Module that converts an object to a dictionary description for JSON serialization."""

def class_to_json(obj):
    """Converts an object to a dictionary description for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary containing the serializable attributes of the object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Filter out non-serializable attributes
    serializable_attributes = {}
    for key, value in attributes.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
