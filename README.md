# Introduction to Python. Final task.
You are proposed to implement Python RSS-reader using  **python 3.9**.

The task consists of few iterations. Do not start new iteration if the previous one is not implemented yet.

## Common requirements.
* It is mandatory to use `argparse` module.
* Codebase must be covered with unit tests with at least 50% coverage.
* Yor script should **not** require installation of other services such as mysql server,
postgresql and etc. (except Iteration 6). If it does require such programs,
they should be installed automatically by your script, without user doing anything.
* In case of any mistakes utility should print human-readable.
error explanation. Exception tracebacks in stdout are prohibited in final version of application.
* Docstrings are mandatory for all methods, classes, functions and modules.
* Code must correspond to `pep8` (use `pycodestyle` utility for self-check).
  * You can set line length up to 120 symbols.
* Commit messages should provide correct and helpful information about changes in commit. Messages like `Fix bug`, 
`Tried to make workable`, `Temp commit` and `Finally works` are prohibited.

## [Iteration 1] One-shot command-line RSS reader.
RSS reader should be a command-line utility which receives [RSS](wikipedia.org/wiki/RSS) URL and prints results in human-readable format.

You are free to choose format of the news console output. The textbox below provides an example of how it can be implemented:

```shell
$ rss_reader.py "https://news.yahoo.com/rss/" --limit 1

Feed: Yahoo News - Latest News & Headlines

Title: Nestor heads into Georgia after tornados damage Florida
Date: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

[image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
march across a swath of the U.S. Southeast.


Links:
[1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
[2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)

```

Utility should provide the following interface:
```shell
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

```

In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.



With the argument `--verbose` your program should print all logs in stdout.

### Task clarification (I)

1) If `--version` option is specified app should _just print its version_ and stop.
2) User should be able to use `--version` option without specifying RSS URL. For example:
```
> python rss_reader.py --version
"Version 1.4"
```
3) The version is supposed to change with every iteration.
4) If `--limit` is not specified, then user should get _all_ available feed.
5) If `--limit` is larger than feed size then user should get _all_ available news.
6) `--verbose` should print logs _in the process_ of application running, _not after everything is done_.
7) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout_.
8) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout in JSON format_.
9) It is preferrable to have different custom exceptions for different situations(If needed).
10) The `--limit` argument should also affect JSON generation.
11) Format of the RSS Feed can be found [_here_](https://www.rssboard.org/rss-draft-1). We would check for the fields which are required.
12) All html tags should be properly processed in stdout and json.


### HTML tags processing rules:
* Rule 1: List Item processing.
```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```
```
  * Item 1
  * Item 2
  * Item 3
```
```json
{
}
```
* Rule 2: Heading tag processing.
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
```
```
Heading 1
=========

Heading 2
=========

Heading 3
=========

```
* Rule 3: Block item processing.
```html
<p>
This paragraph
contains a lot of lines
in the source code,
but the browser 
ignores it.
</p>

<p>
This paragraph
contains      a lot of spaces
in the source     code,
but the    browser 
ignores it.
</p>

<p>
The number of lines in a paragraph depends on the size of your browser window. If you resize the browser window, the number of lines in this paragraph will change.
</p>
```
```
This paragraphcontains a lot of linesin the source code,but the browser ignores it.
This paragraphcontains a lot of spacesin the source code,but the browser ignores it.
The number of lines in a paragraph depends on the size of your browser window. If you resize the browser window, the number of lines in this paragraph will change.
```
---
Implementations will be checked with the latest cPython interpreter of 3.9 branch.
---

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability. **John F. Woods**
