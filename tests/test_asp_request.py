from core.asp.request import ASPRequest


def test_request():

    req = ASPRequest(
        task="chat",
    )

    assert req.task == "chat"