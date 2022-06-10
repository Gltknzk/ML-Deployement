import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler, MinMaxScaler
st.title("Auto Price Prediction")
st.text('This is some text.')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header('This is a header')
st.subheader('This is a subheader')
st.success("This is a success masseage")
st.info("this is a purely info message")
#date input
import datetime
today=st.date_input("Today is")
#time input
the_time=st.time_input("The time is", datetime.time(8,45))#st.error("This is an error")
#st.help(range)
#image
#img = Image.open("images.jpeg")
#st.image(img, caption="cattie", width=300)
#my_video = open("ml.mov",'rb')
#st.video(my_video)
#st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")
#checkbox
#cbox = st.checkbox("Automatic Transmission or Manual Transmission")
#if cbox:
#    st.write("Automatic")
#else:
#    st.write("Manual")
#radio
#st.write("")
#st.write("Your favourite color is {}".format(status))
#st.write(f"Your favourite color is {status}")
#button

#st.button("Button")
#if st.button("Analyze"):
#    st.success("Analyze Results are:")
# select box

#st.write("You selected this option:", occupation)
#multi_select
#multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
#slider
#slider

#option2 = st.slider("Select a number", 0.2, 30.2, 5.2, 0.2)
#result=option1*option2
#st.write("multiplication of two options is:",result)
#text_input
#name = st.text_input("Enter your name", placeholder="Your name here")
#if st.button("Submit"):
#    st.write("Hello {}".format(name.title()))
#code
#st.code("import pandas as pd")
#st.code("import pandas as pd\nimport numpy as np")
#with st.echo():
#    import pandas as pd
 #   import numpy as np
  #  df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
   # df

#sidebar
#st.sidebar.title("Sidebar title")
#st.sidebar.header("Sidebar header")
#a=st.sidebar.slider("input",0,5,2,1)
#x=st.sidebar.slider("input2")
#st.write("# sidebar input result")
#st.success(a*x)
#dataframe
#st.write("# dataframes")
#df = pd.read_csv("Advertising.csv", nrows=(100))
#st.table(df.head())
#st.write(df.head()) #dynamic, you can sort, swiss knife
#st.dataframe(df.head())#dynamic


#st.table(df.head())
#st.write(df.describe())
#final_scaler=MinMaxScaler()
#my_dict=final_scaler.fit(my_dict)
#my_dict = final_scaler.transform(my_dict)
#
import pickle
filename = 'g11_model'
model = pickle.load(open(filename, 'rb'))
make_model = st.radio("Select a model",("Audi A3","Renault Clio","Opel Astra","Renault Duster"))
Gearing_Type=st.radio("Automatic Transmission or Manual Transmission", ["Manual", "Automatic", "Semi-Automatic"])
km = st.sidebar.number_input("Select mileage", min_value=5, max_value=400000,step=500)
hp_kW = st.sidebar.number_input("Select Horse Power", min_value=40, max_value=350,step=20)
age = st.sidebar.number_input("Select Age of the Car", min_value=0, max_value=4,step=1)
my_dict = {
    "Gearing_Type": Gearing_Type,
    "make_model": make_model,
    "km": km,
    "hp_kW":hp_kW,
    "age":age
}
df = pd.DataFrame.from_dict([my_dict])

df = pd.get_dummies(df)
columns_name=['hp_kW', 'km', 'age', 'make_model_Audi A1', 'make_model_Audi A3',
       'make_model_Opel Astra', 'make_model_Opel Corsa',
      'make_model_Opel Insignia', 'make_model_Renault Clio',
      'make_model_Renault Duster', 'make_model_Renault Espace',
     'Gearing_Type_Automatic', 'Gearing_Type_Manual',
    'Gearing_Type_Semi-automatic']
df = df.reindex(columns=columns_name, fill_value=0)

st.table(df)
if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred)