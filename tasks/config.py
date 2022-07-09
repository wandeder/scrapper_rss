# ===================== #
# DONT CHANGE THIS FILE #
# ===================== #
from typing import Protocol


class Config(Protocol):
    """Configuration object for RSS reader."""

    version: bool
    json: bool
    verbose: bool
    limit: int
    source: str
