

from uuid import uuid4

# Store job statuses and paths
jobs = {}

def create_job():
    job_id = str(uuid4())
    jobs[job_id] = {"status": "pending", "output": None}
    return job_id

def update_job_status(job_id, status):
    if job_id in jobs:
        jobs[job_id]["status"] = status

def set_job_output(job_id, output_data):
    if job_id in jobs:
        jobs[job_id]["output"] = output_data
        jobs[job_id]["status"] = "done"

def get_job_status(job_id):
    return jobs.get(job_id, {"status": "not_found"})

def get_job_result(job_id):
    job = jobs.get(job_id)
    return job["output"] if job and job["status"] == "done" else None
