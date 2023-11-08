#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words_in_hot_posts(subreddit,
                             words_to_count,
                             after=None,
                             word_counts={}):
    """Prints counts of specified words of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        words_to_count (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        word_counts (dict): The parameter to store results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent and disable following redirects
    headers = {'User-Agent': 'RedditDataAnalyzer/1.0 (ALX Africa)'}
    params = {'limit': 100}  # Limit the number of posts to 100 (maximum)

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        # Extract and parse the titles of the posts
        for post in data.get('data', {}).get('children', []):
            title = post.get('data', {}).get('title', '').lower()
            words_in_title = title.split()

            # Count the occurrences of keywords in the title
            for word in words_to_count:
                if word.lower() in words_in_title:
                    times = words_in_title.count(word.lower())
                    if word_counts.get(word.lower()) is None:
                        word_counts[word.lower()] = times
                    else:
                        word_counts[word.lower()] += times

        # Check if there are more pages (pagination) and continue the recursion
        after = data.get('data', {}).get('after')
        if after:
            return count_words_in_hot_posts(subreddit,
                                            words_to_count,
                                            after,
                                            word_counts)

        if len(word_counts) == 0:
            return

        # If no more pages, print the sorted results
        sorted_word_counts = sorted(word_counts.items(),
                                    key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print("{}: {}".format(word, count))

    elif response.status_code == 404:
        return
    else:
        return
