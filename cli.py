import database
from datetime import datetime


def create_post():
    title = input("Enter post title: ")
    body = input("Enter post body: ")
    posts = database.load_posts()
    post_id = len(posts) + 1
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    post = {
        "title": title,
        "body": body,
        "post_id": post_id,
        "date": date
    }
    posts.append(post)
    database.save_posts(posts)

# Implement method to read all posts or specific post if given post_id


def read_post(post_id=None):
    posts = database.load_posts()
    if post_id:
        post = next(
            (element for element in posts if element["post_id"] == post_id), None)
        if post:
            print(
                f"ID: {post['post_id']}\nTitle: {post['title']}\nBody: {post['body']}\nDate: {post['date']}\n")
        else:
            print("No post with ID: {post_id} was found.")
    else:
        for post in posts:
            print(
                f"ID: {post['post_id']}\nTitle: {post['title']}\nBody: {post['body']}\nDate: {post['date']}\n")


# Implement method to update post given post_id

def update_post(post_id):
    posts = database.load_posts()
    post = next(
        (element for element in posts if element['post_id'] == post_id), None)
    if post:
        title = input("Enter title or leave empty: ")
        body = input("Enter body or leave empty: ")
        if title:
            post["title"] = title
        if body:
            post["body"] = body
        database.save_posts(posts)
    else:
        print("No post with ID: {post_id} was found.")

# implement method to delete post given post_id


def delete_post(post_id):
    posts = database.load_posts()
    new_posts = [element for element in posts if element["post_id"] != post_id]
    if len(posts) == len(new_posts):
        print("No post with ID: {post_id} was found.")
    else:
        database.save_posts(new_posts)

# implement method to delete all post


def delete_all():
    database.save_posts([])

# implement method to search post


def search_posts(search_term):
    posts = database.load_posts()
    result = [element for element in posts if search_term in element["title"]]
    for post in result:
        print(
            f"ID: {post['post_id']}\nTitle: {post['title']}\nBody: {post['body']}\nDate: {post['date']}\n")
