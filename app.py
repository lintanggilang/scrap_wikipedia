import streamlit as st
import pandas as pd
import requests

def fetch_tables(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ini akan memunculkan kesalahan jika permintaan HTTP mengembalikan kode status kesalahan
        html_content = response.text
        tables = pd.read_html(html_content)
        return tables, None
    except Exception as e:
        error_message = str(e)  # Ini akan memberikan pesan kesalahan yang lebih rinci
        return None, error_message

def main():
    st.title('URL Table Extractor')

    url = st.text_input('Masukkan URL:', '')

    if st.button('Ambil Tabel'):
        if url:
            tables, error = fetch_tables(url)

            if tables:
                for i, table in enumerate(tables, 1):
                    st.write(f"Tabel {i}")
                    st.write(table)
            elif error:
                st.error(error)

if __name__ == '__main__':
    main()
