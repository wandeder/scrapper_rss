# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import json as JS
import xml.etree.ElementTree as ET


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    channel_tag_list = ['title', 'link', 'lastBuildDate', 'pubDate', 'languadge',
                            'category', 'managinEditor', 'description',]
    item_tag_list = ['title', 'author', 'pubDate', 'link', 'category', 'description']

    def to_parse(xml: str, limit) -> list:
        xml = ET.fromstring(xml)
        result = []
        channel_count = 0
        for channel in xml:
            item_count = 0
            if channel_count == limit:
                break
            channel_dict = dict()

            for channel_tag in channel:
                if channel_tag.tag in channel_tag_list:
                    channel_dict[channel_tag.tag] = channel_tag.text

            if channel.find('item'):
                items_list = []

                for item in channel.findall('item'):
                    if item_count == limit:
                        break
                    item_dict = dict()

                    for item_tag in item:
                        if item_tag.tag in item_tag_list:   
                            item_dict[item_tag.tag] = item_tag.text

                    items_list.append(item_dict)
                    item_count += 1

                channel_dict['items'] = items_list

            result.append(channel_dict)
            channel_count += 1

        return result

    def print_in_console(result: list) -> list:
        result_str = []
        ch_title_colsole = ['Feed', 'Link', 'Last Build Date', 'Date', 
                            'Languadge', 'Categories','Editor', 'Description']
        item_title_colsole = ['Title', 'Author', 'Date', 'Link', 'Category', 'Description']

        for channel in result:
            for tag in channel_tag_list:
                if channel.get(tag):
                    index = channel_tag_list.index(tag)
                    result_str.append(f"{ch_title_colsole[index]}: {channel.get(tag)}")

            result_str.append('')
            if channel.get('items'):
                for item in channel.get('items'):
                    for tag in item_tag_list:
                        if item.get(tag):
                            index = item_tag_list.index(tag)
                            if tag == 'description':
                                result_str.append(f"\n{item.get(tag)}\n")
                            else:
                                result_str.append(f"{item_title_colsole[index]}: {item.get(tag)}")
        return result_str
    
    def print_in_json(result: list) -> list:
        if len(result) == 1:
            result = result[0]
        return JS.dumps(result, indent=2)
    
    if json:
        return print_in_json(to_parse(xml, limit))
    else:
        return print_in_console(to_parse(xml, limit))


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
