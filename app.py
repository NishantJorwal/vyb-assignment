import streamlit as st
from nutrition_model2 import estimate_messy_dish

st.set_page_config(page_title="Indian Dish Nutrition Estimator", page_icon="🍛")
st.title("🍽️ Indian Nutrition Estimator")
st.markdown("Enter a dish name (like *aloo paratha*, *rajma chawal*, etc.)")

dish_name = st.text_input("Dish Name")

if dish_name:
    with st.spinner("Estimating nutrition..."):
        try:
            issues = []
            result = estimate_messy_dish(dish_name, issues)
            st.success("Estimation complete!")
            st.json(result)
        except Exception as e:
            st.error(f"Error: {e}")
