# ===================== #
# DONT CHANGE THIS FILE #
# ===================== #
# You shouldn't change signatures of the initial functions,
# and should use modules that were initially imported.
# Feel free to split the code into multiple functions or modules.

from argparse import ArgumentParser
from typing import Optional, Sequence, cast

from config import Config
from task import rss_reader


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

    args = cast(Config, parser.parse_args(argv))

    # RSS READER FUNCTION IS THE ONE WHERE YOU LOGIC SHOULD BELONG
    rss_reader(args)


if __name__ == "__main__":
    main()
