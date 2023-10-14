import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

st.title('Heart Disease Dataset')
st.caption('Presented by Sandhya Kilari')
st.divider()

# Load the dataset into the dataframe
df_heart = pd.read_csv(r"C:\Users\ksand\Downloads\heart.csv")

# Check if there are any missing values in the dataset and drop them
df_heart.isna().sum().dropna()

st.title("Select desired X and Y Variables from the Heart Disease Dataset")
x_variable = st.selectbox("X Variable", df_heart.columns)
y_variable = st.selectbox("Y Variable", df_heart.columns)

data_button = st.selectbox('Please choose preferred visualization', ['Scatter Plot', 'Heatmap', 'Histogram Plot', 'Line Plot', 'Boxplot', 'Relational Plot', 'Distribution Plot'])

if data_button == 'Scatter Plot':
    scatter_plot = sns.scatterplot(data=df_heart, x=x_variable, y=y_variable)
    st.pyplot(scatter_plot.figure)

elif data_button == 'Heatmap':
    plt.figure(figsize=(10,10))
    heatmap = sns.heatmap(df_heart.corr(numeric_only=True), annot=True, cmap="crest")
    st.pyplot(heatmap.figure)

elif data_button == 'Histogram Plot':
    histplot = sns.histplot(data=df_heart, x=x_variable, binwidth=3)
    st.pyplot(histplot.figure)

elif data_button == 'Line Plot':
    lineplot = sns.lmplot(x=x_variable, y=y_variable, hue="target", data=df_heart)
    st.pyplot(lineplot.figure)

elif data_button == 'Boxplot':
    boxplot = sns.boxplot(x=x_variable, hue='target', data = df_heart)
    st.pyplot(boxplot.figure)

elif data_button == 'Relational Plot':
    relplot = sns.relplot(df_heart, x=x_variable, y=y_variable, hue="target", kind="line")
    st.pyplot(relplot.figure)

elif data_button == 'Distribution Plot':
    distplot = sns.displot(df_heart, x=x_variable, hue = "target", col="sex", kind="kde", rug=True)
    st.pyplot(distplot.figure)
    