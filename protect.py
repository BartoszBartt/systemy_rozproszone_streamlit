import streamlit as st
from database import add_user, find_password_by_name, find_username
from passlib.hash import pbkdf2_sha256

def login_page():
    st.title("Logowanie")

    username = st.text_input("Nazwa użytkownika")
    password = st.text_input("Hasło", type="password")

    if st.button("Zaloguj się"):
        try:
            user_password = find_password_by_name(name=username)
        except Exception as e:
            st.error("Brak użytkoniwka w bazie danych.")
            
        if pbkdf2_sha256.verify(password, user_password):
            st.success("Zalogowano pomyślnie!")
        else:
            st.error("Nieprawidłowa nazwa użytkownika lub hasło.")

# Strona rejestracji
def register_page():
    st.title("Rejestracja")

    username = st.text_input("Nazwa użytkownika")
    password = st.text_input("Hasło", type="password")

    if st.button("Zarejestruj się"):
        if find_username(username):
            st.error("Nazwa użytkownika jest już zajęta.")
        else:
            hashed_password = pbkdf2_sha256.hash(password)
            add_user(user=username, password=hashed_password)
            st.success("Konto zostało utworzone pomyślnie!")