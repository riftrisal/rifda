import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from utils.load_data import data_desa
from utils.preprocessing import preprocess_data
from utils.models import build_ncf_model

# Load environment variables from .env
load_dotenv()

# Fetch ratings data
ratings_df = data_desa()

# Preprocess data
preprocessed_df, num_users, num_items, user_encoder, item_encoder = preprocess_data(ratings_df)

# Split data into training and testing sets
train_df, test_df = train_test_split(preprocessed_df, test_size=0.2, random_state=42)

# Prepare input data
X_train = {
    'user_input': train_df['user_id'].values,
    'item_input': train_df['item_id'].values
}
y_train = train_df['Rating bantuan'].values

X_test = {
    'user_input': test_df['user_id'].values,
    'item_input': test_df['item_id'].values
}
y_test = test_df['Rating bantuan'].values

# Build the NCF model
model = build_ncf_model(num_users=num_users, num_items=num_items, embedding_size=50)

# Define callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('models/ncf_model.h5', save_best_only=True, monitor='val_loss', mode='min')

# Train the model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=50,
    batch_size=64,
    callbacks=[early_stopping, model_checkpoint],
    verbose=1
)

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test MAE: {test_mae:.4f}")