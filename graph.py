# graph.py

from langgraph.graph import StateGraph, START, END
from state import JobState

from agents.job_collector import JobCollectorAgent
from agents.job_analyzer import JobAnalyzerAgent
from agents.job_classifier import JobClassifierAgent
from agents.resume_writer import ResumeWriterAgent
from agents.report_writer import ReportWriterAgent


def create_graph():

    graph = StateGraph(JobState)

    collector = JobCollectorAgent()
    analyzer = JobAnalyzerAgent()
    classifier = JobClassifierAgent()
    resume = ResumeWriterAgent()
    report = ReportWriterAgent()

    graph.add_node("collector", collector.collect_jobs)
    graph.add_node("analyzer", analyzer.analyze)
    graph.add_node("classifier", classifier.classify)
    graph.add_node("resume", resume.write_resume)
    graph.add_node("report", report.write_report)

    graph.add_edge(START, "collector")
    graph.add_edge("collector", "analyzer")
    graph.add_edge("analyzer", "classifier")
    graph.add_edge("classifier", "resume")
    graph.add_edge("resume", "report")
    graph.add_edge("report", END)

    return graph.compile()