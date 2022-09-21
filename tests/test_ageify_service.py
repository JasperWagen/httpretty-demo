import httpretty
import json

from ageify_service import handler


@httpretty.activate()
def test_ageify_service_jasper():
    name = "jasper"
    event = {"queryStringParameters": {"name": name}}
    httpretty.register_uri(
        httpretty.GET,
        "https://api.agify.io/?name={name}",
        body='{"name":"jasper","age":39,"count":3636}',
    )
    assert handler(event, None) == json.dumps(
        {"status_code": 200, "ageify": {"name": name, "age": 39}}
    )


@httpretty.activate()
def test_ageify_service_james():
    name = "james"
    event = {"queryStringParameters": {"name": name}}
    httpretty.register_uri(
        httpretty.GET,
        "https://api.agify.io/?name={name}",
        body='{"name":"james","age":13,"count":3636}',
    )
    assert handler(event, None) == json.dumps(
        {"status_code": 200, "ageify": {"name": name, "age": 13}}
    )


@httpretty.activate()
def test_ageify_service_no_name():
    event = {"queryStringParameters": {"name": ""}}
    httpretty.register_uri(
        httpretty.GET,
        "https://api.agify.io/?name={name}",
        body="",
        status=404,
    )

    assert handler(event, None) == json.dumps(
        {
            "status_code": 404,
            "error": "404 Client Error: Not Found for url: https://api.agify.io/?name=",
            "name": "",
        }
    )


@httpretty.activate()
def test_ageify_service_500():
    event = {"queryStringParameters": {"name": ""}}
    httpretty.register_uri(
        httpretty.GET,
        "https://api.agify.io/?name={name}",
        body="",
        status=500,
    )

    assert handler(event, None) == json.dumps(
        {
            "status_code": 500,
            "error": "500 Server Error: Internal Server Error for url: https://api.agify.io/?name=",
            "name": "",
        }
    )
