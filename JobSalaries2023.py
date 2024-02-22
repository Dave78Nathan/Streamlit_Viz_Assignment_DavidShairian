import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    st.title('Tech Job Salaries for 2023')

    # Load data
    jobs_data = 'C:\\Users\\david\\OneDrive\\Desktop\\PlotlyActivity_DavidShairian\\Upd_Viz_DavidShairian\\jobs_in_data.csv'
    df = pd.read_csv(jobs_data, sep=';')
    
    # Sidebar options
    st.sidebar.title('Options')
    num_rows = st.sidebar.slider('Number of Rows to Display', min_value=100, max_value=1000, value=500, step=100)
    selected_category = st.sidebar.selectbox('Select Job Category', df['job_category'].unique())

    # Filter data by selected job category
    df_job = df.head(num_rows)
    if selected_category:
        df_job = df_job[df_job['job_category'] == selected_category]
    
    # Check if df_job is empty
    if df_job.empty:
        st.write("No data available for the selected category.")
    else:
        # Calculate average salary
        average_salary_df = df_job.groupby('job_category')['salary_in_usd'].mean().reset_index()

        # Plot bar chart
        fig = px.bar(average_salary_df, x='job_category', y='salary_in_usd', title='Salaries for tech jobs for 2023 in USD')
        fig.update_layout(title='Salaries for tech jobs for 2023 in USD (Yearly)', yaxis_tickformat=',.0f')

        # Display the plot and filtered data
        st.plotly_chart(fig)
        st.subheader('Filtered Data')
        st.write(df_job)

main()