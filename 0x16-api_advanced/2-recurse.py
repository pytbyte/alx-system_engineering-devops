#!/usr/bin/python3
"""
Recursive function that queries Reddit API returns a list containing the
titles of all hot articles for a given subreddit.
"""
import requests


def get_hot_titles(subreddit, title_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    custom_headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    query_params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        query_params['after'] = after

    response = requests.get(base_url,
                            headers=custom_headers,
                            params=query_params,
                            allow_redirects=False)

    if response.status_code == 200:
        response_data = response.json()

        for post in response_data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '')
            title_list.append(title)

        # Check if there are more pages (pagination) and continue the recursion
        after = response_data.get('data', {}).get('after')
        if after:
            return get_hot_titles(subreddit, title_list, after)

        # If no more pages, return the title_list
        return title_list
    else:
        return None
