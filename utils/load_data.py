import os
from dotenv import load_dotenv
from supabase import create_client
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Fetch Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def data_desa():
    """
    Fetch ratings data from Supabase.
    Returns:
        DataFrame: Pandas DataFrame containing user_id, item_id, and rating.
    """
    try:
        response = supabase.table("data_desa").select("*").execute()
        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            print("No data found in the 'ratings' table.")
            return pd.DataFrame()
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Debugging: Fetch and display data
    ratings_df = data_desa()
    print(ratings_df.head())