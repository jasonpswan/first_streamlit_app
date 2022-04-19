import streamlit

streamlit.title ('My Mum\'s New Healthy Diner')

streamlit.header ('Breakfast Favourites')
streamlit.text ('🥣 Omega 3 and Bluberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')



# Section 2 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add a pick list for them to choose the fruit for their smoothie
fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
