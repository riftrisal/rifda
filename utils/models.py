import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense, Concatenate
from tensorflow.keras.models import Model

def build_ncf_model(num_users, num_items, embedding_size=50):
    """
    Build a Neural Collaborative Filtering (NCF) model.
    Parameters:
        num_users (int): Number of unique users.
        num_items (int): Number of unique items.
        embedding_size (int): Size of the embedding vectors.
    Returns:
        Model: Compiled TensorFlow model.
    """
    # User input
    user_input = Input(shape=(1,), name='user_input')
    user_embedding = Embedding(input_dim=num_users, output_dim=embedding_size, name='user_embedding')(user_input)
    user_vecs = Flatten(name='flatten_user')(user_embedding)

    # Item input
    item_input = Input(shape=(1,), name='item_input')
    item_embedding = Embedding(input_dim=num_items, output_dim=embedding_size, name='item_embedding')(item_input)
    item_vecs = Flatten(name='flatten_item')(item_embedding)

    # Dot product
    dot_product = Dot(axes=1, name='dot_product')([user_vecs, item_vecs])

    # Concatenate user and item embeddings
    concat = Concatenate(name='concatenate')([user_vecs, item_vecs])

    # Fully connected layers
    dense_1 = Dense(128, activation='relu', name='dense_1')(concat)
    dense_2 = Dense(64, activation='relu', name='dense_2')(dense_1)
    dense_3 = Dense(32, activation='relu', name='dense_3')(dense_2)

    # Output layer
    output = Dense(1, activation='sigmoid', name='output')(dense_3)

    # Build the model
    model = Model(inputs=[user_input, item_input], outputs=output)

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    return model

if __name__ == "__main__":
    # Debugging: Build and summarize the model
    model = build_ncf_model(num_users=100, num_items=200, embedding_size=50)
    model.summary()