from setuptools import setup, find_packages

test_deps = [
    "pytest",
    "pytest-pylint",
    "pytest-cov"
]

extras = {
    'test': test_deps,
}

classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name='jobs_scraper',
    version='0.0.2',
    description="A simple job postings scraper for Indeed.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vittoriotriassi/jobs_scraper',
    author='Vittorio Triassi',
    author_email='vi.triassi@gmail.com',
    license='MIT',
    classifiers=classifiers,
    packages=find_packages(),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[
        'pandas',
        'requests',
        'bs4',
        'fake_useragent',
        'tqdm',
        'lxml',
    ],
    extras_require=extras,
)
