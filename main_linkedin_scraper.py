# main.py

import subprocess
import argparse

def main(email, password):
    urls = [
        "https://www.linkedin.com/in/nicoihezi/",
        # Add more URLs here...
    ]

    for url in urls:
        subprocess.call(['python', 'linkedinscraper.py', '--url', url, '--email', email, '--password', password])
    
    print("DONE")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Main script for LinkedIn scraper.')
    parser.add_argument('--email', type=str, help='LinkedIn login email.')
    parser.add_argument('--password', type=str, help='LinkedIn login password.')

    args = parser.parse_args()

    main(args.email, args.password)
