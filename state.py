# state.py
from typing import TypedDict, List, Dict

class JobState(TypedDict):
    jobs: List[Dict]
    analyzed_jobs: List[Dict]
    classified_jobs: List[Dict]
    resume: str
    report: str