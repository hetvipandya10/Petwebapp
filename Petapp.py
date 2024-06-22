import streamlit as st

st.title("Welcome to Pet App")
from PIL import Image
img = Image.open("C:/Users/hetvi/OneDrive/Desktop/python code/JZqiYGvm_400x400.jpeg")

PetType=st.slider("Select PetType=",0,3)
Breed=st.slider("Select Breed=",0,5)
AgeMonths=st.slider("Select AgeMonths=",1,179)
Color=st.slider("Select Color=",0,4)
WeightKg=st.slider("Select WeightKg=",1.0,29.9)
Vaccinated=st.slider("Select Vaccinated=",0,1)
HealthCondition=st.slider("SelectHealthCondition=",0,1)
TimeInShelterDays=st.slider("Select TimeInShelterDays=",1,89)
Adoptionfee=st.slider("Select Adoptionfee=",0,499)
PreviousOwner=st.slider("Select PreviousOwner=",0,1)
AdoptionLikelihood=st.slider("Select AdoptionLikelihood=",0,1)

import pickle
model=pickle.load(open("Pet.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[PetType,Breed,AgeMonths,Color,WeightKg,Vaccinated,HealthCondition,TimeInShelterDays,Adoptionfee,PreviousOwner,AdoptionLikelihood]])
    st.success("The Type is "+ prd[0])