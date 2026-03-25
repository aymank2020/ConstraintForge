"""Domain storage backends and restoration strategies."""

from cforge.storage.trail import Trail, TrailEntry
from cforge.storage.sparse_set import SparseSet

__all__ = ["Trail", "TrailEntry", "SparseSet"]
