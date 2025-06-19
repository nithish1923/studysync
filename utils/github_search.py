
import requests

def fetch_github_repos(topic, max_results=3):
    headers = {"Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/search/repositories?q={topic}&sort=stars&order=desc&per_page={max_results}"
    response = requests.get(url, headers=headers)
    data = response.json()
    return [item["html_url"] for item in data.get("items", [])]
