import streamlit as st
from streamlit.components.v1 import html
#this code below is the statcounter tracking code

def statcounter():

    statcounter_script= """
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
#components.html(statcounter,width=200, height=200)  

cookie_banner = """
<div id="cookie-banner" style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f1f1f1; padding: 10px; text-align: center;">
    This website uses cookies to ensure you get the best experience on our website.
    <button onclick="acceptCookies()" style="margin-left: 10px;">Accept</button>
    <button onclick="rejectCookies()" style="margin-left: 10px;">Decline</button>
</div>

<script>
function acceptCookies() {
    var gaScript = document.createElement('script');
    gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-8H46WZXW14';
    gaScript.onload = function() {
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-8H46WZXW14');
    };
    gaScript.onerror = function() {
        console.error('Failed to load Google Analytics script');
    };
    document.head.appendChild(gaScript);

    document.getElementById('cookie-banner').style.display = 'none';
}

function rejectCookies() {
    document.getElementById('cookie-banner').style.display = 'none';
}
</script>
"""


# Main Streamlit app
def main():
    st.title('My Streamlit App for myselfESU')

    # Inject Google Analytics script
    # Your app content goes here
    st.write("Welcome to my Streamlit app test version!")
    #statcounter()
    st.session_state['track_statcounter'] = 'yes'
    html(cookie_banner)
    if st.session_state.track_statcounter:
        statcounter()
# Entry point of the app
if __name__ == "__main__":
    main()


 