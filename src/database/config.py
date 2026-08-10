# import streamlit as st

# from supabase import create_client, Client

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]

# )

import os
import streamlit as st
from supabase import create_client, Client

def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return os.environ.get(key)

supabase: Client = create_client(
    get_secret("SUPABASE_URL"),
    get_secret("SUPABASE_KEY")
)