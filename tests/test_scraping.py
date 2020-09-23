from unittest import TestCase
import pytest
from jobs_scraper.scraping import JobsScraper
import pandas as pd


class TestScraping(TestCase):
    """Test to validate JobsScraper."""
    def setUp(self):
        self._scraper = JobsScraper(headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'},
                                    url='https://www.indeed.nl/vacatures?q=software+engineer&l=', pages=3)


    def test_scraping(self):
        
        self._scraper.scrape()
        
