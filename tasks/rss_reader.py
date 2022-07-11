# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import Optional, Sequence, cast, Protocol


class UnhandledException(Exception):
    pass


class ConfigSignature(Protocol):
    """Parameters that configuration object will have"""

    version: bool
    json: bool
    verbose: bool
    limit: int
    source: str


def rss_reader(args: ConfigSignature):
    """
    The main function of your task.
    """
    # Your code goes here
    pass


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument("--version", help="Print version info", action="store_true")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--verbose", help="Outputs verbose status messages", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = cast(ConfigSignature, parser.parse_args(argv))

    # RSS READER FUNCTION IS THE ONE WHERE YOU LOGIC SHOULD BELONG
    try:
        rss_reader(args)
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
