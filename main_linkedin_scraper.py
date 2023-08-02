# main.py

import subprocess

def main():
    urls = [
        "https://www.linkedin.com/in/ali-malik-b1747965/",
        "https://www.linkedin.com/in/nicoihezi/"
        # Add more URLs here...
    ]

    for url in urls:
        subprocess.call(['python', 'linkedinscraper.py', url])

    print("=== ALL DONE ===")

if __name__ == "__main__":
    main()
