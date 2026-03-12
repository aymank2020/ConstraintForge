"""Core primitives: Variable, Domain, Constraint."""

from cforge.core.variable import Variable
from cforge.core.domain import Domain
from cforge.core.constraint import Constraint, BinaryConstraint, UnaryConstraint

__all__ = ["Variable", "Domain", "Constraint", "BinaryConstraint", "UnaryConstraint"]
