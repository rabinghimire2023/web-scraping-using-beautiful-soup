"""
Web Scraping of Job Posts,
"""
import csv
import requests
from bs4 import BeautifulSoup


# Scraping
def scrape_jobs(url, output_folder):
    """
    Scrapes job listings data from the url and stores it in a CSV file.

    Args:
        url : The URL to be scraped.
        output_folder : The folder to store all scarped data in .csv format.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", class_="card-content",)
    
    with open(output_folder, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Title", "Company", "Location" ,"Published Date", "Apply Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for job in job_listings:
            title = job.find("h2", class_="title is-5").text.strip()
            subtitle = job.find("h3", class_="subtitle is-6 company").text.strip()
            location = job.find("p", class_="location").text.strip()
            published_date = job.find("time").text.strip()
            apply_link = job.find("a", class_="card-footer-item", text="Apply")["href"]
            # print("Job Title:", title, "\n", subtitle, "\n", location, "\n", published_date, "\n", apply_link)
            
            writer.writerow({"Title":title, "Company":subtitle, "Location":location, "Published Date":published_date, "Apply Link":apply_link})
    

if __name__ == "__main__":
    URL = "https://realpython.github.io/fake-jobs/"
    OUTPUT_FOLDER = "job_data.csv"
    scrape_jobs(URL,OUTPUT_FOLDER)        
  

