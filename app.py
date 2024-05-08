import streamlit as st

# Function to inject Google Analytics script
def inject_google_analytics():
    # Google Analytics script
    google_analytics_js = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-D39YXHSX0V"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-D39YXHSX0V');
    </script>
    """

    # Display the Google Analytics script
    st.markdown(google_analytics_js, unsafe_allow_html=True)

# Main Streamlit app
def main():
    st.title('My Streamlit App')

    # Inject Google Analytics script
    inject_google_analytics()

    # Your app content goes here
    st.write("Welcome to my Streamlit app!")

# Entry point of the app
if __name__ == "__main__":
    main()