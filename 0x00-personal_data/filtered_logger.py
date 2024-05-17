#!/usr/bin/env python3
'''A module for filtering logs '''

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: List[str],
        separator: str
) -> str:
    """Filters a log line
    """
    updated_message = message
    for field in fields:
        pattern = re.compile(fr'({field}=[^{separator}]*)')
        updated_message = re.sub(
            pattern, lambda m: f"{field}={redaction}", updated_message
        )
    return updated_message
