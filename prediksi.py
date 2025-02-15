import numpy as np

# Contoh data baru yang ingin diprediksi
new_data = pd.DataFrame({
    'user_id': [98, 99],  # Ganti dengan user_id yang ingin Anda prediksi
    'item_id': [198, 199]  # Ganti dengan item_id yang ingin Anda prediksi
})

# Encode user_id dan item_id menggunakan encoder yang sudah ada
new_data['user_id'] = user_encoder.transform(new_data['user_id'])
new_data['item_id'] = item_encoder.transform(new_data['item_id'])

# Persiapkan input data untuk prediksi
X_new = {
    'user_input': new_data['user_id'].values,
    'item_input': new_data['item_id'].values
}

# Lakukan prediksi
predictions = model.predict(X_new)

# Tampilkan hasil prediksi
for i, prediction in enumerate(predictions):
    print(f"Prediksi untuk user {new_data['user_id'].iloc[i]} dan item {new_data['item_id'].iloc[i]}: {prediction[0]:.4f}")