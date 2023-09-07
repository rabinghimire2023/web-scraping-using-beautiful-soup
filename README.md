
# Web Scraping Using Beautiful Soup

## Introduction
Web Scraping is the process of collecting unstructured an structured data in an automated manner.It is the methods of extracting inormation or data from websites. It involves automated software or tools, commonly known as web scrapers or web crawlers, that navigates through web pages, access and retrive data, and then store or mainpulate that data for various purposes. Web Scraping is a valuable technique for collecting data from the intenet at scale, and it has a wide range of applications across different indsutries.

### Use cases of Web Scraping
- Price monitoring and comparison
- Market Research and Competitive Analysis
- News Aggregation and Analysis
- Lead Generation
- Real Estate Data Collection
- Social Media Analysis
- Academic Research
- Weather Data Retrieval
- Job Market Insights
- Stock Market Analysis
- Travel and Flight Information
- Content Aggregation and Content Creation
- Language Learning and Translation

## The Basics of web data extraction
A web scrapper automates the process of extracting information from other webistes, quickly and accurately. The process involves two parts: **web Crawler** and **web scraper**.

The web crawler is the horse, and the scraper is the chariot.

### Differences between web crawler and web scraper
#### The crawler
A web crawler, which we generally call a "spider", is an aritficial intelligence that browses the internet to index and search for content by following links and exploring.
#### The scraper
A web scraper is a specialized tool designed to accuratley and quickly extract data from a web page. Web data scraping tools vary widely in design and complexity, depending on the project.

## Web scraping using Beautiful Soup
Beautiful Soup is a python for pulling data out of HTML and XML files. It works with parser to provide idiomatic ways of navgating, searching, and modifying the parse tree.

## Installation of Beautiful Soup (Windows)
Creating a virtual environment (optional)
```python
py -m venv env
.\env\Scripts\activate
```
Installing Beautiful Soup
```python
pip install beautifulsoup4
```
Installing a parser
```python
pip install lxml
pip install html5lib
```
Importing Beautiful Soup
```python
import requests
from bs4 import BeautifulSoup
```

## Web Scraping of Job posts
The above python script is designed to scrape the job posts, company name, location, published date and apply link from the url ("https://realpython.github.io/fake-jobs/"
) and store the scraped data in a CSV file.

- Clone the project
```
git clone git@github.com:rabinghimire2023/web-scraping-using-beautiful-soup.git
```
- Install the required libraries
```
pip install -r requirements.txt
```

## References
1. https://www.tutorialspoint.com/beautiful_soup/index.htm
2. https://realpython.com/beautiful-soup-web-scraper-python/
3. https://www.crummy.com/software/BeautifulSoup/bs4/doc/



