import streamlit as st

st.markdown("<h1 style='text-align: center;'>⚡ Volt Track</h1>", unsafe_allow_html=True)
volt = st.text_input("Enter Your EV Voltage",placeholder="e.g. 62.02")
st.markdown("""
    <style>
    div.stButton > button {
        height: 3em;
        width: 8em;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

with st.container(horizontal=True):
   st.button("Reset",type="primary")
     
   if st.button("Calculate",type="secondary"):
      MAX_VOLT = 68.7
      MIN_VOLT = 50.0
      MAX_RANGE = 70.0
    
      try:
        voltage = float(volt)

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
                     st.metric(label="Used Battery", value=f"{int(used_battery)}%")

        
                   
            with st.container(horizontal=True):
  

                with st.container(border=True):
              
                     st.metric(label="Estimated Range", value=f"{est_range:.1f} km")



 

                with st.container(border=True):
              
                    st.metric(label="Travel Range", value=f"{travel_range:.1f} km")

    
            if percentage >= 90:
                st.success("Battery is Good")
            elif percentage >= 75:
                st.success("The charge is still strong")
            elif percentage >= 50:
                st.success("The power is half-depleted")
            elif percentage >= 25:
                st.success("The energy is running low")
            else:
                st.warning("Battery is critically low")


        
        

      except ValueError:
             battery_percentage = 0 
             estimated_range = 0
             used_battery = 0
             travel_range = 0
    


