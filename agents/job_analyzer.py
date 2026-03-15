# agents/job_analyzer.py

from langchain.chat_models import init_chat_model

class JobAnalyzerAgent:

    def __init__(self):
        self.llm = init_chat_model("gpt-5-mini", model_provider="openai")

    def analyze(self, state):

        analyzed = []

        for job in state["jobs"]:

            prompt = f"""
            다음 채용공고를 분석하세요.

            제목: {job['title']}

            다음을 추출하세요:
            - 직무
            - 요구 기술
            - 경력 요구사항
            """

            result = self.llm.invoke(prompt).content

            job["analysis"] = result
            analyzed.append(job)

        state["analyzed_jobs"] = analyzed
        return state