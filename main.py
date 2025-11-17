import streamlit as st
import random

st.title("Aplikasi Interaktif Matematika Dasar")

st.write("Pilih operasi matematika dan selesaikan soal yang diberikan!")

# Pilihan operasi
operation = st.selectbox(
    "Pilih Operasi",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)")
)

# Fungsi untuk membuat soal
def generate_question(op):
    if op == "Penjumlahan (+)":
        a, b = random.randint(1, 100), random.randint(1, 100)
        question = f"{a} + {b}"
        answer = a + b
    elif op == "Pengurangan (-)":
        a, b = random.randint(1, 100), random.randint(1, 100)
        if a < b:
            a, b = b, a
        question = f"{a} - {b}"
        answer = a - b
    elif op == "Perkalian (×)":
        a, b = random.randint(1, 12), random.randint(1, 12)
        question = f"{a} × {b}"
        answer = a * b
    else:
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer
        question = f"{a} ÷ {b}"
    return question, answer

if st.button("Buat Soal Baru"):
    st.session_state['question'], st.session_state['answer'] = generate_question(operation)
    st.session_state['feedback'] = ""

if "question" not in st.session_state:
    st.session_state['question'], st.session_state['answer'] = generate_question(operation)
    st.session_state['feedback'] = ""

st.write(f"Soal: **{st.session_state['question']}**")

user_answer = st.number_input("Jawab di sini", value=0, step=1)

if st.button("Cek Jawaban"):
    if user_answer == st.session_state['answer']:
        st.session_state['feedback'] = "✅ Jawaban benar!"
    else:
        st.session_state['feedback'] = f"❌ Jawaban salah. Coba lagi atau buat soal baru!"

st.write(st.session_state['feedback'])
