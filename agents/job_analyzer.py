# agents/job_collector.py

import requests
from bs4 import BeautifulSoup
from state import JobState

class JobCollectorAgent:

    def collect_jobs(self, state: JobState) -> JobState:

        url = "https://www.jobkorea.co.kr/Search/?stext=AI"

        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        jobs = []

        for item in soup.select(".list-post li")[:10]:

            title = item.select_one("a.title").text.strip()
            company = item.select_one(".name").text.strip()

            jobs.append({
                "title": title,
                "company": company
            })

        state["jobs"] = jobs
        return state