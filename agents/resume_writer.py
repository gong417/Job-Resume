# agents/resume_writer.py

from langchain.chat_models import init_chat_model

class ResumeWriterAgent:

    def __init__(self):
        self.llm = init_chat_model("gpt-5-mini", model_provider="openai")

    def write_resume(self, state):

        jobs = state["classified_jobs"]

        prompt = f"""
        다음 채용공고들을 기반으로 맞춤 이력서를 작성하세요.

        {jobs}

        포함 내용
        - 핵심 기술
        - 프로젝트
        - 경험 강조
        """

        result = self.llm.invoke(prompt).content

        state["resume"] = result
        return state