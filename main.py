import streamlit as st

st.markdown("<h1 style='text-align: center;'>⚡ Volt Track</h1>", unsafe_allow_html=True)
voltage_option = st.selectbox(
        "Select Voltage Type:",
        ["48V", "60V", "72V"])
input_voltage = st.text_input("Enter Your EV Voltage",placeholder="e.g. 62.02")
st.markdown("""
    <style>
    div.stButton > button {
        height: 5em;
        width: 32em;
        font-size: 10px;
        
    }
    </style>
    """, unsafe_allow_html=True)




def calculate_48v(input_voltage):
    MAX_VOLT = 54.6
    MIN_VOLT = 44.0
    MAX_RANGE = 60.0
    
    try:
        voltage = float(input_voltage)

        if voltage < MIN_VOLT:
             percentage = 0.0
        elif voltage > MAX_VOLT:
             percentage = 100.0
        else:
            percentage = ((voltage - MIN_VOLT) / (MAX_VOLT - MIN_VOLT)) * 100
            est_range = (percentage / 100) * MAX_RANGE
            used_battery = 100 - percentage
            travel_range = MAX_RANGE - est_range

        with st.container(horizontal=True):

                with st.container(border=True):
                
                    st.metric(label="Battery Percentage", value=f"{int(percentage)}%")



                with st.container(border=True):
                      st.metric(label="Estimated Range", value=f"{est_range:.1f} km")
                     

        
                   
        with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{travel_range:.1f} km")
            
            

    
        if percentage >= 90:
                st.info("Battery is Good")
        elif percentage >= 75:
                st.success("The charge is still strong")
        elif percentage >= 50:
                st.success("The power is half-depleted")
        elif percentage >= 25:
                st.success("The energy is running low")
        else:
                st.warning("Battery is critically low")
        
        
        
        st.markdown("<h2 style='text-align: center;'>🛵 EV Bike Note</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.6V | Low: 42.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")

        with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 68.7V | Low: 50.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

        with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.6V | Low: 62.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 80-90 KM")
        st.markdown("<h4 style='text-align: center;'>Scan to Download the App</h4>", unsafe_allow_html=True)
        st.image("Volt Track.png",width=320)
        st.markdown("<h3 style='text-align: center;'>Volt Track</h3>", unsafe_allow_html=True)
        

        
        

    except:
             st.write("No Value Here")
    

def calculate_60v(input_voltage):
    MAX_VOLT = 68.7
    MIN_VOLT = 50.0
    MAX_RANGE = 70.0
    
    try:
        voltage = float(input_voltage)

        if voltage < MIN_VOLT:
             percentage = 0.0
        elif voltage > MAX_VOLT:
             percentage = 100.0
        else:
            percentage = ((voltage - MIN_VOLT) / (MAX_VOLT - MIN_VOLT)) * 100
            est_range = (percentage / 100) * MAX_RANGE
            used_battery = 100 - percentage
            travel_range = MAX_RANGE - est_range

        with st.container(horizontal=True):

                with st.container(border=True):
                
                    st.metric(label="Battery Percentage", value=f"{int(percentage)}%")



                with st.container(border=True):
                      st.metric(label="Estimated Range", value=f"{est_range:.1f} km")
                     

        
                   
        with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{travel_range:.1f} km")
            
            

    
        if percentage >= 90:
                st.info("Battery is Good")
        elif percentage >= 75:
                st.success("The charge is still strong")
        elif percentage >= 50:
                st.success("The power is half-depleted")
        elif percentage >= 25:
                st.success("The energy is running low")
        else:
                st.warning("Battery is critically low")
        st.markdown("<h2 style='text-align: center;'>🛵 EV Bike Note</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.6V | Low: 42.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")

        with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 68.7V | Low: 50.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

        with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.6V | Low: 62.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 80-90 KM")

        st.markdown("<h4 style='text-align: center;'>Scan to Download the App</h4>", unsafe_allow_html=True)
        st.image("Volt Track.png",width=320)
        st.markdown("<h3 style='text-align: center;'>Volt Track</h3>", unsafe_allow_html=True)
        

    except:
             st.write("No Value Here")
    
           

def calculate_72v(input_voltage):
    MAX_VOLT = 84.6
    MIN_VOLT = 62.0
    MAX_RANGE = 90.0
    
    try:
        voltage = float(input_voltage)

        if voltage < MIN_VOLT:
             percentage = 0.0
        elif voltage > MAX_VOLT:
             percentage = 100.0
        else:
            percentage = ((voltage - MIN_VOLT) / (MAX_VOLT - MIN_VOLT)) * 100
            est_range = (percentage / 100) * MAX_RANGE
            used_battery = 100 - percentage
            travel_range = MAX_RANGE - est_range

        with st.container(horizontal=True):

                with st.container(border=True):
                
                    st.metric(label="Battery Percentage", value=f"{int(percentage)}%")



                with st.container(border=True):
                      st.metric(label="Estimated Range", value=f"{est_range:.1f} km")
                     

        
                   
        with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{travel_range:.1f} km")
            
            

    
        if percentage >= 90:
                st.info("Battery is Good")
        elif percentage >= 75:
                st.success("The charge is still strong")
        elif percentage >= 50:
                st.success("The power is half-depleted")
        elif percentage >= 25:
                st.success("The energy is running low")
        else:
                st.warning("Battery is critically low")

        st.markdown("<h2 style='text-align: center;'>🛵 EV Bike Note</h2>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.6V | Low: 42.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")

        with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 68.7V | Low: 50.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

        with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.6V | Low: 62.0V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 80-90 KM")

        st.markdown("<h4 style='text-align: center;'>Scan to Download the App</h4>", unsafe_allow_html=True)
        st.image("Volt Track.png",width=320)
        st.markdown("<h3 style='text-align: center;'>Volt Track</h3>", unsafe_allow_html=True)
        
        
        

    except:
             st.write("No Value Here")




def perform_calculation(selected_voltage, input_voltage):
    if selected_voltage == "48V":
        return calculate_48v(input_voltage)
    elif selected_voltage == "60V":
        return calculate_60v(input_voltage)
    elif selected_voltage == "72V":
        return calculate_72v(input_voltage)
    else:
        return None
if st.button("Calculate",type="primary"):
        result = perform_calculation(voltage_option, input_voltage)
