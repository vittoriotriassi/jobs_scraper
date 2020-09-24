import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class JobsScraper:
    """JobsScraper is a simple job postings scraper for Indeed."""
    def __init__(self, url: str, pages: int):
        """
        Create a JobsScraper object.

        Parameters
        ------------
        url: str
            Url to be scraped.
            Please provide the general query from the Indeed homepage.
        pages: int
            Number of pages to be scraped.
            Each page contains 15 results.
        """
        self._url = url
        self._ua = UserAgent()
        self._headers = {'User-Agent': self._ua.random}
        self._pages = pages
        self._jobs = []
        
    def _extract_page(self, page):

        r = requests.get("{}&start={}".format(self._url, page), headers = self._headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        return soup

    def _transform_page(self, soup):

        jobs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')

        for job in jobs:

            try:
                title = job.find('a', class_ = 'jobtitle').text.strip().replace('\n', '')
            except:
                title = None
            try:
                company = job.find('span', class_ = 'company').text.strip().replace('\n', '')
            except:
                company = None
            try:
                summary = job.find('div', {'class':'summary'}).text.strip().replace('\n', '')
            except:
                summary = None
            try:
                location = job.find('span', class_ = 'location').text.strip().replace('\n', '')
            except:
                location = None
            try:
                salary = job.find('span', class_ = 'salary').text.strip().replace('\n', '')
            except:
                salary = None

            job = {
                'title': title,
                'location': location,
                'company': company,
                'summary': summary,
                'salary': salary
            }

            self._jobs.append(job)

    def scrape(self) -> pd.DataFrame:
        """
        Perform the scraping of the url provided in the class constructor.
        If duplicates are found, they get dropped.

        Returns
        ------------
        df: pd.DataFrame
            Return a scraped Dataframe.
        """

        for i in range(0, self._pages * 10, 10):

            page = self._extract_page(i)
            self._transform_page(page)
        
        df = pd.DataFrame(self._jobs)
        df.drop_duplicates(inplace=True)

        return df