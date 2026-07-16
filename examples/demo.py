from core.asp.request import ASPRequest
from core.asp.service import ASPService


def main():

    service = ASPService()

    request = ASPRequest(
        task="summarize_pdf",
        budget="low",
        quality="high",
        latency="normal",
        estimated_input_tokens=10000,
        estimated_output_tokens=1500,
    )

    response = service.optimize(request)

    print("\n========== RESULT ==========")

    print(response.model_dump())

    print("============================")


if __name__ == "__main__":
    main()