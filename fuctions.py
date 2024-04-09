import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
import joblib
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import calendar

dt = pd.read_csv('Data.csv')


def display_game_info(game_title, df):
    if game_title:
        game_info = df[df['title'] == game_title]
        st.write("**Title:**\t", game_info['title'].values[0])
        st.write("**Score:**\t", game_info['score'].values[0])
        
        score_phrase = game_info['score_phrase'].values[0]
        if score_phrase == "Masterpiece":
            st.write("**Score Phrase:**\t", "<span style='color:gold'>{}</span>".format(score_phrase), unsafe_allow_html=True)
        else:
            score_value = game_info['score'].values[0]
            r = int(max(255 - (score_value * 255 / 10), 0))
            g = int(min(score_value * 255 / 10, 255))
            color_code = "#{:02x}{:02x}00".format(r, g)
            st.write("**Score Phrase:**\t", "<span style='color:{}'>{}</span>".format(color_code, score_phrase), unsafe_allow_html=True)
        
        st.write("**Platform:**\t", game_info['platform'].values[0])
        st.write("**Genre:**\t", game_info['genre'].values[0])
        st.write("**Release Year:**\t", game_info['release_year'].values[0])
        
        release_month = game_info['release_month'].values[0]
        month_names = ["January", "February", "March", "April", "MAY", "June", "July", "August", "September", "October", "November", "December"]
        month_name = month_names[release_month - 1]
        st.write("**Release Month:** ", month_name)

   
def display_score_dist(df):
    st.header('Score Distribution')
    score_counts = df['score'].value_counts()
    st.bar_chart(score_counts)
    st.write("""
    Distribusi skor game cenderung miring ke kiri, yang menunjukkan:
    - Mayoritas game diterima dengan baik, dengan skor sekitar 8.
    - Ada lebih sedikit game yang kurang diterima dengan baik, dengan skor di bawah 5.
    """)

def display_genre_dist(df):
    st.header('Genre Distribution')
    genre_counts = df['genre'].value_counts()
    genre_counts_sorted = genre_counts.sort_values(ascending=False)
    st.bar_chart(genre_counts_sorted)
    st.write("""
    Distribusi genre menunjukkan bahwa:
    - Genre "Action" dan "Adventure" adalah yang paling banyak diproduksi dan kemungkinan besar paling populer di kalangan pemain.
    - Genre "RPG", "Shooter", dan "Racing" juga cukup populer, tetapi tidak sebanyak "Action" dan "Adventure".
    - Pengembang game mungkin ingin fokus pada genre "Action" dan "Adventure" untuk menjangkau audiens yang lebih luas.
    """)

def display_year_dist(df):
    st.header('Release Year Distribution')
    year_counts = df['release_year'].value_counts()
    st.bar_chart(year_counts)
    st.write("""
    Distribusi tahun rilis menunjukkan bahwa:
    - Industri game telah mengalami pertumbuhan yang signifikan sejak awal 2000-an, dengan jumlah rilis tahunan yang meningkat secara dramatis.
    - Puncak rilis tahunan mungkin mencerminkan periode waktu ketika teknologi game dan akses ke game mencapai titik tertentu, memungkinkan lebih banyak game diproduksi dan didistribusikan.
    - Penurunan dalam rilis tahunan setelah puncak mungkin mencerminkan pergeseran dalam industri, seperti pergeseran ke game mobile atau perubahan lain dalam perilaku konsumen.
    """)

def display_month_dist(df):
    st.header('Release Month Distribution')
    bulan_counts = df['release_month'].value_counts()
    bulan_dict = {i: calendar.month_name[i] for i in range(1, 13)}
    bulan_counts.index = bulan_counts.index.map(bulan_dict)
    st.bar_chart(bulan_counts)
    st.write("""
    Distribusi bulan rilis menunjukkan bahwa:
    - Sebagian besar game dirilis pada akhir tahun, dengan puncaknya pada bulan Oktober dan November. Ini mungkin untuk memanfaatkan musim belanja liburan.
    - Bulan-bulan dengan rilis yang lebih sedikit, seperti Mei dan Juni, mungkin mencerminkan periode waktu ketika konsumen kurang mungkin membeli game baru.
    """)

