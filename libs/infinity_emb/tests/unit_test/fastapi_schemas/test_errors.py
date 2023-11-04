from infinity_emb.fastapi_schemas.errors import openai_exception_handler, OpenAIException
import json

def test_exception():
    det = dict(message="a tested error", code=418)
    
    exception = openai_exception_handler(
        request=None,
        exc=OpenAIException(**det)
    )
    
    body = json.loads(exception.body)
    assert "error" in body
    assert body["error"]["message"] == det["message"]
    assert body["error"]["code"] == det["code"]

    
    