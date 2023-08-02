# linkedin_scraper.py

import sys
import csv
import argparse
from linkedin_scraper import Person, actions
from selenium import webdriver

def main(url, email, password):
    driver = webdriver.Chrome()

    actions.login(driver, email, password)

    person = Person(url, driver=driver)

    with open('output.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Latest Institution', 'Location', 'Company', 'Job Title', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Only write the header once.
        if csvfile.tell() == 0:
            writer.writeheader()

        print(person)
        
        writer.writerow(
            {
                'Name': person.name, 
                'Latest Institution': person.experiences[0].institution_name,
                'Location': person.experiences[0].location,
                'Company': person.company, 
                'Job Title': person.job_title,
                'URL':person.linkedin_url
            }
        )
    
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='LinkedIn scraper.')
    parser.add_argument('--url', type=str, help='LinkedIn profile URL.')
    parser.add_argument('--email', type=str, help='LinkedIn login email.')
    parser.add_argument('--password', type=str, help='LinkedIn login password.')

    args = parser.parse_args()

    main(args.url, args.email, args.password)
