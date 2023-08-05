import numpy as np
import cloudpickle as cp
from urllib.request import urlopen
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

# pickle_in = cp.load(urlopen("https://drive.google.com/uc?export=download&id=1c2Uwixm-3epbMjPScMWj91iSMVMaTsV9")) 
# classifier=pickle.load(pickle_in)
classifier = cp.load(urlopen("https://drive.google.com/uc?export=download&id=1c2Uwixm-3epbMjPScMWj91iSMVMaTsV9"))
def welcome():
    return "Welcome All"

def prediction_tiatnic(Pclass,Sex,SibSp,Parch,Embarked,Fare_category,Age_Category):
    prediction=classifier.predict([[Pclass,Sex,SibSp,Parch,Embarked,Fare_category,Age_Category]])
    print(prediction)
    return prediction



def main():
    st.title("Titanic Survival Prediction")
    html_temp = """
    <div style="background-color:black;padding:10px;color: white">
    <h2 style="color:white;text-align:center;">Titanic Survival App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pclass = st.text_input("Pclass","Type Here")
    Sex = st.text_input("Sex","Type Here")
    SibSp = st.text_input("SibSp","Type Here")
    Parch = st.text_input("Parch","Type Here")
    Embarked = st.text_input("Embarked","Type Here")
    Fare_category = st.text_input("Fare_category","Type Here")
    Age_Category = st.text_input("Age_Category","Type Here")
    result=""
    if st.button("Predict"):
        result=prediction_tiatnic(Pclass,Sex,SibSp,Parch,Embarked,Fare_category,Age_Category)
    if(result == 0):
      result = 'Not Survived'
    if(result == 1):
      result = 'Survived'  
    st.success(f'The Person {result}')
    if st.button("Information of Elements"):
        st.text("Lets Understand How it Works")
        st.text("Built with Streamlit by Pranshu Soni")
        st.text("Embarked = C: 1, S: 2, Q: 3")
        st.text("Fare_category = Low: 0, Middle: 1, Upper_middle: 2, high: 3")
        st.text("Age_Category = young: 0, teenage :1, adults: 2, senior:3")
        st.text("Pclass = 1,2,3")
        st.text("Parch = 0,1,2,5,3,4,6")
        st.text("SibSp = 1, 0, 3, 4, 2, 5, 8")
        st.text("Sex = female: 1, male: 2")
        html1 = ''' <div>
        <h2 style="color:white;text-align:center;">Variable info</h2>
        Variable	Definition	Key
        survival	Survival	0 = No, 1 = Yes
        pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
        sex:	Male,Female	
        Age_category: 	Age category young teenage adult senior	
        sibsp	# of siblings / spouses aboard the Titanic	
        parch	# of parents / children aboard the Titanic	
        fare cagegory	: Passenger fare clas	
        embarked:	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton
        </div>'''
        st.markdown(html1, unsafe_allow_html = True)
if __name__=='__main__':
    main()