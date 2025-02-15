import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    """
    Preprocess the ratings data.
    Parameters:
        df (DataFrame): Pandas DataFrame containing user_id, item_id, and rating.
    Returns:
        DataFrame: Preprocessed DataFrame with encoded user_id and item_id.
        int: Number of unique users.
        int: Number of unique items.
        LabelEncoder: Encoder for user_id.
        LabelEncoder: Encoder for item_id.
    """
    # Encode user_id and item_id
    user_encoder = LabelEncoder()
    item_encoder = LabelEncoder()

    df['user_id'] = user_encoder.fit_transform(df['user_id'])
    df['item_id'] = item_encoder.fit_transform(df['item_id'])

    num_users = len(user_encoder.classes_)
    num_items = len(item_encoder.classes_)

    return df, num_users, num_items, user_encoder, item_encoder

if __name__ == "__main__":
    # Debugging: Load and preprocess data
    from load_data import data_desa
    ratings_df = data_desa()
    preprocessed_df, num_users, num_items, user_encoder, item_encoder = preprocess_data(ratings_df)
    print(preprocessed_df.head())
    print(f"Number of Users: {num_users}")
    print(f"Number of Items: {num_items}")