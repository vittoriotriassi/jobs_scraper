from setuptools import setup, find_packages

test_deps = [
    "pytest",
    "pytest-pylint",
    "pytest-cov",
    "requests",
    "bs4"
]

extras = {
    'test': test_deps,
}

setup(
    name='jobs_scraper',
    version='1.0',
    description="A simple job postings scraper for Indeed.",
    packages=find_packages(),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[
        'pandas',
        'requests',
        'bs4',
        'fake_useragent'
    ],
    extras_require=extras,
)
