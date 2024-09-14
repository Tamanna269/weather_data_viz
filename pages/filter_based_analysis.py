import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    url = 'Weather Data.csv'
    df = pd.read_csv(url)
    return df

df = load_data()

#'Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather'

# Display basic information about the dataset
st.title("Weather Data Analysis")
st.sidebar.title("Navigation")

if st.sidebar.checkbox("Show Dataset Information", value=True):
    st.subheader("Dataset Description")
    st.write(df.describe())

# Bivariate Analysis
st.sidebar.subheader("Bivariate Analysis")

# Scatter plot for Temperature vs. Humidity
if st.sidebar.checkbox("Show Temperature vs. Humidity"):
    st.subheader("Temperature vs. Humidity")
    fig = px.scatter(df, x='Temp_C', y='Dew Point Temp_C', title='Temperature vs. Humidity')
    st.plotly_chart(fig)

# Correlation Analysis
if st.sidebar.checkbox("Show Correlation Matrix"):
    st.subheader("Correlation Matrix")
    correlation = df[['Temp_C', 'Dew Point Temp_C']].corr()
    fig = px.imshow(correlation, text_auto=True, title='Correlation Matrix')
    st.plotly_chart(fig)

# Boxplot for Temperature by Weather Condition
if st.sidebar.checkbox("Show Temperature by Weather Condition"):
    st.subheader("Temperature by Weather Condition")
    fig = px.box(df, x='Weather', y='Temp_C', title='Temperature by Weather Condition')
    st.plotly_chart(fig)

# Multivariate Analysis
st.sidebar.subheader("Multivariate Analysis")

# Pairplot of numerical features
if st.sidebar.checkbox("Show Pairplot"):
    st.subheader("Pairplot")
    fig = px.scatter_matrix(df, dimensions=['Temp_C', 'Dew Point Temp_C', 'Wind Speed_km/h',  'Rel Hum_%',], title='Pairplot')
    st.plotly_chart(fig)

# Correlation Matrix Heatmap
if st.sidebar.checkbox("Show Heatmap of Correlation Matrix"):
    st.subheader("Heatmap of Correlation Matrix")
    corr_matrix = df[['Temp_C', 'Dew Point Temp_C', 'Wind Speed_km/h', 'Rel Hum_%',]].corr()
    fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='thermal', title='Heatmap of Correlation Matrix')
    st.plotly_chart(fig)

