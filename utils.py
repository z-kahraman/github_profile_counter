import json
import os

VIEWS_FILE = "views.json"

def load_views():
    if not os.path.exists(VIEWS_FILE):
        return {}
    with open(VIEWS_FILE, "r") as file:
        return json.load(file)

def save_views(views):
    with open(VIEWS_FILE, "w") as file:
        json.dump(views, file)

def increment_view_count(page_id: str) -> int:
    views = load_views()
    if page_id in views:
        views[page_id] += 1
    else:
        views[page_id] = 1
    save_views(views)
    return views[page_id]

