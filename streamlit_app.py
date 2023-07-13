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

st.title("Happy Hamburgers")

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
  "Hey, my name is Kaela and I just finished my first year of highschool. Althogh I only have a year of experince with high level computer lanuges, I hope to find the capiblity to learn new computing lagnues outside of JavaScript."
)
st.title("Disney Movies")

# Load the data set
df = pd.read_csv("disney_movies.csv")

# Inspection code
st.header("Inspection")

st.write(df.head())
st.markdown("\n")
st.markdown(
  "This displays the first five movies in the dataframe and the first five movies that disney ever produced. This shows that the movies are arranged in order of release date from earliest released to newest"
)

col1, col2 = st.columns(2)
col2.write(df.columns)
col2.write("\n")
col2.markdown(
  "This shows the names of each column of the dataframe, namely 'movie_title', 'release_date', 'genre', 'mpaa_rating', 'total_gross', and 'inflation_adjusted_gross'."
)

col1.dataframe(df.describe())
col1.markdown("\n")
col1.markdown(
  "Here we are displaying the statistics of the data such as the mean, minimum, and maximum values of each column"
)

st.write(df.shape)
st.markdown("\n")
st.markdown(
  ".shape reveals that this dataframe of disney movies has 579 rows and 6 columns of data."
)

st.write(df.tail())
st.markdown("\n")
st.markdown(
  "This display shows the last five movies in our dataframe and the the newest 5 disney movies produced. It is of note that the dataset we used shows every movie up to 2016"
)

st.header("Cleaning")
# Cleaning code:
# checking for null values:
st.write(df.isna().sum())
st.markdown("\n")
st.markdown(
  "isna.sum is a code that checks for any missing information within the dataset in this case we had 17 nul values in genre and 56 in mappa rating"
)

# Drop the column
df.drop("inflation_adjusted_gross", axis=1, inplace=True)
st.write(df.head())
st.markdown("\n")
st.markdown(
  ".drop code allows you to get rid of a column, witch we used to get rid inflation adjusted gross and any other irrelivent information"
)

# Remove Null values
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
st.write(df.isna().sum())
st.markdown("\n")
st.markdown(
  "Dropna allows you to remove all the nul values in a data set making a more detailed"
)
st.markdown("\n")
st.write (".reset_index allows you to replace the original data set with the updated one without nuls or unnecessary columns."
)

# Analysis and Visualizations:
st.title("Analysis and Visualizations")

st.header("Hypothesis 1: How’s genre related to salary?")

fig = plt.figure(figsize=(10, 4))
sns.set_theme()
sns.scatterplot(data=df, x="genre", y="total_gross", hue="genre")
st.pyplot(fig)

st.subheader("Analysis:")
st.write(
  "Adventure movies were able to make the most money while documentary or horror movies were the least successful for Disney and most genres have somewhat consistant earnings. The most inconsistent seems to be action movies with only 3 movies that had high total grossing."
)

st.header(
  "Hypothesis 2: What was the most popular disney movie from 2000 to 2010?")

data_disney = df[(df["release_date"] >= "2000-01-01")
                 & (df['release_date'] <= "2010-12-31")]
fig2 = px.bar(data_disney,
             x="movie_title",
             y="total_gross",
             color="release_date")
fig2.show()
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Analysis:")
st.write(
  "I found that Toy Story 3, Finding Nemo, Pirates of the Carribean: Dead Man's Chest, and Alice in Wonderland were the most popular movies. The other movies reached a gross of under 300 million dollars."
)

st.header(
  "Hypothesis 3: What is the correlation between box total gross and release date?"
)

df['release_date'] = pd.to_datetime(df['release_date'])
fig3 = px.scatter(df, x="release_date", y="total_gross", color="movie_title")
fig3.show()
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Analysis:")
st.write("The correlation between release date and total gross is an exponentinal strong positive correlation in which you can clearly see the effects of inflation and evolution of Disney movies.")

st.header("Hypothesis 4: What decade produced the most Disney movies?")

