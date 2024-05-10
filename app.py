import streamlit as st
import streamlit.components.v1 as components

#this code below is the statcounter tracking code
statcounter= """

    <!-- Default Statcounter code for testto
https://912-app-test-2mzhv9bgobnsxgnuga9n7e.streamlit.app/ -->
<script type="text/javascript">
var sc_project=12997381; 
var sc_invisible=1; 
var sc_security="8ce07403"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js" async></script>
<noscript><div class="statcounter"><a title="Web Analytics"
href="https://statcounter.com/" target="_blank"><img class="statcounter"
src="https://c.statcounter.com/12997381/0/8ce07403/1/" alt="Web Analytics"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code --
"""
# Main Streamlit app
def main():
    st.title('My Streamlit App for myselfESU')

    # Inject Google Analytics script
    # Your app content goes here
    st.write("Welcome to my Streamlit app!")
    components.html(statcounter,width=200, height=200)  
# Entry point of the app
if __name__ == "__main__":
    main()


 