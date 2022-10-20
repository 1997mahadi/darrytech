import streamlit as st
import plotly_express as px
import pandas as pd

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Data Visualization App")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application using Visualization Settings on the sidebare.")

# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Lineplots':
    st.sidebar.subheader("Line Plot Settings")
    try:
        x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
        
@st.cache
def load_data():
    data = pd.read_csv('case_time_series (2).csv')
    return data
       
        

st.header('COVID-19 Data Visualization:')
st.write("Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.")

st.write("Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age.") 

st.write("The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently. Get vaccinated when it’s your turn and follow local guidance.")

st.write("The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell.")
      
st.image("Screen Shot 2020-07-02 at 10.41.50 am.png")

data_load_state = st.text('Loading data...')
st.markdown('Dataset :')
data=load_data()
st.write(data)
numeric_columns = list(data.select_dtypes(['float', 'int']).columns)
non_numeric_columns = list(data.select_dtypes(['object']).columns)
non_numeric_columns.append(None)
print(non_numeric_columns)

st.sidebar.subheader("Scatterplot Settings")
st.markdown('Scatterplots')
x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
plot = px.scatter(data_frame=data, x=x_values, y=y_values, color=color_value)
# display the char
st.plotly_chart(plot)

   
df= data.drop(['Date'], axis=1)        
st.markdown('Boxplot')
plot = px.box(data_frame=df)
st.plotly_chart(plot)



st.sidebar.subheader("Histogram Settings")
st.markdown('Histogram')
x = st.sidebar.selectbox('Feature', options=numeric_columns)
bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                             max_value=100, value=40)
color_value = st.sidebar.selectbox("Colored", options=non_numeric_columns)
plot = px.histogram(x=x, data_frame=data, color=color_value)
st.plotly_chart(plot)


st.markdown('Lineplots')
st.line_chart(df)



      
