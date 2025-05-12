import streamlit as st
from nutrition_model2 import estimate_nutrition, estimate_messy_dish

st.set_page_config(page_title="Indian Dish Nutrition Estimator", page_icon="🍛")
st.title("🍽️ Indian Nutrition Estimator")
st.markdown("Enter a dish name (like *aloo paratha*, *rajma chawal*, etc.)")

dish_name = st.text_input("Dish Name")

if dish_name:
    with st.spinner("Estimating nutrition..."):
        try:
            # Call the estimate_nutrition function
            result = estimate_nutrition(dish_name)
            st.success("Estimation complete!")
            # Display the result using st.write to handle non-JSON formatted strings
            st.write(result['result'])
        except Exception as e:
            st.error(f"Error: {e}")

#  Part 2: Messy Reality (Edge Case Handling)
# You will be given a test JSON with 5 dish inputs like:
# ```json
# [
# { "dish": "Jeera Aloo (mild fried)"
# ,
# "issues": ["ingredient synonym"
# ,
# "quantity missing"] },
# { "dish": "Gobhi Sabzi"
# ,
# "issues": ["ambiguous dish type"] },
# { "dish": "Chana masala"
# ,
# "issues": ["missing ingredient in nutrition DB"] },
# { "dish": "Paneer Curry with capsicum"
# ,
# "issues": ["unit in 'glass'"
# ,
# "spelling variation"] },
# { "dish": "Mixed veg"
# ,
# "issues": ["no fixed recipe"
# ,
# "ambiguous serving size"] }
# ]
# ```
# ⛏ **Your Job:**
# * Show how your code handles each (default values, logging, graceful degradation)
# * Include a **log of assumptions made per dish**


st.markdown("### Messy Dish Estimator")
input_json_dish_issues = st.text_area("Enter dish name and issues (JSON format)",
    value='''[
    { "dish": "Jeera Aloo (mild fried)", "issues": ["ingredient synonym", "quantity missing"] },
    { "dish": "Gobhi Sabzi", "issues": ["ambiguous dish type"] },
    { "dish": "Chana masala", "issues": ["missing ingredient in nutrition DB"] },
    { "dish": "Paneer Curry with capsicum", "issues": ["unit in 'glass'", "spelling variation"] },
    { "dish": "Mixed veg", "issues": ["no fixed recipe", "ambiguous serving size"] }
]''')
if input_json_dish_issues:
    try:
        # Parse the JSON input
        parsed_input = eval(input_json_dish_issues)
        if isinstance(parsed_input, list):
            for entry in parsed_input:
                dish_name_messy = entry.get("dish")
                issues = entry.get("issues", [])
                if dish_name_messy and issues:
                    with st.spinner(f"Estimating nutrition for {dish_name_messy}..."):
                        try:
                            # Call the estimate_messy_dish function
                            result = estimate_messy_dish(dish_name_messy, issues)
                            st.success(f"Estimation for {dish_name_messy} complete!")
                            # Display the result using st.write to handle non-JSON formatted strings
                            st.write(result['result'])
                        except Exception as e:
                            st.error(f"Error estimating {dish_name_messy}: {e}")
                else:
                    st.warning("Dish name or issues missing in input.")
        else:
            st.error("Input should be a list of dictionaries.")
    except Exception as e:
        st.error(f"Error parsing JSON: {e}")
