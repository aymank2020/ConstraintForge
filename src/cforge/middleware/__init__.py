"""Middleware: hooks, plugins, and event system for solver extensibility."""

from cforge.middleware.hooks import SolverHook, HookManager
from cforge.middleware.events import SolverEvent, EventBus

__all__ = ["SolverHook", "HookManager", "SolverEvent", "EventBus"]
