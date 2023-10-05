import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

st.title('Wisconsin Breast Cancer Insights')
st.caption('EDA by group 3')
st.text('Lan Jin, Sandhya Kilari, Sahana Manjunath, Kyllan Wunder')
st.divider()

#Breast Cancer Wisconsin (Diagnostic) Data Set
df_cancer = pd.read_csv('https://github.com/SandhyaKilari/datascience/blob/main/data.csv')

tab1, tab2, tab3, tab4 = st.tabs(['heatmap', 'lmplot', 'replot', 'displot'])
                                  
with tab1:
    st.button("Reset", type="primary")
    if st.button('test'):
        st.write('hello')
    else:
        st.write("GoodBye")
    plt.figure(figsize=(20,20))
    heatmap = sns.heatmap(df_cancer.corr(), annot=True, cmap="crest")
    st.pyplot(heatmap.figure)
    

with tab2:
    lmplot = sns.lmplot(x="fractal_dimension_worst", y="fractal_dimension_se", hue="diagnosis", col="diagnosis", lowess=True, data=df_cancer)
    st.pyplot(lmplot.figure)
with tab3:
    replot = sns.relplot(df_cancer, x="radius_mean", y="fractal_dimension_worst", hue="diagnosis")
    st.pyplot(replot.figure)

with tab4:
    displot = sns.displot(df_cancer, x="radius_mean", hue = "diagnosis", col="diagnosis", kind="kde", rug=True)
    st.pyplot(displot.figure)
