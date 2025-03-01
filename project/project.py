from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)

# Jooble API credentials
JOOBLE_API_URL = "https://jooble.org/api/f133121f-8588-494c-b1da-b55fb38467f4"  # Replace with your actual API key

# Keywords for bootcamp-friendly jobs
BOOTCAMP_KEYWORDS = [
    "bootcamp graduate", "coding bootcamp", "self-taught", "entry-level developer",
    "junior developer", "apprenticeship program", "new grad program",
    "no degree required", "GitHub profile preferred", "technical projects"
]

def main():
    return

# Function to fetch jobs from Jooble API
def search_jooble_jobs(keywords, job_type=None):
    all_jobs = []

    # Iterate over each keyword and perform a separate search using Jooble API
    for keyword in keywords:
        # Adjust payload to include 'Seattle, WA' for location
        payload = {
            'keywords': f"developer jobs {keyword}",
            'location': 'Seattle, WA',  # Set location to Seattle, WA
            'page': 1  # Jooble paginates the results, so you can adjust the page
        }

        try:
            response = requests.post(JOOBLE_API_URL, json=payload)

            # Check if response is successful
            response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)

            # Try to parse the response JSON
            results = response.json()

            # Check for error in the response body
            if 'error' in results:
                print(f"Error from Jooble API: {results['error']}")
                continue

            # Collect jobs from the response
            jobs = []
            if 'jobs' in results:
                for item in results['jobs']:
                    title = item.get("title", "")
                    link = item.get("link", "")
                    snippet = item.get("description", "")

                    # Categorize jobs based on job_type (optional filter)
                    if job_type:
                        if job_type.lower() in title.lower() or job_type.lower() in snippet.lower():
                            jobs.append((title, snippet, link))
                    else:
                        jobs.append((title, snippet, link))

            # Add the found jobs to all_jobs list
            all_jobs.extend(jobs)

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to parse JSON from the response. Response text: {response.text}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return all_jobs

# Function to save jobs in SQLite
def save_to_db(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, title TEXT, description TEXT, link TEXT)''')

    for job in jobs:
        cursor.execute("INSERT INTO jobs (title, description, link) VALUES (?, ?, ?)", job)

    conn.commit()
    conn.close()

# Route for Front-End Developer jobs
@app.route("/frontend")
def frontend():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS, "front-end")  # Search for front-end developer jobs
    save_to_db(jobs)
    return render_template("job_category.html", jobs=jobs, category="Front-End Developer")

# Route for Back-End Developer jobs
@app.route("/backend")
def backend():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS, "back-end")  # Search for back-end developer jobs
    save_to_db(jobs)
    return render_template("job_category.html", jobs=jobs, category="Back-End Developer")

# Route for Full-Stack Developer jobs
@app.route("/fullstack")
def fullstack():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS, "full-stack")  # Search for full-stack developer jobs
    save_to_db(jobs)
    return render_template("job_category.html", jobs=jobs, category="Full-Stack Developer")

# Route for Python Developer jobs
@app.route("/python")
def python():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS, "python")  # Search for Python developer jobs
    save_to_db(jobs)
    return render_template("job_category.html", jobs=jobs, category="Python Developer")

# Route for JavaScript Developer jobs
@app.route("/javascript")
def javascript():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS, "javascript")  # Search for JavaScript developer jobs
    save_to_db(jobs)
    return render_template("job_category.html", jobs=jobs, category="JavaScript Developer")

# Route to fetch & display all jobs
@app.route("/")
def index():
    jobs = search_jooble_jobs(BOOTCAMP_KEYWORDS)
    save_to_db(jobs)
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
