"""Global constraints: AllDifferent, Sum, Element, Cardinality."""

from cforge.global_cstr.alldiff import AllDifferent
from cforge.global_cstr.linear import SumConstraint, ScalarProduct
from cforge.global_cstr.element import ElementConstraint
from cforge.global_cstr.cardinality import CardinalityConstraint

__all__ = [
    "AllDifferent",
    "SumConstraint",
    "ScalarProduct",
    "ElementConstraint",
    "CardinalityConstraint",
]
