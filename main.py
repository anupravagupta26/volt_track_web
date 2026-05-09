import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
# st.set_page_config(page_title="Multi Screen App", layout="centered")

# ---------------------------
# Session State Initialization
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------
# Navigation Functions
# ---------------------------
def go_to(page_name):
    st.session_state.history.append(st.session_state.page)
    st.session_state.page = page_name




def go_back():
    if st.session_state.history:
        st.session_state.page = st.session_state.history.pop()

# ---------------------------
# Home Screen
# ---------------------------
def home_page():
    st.image("logo.png",width=320)
    st.markdown("<h1 style='text-align: center;'>Volt Track</h1>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    div.stButton > button {
        height: 5em;
        width: 32em;
        background-color: #fcb103;
        
        font-size: 10px;
        
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    if st.button("Start"):
            go_to("screen1")




# ---------------------------
# Screen 1
# ---------------------------
def screen1():
    st.markdown("<h1 style='text-align: center;'>🛵 Volt Track</h1>", unsafe_allow_html=True)
    voltage_option = st.selectbox(
        "Select Voltage Type:",
        ["48V", "60V", "72V"])
    input_voltage = st.text_input("Enter Your EV Voltage",placeholder="Enter Your EV Voltage")
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
        MAX_VOLT = 54.60
        MIN_VOLT = 42.00
        MAX_RANGE = 60.00
    
        try:
            voltage = float(input_voltage)

            if voltage < MIN_VOLT:
             percentage = 0.0
            elif voltage > MAX_VOLT:
             percentage = 100.0
            else:
                percentage = ((voltage - MIN_VOLT) / (MAX_VOLT - MIN_VOLT)) *100
                est_range = (percentage / 100) * MAX_RANGE
                used_battery = 100 - percentage
                travel_range = MAX_RANGE - est_range

            with st.container(horizontal=True):

                with st.container(border=True):
                
                    st.metric(label="Battery Percentage", value=f"{int(percentage)}%")



                with st.container(border=True):
                      st.metric(label="Estimated Range", value=f"{int(est_range)} km")
                     

        
                   
            with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{int(travel_range)} km")
            
            

    
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

            col1,col2,col3 = st.columns(3)

            with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.60V | Low: 42.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")

            with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 67.20V | Low: 52.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

            with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.00V | Low: 60.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 80-90 KM")


            

            st.markdown("<h4 style='text-align: center;'>Scan to Download the App</h4>", unsafe_allow_html=True)
            st.image("Volt Track.png",width=320)
            st.markdown("<h3 style='text-align: center;'>Volt Track</h3>", unsafe_allow_html=True)
        except:
             st.write("No Value Here")
    

    def calculate_60v(input_voltage):
        MAX_VOLT = 67.20
        MIN_VOLT = 52.00
        MAX_RANGE = 70.00
    
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
                      st.metric(label="Estimated Range", value=f"{int(est_range)} km")
                     

        
                   
            with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{int(travel_range)} km")
            
            

    
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

            col1,col2,col3  = st.columns(3)

       
            with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.60V | Low: 42.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")
            with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 67.20V | Low: 52.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

            with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.00V | Low: 60.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 80-90 KM")


       

            st.markdown("<h4 style='text-align: center;'>Scan to Download the App</h4>", unsafe_allow_html=True)
            st.image("Volt Track.png",width=320)
            st.markdown("<h3 style='text-align: center;'>Volt Track</h3>", unsafe_allow_html=True)
        

        except:
             st.write("No Value Here")
    
           

    def calculate_72v(input_voltage):
        MAX_VOLT = 84.00
        MIN_VOLT = 60.00
        MAX_RANGE = 90.00
    
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
                      st.metric(label="Estimated Range", value=f"{int(est_range)} km")
                     

        
                   
            with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{int(travel_range)} km")
            
            

    
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

            col1,col2,col3  = st.columns(3)

       
            with col1:
                st.info("**48V Variant**")
                st.write("🔋 Full: 54.60V | Low: 42.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 50-60 KM")
            with col2:
                st.success("**60V Variant**")
                st.write("🔋 Full: 67.20V | Low: 52.00V")
                st.write("⚡ Charge: 4-5 Hrs")
                st.write("🛣️ Range: 60-70 KM")

            with col3:
                st.warning("**72V Variant**")
                st.write("🔋 Full: 84.00V | Low: 60.00V")
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



# ---------------------------
# Main App Router
# ---------------------------
if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "screen1":
    screen1()

