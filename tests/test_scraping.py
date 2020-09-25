from unittest import TestCase
import pytest
from jobs_scraper.scraping import JobsScraper
import pandas as pd


class TestScraping(TestCase):
    """Test to validate JobsScraper."""
    def setUp(self):
        
        self._scraper = JobsScraper(country = "NL", position = "Software Engineer", location = "", pages = 2, max_delay = 1)


    def test_scraping(self):
        """Test to validate that the scraping works as expected."""
        self._scraper.scrape()
        
