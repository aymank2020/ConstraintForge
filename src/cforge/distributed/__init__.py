"""Distributed solving: work splitting and result aggregation."""

from cforge.distributed.splitter import WorkSplitter, SubProblem
from cforge.distributed.aggregator import ResultAggregator

__all__ = ["WorkSplitter", "SubProblem", "ResultAggregator"]
