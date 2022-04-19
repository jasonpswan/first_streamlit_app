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


# Add a pick list so they can choose what they want in their smoothie
streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index))

# Display the data set so they can see which fruit (and portion sizes) we have available
streamlit.dataframe(list(my_fruit_list.index, ['Avocado', 'Strawberry'])
