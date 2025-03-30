# JobScraper

## Description
JobScraper is a web application developed as a final project for Harvard's CS50P course. The application scrapes job boards to aggregate listings for positions suitable for coding boot camp graduates in specified locations. It features a customizable dictionary of keywords that can be edited to refine the search criteria used by the web scraper.

## Features
- **Web Scraping**: Collects job listings from jooble.com, focusing on positions appropriate for coding boot camp graduates.
- **Keyword Customization**: Allows users to edit a dictionary of keywords to expand or narrow the job search.
- **Location-Based Search**: Enables users to specify a location to find relevant job openings in that area.

## Installation
*Note: Specific installation instructions are not provided in the repository. The following are general steps to set up a Python-based web application:*

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/JPBradley3/JobScraper.git
   ```

2. **Navigate to the Project Directory**:
   ```sh
   cd JobScraper
   ```

3. **Set Up a Virtual Environment** (optional but recommended):
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
   *Note: The repository does not include a `requirements.txt` file. You may need to create one based on the project's dependencies.*

## Usage
To run the application locally:

1. **Start the Application**:
   ```sh
   python app.py
   ```

2. **Access the Application**:
   Open a web browser and navigate to `http://localhost:5000` (or the specified port number) to use the application.

*Note: The main application file is assumed to be `app.py` based on standard conventions, though the repository does not specify this.*

## Technologies Used
- **Programming Language**: Python
- **Libraries and Frameworks**:
  - **Flask**: Used for creating the web application.
  - **Requests**: Utilized for making HTTP requests to fetch job listings.
  - **BeautifulSoup**: Employed for parsing HTML content and extracting job data.

## License
*The repository does not specify a license. It's advisable to contact the repository owner for clarification before using or distributing the code.*

For more detailed information, please visit the [JobScraper GitHub repository](https://github.com/JPBradley3/JobScraper).
