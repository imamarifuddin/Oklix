from domain import TaskRequest


def test_task_request():
    task = TaskRequest(
        task="summarize_pdf",
        estimated_input_tokens=5000,
        estimated_output_tokens=1000,
    )

    assert task.task == "summarize_pdf"
    assert task.estimated_input_tokens == 5000
    assert task.estimated_output_tokens == 1000