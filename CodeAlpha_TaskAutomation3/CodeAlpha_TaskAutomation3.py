import requests
import re

# Take URL and file name from user
url = input("Enter webpage URL: ")
output_file = input("Enter output file name (with .txt): ")

# Send request to webpage
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    # Extract title using regex
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

    if title_match:
        title = title_match.group(1)

        # Save title to file
        with open(output_file, "w") as file:
            file.write(title)

        print("Webpage title scraped successfully!")
        print("Title:", title)
    else:
        print("Title not found.")
else:
    print("Could not open the webpage.")
