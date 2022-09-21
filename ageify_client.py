import requests as re


def ageify_client(name):
    url = f"https://api.agify.io/?name={name}"
    response = re.get(url)
    return response
