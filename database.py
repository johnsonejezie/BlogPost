import os
import json

DB_FILE = "post_database.json"

def load_posts():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return []

def save_posts(posts):
    with open(DB_FILE, 'w') as file:
        json.dump(posts, file)

def delete_all():
    save_posts([])