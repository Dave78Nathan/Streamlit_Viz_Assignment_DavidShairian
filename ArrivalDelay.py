import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Disable the warning
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Average Arrival Delay for Each Airline, by Month')

# Load data
df_flight = pd.read_csv("C:\\Users\\david\\OneDrive\\Desktop\\PlotlyActivity_DavidShairian\\Upd_Viz_DavidShairian\\flight_delays.csv", index_col="Month", sep=';')

# Interactive features
selected_airlines = st.multiselect('Select Airlines', df_flight.columns)

if selected_airlines:
    df_selected = df_flight[selected_airlines]
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title("Average Arrival Delay for Selected Airlines, by Month")
    sns.heatmap(data=df_selected, annot=True, ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Airline")
    st.pyplot(fig)
else:
    st.write("Please select at least one airline.")