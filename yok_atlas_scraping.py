import requests
from bs4 import BeautifulSoup
import csv

# URL extensions for different types of data to scrape
url_extensions = {
    "main_info": "1000_1.php?y=",
    "settlement_statistics": "1000_2.php?y=",
    "Gender_distribution_of_students": "1010.php?y=",
    "geographic_places_where_students_come_from": "1020ab.php?y=",
    "provinces_of_students": "1020c.php?y=",
    "educational_status_of_students": "1030a.php?y=",
    "high_school_graduation_years_of_students": "1030b.php?y=",
    "high_school_fields_of_students": "1050b.php?y=",
    "high_school_types_of_students": "1050a.php?y=",
    "high_schools_from_which_students_graduated": "1060.php?y=",
    "students_school_firsts": "1030c.php?y=",
    "base_score_and_achievement_statistics": "1000_3.php?y=",
    "last_placed_student _profile": "1070.php?y=",
    "YKS_net_averages_of_students": "1210a.php?y=",
    "students_YKS_scores": "1220.php?y=",
    "YKS_success_order_of_students": "1230.php?y=",
    "preference_statistics_across_the_country": "1080.php?y=",
    "in_which_preferences_students_settled": "1040.php?y=",
    "preference_tendency_general": "1300.php?y=",
    "preference_tendency_university_type": "1310.php?y=",
    "preference_tendency_universities": "1320.php?y=",
    "preference_tendency_provinces": "1330.php?y=",
    "preference_tendency_same_programs": "1340a.php?y=",
    "preference_tendency_programs": "1340b.php?y=",
    "conditions": "1110.php?y=",
}

# Base URL for the scraping site
base_url = "https://yokatlas.yok.gov.tr/content/lisans-dynamic/"

# Function to scrape department and university names from HTML content
def scrape_department_and_university_name(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    department_name_header = soup.find('big')  # Find department name in the content
    department_name = department_name_header.text.strip() if department_name_header else "Unknown Department"
    university_name_rows = soup.find_all('td', class_='thb text-left')
    university_name = "Unknown University"
    for row in university_name_rows: # Extract university name
        if row.text.strip() == "Üniversite":
            university_name_row = row.find_next_sibling('td')
            if university_name_row:
                university_name = university_name_row.text.strip()
            break
    return department_name, university_name

# Function to perform the web scraping and write data to a CSV file
def scrape_and_write_to_csv(csv_file_path, url_extensions, selected_data_types):
    successful_requests = 0
    failed_requests = 0
    failed_program_codes = []
    with open(csv_file_path, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Data Type", "Program Code", "Department Name", "University Name", "Additional Info"])
        with open("UniversityProgramCodes.txt", "r") as program_codes_file:
            lines = program_codes_file.readlines()
            for line in lines:
                program_code = line.strip()
                data_collected_for_this_code = False
                main_info_url = f"{base_url}{url_extensions['main_info']}{program_code}"
                main_response = requests.get(main_info_url, verify=False)
                if main_response.status_code == 200:
                    department_name, university_name = scrape_department_and_university_name(main_response.content)
                    for data_type in selected_data_types:
                        if data_type in url_extensions:
                            data_url = f"{base_url}{url_extensions[data_type]}{program_code}"
                            data_response = requests.get(data_url, verify=False)
                            if data_response.status_code == 200:
                                soup = BeautifulSoup(data_response.content, "html.parser")
                                data_rows = soup.find_all("tr")[1:]
                                for row in data_rows:
                                    cols = row.find_all("td")
                                    row_data = [col.text.strip() for col in cols]
                                    writer.writerow(
                                        [data_type, program_code, department_name, university_name] + row_data)
                                if not data_collected_for_this_code:
                                    successful_requests += 1
                                    data_collected_for_this_code = True 
                            else:
                                failed_requests += 1
                else:
                    failed_requests += 1
                    failed_program_codes.append(program_code)

    return successful_requests, failed_requests, failed_program_codes


# Main scraping logic starts here
selected_data_types = ["main_info"]  # Define which data types to scrape
csv_file_path = "university_data.csv"  # Define the CSV file path for output
successful_requests, failed_requests, failed_program_codes = scrape_and_write_to_csv(csv_file_path, url_extensions, selected_data_types)

print(f"Number of successful requests: {successful_requests}")
print(f"Number of unsuccessful requests: {failed_requests}")

if failed_program_codes:
    print("Program codes that cannot be scraped:", ", ".join(failed_program_codes))

else:
    print("Successfully scraped data from all program codes.")