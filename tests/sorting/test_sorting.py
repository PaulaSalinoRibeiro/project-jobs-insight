from src.sorting import sort_by
from copy import deepcopy


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1200, "max_salary": 6000, "date_posted": "2021-10-21"},
        {"min_salary": 1600, "max_salary": 3000, "date_posted": "2022-10-21"},
    ]

    jobs_max_salary = deepcopy(jobs)

    jobs_min_salary = deepcopy(jobs)

    sort_by(jobs_max_salary, "max_salary")

    assert jobs_max_salary[0]["max_salary"] == 6000

    sort_by(jobs_min_salary, "min_salary")

    assert jobs_min_salary[0]["min_salary"] == 1200

    sort_by(jobs, "date_posted")

    assert jobs[0]["date_posted"] == "2022-10-21"
