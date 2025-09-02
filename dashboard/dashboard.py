import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    day_df = pd.read_csv("data/day.csv")
    hour_df = pd.read_csv("data/hour.csv")
    
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    return day_df, hour_df

bikes_day_df, bikes_hour_df = load_data()

st.header('🚲 Dashboard Analisis Penyewaan Sepeda')
st.markdown("Dashboard ini menampilkan analisis data dari set data Bike Sharing.")
st.markdown("Terdapat dua set data: data harian (`day.csv`) dan data per jam (`hour.csv`). Keduanya mencakup informasi tentang jumlah penyewaan sepeda, kondisi cuaca, dan faktor lainnya.")

st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Cuaca')

time_granularity = st.radio(
    "Pilih Granularitas Waktu:",
    ('Harian', 'Per Jam')
)

weather_map = {1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan/Salju', 4: 'Hujan Deras/Badai'}
bikes_day_df['weather_desc'] = bikes_day_df['weathersit'].map(weather_map)
bikes_hour_df['weather_desc'] = bikes_hour_df['weathersit'].map(weather_map)

if time_granularity == 'Harian':
    weather_daily_mean = bikes_day_df.groupby('weather_desc')['cnt'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x=weather_daily_mean.index, 
        y=weather_daily_mean.values, 
        hue=weather_daily_mean.index, 
        palette=colors, 
        ax=ax, 
        legend=False
    )
    ax.set_title('Rata-rata Penyewaan Harian', fontsize=16)
    ax.set_xlabel(None)
    ax.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig)
else:
    weather_hourly_mean = bikes_hour_df.groupby('weather_desc')['cnt'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x=weather_hourly_mean.index, 
        y=weather_hourly_mean.values, 
        hue=weather_hourly_mean.index, 
        palette=colors, 
        ax=ax, 
        legend=False
    )
    ax.set_title('Rata-rata Penyewaan Per Jam', fontsize=16)
    ax.set_xlabel(None)
    ax.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
    st.pyplot(fig)

st.markdown("""
**Kesimpulan:**
- **Pola Cuaca:** Kondisi cuaca memiliki korelasi kuat dengan jumlah penyewaan. Rata-rata penyewaan tertinggi terjadi pada saat cuaca **Cerah**. Jumlahnya menurun secara signifikan saat cuaca **Berkabut** dan anjlok drastis saat **Hujan Ringan/Salju**.
- **Data Harian vs. Per Jam:** Pola ini konsisten baik pada data harian maupun per jam, menunjukkan bahwa keputusan untuk menyewa sepeda sangat dipengaruhi oleh kondisi cuaca saat itu.
""")

st.markdown("---")

st.subheader('Puncak Jam Penyewaan Sepeda')

user_type = st.selectbox(
    label="Pilih Tipe Pengguna untuk Dianalisis:",
    options=('Keseluruhan', 'Pengguna Casual', 'Pengguna Registered')
)

if user_type == 'Pengguna Casual':
    hourly_rentals = bikes_hour_df.groupby('hr')['casual'].mean()
    plot_color = 'orange'
    title_suffix = '(Pengguna Casual)'
    st.markdown("""
    **Kesimpulan (Pengguna Casual):**
    Pola penyewaan per jam menunjukkan adanya **satu puncak (unimodal)** yang mencerminkan perilaku pengguna kasual:
    - **Puncak Siang:** Terjadi lonjakan pada pukul **12:00 - 14:00**, mencerminkan waktu istirahat makan siang atau aktivitas santai di siang hari.
    """)
elif user_type == 'Pengguna Registered':
    hourly_rentals = bikes_hour_df.groupby('hr')['registered'].mean()
    plot_color = 'green'
    title_suffix = '(Pengguna Registered)'
    st.markdown("""
    **Kesimpulan (Pengguna Registered):**
    Pola penyewaan per jam menunjukkan adanya **dua puncak (bimodal)** yang jelas, yang sangat mencerminkan perilaku komuter:
    - **Puncak Pagi:** Terjadi lonjakan tajam pada pukul **08:00**, sesuai dengan jam berangkat kerja atau sekolah.
    - **Puncak Sore:** Puncak tertinggi terjadi pada pukul **17:00 - 18:00**, sesuai dengan jam pulang kerja.        
    """)
else:
    hourly_rentals = bikes_hour_df.groupby('hr')['cnt'].mean()
    plot_color = 'dodgerblue'
    title_suffix = '(Keseluruhan)'
    st.markdown("""
    **Kesimpulan (Keseluruhan):**
    Pola penyewaan per jam menunjukkan adanya **dua puncak (bimodal)** yang jelas, yang sangat mencerminkan perilaku komuter:
    - **Puncak Pagi:** Terjadi lonjakan tajam pada pukul **08:00**, sesuai dengan jam berangkat kerja atau sekolah.
    - **Puncak Sore:** Puncak tertinggi terjadi pada pukul **17:00 - 18:00**, sesuai dengan jam pulang kerja.        
    """)


fig_hourly, ax_hourly = plt.subplots(figsize=(14, 7))
sns.lineplot(
    x=hourly_rentals.index, 
    y=hourly_rentals.values, 
    color=plot_color,
    linewidth=2.5, 
    marker='o', 
    markersize=8, 
    ax=ax_hourly
)

if user_type == 'Keseluruhan':
    ax_hourly.axvline(x=8, color='coral', linestyle='--', linewidth=2, label='Puncak Pagi (08:00)')
    ax_hourly.axvline(x=17, color='crimson', linestyle='--', linewidth=2, label='Puncak Sore (17:00)')
    ax_hourly.legend()

ax_hourly.set_title(f'Rata-rata Penyewaan Sepeda per Jam {title_suffix}', fontsize=18) # Judul dinamis
ax_hourly.set_xlabel('Jam dalam Sehari', fontsize=12)
ax_hourly.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
ax_hourly.set_xticks(range(0, 24))


st.pyplot(fig_hourly)

st.caption("Dibuat berdasarkan analisis dari Bike Sharing Dataset.")
