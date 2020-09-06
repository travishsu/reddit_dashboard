import streamlit as st
import pandas as pd

from reddit import Reddit
from config import subscribed_subrs

mode = st.sidebar.radio(
    "top from domain or top in subr",
    ("domain", "subr")
)
subr = st.sidebar.selectbox(
    "Which subreddit?",
    subscribed_subrs
)

custom_subr = st.sidebar.text_input(
    "New subreddit?",
    value='null'
)

time_filter = st.sidebar.selectbox(
    "Time range",
    ("day", "week", "month", "all")
)

domain = st.sidebar.text_input("Domain", value='imgur.com')

reddit_url = 'https://reddit.com'
reddit = Reddit()
if mode == 'subr':
    submissions = reddit.top_k_in_subreddit(
        subr if custom_subr == 'null' else custom_subr,
        time_filter=time_filter
    )
elif mode == 'domain':
    submissions = reddit.top_k_from_domain(
        domain,
        time_filter=time_filter
    )

records = [(s.score, s.title, s.permalink) for s in submissions]
df = pd.DataFrame(records, columns=['score', 'title', 'permalink'])
df = df.assign(permalink=reddit_url+df.permalink)
df = df.sort_values(by='score', ascending=False)

st.title('Top 100')
st.table(df)
