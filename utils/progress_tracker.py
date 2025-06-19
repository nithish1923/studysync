
import json
import os

PROGRESS_FILE = "user_progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(user_email, day, status):
    data = load_progress()
    if user_email not in data:
        data[user_email] = {}
    data[user_email][day] = status
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_user_progress(user_email):
    data = load_progress()
    return data.get(user_email, {})
