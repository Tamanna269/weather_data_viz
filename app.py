import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    # Replace with the path to your dataset
    df = pd.read_csv('Weather Data.csv')
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    return df
# Main function to run the app
def main():
    # Load data
    df = load_data()
    
    st.title("Weather Data visualization")
    # Sidebar for column selection
    st.sidebar.title("Select a Column")
    column = st.sidebar.radio(
        "Choose a column to display:",
        df.columns.tolist()[1:]
    )

    # Display the selected column data
    st.header(f"Visualizations for {column}")

    # Check if the selected column is numeric for plotting
    if pd.api.types.is_numeric_dtype(df[column]):
        fig_hist = px.histogram(df, x=column, title=f"Histogram of {column}")
        st.plotly_chart(fig_hist)

        fig_box = px.box(df, y=column, title=f"Box Plot of {column}")
        st.plotly_chart(fig_box)

        fig_line = px.line(df, y=column, title=f"Line Plot of {column}")
        st.plotly_chart(fig_line)

        # Scatter plot might require another numeric or categorical variable
        if 'Date/Time' in df.columns:
            dated_df = df.set_index('Date/Time').copy()
            period = st.selectbox("Select period",['D','M','2M'])
            num_cols = dated_df.select_dtypes(include='number').columns.tolist()
            dated_df = dated_df.resample(period)[num_cols].mean()
            fig_scatter = px.bar(dated_df, x=dated_df.index, y=column, title=f"Scatter Plot of {column} over Time")
            st.plotly_chart(fig_scatter)
        else:
            st.write("No 'Date' column found for scatter plot over time.")
    else:
        st.write(f"The selected column {column} is not numeric, so graphs are not available.")

if __name__ == "__main__":
    main()