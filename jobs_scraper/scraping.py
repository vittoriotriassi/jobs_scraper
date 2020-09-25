import requests
import pandas as pd
from time import sleep
import random
from bs4 import BeautifulSoup
from itertools import cycle
from fake_useragent import UserAgent
from tqdm import tqdm

class JobsScraper:
    """JobsScraper is a simple job postings scraper for Indeed."""

    def __init__(self, url: str, pages: int, max_delay = 0):
        """
        Create a JobsScraper object.

        Parameters
        ------------
        url: str
            Url to be scraped.
            Please provide the general query from the Indeed homepage.
        pages: int
            Number of pages to be scraped. Each page contains 15 results.
        max_delay: int, default=0
            Max number of seconds of delay for the scraping of a single posting.
        """
        self._url = url
        self._ua = UserAgent()
        self._headers = {'User-Agent': self._ua.random}
        self._pages = pages
        self._proxy = []
        self._max_delay = max_delay
        self._jobs = []

    def _proxies(self):

        url = 'https://www.sslproxies.org/'

        r = requests.get(url, headers=self._headers)

        df = pd.read_html(r.text)
        df[0].dropna(inplace=True)
        df[0]['Port'] = df[0]['Port'].astype(int).astype(str)
        df[0]['IP_Port'] = df[0]['IP Address'].str.cat(df[0]['Port'], sep=":")
        proxies_pool = df[0]['IP_Port'].tolist()
        self._proxy = cycle(proxies_pool)

    def _extract_page(self, page):

        current_proxy = next(self._proxy)

        with requests.Session() as request:
            r = request.get(url="{}&start={}".format(self._url, page), proxies={
                            "http://": current_proxy, "https://": current_proxy}, headers=self._headers, timeout=30)

        soup = BeautifulSoup(r.content, 'html.parser')

        return soup

    def _transform_page(self, soup):

        jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job in jobs:

            try:
                title = job.find(
                    'a', class_='jobtitle').text.strip().replace('\n', '')
            except:
                title = None
            try:
                company = job.find(
                    'span', class_='company').text.strip().replace('\n', '')
            except:
                company = None
            try:
                summary = job.find(
                    'div', {'class': 'summary'}).text.strip().replace('\n', '')
            except:
                summary = None

            if job.find('div', class_='location'):
                try:
                    location = job.find(
                        'div', class_='location').text.strip().replace('\n', '')
                except:
                    location = None
            else:
                try:
                    location = job.find(
                        'span', class_='location').text.strip().replace('\n', '')
                except:
                    location = None
            try:
                salary = job.find(
                    'span', class_='salary').text.strip().replace('\n', '')
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

            print("Scraping {}...".format(title))

            if self._max_delay > 0:
                sleep(random.randint(0, self._max_delay))
            
            

    def scrape(self) -> pd.DataFrame:
        """
        Perform the scraping of the url provided in the class constructor.
        If duplicates are found, they get dropped.

        Returns
        ------------
        df: pd.DataFrame
            Return a scraped Dataframe.
        """

        self._proxies()

        for i in tqdm(range(0, self._pages * 10, 10), desc = "Scraping in progress...", total = self._pages):

            page = self._extract_page(i)
            self._transform_page(page)

        df = pd.DataFrame(self._jobs)
        df.drop_duplicates(inplace=True)

        return df
