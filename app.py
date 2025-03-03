import streamlit as st

# App Title
st.title("🎯 Unit Converter")

# Conversion Types
conversion_types = ["Length", "Weight", "Temperature"]

# Give conversion options to user
conversion_choice = st.selectbox("💠Select Conversion Type:", conversion_types)

# Length Conversion
if conversion_choice == "Length":
    length_units = ["Meters", "Centimeters", "Kilometers", "Feet", "Inches"]
    input_value = st.number_input("💠Enter Length Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("💠From Unit:", length_units)
    to_unit = st.selectbox("💠To Unit:", length_units)


    # Define Conversion Dictionaries
    length_conversion = {
        "Meters":1,
        "Centimeters":0.01,
        "Kilometers":1000,
        "Feet":0.555,
        "Inches":0.0254
    }

    # Conversion Logic
    if st.button("⏱Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"{input_value},{from_unit} is equal to {result:.2f},{to_unit}")

# Weight Conversion
elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("💠Enter Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("💠From Unit:", weight_units)
    to_unit = st.selectbox("💠To Unit:", weight_units)


    # Weight Conversion Dictionaries
    weight_conversion = {
        "Kilograms":1,
        "Grams":0.001,
        "Pounds":0.453592,
        "Ounces":0.0283495
    }

    # Weight Conversion Logic
    if st.button("⏱Convert"):
        result = input_value * weight_conversion[from_unit] / weight_conversion[to_unit]
        st.success(f"{input_value},{from_unit} == {result:.2f},{to_unit}")

# Temperature Conversion
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("💠Enter Temperature Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("💠From Unit:", temperature_units)
    to_unit = st.selectbox("💠To Unit:", temperature_units)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value-32)* 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return (value - 273.15)
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    if st.button("⏱Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value:.2f} {from_unit} == {result:.2f} {to_unit}")                