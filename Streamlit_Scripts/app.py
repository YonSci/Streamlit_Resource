import streamlit as st

# Display texts with Streamlit
# Markdown

st.markdown("# This is a markdown")

st.markdown("## This is a markdown")

st.markdown("### This is a markdown")

st.markdown("#### This is a markdown")

st.markdown("##### This is a markdown")

st.markdown("###### This is a markdown")

# Title, Header, Subheader, text, & write​

st.title("This is a title")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("This is a text")

st.write("This is a write")


# # Write text​
st.write("Text with write")

# # Writing python inbuilt function range()​
st.write(range(10))
st.text(range(10))


# # Success​
st.success("Success")

# # Information​
st.info("Information")

# # Warning ​
st.warning("Warning")

# # Error​
st.error("Error")

# # Exception - This has been added later​
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)



# Caption, Code, & latex​

st.caption("this is the caption")

st.code("x=2021")

st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Display an image, video or audio file with Streamlit​


# import Image from pillow to open images​
from PIL import Image

img = Image.open("streamlit.png")
# display image using streamlit​
st.image(img, width=200, caption='streamlit logo')

# Import Audio and video

# st.audio("Audio.mp3")
# st.video("video.mp4")

# Widgets ​

# title of the checkbox is 'Show/Hide'​
if st.checkbox("Show/Hide"):
     st.text("Showing the widget")
     
     
# Create a simple button that does nothing​
st.button("Click me for no reason")


# Create a button, that when clicked, shows a text​
if(st.button("About")):
    st.text("This button is clicked")

# Radio button

status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
    
status1 = st.radio("Select Gender: ", ('xxx', 'yyy', 'zzz'))
st.write("Your status is: ", status1)

    
# Selection Box & Multi-Selectbox​   

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",  ['Dancing', 'Reading', 'Sports'])

st.write("You selected", len(hobbies), 'hobbies')


# Slider & Select_Slider​

level = st.slider("Select the level", 1, 5)
# .format() is used to print value of a variable at a specific position​
st.text('Selected: {}'.format(level))

st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    
    

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
    
    
# Display progress and status with Streamlit
# st.balloons()

#st.subheader("progress bar")
#st.progress(10)

#import time
#st.subheader("with the execution")
#with st.spinner('Wait for it...'):    
#    time.sleep(10)
    
# Sidebar and container​

st.sidebar.title("This is side bar")
st.sidebar.button("Click")
st.sidebar.radio("Pick Gender", ["Male", "Feamle"] )

container = st.container()
container.write("This is written inside the container") 
st.write("This is written inside the container")

st.markdown("### Display graphs with Streamlit")

st.markdown("### Plot with pyplot")
# pyplot 
import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=5)
st.pyplot(fig)

st.markdown("### Line chart")
# Line Chart 
import pandas as pd
df= pd.DataFrame(np.random.randn(10, 2),  columns=['x', 'y'])
df
st.line_chart(df)

st.markdown("### Bar chart")
# Bar Chart
df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
df
st.bar_chart(df)

st.markdown("### Area chart")
# Area Chart 
df= pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
df
st.area_chart(df)

st.markdown("### Plot with Altair")
import altair as alt
df= pd.DataFrame(np.random.randn(500, 3),   columns=['x','y','z'])
c = alt.Chart(df).mark_circle().encode(   x='x', y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

# Display maps with Streamlit

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [9.00, 38.763],columns=['lat', 'lon'])
st.map(df)