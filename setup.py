#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="twitter-sentiment",
    author_email='dipanwitamallick2015@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="sentiment analysis on twitter data, saving the result ine elastic search and visualizing the data in kibana",
    entry_points={
        'console_scripts': [
            'twitter_sentiment=twitter_sentiment.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='twitter_sentiment',
    name='twitter_sentiment',
    packages=find_packages(include=['twitter_sentiment', 'twitter_sentiment.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dipanwita2019/twitter_sentiment',
    version='0.1.0',
    zip_safe=False,
)
