# agents/report_writer.py

from langchain.chat_models import init_chat_model

class ReportWriterAgent:

    def __init__(self):
        self.llm = init_chat_model("gpt-5-mini", model_provider="openai")

    def write_report(self, state):

        prompt = f"""
        다음 채용공고 분석 결과를 보고서 형태로 정리하세요.

        {state["classified_jobs"]}

        포함
        - 채용 트렌드
        - 많이 요구되는 기술
        - 지원 전략
        """

        state["report"] = self.llm.invoke(prompt).content

        return state