import streamlit as st
import pandas as pd
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Bantuan Sosial Cijulang",
    page_icon="🏘️",
    layout="wide"
)

# Fungsi untuk setiap halaman
def beranda():
    st.header("🏠 Beranda")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn.pixabay.com/photo/2017/09/06/22/42/village-2724111_1280.jpg", 
                caption="Desa Cijulang")
    with col2:
        st.markdown("""
        **Selamat datang di Sistem Bantuan Sosial Desa Cijulang**
        
        Aplikasi ini membantu dalam:
        - 🎯 Rekomendasi bantuan sosial
        - 📊 Monitoring distribusi
        """)
        
    st.divider()
    st.subheader("📊 Statistik Terkini")
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("Total Penduduk", "850 Jiwa", "2% vs 2023")
    col_stat2.metric("Bantuan Aktif", "15 Program", "3 program baru")
    col_stat3.metric("Kepuasan Masyarakat", "92%", "4% ↑")

def rekomendasi():
    st.header("📑 Rekomendasi Bantuan")
    with st.expander("🔍 Filter Pencarian", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            usia = st.slider("Usia", 0, 100, 30)
            pekerjaan = st.selectbox("Pekerjaan", ["Petani", "Pedagang", "Nelayan", "Lainnya"])
        with col2:
            status = st.radio("Status", ["Menikah", "Belum Menikah", "Duda/Janda"])
            penghasilan = st.number_input("Penghasilan per Bulan (Rp)", 0, 20000000, 1500000)
    
    if st.button("🚀 Generate Rekomendasi", type="primary"):
        with st.spinner("Mencari rekomendasi terbaik..."):
            # Simulasi hasil
            recommendations = {
                "Program": ["PKH", "BPNT", "Bansos Sembako"],
                "Tingkat Kecocokan": ["95%", "88%", "75%"]
            }
            df = pd.DataFrame(recommendations)
            st.dataframe(df,
                        use_container_width=True,
                        column_config={
                            "Tingkat Kecocokan": st.column_config.ProgressColumn(
                                format="%f",
                                min_value=0,
                                max_value=100
                            )
                        })
            
def data_penduduk():
    st.header("📁 Data Penduduk")
    with st.sidebar.expander("⚙️ Filter Data"):
        dusun = st.multiselect("Pilih Dusun", ["Cicurug", "Cikole Kulon", "Cikole Wetan"])
        bantuan = st.selectbox("Jenis Bantuan", ["Semua"] + ["PKH", "BPNT", "BST"])
    
    # Simulasi data
    data = pd.DataFrame({
        "Nama": ["Budi Setiawan", "Siti Aminah", "Ahmad Yusuf"],
        "Dusun": ["Cicurug", "Cikole Wetan", "Cikole Kulon"],
        "Bantuan": ["PKH, BPNT", "BST", "BPNT"],
        "Status": ["Aktif", "Non-Aktif", "Aktif"]
    })
    
    st.dataframe(data,
                use_container_width=True,
                column_config={
                    "Status": st.column_config.SelectboxColumn(
                        options=["Aktif", "Non-Aktif"]
                    )
                },
                hide_index=True)

def tentang():
    st.header("📌 Tentang Aplikasi")
    st.markdown("""
    ### Versi 1.0.0
    Dibangun untuk membantu pemerintahan desa dalam:
    1. Manajemen bantuan sosial
    2. Analisis kebutuhan masyarakat
    3. Pelaporan otomatis
    
    **Tim Pengembang**:
    - 👨💻 Kepala Desa Cijulang
    - 👩💼 Dinas Sosial Kabupaten
    - 🛠️ Tim Teknis Desa
    """)
    
    st.divider()
    st.subheader("📞 Kontak Kami")
    st.write("📧 Email: [bansos@cijulang.desa.id](mailto:bansos@cijulang.desa.id)")
    st.write("📱 WhatsApp: +62 812-3456-7890")

# Navigasi utama
with st.sidebar:
    st.title("🌐 Navigasi")
    menu = st.radio(
        "Menu Utama",
        options=["Beranda", "Rekomendasi", "Data Penduduk", "Tentang"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.divider()
    with st.expander("🔧 Pengaturan"):
        theme = st.selectbox("Tema", ["Light", "Dark"])
        notifikasi = st.toggle("Notifikasi", True)
    
    st.divider()
    st.markdown("🔐 [Login Admin](https://cijulang.desa.id)")
    st.caption("Versi 1.0 | © 2024 Desa Cijulang")

# Routing halaman
if menu == "Beranda":
    beranda()
elif menu == "Rekomendasi":
    rekomendasi()
elif menu == "Data Penduduk":
    data_penduduk()
elif menu == "Tentang":
    tentang()
