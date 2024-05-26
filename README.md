---

# YÖK Atlas Data Scraper

This Python script is designed to scrape various types of data from the YÖK Atlas website and save the collected data into a CSV file.

Codes are still draft. Updates will be added.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Functions](#functions)
- [scrape_department_and_university_name](#scrape_department_and_university_name)
- [scrape_and_write_to_csv](#scrape_and_write_to_csv)
- [Data Types](#data-types)
- [Output](#output)
- [Notes](#notes)
- [License](#license)

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `csv` module (comes with Python standard library)

You can install the required libraries using pip:
```sh
pip install requests beautifulsoup4
```

## Usage

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Run the Script**:
    ```sh
    python yok_atlas_scraping.py
    ```

3. The script will generate a CSV file named `university_data.csv` in the same directory.

4. **Note**:
   - Ensure that your internet connection is stable to avoid failed requests. If any program codes cannot be scraped, they will be listed in the console output.
   - Don't forget to paste the codes of the university you want to encrypt in the txt file.

## Functions

### scrape_department_and_university_name

```python
def scrape_department_and_university_name(html_content):
```

This function extracts the department and university names from the provided HTML content. It uses BeautifulSoup to parse the HTML and find the relevant tags containing the required information.

### scrape_and_write_to_csv

```python
def scrape_and_write_to_csv(csv_file_path, url_extensions, selected_data_types):
```

This function handles the main scraping logic and writes the collected data to a CSV file. It iterates over a range of program codes, constructs URLs for different data types, and scrapes the data if the response status is 200 (OK). It also keeps track of successful and failed requests.

## Data Types

The script can scrape the following types of data from the YÖK Atlas website:

- Main Information
- Settlement Statistics
- Gender Distribution of Students
- Geographic Places Where Students Come From
- Provinces of Students
- Educational Status of Students
- High School Graduation Years of Students
- High School Fields of Students
- High School Types of Students
- High Schools From Which Students Graduated
- Students' School Firsts
- Base Score and Achievement Statistics
- Last Placed Student Profile
- YKS Net Averages of Students
- Students' YKS Scores
- YKS Success Order of Students
- Preference Statistics Across the Country
- In Which Preferences Students Settled
- Preference Tendency General
- Preference Tendency University Type
- Preference Tendency Universities
- Preference Tendency Provinces
- Preference Tendency Same Programs
- Preference Tendency Programs
- Conditions

## Output

The script generates a CSV file named `university_data.csv` which contains the scraped data. The CSV file includes columns for data type, program code, department name, university name, and the specific fields of data scraped from the website.

## Notes

- Ensure that your internet connection is stable to avoid failed requests.
- The script uses a range of program codes for demonstration purposes. Adjust the range as necessary for your use case.
- If any program codes cannot be scraped, they will be listed in the console output.
- If you want to scrape additional types of data, modify the `selected_data_types` list in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
