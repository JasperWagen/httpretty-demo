import json
from requests.exceptions import HTTPError
import ageify_client


def handler(event, _):
    """Lambda handler to return the average age of someone with a given name."""
    name = event["queryStringParameters"]["name"]
    try:
        response = ageify_client.ageify_client(name)
        response.raise_for_status()
        age = response.json()["age"]

    except HTTPError as e:
        return json.dumps(
            {"status_code": e.response.status_code, "error": str(e), "name": name}
        )

    return json.dumps({"status_code": 200, "ageify": {"name": name, "age": age}})


if __name__ == "__main__":
    print(handler({"queryStringParameters": {"name": "Jasper"}}, None))