import streamlit as st 
from encryption import Encryption
from decryption import Decryption

st.title("Columnar Transposition Cipher")

col_key1, col_key2 = st.columns(2, gap="large")
with col_key1:
    cipher_key = st.text_input("What's your Transposition Cipher key?")

tab1, tab2 = st.tabs(["Encryption", "Decryption"]) 

with tab1:
    with st.form("encryption"):
        text_to_enc = st.text_area("Write your message....")
        button_to_enc = st.form_submit_button("Encrypt")
    
    if button_to_enc:
        en = Encryption(cipher_key)
        encrypted = en.encrypt(text_to_enc)
        st.caption("Encrypted Text:")
        with st.container():
            st.text(encrypted)
with tab2:
    with st.form("decryption"):
        text_to_dec = st.text_area("Write your encrypted message....")
        button_to_dec = st.form_submit_button("Decrypt")
    
    if button_to_dec:
        de = Decryption(cipher_key)
        decrypted = de.decrypt(text_to_dec)
        st.caption("Decrypted Text:")
        with st.container():
            st.text(decrypted)