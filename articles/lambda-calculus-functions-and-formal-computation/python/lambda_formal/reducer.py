from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Var:
    name: str


@dataclass(frozen=True)
class Lam:
    param: str
    body: object


@dataclass(frozen=True)
class App:
    fn: object
    arg: object


def pretty(term: object) -> str:
    if isinstance(term, Var):
        return term.name
    if isinstance(term, Lam):
        return f"(lambda {term.param}. {pretty(term.body)})"
    if isinstance(term, App):
        return f"({pretty(term.fn)} {pretty(term.arg)})"
    return str(term)


def substitute(term: object, var: str, value: object) -> object:
    if isinstance(term, Var):
        return value if term.name == var else term
    if isinstance(term, Lam):
        if term.param == var:
            return term
        return Lam(term.param, substitute(term.body, var, value))
    if isinstance(term, App):
        return App(substitute(term.fn, var, value), substitute(term.arg, var, value))
    return term


def beta_reduce_once(term: object) -> object:
    if isinstance(term, App) and isinstance(term.fn, Lam):
        return substitute(term.fn.body, term.fn.param, term.arg)
    if isinstance(term, App):
        return App(beta_reduce_once(term.fn), beta_reduce_once(term.arg))
    if isinstance(term, Lam):
        return Lam(term.param, beta_reduce_once(term.body))
    return term


def demo_identity_reduction() -> list[str]:
    term = App(Lam("x", Var("x")), Var("a"))
    reduced = beta_reduce_once(term)
    return [pretty(term), pretty(reduced)]
