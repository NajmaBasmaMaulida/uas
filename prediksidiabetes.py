import streamlit as st
import numpy as np
import joblib

st.title("Prediksi Diabetes (Ya/Tidak)")

# Input form
with st.form("form_prediksi"):
    st.subheader("Masukkan nilai fitur:")

    HighBP = st.selectbox("Tekanan Darah Tinggi (HighBP)", [0, 1])
    HighChol = st.selectbox("Kolesterol Tinggi (HighChol)", [0, 1])
    CholCheck = st.selectbox("Pemeriksaan Kolesterol (CholCheck)", [0, 1])
    BMI = st.slider("BMI", 10, 50, 25)
    Smoker = st.selectbox("Perokok (Smoker)", [0, 1])
    Stroke = st.selectbox("Riwayat Stroke (Stroke)", [0, 1])
    HeartDiseaseorAttack = st.selectbox("Penyakit Jantung/Serangan (HeartDiseaseorAttack)", [0, 1])
    PhysActivity = st.selectbox("Aktivitas Fisik (PhysActivity)", [0, 1])
    Fruits = st.selectbox("Konsumsi Buah (Fruits)", [0, 1])
    Veggies = st.selectbox("Konsumsi Sayuran (Veggies)", [0, 1])
    HvyAlcoholConsump = st.selectbox("Konsumsi Alkohol Berat (HvyAlcoholConsump)", [0, 1])
    AnyHealthcare = st.selectbox("Punya Asuransi Kesehatan (AnyHealthcare)", [0, 1])
    NoDocbcCost = st.selectbox("Tidak ke Dokter karena Biaya (NoDocbcCost)", [0, 1])
    GenHlth = st.slider("Status Kesehatan Umum (GenHlth)", 1, 5, 3)
    MentHlth = st.slider("Jumlah Hari Tidak Sehat Mental (MentHlth)", 0, 30, 0)
    PhysHlth = st.slider("Jumlah Hari Tidak Sehat Fisik (PhysHlth)", 0, 30, 0)
    DiffWalk = st.selectbox("Kesulitan Berjalan (DiffWalk)", [0, 1])
    Sex = st.selectbox("Jenis Kelamin (Sex, 0=Perempuan, 1=Laki-laki)", [0, 1])
    Age = st.slider("Usia", 18, 80, 30)
    Education = st.slider("Tingkat Pendidikan (Education)", 1, 6, 3)
    Income = st.slider("Pendapatan (Income)", 1, 8, 4)

    submitted = st.form_submit_button("Prediksi")

# Jika tombol ditekan, lakukan prediksi
if submitted:
    # Siapkan input
    input_data = np.array([[ 
        HighBP, HighChol, CholCheck, BMI, Smoker, Stroke,
        HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
        HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
        MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income
    ]])

    # Muat model (ubah path sesuai lokasi model kamu)
    model = joblib.load("model_diabetes.pkl")

    # Prediksi
    pred = model.predict(input_data)[0]

    # Tampilkan hasil
    hasil = "Penderita Diabetes" if pred == 1 else "Tidak Diabetes"
    st.success(f"Hasil Prediksi: *{hasil}*")
