import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title('Test till you drop')

st.markdown("""
Dit is mijn testpagina! 

xoxo
""")

st.sidebar.header('User Input Features')

# creating lists
index=["Afval", "Bankkosten", "Belasting", "Energie", "Huur gereedschap", "Huur de Brouwer", "Huur Warmenhoven", "Kantine", "Materiaal (MA)", "Materieel (ML)", "Notaris", "Parkeerkosten", "Service", "Storting de Brouwer", "Storting Warmenhoven", "Vergunning", "Verzekering", "Werk derden", "ZZP", "Inkomsten"]
jaar_2018 =[-1999.94, -34.20, 0, -868.97, -1683.76, 0, 0, -136.75, -52501.57, 0, 0, 0, 0, 27500, 22500, -4823.96, 1003.57, 0, -40152.80, 0]
jaar_2017 =[-5111.78, -29.50, 0, -453, -11630.95, 0, 0, -126.17, -23069.63, -3000.59, -7508.50, -67.70, 0, 75000, 75000, -851.50, -2321.63, -55161.60, -38616.16, 0]
jaar_2019 =[-373.53, -35.25, 0, -3470.25, -200, 0, 0, -143.73, -60954.95, 0, 0, -19.68, 0, 18500, 68500, 0, -2500.36, -6110, -46801.77, 0]
jaar_2020 = [0, -36.75, -1227.03, -3719.83, 0, -9040, -13560, -163.39, -27278.98, 0, 0, 0, -60, 500, 7500, -286.45, -57.68, 0, -27055.61, 35726.71]
# creating the DataFrame
df = pd.DataFrame(list(zip(index, jaar_2017, jaar_2018, jaar_2019, jaar_2020))) 
  
# displaying the DataFrame
villa = df.rename(columns = {0: 'Categorie', 1:'2017', 2:'2018', 3:'2019', 4: '2020' })

villa["Totaal per categorie"] = villa.sum(axis=1)

fig = go.Figure()
fig.add_trace(go.Bar(x=villa['Categorie'],
                     y=villa["2017"],
                     name="2017"))
fig.add_trace(go.Bar(x=villa['Categorie'],
                     y=villa["2018"],
                     name="2018"))
fig.add_trace(go.Bar(x=villa['Categorie'],
                     y=villa["2019"],
                     name="2019"))
fig.add_trace(go.Bar(x=villa['Categorie'],
                     y=villa["2020"],
                     name="2020"))
fig.update_layout(
    title_text='Inkomsten en uitgaven 2017-2020', # title of plot
    title_x=0.5,
    yaxis_title_text="Aantal (in EUR)")

st.plotly_chart(fig)

Balans = {'Categorie': 'Balans', '2017': '2051.29', '2018': '-26299.69', 
                  '2019': '-32051.91', '2020': '-35461.69'}

villa_compleet = villa.append(Balans, ignore_index = True)


villa_compleet

