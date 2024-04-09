import streamlit as st
import pandas as pd
from fuctions import *


df = pd.read_csv('Data_Cleaned.csv')
dt = pd.read_csv('Data.csv')

with st.sidebar:
    selected = st.selectbox('Video Game Reviews', ['Home','Information', 'Data Distribution', 'Relation', 'Composition & Comparison', 'Predict'], index=0)

if selected == 'Home':
    st.title("Analisis Dataset IGN Games from Best to Worst")
    st.subheader("Business Objective")
    st.write("Tujuan bisnis dari dataset 'IGN games from best to worst' adalah untuk memahami faktor-faktor apa yang mempengaruhi rating (skor) dari video games. Selain itu, kita dapat membuat prediksi skor berdasarkan fitur-fitur tertentu dari video game tersebut. Analisis ini dapat membantu pengembang game, penerbit, dan pemain untuk memahami elemen-elemen apa yang dapat meningkatkan atau menurunkan kualitas suatu permainan.")

    st.subheader("Assess Situation")
    st.write("Situasi bisnis yang mendasari analisis ini adalah keinginan industri game untuk memahami faktor-faktor kunci yang dapat memengaruhi kesuksesan suatu game. Dengan pemahaman yang lebih baik tentang aspek-aspek yang berkaitan dengan skor, para pengembang game dapat fokus pada elemen-elemen tersebut untuk meningkatkan kualitas dan penerimaan game di pasar.")

    st.subheader("Data Mining Goals")
    st.write("Tujuan dari Data Mining pada dataset ini adalah untuk memahami hubungan antara variabel-variabel seperti platform, genre, tahun rilis, dan lainnya dengan skor suatu game. Selain itu, kita dapat mengembangkan model prediktif yang dapat memperkirakan skor game berdasarkan fitur-fitur tersebut. Hal ini dapat membantu pengambilan keputusan di industri game untuk meningkatkan kualitas dan daya tarik game.")

    st.subheader("Project Plan")
    st.write("Rencana proyek untuk menganalisis dataset ini dimulai dengan pemahaman mendalam tentang karakteristik dataset, seperti distribusi skor, platform yang dominan, genre yang populer, dan lainnya. Selanjutnya, eksplorasi data akan dilakukan untuk mengidentifikasi pola-pola menarik dan korelasi antar variabel. Kualitas data akan dievaluasi, dan langkah-langkah pra-pemrosesan data akan diambil untuk mengatasi masalah data.")
    st.write("Analisis ini dapat memberikan wawasan berharga kepada industri game untuk meningkatkan kualitas dan penerimaan game, serta membantu pemain dalam membuat pilihan berdasarkan preferensi mereka.")

    st.markdown("---")

    st.write("Please select an option from the sidebar to explore further.")


if selected == 'Information':
    st.title("Video Game Information")
    st.write("Select a video game to learn more about it:")

    game_titles = [''] + sorted(df['title'].unique().tolist())
    game_title = st.selectbox("Game Title", game_titles)
    
    display_game_info(game_title, df)

if (selected == 'Data Distribution'):
    st.title("Data Distribution")
    display_score_dist(df)
    display_genre_dist(df)
    display_year_dist(df)
    display_month_dist(df)
    display_platform_dist(df)


if (selected == 'Relation'):
    st.title('Relations')
    display_average_score_by_year(df)
    display_score_by_platform(df)
    display_score_by_genre(df)


if (selected == 'Composition & Comparison'):
    st.title('Composition')
    display_score_composition_by_platform(df)
    display_score_composition_by_genre(df)
    st.title('Comparison')
    plat_compr(df)
    genre_compr(df)

if (selected == 'Predict'):
    st.title('Predict Game Score Sentiment')
    st.write("""
    Setelah memasukkan input yang diperlukan, program akan memberikan prediksi tentang skor sentiment yang mungkin diberikan untuk game berdasarkan input tersebut. 
    """)
    predict()
