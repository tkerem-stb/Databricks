import requests
import os
from config import DATABRICKS_HOST, DATABRICKS_TOKEN
import json

# Set up environment variables
DATABRICKS_HOST = DATABRICKS_HOST
DATABRICKS_TOKEN = DATABRICKS_TOKEN

# API request to list jobs
url = f"{DATABRICKS_HOST}/api/2.1/jobs/list"
headers = {"Authorization": f"Bearer {DATABRICKS_TOKEN}"}


response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Connection is successful.')
    jobs = response.json().get("jobs", [])
    for job in jobs:
        # print(f"Job ID: {job['job_id']}, Name: {job['settings']['name']}")
        job_id = job.get('job_id')
        job_name = job.get('settings', {}).get('name')
        run_url = f'{DATABRICKS_HOST}/api/2.0/jobs/runs/list?job_id={job_id}'
        print(run_url)
        run_response = requests.get(run_url, headers=headers)  
        # print (run_response)  
            
else:
    print(f"Error: {response.status_code} - {response.text}")

 # Get the job run status

if run_response.status_code == 200:
    print('run_response is successful.')
    # runs = run_response.json()
    # #Write run_response.json
    # with open('run_response.json','w') as file:
    #   json.dump(runs,file, indent = 4)
    runs = run_response.json().get('runs', [])
    print(runs)
    # for run in runs:
    #     print(run)
#         start_time = run.get('start_time')
#         # if start_time and start_time >= one_year_ago:
#         run_status = run.get('state', {}).get('life_cycle_state')
#         print(f'Job ID: {job_id}, Job Name: {job_name}, Status: {run_status}, Start Time: {start_time}')
#         # else:
#             # print(f'Failed to get runs for Job ID: {job_id}, Job Name: {job_name}')
# else:
#     print(f'Error: {response.status_code}')
#     print(response.text)



runs = run_response.json().get('runs', [])
    print(runs)
this returns empty []
