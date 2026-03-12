"""ConstraintForge: Constraint satisfaction solver with propagation and learning."""

from cforge.core.variable import Variable
from cforge.core.domain import Domain
from cforge.core.constraint import Constraint, BinaryConstraint, UnaryConstraint
from cforge.solver.backtrack import BacktrackSolver
from cforge.global_cstr.alldiff import AllDifferent
from cforge.global_cstr.linear import SumConstraint

__version__ = "0.4.0"

__all__ = [
    "Variable",
    "Domain",
    "Constraint",
    "BinaryConstraint",
    "UnaryConstraint",
    "BacktrackSolver",
    "AllDifferent",
    "SumConstraint",
]
