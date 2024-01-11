# Importing Libraries

# import Streamlit library as st
import streamlit as st
# import the pickle module, which is used for serializing and deserializing Python objects.
import pickle 


# Setting Title
# st.title("Iris Flower Prediction") 
st.title(':blue[Flower Species Classifier ML Model]')

# Loading the Classifier Model

# opens the  'classifier.pkl' in binary read mode ('rb')
pickle_in = open('classifier.pkl', 'rb') 

# load the machine learning model (classifier) using pickle.load()
classifier = pickle.load(pickle_in) 


# Defining Prediction Function

def prediction(sepal_length, sepal_width, petal_length, petal_width):   
    prediction = classifier.predict( 
        [[sepal_length, sepal_width, petal_length, petal_width]]) 
    return prediction 

# Taking User Input
   
sepal_length = st.number_input('Sepal Length')  
sepal_width = st.number_input('Sepal Width')   
petal_length = st.number_input('Petal Length')   
petal_width = st.number_input('Petal Width')   


# Making Prediction on Button Click

# empty string result is initialized
result =""

if st.button("Predict"): 
    result = prediction(sepal_length, sepal_width, petal_length, petal_width) 
    # st.success('The output is {}'.format(result)) 
    if(result == 0):
        st.success("Iris-setosa")
    elif(result == 1 ):
        st.success("Iris-versicolor")
    elif(result == 2):
        st.success("Iris-virginica")     