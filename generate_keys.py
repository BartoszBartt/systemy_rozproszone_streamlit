import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Bartosz Bartoszewski", "Kasia Bator"]
usernames = ["Bartek", "Kasia"]
passwords = ["Bartek", "Kasia"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as f:
    pickle.dump(hashed_passwords, f)
