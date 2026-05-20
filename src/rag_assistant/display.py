def print_answer_and_sources(result: dict) -> None:
    print("\n--- Answer ---")
    print(result["answer"])

    print("\n--- Sources ---")
    for source in result["sources"]:
        print(source)