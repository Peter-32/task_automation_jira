import streamlit as st
from time import sleep
from streamlit import caching
from pandas import DataFrame, read_csv

caching.clear_cache()

# Read data
options_df = read_csv("options.csv")
options3_df = read_csv("options3.csv")
df = read_csv("example_data.csv")
with  open('ticket_number.txt') as f:
    ticket_number = int(f.read())
    if ticket_number > 1:
        with open('ticket_number.txt', 'w') as f:
            f.write("0")
        ticket_number = 0

# Get key
key = df.iloc[ticket_number].key
project = key.split('-')[0]

# Display header and description
key
st.header(df.iloc[ticket_number].title)
df.iloc[ticket_number].description

# Display option box
option = st.selectbox(
'Which Type Is This?',
options_df.loc[options_df['project'] == project]['options']
)

# Display text box
option2 = st.text_input('Add a New Type', '')

option3 = st.selectbox(
'How should we automate this task?',
options3_df.loc[options_df['project'] == project]['options']
)

option4 = st.text_input('Add a New Automation Choice', '')

# Text box input response
if option2 != '':
    with open('options.csv', 'a') as f:
        f.write('\n' + project + ',' + option2)
    option2 = ''
if option4 != '':
    with open('options3.csv', 'a') as f:
        f.write('\n' + project + ',' + option4)
    option4 = ''

# Update the issue number
if st.button("Save"):
    with open('ticket_number.txt', 'w') as f:
        f.write(str(ticket_number + 1))
    with open('data_labeling.csv', 'a') as f:
        f.write('\n' + key + ',' + option + "," + option3)
else:
    pass

st.button("Next")
