import streamlit as st
import requests

# Ganti token akses Anda di sini
access_token = 'EAAQiX0WXmGMBOx8QEWBHZAs2NRIfnPhxqtF6VS4jnriyvpvT8b6oOHumvBeKx4YZBSgEXVRnnmPn0jg0NkiP3oX6ILRueWHVUcch2hV3vZAjH8tYuwu004b5jfQVFOR8nN3kZC7cAQMPyVfKV2rHPuyv1ZB8nD6E52ZBIOgKN21UrxVVxZCVNPiSzN3QvUI3MeO3cFV3WhZA'

# Fungsi untuk mendapatkan rekomendasi interest dari Meta Marketing API
def get_interest_recommendations(query, limit, access_token):
    url = f'https://graph.facebook.com/v14.0/search'
    params = {
        'type': 'adinterest',
        'q': query,
        'limit': min(limit, 10000),  # Batasi limit maksimum menjadi 10,000
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [interest['name'] for interest in data['data']]
    else:
        st.error(f"Error: {response.status_code}")
        st.json(response.json())
        return []

# Konfigurasi halaman Streamlit dengan tema bawaan
st.set_page_config(layout="wide", page_title="Meta Marketing API Interest Recommendations", page_icon=":bar_chart:")

# Konten aplikasi Streamlit
st.title('Meta Marketing API Interest Recommendations')
query = st.text_input('Masukkan kata kunci:', 'fitness')
limit = st.number_input('Masukkan batas (hingga 10,000):', min_value=1, max_value=10000, value=1000)

if st.button('Dapatkan Rekomendasi'):
    interests = get_interest_recommendations(query, limit, access_token)
    if interests:
        st.write('### Rekomendasi Interest')
        st.write(', '.join(interests))
    else:
        st.write('Tidak ada rekomendasi yang ditemukan.')
