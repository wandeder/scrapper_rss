# Introduction to Python. Final task.
For this task you are proposed to implement together with us RSS-reader using **python3.9**.

For the purposes of the testing we are going to isolate the parts you are going to work on. Namely you are going to work only on the RSS (XML) scrapping part. Your task is to parse RSS document and provide two pretty formatted output types: JSON and standard output.


We are going to implement for you:
* Command line parsing.
* Receiving of the XML document from the web.

Due to the fact that you can come up with your own style of formatting and that would be difficult for us to test later on. We will provide you with the exact style for the format to ease the testing part.

Format RSS feed that you are going to parse is [RSS 2.0](https://www.rssboard.org/rss-draft-1) you can follow the link to get the full understanding of the specification. But in this task we are asking following requirements:
```html
<channel>...</channel> <!-- Required tags are <title>, <link>, <description>  but we are asking you to be able to parse <title>, <link>, <description>, <category>, <language>, <lastBuildDate>, <managingEditor>, <pubDate>, <item> -->
<item>...</item> <!-- All of the fields here are optional, but item should have at least <title> or <description>, but for the purposes of the test we are asking to be able to parse <title>, <author>, <pubDate>, <link>, <category>, <description> -->
```

Order of the RSS items in all output types should be folowing:
* For `<channel>` element:
  1. `<title>`
  2. `<link>`
  3. `<lastBuildDate>`
  4. `<pubDate>`
  5. `<language>`
  6. `<category>` `for category in categories`
  7. `<managinEditor>`
  8. `<description>`
  9. `<item>` `for item in items`
* For `<item>` element:
  1. `<title>`
  2. `<author>`
  3. `<pubDate>`
  4. `<link>`
  5. `<category>`
  6. `<description>`

Command line interface is going to have following interface. You can use it for the testing purposes. When you will be developing xml document parsing.
 ```shell
usage: rss_reader.py [-h] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

```

**Console Output:**

* For `<channel>` element:
  1. `<title>` is equal Feed
  2. `<link>` is equal to Link
  3. `<lastBuildDate>` is equal to Last Build Date
  4. `<pubDate>` is equal to Date 
  5. `<language>` is equal to Language
  6. `<category>` `for category in categories` is equal to Categories: category1, category2
  7. `<managinEditor>` is equal to Editor
  8. `<description>` is equal to Description
  9. `<item>` `for item in items` each item is separated by custom separator and all items within except for description are stick together.
* For `<item>` element:
  1. `<title>` is equal to Title
  2. `<author>` is equal to Author
  3. `<pubDate>` is equal to Date
  4. `<link>` is equal to Link
  5. `<category>` is equal to Categories: category1, category2
  6. `<description>` is on the separate line without any name.

For the console output we are looking for the order of the things channel items goes first then goes all of the items. between channel and items you can have custom separator and standard new lines, also description within item should be on the new line. For example:
```shell
Feed: Yahoo News - Latest News & Headlines
Link: https://news.yahoo.com/rss
Description: Yahoo news description

Title: Nestor heads into Georgia after tornados damage Florida
Date: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
march across a swath of the U.S. Southeast... <--- !!! THIS IS DESCRIPTION !!!

=========================== <--- !!! CUSTOM SEPARATOR !!!

Title: Some other title
Date: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://some.other.link/some-other-news


Some other new cool information. <--- !!! THIS IS DESCRIPTION
```
**JSON Output:**

In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.

For the JSON output we are looking for the standard names:
But we ask for the pretty output:

```json
{
  "title": "Yahoo News - Latest News & Headlines",
  "link": "https://news.yahoo.com/rss",
  "description": "Yahoo news description"
  "items": [
    {
      "title": "Nestor heads into Georgia after tornados damage Florida",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
march across a swath of the U.S. Southeast..."
    },
    {
      "title": "Some other title",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Some other new cool information."
    }
  ]
}
```
Meaning that you should have indent to be equal to two spaces.


---
Implementations will be checked with the latest cPython interpreter of 3.9 branch.
---

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability. **John F. Woods**
