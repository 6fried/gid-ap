#!/usr/bin/env python

import requests
import json
import csv

headers = {
    "Content-Type": "application/json",
}

url = "https://analytics.api.aiesec.org/v2/applications/analyze.json?access_token=vnQ19HUU9eZhZ2s-IBIdBq2RM3K0RtFZyQfp8w325ek&start_date=2024-02-14&end_date=2024-07-31&performance_v3%5Boffice_id%5D=1623"

response = requests.get(url=url, headers=headers)

if response.status_code == 200:
  data = response.json()
  formatted_data = json.dumps(data, indent=4)

  rows = [
    ["Status", "Applicants", "Unique Applicants"],
    ["Approved", data["approved_total"]["doc_count"], data["approved_total"]["applicants"]["value"]],
    ["Realized", data["realized_total"]["doc_count"], data["realized_total"]["applicants"]["value"]]
  ]

  csv_file = "output.csv"

  with open(csv_file, "w") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

else:
  print(f"Error: {response.status_code}, {response.text}")
