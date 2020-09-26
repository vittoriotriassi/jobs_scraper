# jobs_scraper (WIP)

[![Build Status](https://travis-ci.com/vittoriotriassi/jobs_scraper.svg?branch=master)](https://travis-ci.com/vittoriotriassi/jobs_scraper)

jobs_scraper is a simple job postings scraper for Indeed.

## Installation

Run the following to install the package:
```python
pip install jobs_scraper
```

## Usage

```python
from jobs_scraper.scraping import JobsScraper

# Let's create a new JobsScraper object and perform the scraping for a given query.
scraper = JobsScraper(country="nl", position="Data Engineer", location="Amsterdam", pages=3)
df = scraper.scrape()
```

In this way, we scrape the first three pages for the query "Data Engineer" based in "Amsterdam" on the Dutch version of the portal Indeed.
The ```scrape``` method returns a Pandas dataframe, therefore it is possible to export it into a csv file.

#### Additional Parameters
Bearing in mind that this package is meant only for educational purposes, a delay in the requests can be provided.
By setting ```max_delay``` in the constructor, a job posting will be randomly scraped in an interval between ```0``` and ```max_delay``` seconds.
```python
scraper = JobsScraper(country="..", position="...", location="...", pages=..., max_delay=5)
```