df['release_decade'] = (df['release_date'].dt.year // 10) * 10
decade_counts = df['release_decade'].value_counts().sort_index()
fig4 = px.bar(x=decade_counts.index,
             y=decade_counts.values,
             labels={
               'x': 'Decade',
               'y': 'Number of Movies'
             },
             title='Disney Movies by Decade',
             template='plotly_white')
fig4.show()
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Analysis:")
st.write(
  "I found that the 1990s released the most Disney movies, followed by the 2000s. This surprised me as I would have thought the most recent decade would have released the most disney movies. I would assume 2010 to 2020 would have released the most movies if the data was not cut off at 2016. The 1930s have the least amount of movies produced. This makes sense considering the company released their first movie in 1937, leaving the decade only 3 years to make more."
)

st.header(
  "Hypothesis 5: Is there a correlation between decade and genre popularity?")

compare_disney = df.groupby(
  'genre')['release_decade'].value_counts().reset_index(name='count')
fig5 = px.scatter(compare_disney, x="release_decade", y="count", color="genre")
fig5.show()
st.plotly_chart(fig5, use_container_width=True)

st.subheader("Analysis:")
st.write(
  "I found that the popularity of genres changed each decade. Comedy was very popular in the 80s all the way to the 00s but then adventure tops the 2010s. The genre popularity also depended on the amount of movies release that decade. Overall Comdey, Drama, Adventure and Action found themselves with more movies produced then other genres."
)

# hypothosis: 6
st.header("Hypothesis 6: What month was most popular to release movies?")

df["release_date"] = pd.to_datetime(df["release_date"])
df["month"] = df['release_date'].dt.month
month_df = df.groupby("month")['total_gross'].mean().reset_index()
fig6 = px.line(month_df, x="month", y="total_gross")
fig6.show()
st.plotly_chart(fig6, use_container_width=True)

st.subheader("Analysis:")
st.write(
  "I found that the overall popularity of disney movies rises and falls in spikes throughout the year. May is the month that is most popular to release movies, and September was the least. Overall the summer and winter months seem to be the most popular season to release movies and the season in between not as much."
)

# hypothosis: 7
#Code:
st.header("Hypothesis 7: Is there a change between movie genre and rating?")

compare_disney = df.groupby('genre')['mpaa_rating'].value_counts().reset_index(
  name='count')
fig7 = px.bar(compare_disney, x="genre", y="count", color="mpaa_rating")
fig7.show()
st.plotly_chart(fig7, use_container_width=True)

st.subheader("Analysis:")
st.write(
  "I found that all Black Comedy movies are all rated R, and all of the Concert/Performance movies are rated G. The other categories each have multiple ratings, but some constant ratings are R, PG, and PG-13."
)

# hypothosis: 8
st.subheader("Hypothesis 8: Which movie produced the most revenue by rating?")

sns.set_theme()
fig8 = plt.figure(figsize=(10, 4))
sns.scatterplot(
  data=df,
  x="total_gross",
  y="mpaa_rating",
)
st.pyplot(fig8)

st.subheader("Analysis:")
st.write(
  "I discovered that the films rated PG-13 did the best overall in terms of the ability to make record breaking amounts of money. As you can tell from the gragh above, R rated movies did the worst in the total amount of gross income."
)

st.title("Summary of Analysis")
st.markdown("---")
st.write(
  "In the end we came up with 8 different questions from analyzing the Disney Movies dataset."
)
st.markdown("---")
st.subheader("Hypothesis 1: How’s genre related to salary?")
st.write(
  "Adventure movies had the highest salary while Documentary and Horror had the lowest salary. "
)
st.markdown("---")
st.subheader(
  "Hypothesis 2: What was the most popular disney movie from 2000 to 2010?")
st.write(
  "Toy Story 3, Finding Nemo, Pirates of the Carribean: Dead Man's Chest, and Alice in Wonderland were the most popular movies of the 00s."
)
st.markdown("---")
st.subheader(
  "Hypothesis 3: Is there a correlation between total gross and release date?")
st.write(
  "There is not much of a relation as the higher grossing had more to do with the frequency in which disney released movies."
)
st.markdown("---")
st.subheader("Hypothesis 4: What decade produced the most Disney movies?")
st.write(
  "The 1990s produced the most disney movies while the 1930s and 1970s produced the least."
)
st.markdown("---")
st.subheader(
  "Hypothesis 5: Is there a correlation between decade and genre popularity?")
st.write(
  "Genre popularity changed each decade but, Comedy, action, and adventure stayed consistently near the top from the 1930s to the 2010s."
)
st.markdown("---")
st.subheader("Hypothesis 6: What month was most popular to release movies?")
st.write(
  "It was found that May is the most popular month for disney to release movies while September was the least popular."
)
st.markdown("---")
st.subheader("Hypothesis 7: Is there a change between movie genre and rating?")
st.write(
  "All Black Comedy movies are all rated R, and all Concert/Performance movies are rated G. The rest of the genres vary in rating."
)
st.markdown("---")
st.subheader("Hypothesis 8: Which movie produced the most revenue by rating?")
st.write(
  "Movies rated PG-13 garnered the most gross revenue while movies rated R gained the least amount of gross revenue."
)
