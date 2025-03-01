# CodeCamp Friendly Job Listings Scraper

#### Video Demo:

https://www.youtube.com/watch?v=RBr-AhUBgbk


#### Description:

The Job Scraper Web App is a Python-based web application designed to help users search for developer jobs that are open to bootcamp graduates and self-taught developers. The app aggregates job listings from multiple sources, including Jooble, and allows users to filter job results based on specific keywords and job types. It targets entry-level and junior developer roles that prioritize coding skills over formal education.

Key Features:
Job Search Functionality: The app performs web scraping or API calls to job listing platforms, such as Jooble, using relevant search queries. It looks for keywords like "bootcamp graduate," "junior developer," and "self-taught" to target jobs suitable for bootcamp graduates or self-taught developers.

Keyword and Job Type Filtering: Users can filter job listings based on specific keywords (e.g., "developer," "junior," "backend") and job types (e.g., full-time, part-time).

Location-Based Search: The app supports location-based job searches, with the ability to filter jobs specifically for a location like Seattle, Washington.

Job Display: The job listings are displayed on the main page with key details, such as job titles, descriptions, and application links. Users can view the full job details and directly access the application pages.

Database Integration: The app saves job listings into a local SQLite database, allowing for future reference and access to previously fetched job data.

Testing & Reliability: The app is equipped with unit tests using pytest to ensure that the job fetching and filtering functionalities work correctly. Mock responses are used for testing to simulate different scenarios and edge cases.

Technologies Used:
Flask: A lightweight web framework used to build the web application.
Requests: A Python library used to make HTTP requests to external job listing APIs (Jooble).
SQLite: A lightweight database used for storing job listings locally.
Pytest: A testing framework for running unit tests on the app's features.
Use Case:
The app is designed to help individuals who have completed coding bootcamps or are self-taught but lack formal degrees find job opportunities. It filters out jobs that require traditional education and instead highlights roles where coding skills, personal projects, or bootcamp experience are prioritized. This makes it easier for bootcamp graduates and self-taught developers to find relevant positions without getting lost in a sea of traditional job requirements.

This app provides a simple and effective way to search for entry-level developer roles and explore various opportunities based on real-time data from job boards.
