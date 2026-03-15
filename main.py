from graph import create_graph

def main():

    app = create_graph()

    result = app.invoke({
        "jobs": [],
        "analyzed_jobs": [],
        "classified_jobs": [],
        "resume": "",
        "report": ""
    })

    print("===== Resume =====")
    print(result["resume"])

    print("===== Report =====")
    print(result["report"])


if __name__ == "__main__":
    main()