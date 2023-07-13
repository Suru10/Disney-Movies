#import libraries
import streamlit as st
import pandas as pd
import warnings
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
# team -1
# Jordan inspection and top portion
# bruce - cleaning

# team 2 Visualization, and summary
# Tasha -> summary
# Eddie -> 4
# Kaela -> 4
st.title("Disney Movies")

st.markdown(
  "Hey my name is Bruce I just finished my sophmore year of highschool, I'm new to coding and have just started recently and i've really enjoyed it."
)

st.write(
  "Hi, my name is Eduardo, I just finished my sophmore year of highschool, and I have around 2 years of coding experience in python. I hope to become more versatile and learn other coding languages besides python."
)

st.write(
  "Hi! I'm Tasha and I am going into 11th grade. I have a year of coding experience with languages such as html, css, javascript, python, as well as coding with blocks. I hope to continue pursuing programming and hope to study computer science in university."
)

st.markdown(
  "Hello my name is Jordan, I just finished 10th grade and I have around 2 years of coding experience in languages such as javascript and python."
)

st.markdown(
  "Hoy, my name is Kaela and I just finished my first year of highschool. Althogh I only have a year of experince with high level computer lanuges, I hope to find the capiblity to learn new computing lagnues outside of JavaScript."
)

# Load the data set
df = pd.read_csv("disney_movies.csv")

# Inspection code
st.header("Inspection")
df.head()
st.markdown("\n")
st.markdown("This displays the first five movies in the dataframe and the first five movies that disney ever produced. This shows that the movies are arranged in order of release date from earliest released to newest"
)

df.columns
st.markdown("\n")
st.markdown(
  "This shows the names of each column of the dataframe, namely 'movie_title', 'release_date', 'genre', 'mpaa_rating', 'total_gross', and 'inflation_adjusted_gross'."
)

df.shape
st.markdown("\n")
st.markdown(
  ".shape reveals that this dataframe of disney movies has 579 rows and 6 columns of data."
)

df.describe()
st.markdown("\n")
st.markdown("")

df.tail()
st.markdown("\n")
st.markdown("")

# Cleaning code:
# checking for null values:
df.isna().sum()
st.markdown("\n")
st.markdown(
  "isna.sum is a code that checks for any missing information within the dataset in this case we had 17 nul values in genre and 56 in mappa rating"
)
# Drop the column
df.drop("inflation_adjusted_gross", axis=1, inplace=True)
st.markdown("\n")
st.markdown(
  ".drop code allows you to get rid of a column, witch we used to get rid inflation adjusted gross and any other irrelivent information"
)
# Remove Null values
df.dropna(inplace=True)
# Dropna allows you to remove all the nul values in a data set making a more detailed
df.reset_index(drop=True, inplace=True)

# Analysis and Visualizations:

# Hypothesis 1:

# Code:
st.header("Hypothesis 1: How’s genre related to salary?")
fig = plt.figure(figsize=(10, 4))
sns.set_theme()

sns.scatterplot(
  data=df,
  x="genre",
  y="total_gross",
  hue="genre",
)
st.pyplot(fig)

st.write("findings")

# Summary:
#adventure movies were able to make the most money while documentary or horror movies were the least succsesfull for disney and most genre's have somewhat consitant earnings the most inconsistent sees to be action movies with only 3 movies that had high total grossing

# hypothesis: 2
#Code:
data_disney = df[(df["release_date"] >= "2000-01-01")
                 & (df['release_date'] <= "2010-12-31")]
fig = px.bar(data_disney,
             x="movie_title",
             y="total_gross",
             color="release_date")
fig.show()

#Summary:
st.write('I found that Toy Story 3, Finding Nemo, Pirates of the Carribean: Dead Man's Chest, and Alice in Wonderland were the most popular movies. The other movies reached a gross of under 300 million dollars.')

# hypothosis: 3
# code here:
df['release_date'] = pd.to_datetime(df['release_date'])
fig2 = px.scatter(df, x="release_date", y="total_gross", color="movie_title")
fig2.show()

# summery: As shown in the produced scatter plot, the type of correlation between total gross and release_date is weak positive. You can see that as modern disney movies grossed higher on average than past disney movies. However, that may be due to the fact that disney has released more frequently in the modern era.

# hypothosis: 4

# Code:

df['release_decade'] = (df['release_date'].dt.year // 10) * 10
decade_counts = df['release_decade'].value_counts().sort_index()
fig = px.bar(x=decade_counts.index,
             y=decade_counts.values,
             labels={
               'x': 'Decade',
               'y': 'Number of Movies'
             },
             title='Disney Movies by Decade',
             template='plotly_white')
fig.show()

#Summary:
# I found that the 1990s released the most Disney movies, followed by the 2000s. This surprised me as I would have thought the most recent decade would have released the most disney movies. I would assume 2010 to 2020 would have released the most movies if the data was not cut off at 2016. The 1930s have the least amount of movies produced. This makes sense considering the company released their first movie in 1937, leaving the decade only 3 years to make more.

# hypothosis: 5
# Code:
st.subheader("Hypothesis 5: Is there a correlation between decade and genre popularity?")
compare_disney = df.groupby('genre')['release_decade'].value_counts().reset_index(name='count')
fig2 = px.scatter(compare_disney, x="release_decade", y="count", color="genre")
fig2.show()
# Summary:
# I found that the popularity of genres changed each decade. Comedy was very popular in the 80s all the way to the 00s but then adventure tops the 2010s. The genre popularity also depended on the amount of movies release that decade. Overall Comdey, Drama, Adventure and Action found themselves with more movies produced then other genres.

# hypothosis: 6
st.subheader("Hypothesis 6: What month was most popular to release movies?")
df["release_date"] = pd.to_datetime(df["release_date"])
df["month"] = df['release_date'].dt.month
month_df = df.groupby("month")['total_gross'].mean().reset_index()
fig = px.line(month_df, x="month", y="total_gross")
fig.show()

#Summary:
# I found that the overall popularity of disney movies rises and falls in spikes throughout the year. May is the month that is most popular to release movies and September was the least. Overall the summer and winter months seem to be the most popular season to release movies and the season in between not as much

# hypothosis: 7
#Code:

compare_disney = df.groupby('genre')['mpaa_rating'].value_counts().reset_index(
  name='count')
fig2 = px.bar(compare_disney, x="genre", y="count", color="mpaa_rating")
fig2.show()
#Summary
#I found that all Black Comedy movies are all rated R, and all of the Concert/Performance movies are rated G. The other categories each have multiple ratings, but some constant ratings are R, PG, and PG-13.

# hypothosis: 8

import seaborn as sns

sns.set_theme()

sns.scatterplot(
  data=df,
  x="total_gross",
  y="mpaa_rating",
)

# summery: I discovered that the films with pg13 rateing did the best overall and suprizingly R rated moves did the worst when it comes to gross income.

st.title("Summary of Analysis")