def display_platform_dist(df):
    st.header('Platform Distribution')
    platform_counts = df['platform'].value_counts()
    st.bar_chart(platform_counts)
    st.write("""
    Distribusi platform game menunjukkan bahwa:
    - Sebagian besar game dirilis pada platform seperti PlayStation 2, Xbox 360, dan PlayStation 3. Ini mencerminkan popularitas konsol game ini.
    - Platform lain seperti Wii dan PC juga memiliki jumlah rilis yang signifikan, tetapi tidak sebanyak tiga platform teratas.
    - Pengembang game harus mempertimbangkan platform mana yang paling populer saat merencanakan rilis mereka. Mereka mungkin ingin fokus pada platform dengan jumlah rilis terbanyak, karena ini mungkin mencerminkan di mana sebagian besar pemain berada.
    """)

def display_average_score_by_year(df):
    st.subheader('Average Score by Release Year')
    average_score_by_year = df.groupby('release_year')['score'].mean()
    average_score_by_year.index = average_score_by_year.index.astype(int)
    plt.plot(average_score_by_year.index, average_score_by_year.values, marker='o', color='skyblue', linestyle='-')
    plt.title('Average Score by Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Average Score')
    plt.grid(True)
    st.pyplot(plt)
    st.write("Data skor game IGN dari tahun 1995-2016 menunjukkan tren peningkatan kualitas game secara keseluruhan. Meskipun terdapat fluktuasi dan faktor lain yang perlu dipertimbangkan, data ini dapat bermanfaat bagi pengembang game, gamer, dan industri game untuk meningkatkan kualitas dan pengalaman bermain game.")
    
def display_score_by_platform(df):
    st.subheader('Score by Platform')
    plt.figure(figsize=(10, 15))
    sns.boxplot(x='score', y='platform', data=df, hue='platform')
    plt.title('Score Distribution by Platform')
    plt.xlabel('Score')
    plt.ylabel('Platform')
    st.pyplot(plt)
    st.write('''
    Terdapat perbedaan yang signifikan dalam distribusi skor IGN antar platform. Platform seperti PC, PlayStation 4, dan Xbox One memiliki skor rata-rata yang lebih tinggi dibandingkan platform lain seperti Game Boy Color, Lynx, dan Wii.         

    Actionable Insight :
             
    Fokus pada pengembangan game untuk platform dengan skor IGN tinggi, seperti PC, PlayStation 4, dan Xbox One.''')

def display_score_by_genre(df):
    st.subheader('Score by Genre')
    plt.figure(figsize=(10, 20))
    df.groupby('genre')['score'].mean().sort_values().plot(kind='barh')
    plt.title('Average Score by Genre')
    plt.xlabel('Average Score')
    plt.ylabel('Genre')
    st.pyplot(plt)
    st.write('''
    Data rata-rata skor IGN berdasarkan genre game menunjukkan bahwa terdapat perbedaan kualitas game antar genre. Genre RPG, Action, dan Adventure umumnya memiliki kualitas game yang lebih tinggi dibandingkan genre Music, Sports, Racing, dan Simulation. Faktor-faktor seperti popularitas game, hype, dan tren pasar juga dapat memengaruhi skor game.

    Actionable Insight :
             
    Fokus pada pengembangan game di genre dengan skor IGN tinggi, seperti RPG, Action, dan Adventure.
    Memperhatikan faktor-faktor yang memengaruhi skor IGN, seperti gameplay, grafis, cerita, dan desain.''')


