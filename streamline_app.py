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


# New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input("What fruit would you like information about?", "Kiwi")
streamlit.write("The user entered", fruit_choice)
                                    

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)

# Take the json version of the response and normalise it 
fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())
# Output it to the screen as a table
streamlit.dataframe(fruityvice_normalised)




import snowflake.connector;

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# Add the end user to add a fruit to the fruit load list
add_my_fruit = streamlit.text_input("What fruit would you like to add?" , "Kiwi")
