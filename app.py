import streamlit as st
import pandas as pd

from reddit import Reddit
from config import subscribed_subrs

mode = st.sidebar.radio(
    "top from domain or top in subr",
    ("domain", "subr")
)
subr = st.sidebar.selectbox(
    "which subreddit?",
    subscribed_subrs
)

custom_subr = st.sidebar.text_input(
    "new subreddit?",
    value='null'
)

time_filter = st.sidebar.selectbox(
    "time range",
    ("day", "week", "month", "all")
)

domain = st.sidebar.text_input("which domain", value='imgur.com')

reddit_url = 'https://redd.it/'
reddit = Reddit()
if mode == 'subr':
    st.title(f'Top 100 in subreddit {subr}, {time_filter}')
    submissions = reddit.top_k_in_subreddit(
        subr if custom_subr == 'null' else custom_subr,
        time_filter=time_filter
    )
elif mode == 'domain':
    st.title(f'Top 100 from domain {domain}, {time_filter}')
    submissions = reddit.top_k_from_domain(
        domain,
        time_filter=time_filter
    )

records = [(s.score, s.title, s.id) for s in submissions]
df = pd.DataFrame(records, columns=['score', 'title', 'permalink'])
df = df.assign(permalink=reddit_url+df.permalink)
df = df.sort_values(by='score', ascending=False)

st.table(df)
