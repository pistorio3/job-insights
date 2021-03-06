from .jobs import read


def get_unique_job_types(path):
    types_jobs = set()
    list_jobs = read(path)
    for job in list_jobs:
        types_jobs.add(job["job_type"])
    return list(types_jobs)


def filter_by_job_type(jobs, job_type):
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    industries = set()
    list_jobs = read(path)
    for category in list_jobs:
        if category["industry"] != "":
            industries.add(category["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    list_industries = []
    for job in jobs:
        if job["industry"] == industry:
            list_industries.append(job)
    return list_industries


def get_max_salary(path):
    max_salaries = set()
    list_jobs = read(path)
    for job in list_jobs:
        if job["max_salary"].isnumeric():
            max_salaries.add(int(job["max_salary"]))
    return max(list(max_salaries))


def get_min_salary(path):
    min_salaries = set()
    list_jobs = read(path)
    for job in list_jobs:
        if job["min_salary"].isnumeric():
            min_salaries.add(int(job["min_salary"]))
    return min(list(min_salaries))


def matches_salary_range(job, salary):
    if (
      "min_salary" not in job or "max_salary" not in job
      or not isinstance(job["min_salary"], int)
      or not isinstance(job["max_salary"], int)
      or job["min_salary"] > job["max_salary"]
      or not isinstance(salary, int)
    ):
        raise ValueError("Inputs inválidos")

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            pass
    return list_jobs
