import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
dotenv_path = ".env"  # Sesuaikan jika file .env berada di lokasi lain
loaded = load_dotenv(dotenv_path)

if not loaded:
    print("File .env tidak ditemukan atau gagal dimuat.")
else:
    print("File .env berhasil dimuat!")

# Fetch variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Error: SUPABASE_URL atau SUPABASE_KEY tidak ditemukan.")
    print("Pastikan file .env berisi nilai yang benar.")
else:
    print(f"SUPABASE_URL: {SUPABASE_URL}")
    print(f"SUPABASE_KEY: {SUPABASE_KEY}")

    try:
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Supabase client created successfully!")

        # Test connection by fetching data from a table (e.g., "users")
        response = supabase.table("data_desa").select("*").execute()
        if response.data:
            print("Data from Supabase:")
            print(response.data)
        else:
            print("No data found in the 'users' table.")
    except Exception as e:
        print(f"Failed to connect or fetch data: {e}")
        
        prediksi_response = supabase.table("prediksi").select("*").execute()
        if prediksi_response.error:
         print(f"Error loading prediksi: {prediksi_response.error}")
        else:
         prediksi_df = pd.DataFrame(prediksi_response.data)
        print("Prediksi loaded successfully:")
        print(prediksi_df.head())