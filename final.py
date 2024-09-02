import pickle
import streamlit as st
model1 = pickle.load(open("area.pkl", "rb"))
def myf1():
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>Area Price Prediction</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #6c757d;'>Predict the price based on the area input.</p>",
        unsafe_allow_html=True,
    )
    area = st.number_input(
        "Enter the area value...",
        min_value=0,
        format="%d",
        help="Input the area in square feet",
    )
    pred = st.button(
        "Predict",
        help="Click to predict the price",
        key="predict_button",
        use_container_width=True,
        type="primary",
    )
    if pred:
        op = model1.predict([[area]])
        st.markdown(
           f"<h3 style='text-align: center; color: #FF5733;'>The estimated price for the area is: ₹{op[0]:,.2f}</h3>",
            unsafe_allow_html=True,
        )

myf1()
