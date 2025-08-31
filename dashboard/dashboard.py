import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


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

weather_map = {1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan/Salju', 4: 'Hujan Deras/Badai'}
bikes_day_df['weather_desc'] = bikes_day_df['weathersit'].map(weather_map)
bikes_hour_df['weather_desc'] = bikes_hour_df['weathersit'].map(weather_map)

weather_daily_mean = bikes_day_df.groupby('weather_desc')['cnt'].mean().sort_values(ascending=False)
weather_hourly_mean = bikes_hour_df.groupby('weather_desc')['cnt'].mean().sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x=weather_daily_mean.index, 
    y=weather_daily_mean.values, 
    hue=weather_daily_mean.index, 
    palette=colors, 
    ax=axes[0], 
    legend=False
)
axes[0].set_title('Rata-rata Penyewaan Harian', fontsize=16)
axes[0].set_xlabel(None)
axes[0].set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)

sns.barplot(
    x=weather_hourly_mean.index, 
    y=weather_hourly_mean.values, 
    hue=weather_hourly_mean.index, 
    palette=colors, 
    ax=axes[1], 
    legend=False
)
axes[1].set_title('Rata-rata Penyewaan Per Jam', fontsize=16)
axes[1].set_xlabel(None)
axes[1].set_ylabel(None)

st.pyplot(fig)

st.markdown("""
**Kesimpulan:**
- **Pola Cuaca:** Kondisi cuaca memiliki korelasi kuat dengan jumlah penyewaan. Rata-rata penyewaan tertinggi terjadi pada saat cuaca **Cerah**. Jumlahnya menurun secara signifikan saat cuaca **Berkabut** dan anjlok drastis saat **Hujan Ringan/Salju**.
- **Data Harian vs. Per Jam:** Pola ini konsisten baik pada data harian maupun per jam, menunjukkan bahwa keputusan untuk menyewa sepeda sangat dipengaruhi oleh kondisi cuaca saat itu.
""")

st.markdown("---")

st.subheader('Puncak Jam Penyewaan Sepeda')

hourly_rentals = bikes_hour_df.groupby('hr')['cnt'].mean()

fig_hourly, ax_hourly = plt.subplots(figsize=(14, 7))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, color='dodgerblue', linewidth=2.5, marker='o', markersize=8, ax=ax_hourly)

ax_hourly.axvline(x=8, color='coral', linestyle='--', linewidth=2, label='Puncak Pagi (08:00)')
ax_hourly.axvline(x=17, color='crimson', linestyle='--', linewidth=2, label='Puncak Sore (17:00)')

ax_hourly.set_title('Rata-rata Penyewaan Sepeda per Jam (Keseluruhan)', fontsize=18)
ax_hourly.set_xlabel('Jam dalam Sehari', fontsize=12)
ax_hourly.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
ax_hourly.set_xticks(range(0, 24))
ax_hourly.legend()

st.pyplot(fig_hourly)

st.markdown("""
**Kesimpulan:**
Pola penyewaan per jam menunjukkan adanya **dua puncak (bimodal)** yang jelas, yang sangat mencerminkan perilaku komuter:
- **Puncak Pagi:** Terjadi lonjakan tajam pada pukul **08:00**, sesuai dengan jam berangkat kerja atau sekolah.
- **Puncak Sore:** Puncak tertinggi terjadi pada pukul **17:00 - 18:00**, sesuai dengan jam pulang kerja.
- **Tengah Hari:** Jumlah penyewaan tetap stabil, menunjukkan adanya aktivitas rekreasi atau perjalanan lain di luar jam komuter.
""")

st.caption("Dibuat berdasarkan analisis dari Bike Sharing Dataset.")
