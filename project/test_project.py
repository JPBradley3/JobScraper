import pytest
import requests
from unittest.mock import patch
from app import search_jooble_jobs  # Assuming your function is in a file named 'app.py'


@patch('requests.post')
def test_search_jooble_jobs_success(mock_post):
    # Mocking a successful response from Jooble API with 4 jobs per keyword (2 keywords)
    mock_response = {
        "jobs": [
            {
                "title": "Junior Developer",
                "link": "https://job-link.com",
                "description": "Looking for a junior developer with coding experience."
            },
            {
                "title": "Front-end Developer",
                "link": "https://another-job-link.com",
                "description": "Front-end developer role for a bootcamp graduate."
            },
            {
                "title": "Back-end Developer",
                "link": "https://back-end-job-link.com",
                "description": "Looking for a back-end developer for a growing company."
            },
            {
                "title": "Full-stack Developer",
                "link": "https://full-stack-job-link.com",
                "description": "Full-stack developer with experience in front-end and back-end technologies."
            }
        ]
    }

    # Mocking the return value of requests.post to simulate API response
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    keywords = ["bootcamp graduate", "junior developer"]
    jobs = search_jooble_jobs(keywords)

    # Assert that we have exactly 8 jobs returned (4 jobs per keyword, total 2 keywords)
    assert len(jobs) == 8  # We expect 8 jobs because of the two keywords
    assert jobs[0][0] == "Junior Developer"
    assert jobs[1][0] == "Front-end Developer"
    assert jobs[2][0] == "Back-end Developer"
    assert jobs[3][0] == "Full-stack Developer"
    assert jobs[4][0] == "Junior Developer"
    assert jobs[5][0] == "Front-end Developer"
    assert jobs[6][0] == "Back-end Developer"
    assert jobs[7][0] == "Full-stack Developer"


# Test for handling API error response
@patch('requests.post')
def test_search_jooble_jobs_error(mock_post):
    # Mocking an error response from Jooble API
    mock_post.return_value.status_code = 500  # Internal Server Error
    mock_post.return_value.json.return_value = {"error": "Internal Server Error"}

    keywords = ["bootcamp graduate"]
    jobs = search_jooble_jobs(keywords)

    # Assert that no jobs are returned in case of an error
    assert len(jobs) == 0


# Test for invalid API response format (non-JSON response)
@patch('requests.post')
def test_search_jooble_jobs_invalid_json(mock_post):
    # Mocking a non-JSON response from Jooble API
    mock_post.return_value.status_code = 200
    mock_post.return_value.text = "Not a JSON response"

    keywords = ["junior developer"]
    jobs = search_jooble_jobs(keywords)

    # Assert that no jobs are returned when the response is not valid JSON
    assert len(jobs) == 0


# Test for empty job list
@patch('requests.post')
def test_search_jooble_jobs_no_results(mock_post):
    # Mocking a response with no jobs
    mock_response = {
        "jobs": []
    }
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    keywords = ["junior developer"]
    jobs = search_jooble_jobs(keywords)

    # Assert that no jobs are found when the job list is empty
    assert len(jobs) == 0


@patch('requests.post')
def test_search_jooble_jobs_with_job_type_filter(mock_post):
    # Mocking a successful response with job type filter (same 4 jobs for each keyword)
    mock_response = {
        "jobs": [
            {
                "title": "Junior Developer",
                "link": "https://job-link.com",
                "description": "Looking for a junior developer with coding experience."
            },
            {
                "title": "Back-end Developer",
                "link": "https://back-end-job-link.com",
                "description": "Back-end developer with experience in Python and databases."
            },
            {
                "title": "Front-end Developer",
                "link": "https://another-job-link.com",
                "description": "Front-end developer role for a bootcamp graduate."
            },
            {
                "title": "Full-stack Developer",
                "link": "https://full-stack-job-link.com",
                "description": "Full-stack developer needed for various projects."
            }
        ]
    }

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    keywords = ["bootcamp graduate", "junior developer"]
    job_type = "developer"  # Filtering for "developer" job type
    jobs = search_jooble_jobs(keywords, job_type)

    # Assert that we have exactly 8 jobs, all of which contain "developer" in the title
    assert len(jobs) == 8  # We expect 8 jobs because of the two keywords
    assert all("developer" in job[0].lower() for job in jobs)


# Test for empty keyword input
def test_search_jooble_jobs_empty_keywords():
    # Call the function with empty keywords
    jobs = search_jooble_jobs([])

    # Assert that no jobs are returned when no keywords are passed
    assert len(jobs) == 0


# Run tests if this file is executed directly
if __name__ == '__main__':
    pytest.main()

