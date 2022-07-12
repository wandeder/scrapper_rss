# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence, Union, cast
import requests


class UnhandledException(Exception):
    pass


def rss_parser(
    xmls: List[str],
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xmls: List of XML strings.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xmls = ['<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>']
        >>> rss_parser(xmls)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    # Your code goes here


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

    args = parser.parse_args(argv)
    xmls = [requests.get(src).text for src in args.source]
    try:
        print("\n".join(rss_parser(xmls, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
