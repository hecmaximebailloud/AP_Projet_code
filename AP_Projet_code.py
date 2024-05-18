import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error, mean_absolute_error
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

st.title("Streamlit App with Code Display")

st.header("Displaying Python Code")

# Use st.echo to show the code and execute it
st.subheader("Using st.echo")
with st.echo():
    st.write("This block of code is both shown and executed.")
    st.write("Streamlit makes it easy to create interactive apps.")
