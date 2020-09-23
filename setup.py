from setuptools import setup, find_packages

test_deps = [
    "pytest",
    "pytest-pylint",
    "pytest-cov",
    "requests"
]

setup(
    name='jobs_scraper',
    version='1.0',
    description="A simple job postings scraper for Indeed.",
    packages=find_packages(),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[
        'pandas',
    ],
)