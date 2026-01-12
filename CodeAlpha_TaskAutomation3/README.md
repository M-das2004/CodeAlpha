# CodeAlpha_TaskAutomation3: Webpage Title Scraper

## 📌 Project Overview
This project was developed during my **Python Development Internship** at **CodeAlpha**. The goal of this task was to automate a real-life repetitive task—specifically, extracting specific information from a webpage and saving it locally.

This script allows a user to provide any URL, fetches the webpage's HTML, extracts the `<title>` tag using Regular Expressions, and saves that title to a designated text file.

## 🚀 Features
* **Live Web Scraping:** Uses the `requests` library to fetch real-time data from any accessible URL.
* **Regex Extraction:** Utilizes the `re` module to accurately parse the `<title>` element from HTML source code.
* **Automated File Export:** Automatically handles file creation and writing to store the scraped data.
* **Error Handling:** Validates HTTP response status codes before attempting to process data.

## 🛠️ Key Concepts Used
* **Python Requests:** For handling HTTP GET requests.
* **Regular Expressions (re):** For pattern matching and data extraction.
* **File I/O:** For writing data to `.txt` files.
* **User Interaction:** Interactive CLI for inputting URLs and filenames.
