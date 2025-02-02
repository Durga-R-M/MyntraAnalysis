import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# Sidebar navigation
r = st.sidebar.radio('Main Menu', ['Home', 'Myntra Data Analysis', 'Pie Chart'])

# Home Page
if r == 'Home':
    st.title('MYNTRA DATA ANALYSIS')
    st.subheader("Welcome to the data analysis of the Myntra dataset from Kaggle")
    st.markdown("*You can visualize the exploratory data analysis on the next page* 😎")
    st.image("myntra-logo.png")

# Myntra data analysis Page
elif r == 'Myntra Data Analysis':
    #df = pd.read_csv('../input/myntra-fashion-dataset/Myntra Fasion Clothing.csv')
    df=pd.read_csv("C:/Users/hp/Desktop/MyntraProject/Myntra Fasion Clothing.csv",encoding="ISO-8859-1")

    st.title("Top 15 Original Prices vs. Brand Names")

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(20, 20))
    sns.barplot(
        x=df["OriginalPrice (in Rs)"].value_counts().head(15).values,
        y=df["BrandName"].value_counts().head(15).index,
        ax=ax,
    )

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Top 15 Brand Names")

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(
        x=df["BrandName"].value_counts().head(15).values,
        y=df["BrandName"].value_counts().head(15).index,
        ax=ax,
    )

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Top 8 Categories")

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(
        x=df["Category"].value_counts().head(15).values,
        y=df["Category"].value_counts().head(15).index,
        ax=ax,
    )

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Top 10 Individual_categories")

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(
        x=df["Individual_category"].value_counts().head(10).values,
        y=df["Individual_category"].value_counts().head(10).index,
        ax=ax,
    )

    # Display the plot in Streamlit
    st.pyplot(fig)

elif r=='Pie Chart':
    df=pd.read_csv("C:/Users/hp/Desktop/MyntraProject/Myntra Fasion Clothing.csv",encoding="ISO-8859-1")

    st.title("TOP BRANDS UNDER TSHIRTS CATEGORY")

    # Filter data for 'tshirts' category
    X = df[df["Individual_category"] == "tshirts"]

    # Get top 10 brands
    top_counts = X["BrandName"].value_counts().head(10)
    t = top_counts.values
    r = top_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(t, labels=r, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 10 Brands in T-Shirts Category")

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("TOP BRANDS UNDER SAREES CATEGORY")

    # Filter data for 'SAREES' category
    X = df[df["Individual_category"] == "sarees"]

    # Get top 10 brands
    top_counts = X["BrandName"].value_counts().head(10)
    t = top_counts.values
    r = top_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(t, labels=r, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 10 Brands in sarees Category")

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("TOP BRANDS UNDER TOPS CATEGORY")

    # Filter data for 'TOPS' category
    X = df[df["Individual_category"] == "tops"]

    # Get top 10 brands
    top_counts = X["BrandName"].value_counts().head(10)
    t = top_counts.values
    r = top_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(t, labels=r, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 10 Brands in tops Category")

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Most selling category in women")

    # Filter data for 'Women' category
    K = df[df["category_by_Gender"] == "Women"]

    # Get top 15 most selling categories
    category_counts = K["Individual_category"].value_counts().head(15)
    S = category_counts.values
    V = category_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(S, labels=V, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 15 Most Selling Categories for Women")

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Most selling brand in women")

    # Filter data for 'Women' category
    K = df[df["category_by_Gender"] == "Women"]

    # Get top 15 most selling brand
    brand_counts = K["BrandName"].value_counts().head(15)
    S = brand_counts.values
    V = brand_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(S, labels=V, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 15 Most Selling Categories for Women")

    # Display the plot in Streamlit
    st.pyplot(fig)
    
    st.title("Most selling brand in men")

    # Filter data for 'Men' category
    K = df[df["category_by_Gender"] == "Men"]

    # Get top 15 most selling brand
    brand_counts = K["BrandName"].value_counts().head(15)
    S = brand_counts.values
    V = brand_counts.index

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(S, labels=V, autopct="%1.2f%%", startangle=140, wedgeprops={"edgecolor": "black"})
    ax.set_title("Top 15 Most Selling brands for Men")

    # Display the plot in Streamlit
    st.pyplot(fig)