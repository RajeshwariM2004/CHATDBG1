from chatdbg.util.delta import minimize_failing_input


def buggy_parser(s: str) -> None:
    """
    A tiny demo function for delta debugging.

    It fails whenever the string contains the substring "BAD".
    """
    if "BAD" in s:
        # Simulate a bug that only triggers on certain inputs.
        raise ValueError(f"Found forbidden substring in: {s!r}")


def main():
    # A contrived failing input. In a real setting, this could come from a test.
    failing_input = "xxxGOODxxxBADxxxEVEN_MORE_TEXT"

    print("Original failing input:", repr(failing_input))
    minimized, tb = minimize_failing_input(buggy_parser, failing_input)
    print("Minimized failing input:", repr(minimized))
    print("Exception:", tb)


if __name__ == "__main__":
    main()


