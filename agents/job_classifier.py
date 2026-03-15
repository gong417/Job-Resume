# agents/job_classifier.py

class JobClassifierAgent:

    def classify(self, state):

        classified = []

        for job in state["analyzed_jobs"]:

            text = job["analysis"]

            if "Python" in text or "AI" in text:
                job["category"] = "AI"

            elif "Spring" in text or "Java" in text:
                job["category"] = "Backend"

            else:
                job["category"] = "Other"

            classified.append(job)

        state["classified_jobs"] = classified
        return state