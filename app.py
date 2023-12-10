import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "United States": {
        "Transportation": 0.4,  # kgCO2/mile
        "Electricity": 0.4,  # kgCO2/kWh
        "Diet": 2.5,  # kgCO2/meal, 2.5kgCO2/kg
        "Waste": 0.6  # kgCO2/kg
    },
    "China": {
        "Transportation": 0.2,  # kgCO2/km
        "Electricity": 0.7,  # kgCO2/kWh
        "Diet": 1.5,  # kgCO2/meal, 2.5kgCO2/kg
        "Waste": 0.8  # kgCO2/kg
    },
    "India": {
        "Transportation": 0.1,  # kgCO2/km
        "Electricity": 0.6,  # kgCO2/kWh
        "Diet": 1.0,  # kgCO2/meal, 2.5kgCO2/kg
        "Waste": 0.4  # kgCO2/kg
    },
    "Germany": {
        "Transportation": 0.15,  # kgCO2/km
        "Electricity": 0.3,  # kgCO2/kWh
        "Diet": 2.0,  # kgCO2/meal, 2.5kgCO2/kg
        "Waste": 0.5  # kgCO2/kg
    },
    "Brazil": {
        "Transportation": 0.3,  # kgCO2/km
        "Electricity": 0.2,  # kgCO2/kWh
        "Diet": 1.8,  # kgCO2/meal, 2.5kgCO2/kg
        "Waste": 0.7  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("Personal Carbon Calculator App ⚠️")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India","Brazil","Germany","China","United States"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🍽️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("What is CO2 emissions per capita?")
        st.warning("Carbon dioxide emissions are those stemming from the burning of fossil fuels and the manufacture of cement. They include carbon dioxide produced during consumption of solid, liquid, and gas fuels and gas")
        st.warning("In 2021, CO2 emissions per capita for India was 1.9 tons, for germany 9.42 tons, for USA 15.32 tons, for brazil 2.24 tons, china 7.42 tons.")
