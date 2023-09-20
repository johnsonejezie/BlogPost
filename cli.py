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
        post = next((element for element in posts if element["post_id"] == post_id), None)
        if post:
            print(f"ID: {post['post_id']}\nTitle: {post['title']}\nBody: {post['body']}\nDate: {post['date']}")
        else :
            print("No post with ID: {post_id} was found.")

#Implement method to update post given post_id


#implement method to delete post given post_id


#implement method to delete all post


#implement method to search post