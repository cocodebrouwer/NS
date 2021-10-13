import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title('NS disruptions van 24/09 - 26/09')

st.markdown("""
We zijn studenten van de minor Data Science. Ons is gevraagd een app te produceren van een zelfgekozen API. We hebben hiervoor het internet 
afgestruind en kwamen uiteindelijk terecht bij een gezamelijk factor: **de Nederlandse Spoorwegen (NS)**. Wij hebben gebruik gemaakt van de gegevens 
van de NS-app van de top 10 grootste stations (Grootste treinstations Nederland, n.d.). Hieruit hebben we de volgende APIs gebruikt: 'places' en 
'reisinformatie'. Uit deze twee API hebben we 'GET list places' en 'GET disruptions' gebruikt. 

Vervolgens hebben we de informatie van **vrijdag (24-09-2021)**, **zaterdag (25-09-2021)** en **zondag (26-09-2021)** opgehaald en opgeslagen in een 
dataframe, waarna we in deze app verschillende visualisaties hebben gemaakt. 
""")

st.sidebar.header('User Input Features')


