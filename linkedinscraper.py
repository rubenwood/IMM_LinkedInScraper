# linkedin_scraper.py

import sys
import csv
from linkedin_scraper import Person, actions
from selenium import webdriver

def main(url):
    driver = webdriver.Chrome()

    email = "ruben.wood1@gmail.com"
    password = "TW1nn130092"
    # if email and password isn't given, it'll prompt in terminal
    actions.login(driver, email, password)

    person = Person(url, driver=driver)

    with open('output.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Experiences', 'Latest Institution', 'Location', 'Company', 'Job Title', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Only write the header once.
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Name': person.name, 'Experiences': person.experiences, 'Latest Institution': person.experiences[0].institution_name, 'Location':  person.experiences[0].location, 'Company': person.company, 'Job Title': person.job_title, 'URL': person.linkedin_url})
    
    driver.quit()

if __name__ == "__main__":
    main(sys.argv[1])