def plat_compr(df):
    st.subheader("Comparison of Game Scores Over Time Between PlayStation, Xbox and PC")
    df_playstation = df[df['platform'].str.contains('PlayStation')]
    df_xbox = df[df['platform'].str.contains('Xbox')]
    df_pc = df[df['platform'].str.contains('PC')]
    df_playstation_yearly = df_playstation.groupby('release_year')['score'].mean()
    df_xbox_yearly = df_xbox.groupby('release_year')['score'].mean()
    df_pc_yearly = df_pc.groupby('release_year')['score'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_playstation_yearly.index, df_playstation_yearly, label='PlayStation',marker='o')
    ax.plot(df_xbox_yearly.index, df_xbox_yearly, label='Xbox',marker='o')
    ax.plot(df_pc_yearly.index, df_pc_yearly, label='PC',marker='o')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Score')
    ax.legend()
    plt.grid(True)
    st.pyplot(fig)
    st.write("""
    Dari grafik, kita dapat mengamati bahwa skor rata-rata game untuk ketiga platform telah berfluktuasi sepanjang tahun. 
    Namun, tampaknya ada tren umum peningkatan skor seiring waktu untuk semua platform, yang menunjukkan bahwa kualitas game telah meningkat.
    """)


def genre_compr(df):
    st.subheader("Comparison of Game Scores Over Time for Top 5 Genres")
    top_5_genres = df['genre'].value_counts().nlargest(5).index.tolist()
    df_top_5_genres = df[df['genre'].isin(top_5_genres)]
    df_top_5_genres_grouped = df_top_5_genres.groupby(['release_year', 'genre'])['score'].mean().unstack()
    fig, ax = plt.subplots(figsize=(12, 8))
    for genre in top_5_genres:
        ax.plot(df_top_5_genres_grouped.index, df_top_5_genres_grouped[genre], label=genre,marker='o')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Score')
    ax.legend()
    plt.grid(True)
    st.pyplot(fig)
    st.write('''
    Grafik garis ini menunjukkan bagaimana skor rata-rata game berubah sepanjang waktu untuk lima genre game teratas. Setiap garis mewakili genre yang berbeda.
    Dari grafik, kita dapat melihat bahwa skor rata-rata untuk setiap genre memiliki pola yang berbeda. Beberapa genre menunjukkan peningkatan konsisten dalam skor rata-rata sepanjang waktu, sementara yang lain menunjukkan fluktuasi atau bahkan penurunan.''')

def display_score_composition_by_platform(df):
    st.subheader('Composition of Game Scores by Top 10 Platform')
    platform_scores = df.groupby('platform')['score'].sum().nlargest(10)
    plt.figure(figsize=(8, 8))
    plt.pie(platform_scores, labels=platform_scores.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(plt)

def display_score_composition_by_genre(df):
    st.subheader('Composition of Game Scores by Top 10 Genre')
    platform_scores = df.groupby('genre')['score'].sum().nlargest(10)
    plt.figure(figsize=(8, 8))
    plt.pie(platform_scores, labels=platform_scores.index, autopct='%1.1f%%', startangle=140)
    st.pyplot(plt)
    
def predict():
    model = joblib.load('dtc.pkl')
    encoder = joblib.load('encoder.pkl')

    platform = st.selectbox('Platform', [''] + sorted(dt['platform'].unique().tolist()))
    genre = st.selectbox('Genre', [''] + sorted(dt['genre'].unique().tolist()))
    release_year = st.number_input('Release Year')
    release_month = st.number_input('Release Month')

    if st.button('Predict'):
        df = pd.DataFrame({
            'platform': [platform],
            'genre': [genre],
            'release_year': [release_year],
            'release_month': [release_month]
        })
        df_encoded = pd.DataFrame(encoder.transform(df))
        if hasattr(encoder, 'get_feature_names_out'):
            feature_names = encoder.get_feature_names_out(df.columns)
        else:
            feature_names = encoder.get_feature_names(df.columns)
        df_encoded.columns = feature_names
        prediction = model.predict(df_encoded)
        
        if prediction[0] == 1:
            st.write(f'Predicted score sentiment:', unsafe_allow_html=True)
            st.markdown('<p style="color: lime; font-size:20px;"><b>Positive</b></p>', unsafe_allow_html=True)
        else:
            st.write(f'Predicted score sentiment:', unsafe_allow_html=True)
            st.markdown('<p style="color: red; font-size:20px;"><b>Negative</b></p>', unsafe_allow_html=True)


