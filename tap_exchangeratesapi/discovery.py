"""Discovery functions for the Singer.io tap"""

import json
import os

import singer
from singer import Catalog, metadata

from typing import Dict, List, Any

LOGGER = singer.get_logger()
REPLICATION_METHOD = "INCREMENTAL"


def _get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


# Load schemas from schemas folder
def _load_schemas():
    schemas = {}
    for filename in os.listdir(_get_abs_path("schemas")):
        path = _get_abs_path("schemas") + "/" + filename
        basename = filename.replace(".json", "")
        with open(path) as file:
            schemas[basename] = json.load(file)
    return schemas


def discover() -> Dict[str, Dict[str, Any]]:
    """
    Run discovery

    Returns
    -------
    Dict[str, Dict[str, Any]]
        The list of streams with their associated metadata
    """
    LOGGER.info("Starting discovery mode")
    streams = []
    for stream_name, schema in _load_schemas().items():
        catalog_entry = {
            "stream": stream_name,
            "tap_stream_id": stream_name,
            "schema": schema,
            "metadata": metadata.get_standard_metadata(
                schema=schema["schema"],
                key_properties=["date"],
                valid_replication_keys=["date"],
                replication_method=REPLICATION_METHOD,
            ),
            "key_properties": ["date"],
        }
        streams.append(catalog_entry)
    return Catalog.from_dict({"streams": streams})
