import traceback
from typing import Callable, Tuple


def _run_with_input(func: Callable[[str], None], s: str) -> Tuple[bool, str]:
    """
    Helper: run `func(s)` and return (failed, exception_string).
    """
    try:
        func(s)
        return False, ""
    except Exception as e:
        tb = "".join(traceback.format_exception_only(type(e), e)).strip()
        return True, tb


def minimize_failing_input(func: Callable[[str], None], s: str) -> Tuple[str, str]:
    """
    Very small delta-debugging helper for string inputs.

    Given a function `func` that fails for the string `s`, try to find a
    smaller substring of `s` that still causes a failure.

    This is intentionally simple and intended as a demo, not a full
    ddmin implementation.
    """
    failed, tb = _run_with_input(func, s)
    if not failed:
        raise ValueError("Input does not cause a failure, cannot delta-debug.")

    lo, hi = 0, len(s)
    best = s

    while hi - lo > 1:
        mid = (lo + hi) // 2
        candidate = s[lo:mid]
        if not candidate:
            break
        failed, _ = _run_with_input(func, candidate)
        if failed:
            best = candidate
            hi = mid
        else:
            lo = mid

    return best, tb


