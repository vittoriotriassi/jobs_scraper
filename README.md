# jobs_scraper

[![Build Status](https://travis-ci.com/vittoriotriassi/jobs_scraper.svg?branch=master)](https://travis-ci.com/vittoriotriassi/jobs_scraper)
![PyPI](https://img.shields.io/pypi/v/jobs_scraper?color=informational&label=PyPI)

jobs_scraper is a simple job postings scraper for the website [Indeed](https://www.indeed.com), it is written in Python and is based on the ```requests``` and ```BeautifulSoup``` libraries.

## Installation

Run the following to install the package:
```python
pip install jobs_scraper
```

## Usage
To use jobs_scraper you need to create a new JobsScraper object and provide the following attributes to its constructor:
- ```country```: prefix country.
- ```position```: job position.
- ```location```: job location.
- ```pages```: number of pages to be scraped.

```python
from jobs_scraper import JobsScraper

# Let's create a new JobsScraper object and perform the scraping for a given query.
scraper = JobsScraper(country="nl", position="Data Engineer", location="Amsterdam", pages=3)
df = scraper.scrape()
```

In this way, the first three pages for the example query "Data Engineer" based in "Amsterdam" on the Dutch version of the portal Indeed get scraped.
The ```scrape``` method returns a Pandas dataframe, therefore it is possible to export it into a csv file.

#### Additional Parameters
- ```max_delay```: bearing in mind that this package is meant only for educational purposes, a delay in the requests can be provided.
By setting ```max_delay``` in the constructor, every job posting will be randomly scraped in an interval between ```0``` and ```max_delay``` seconds.

  ```python
  scraper = JobsScraper(country="...", position="...", location="...", pages=..., max_delay=5)
  ```
  
- ```full_urls```: since most of the scraped job urls are pretty long, the returned Pandas dataframe will truncate them, making it not simple to access. Setting ```full_urls``` to ```True```, the scraped urls will not be truncated.
  ```python
  scraper = JobsScraper(country="...", position="...", location="...", pages=..., full_urls=True)
  ```
  
## TODO
- Add rotating proxies to prevent the scraper from being blocked once too many requests are sent.
