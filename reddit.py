import praw

class Reddit:
    def __init__(self):
        creds = {
            'client_id': '16GNnnVKWqFFUQ',
            'client_secret': 'Po8YHLBDEObOi9m1hpLbSCnxF8s',
            'user_agent': 'assssssssffffffffffwefwefrgrthtryjtyj'}

        self.reddit = praw.Reddit(**creds)

    def top_k_from_domain(
        self, domain:str, 
        time_filter:str='all', 
        limit:int=100, 
        display=False):

        submissions = self.reddit.domain(domain).top(time_filter=time_filter, limit=limit)
        submissions = list(submissions)
        if display:
            self.display_listgenerator(submissions)
        return submissions

    def top_k_in_subreddit(
        self, subreddit:str,
        time_filter:str='all',
        limit:int=100,
        display=False):
        submissions = self.reddit.subreddit(subreddit).top(time_filter=time_filter, limit=limit)
        submissions = list(submissions)
        if display:
            self.display_listgenerator(submissions)
        return submissions

    def display_listgenerator(self, submissions):
        for submission in submissions:
            print(submission.score, submission.title)