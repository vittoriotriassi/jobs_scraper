from unittest import TestCase
import pytest
from jobs_scraper.scraping import JobsScraper
import pandas as pd


class TestScraping(TestCase):
    """Test to validate JobsScraper."""
    def setUp(self):
        
        self._scraper = JobsScraper(url='https://www.indeed.nl/vacatures?q=software+engineer&l=', pages=3)


    def test_scraping(self):
        
        self._scraper.scrape()
        
