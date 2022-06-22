import requests
import json

class Post:
    def __init__(self):
        self.blog_posts = self.get_posts()


    def get_posts(self):
        params= {
            "limit": 10,
        }
        posts_endpoint = "https://dummyjson.com/posts"
        with requests.get(posts_endpoint, params=params) as response:
            response.raise_for_status()

        posts = response.json()['posts']
        posts = self.add_short_and_user_string(posts)

        return posts

    def get_user_name(self, id):
        user_endpoint = f"https://dummyjson.com/users/{id}"
        with requests.get(user_endpoint) as response:
            response.raise_for_status()
            user_data = response.json()
            return f"{user_data['firstName']} {user_data['lastName']}"

    def get_all_user_posts(self, id):
        user_posts_endpoint = f"https://dummyjson.com/users/{id}/posts"
        with requests.get(user_posts_endpoint) as response:
            response.raise_for_status()
            user_posts = response.json()["posts"]
        user_posts = self.add_short_and_user_string(user_posts)

        return user_posts

    def get_post_by_id(self, id):
        user_post_endpoint = f'https://dummyjson.com/posts/{id}'
        with requests.get(user_post_endpoint) as response:
            response.raise_for_status()
            post = response.json()
        post = self.add_short_and_user_string(post)
        return post



    def add_short_and_user_string(self, json_data):
        if type(json_data) == list:
            for x in json_data:
                x["short"] = f'{x["body"][len(x["title"]):len(x["title"])+ 45]}....'
                x["user_string"] = self.get_user_name(x["userId"])
            return json_data
        else:
            json_data["short"] =f'{json_data["body"][len(json_data["title"]):len(json_data["title"])+ 45]}....'
            json_data["user_string"] = self.get_user_name(json_data["userId"])
            return json_data
