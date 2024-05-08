import streamlit as st

st.title('My ESU Streamlit app 3')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

import streamlit.components.v1 as components

google_analytics_js = """
<!-- Global site tag (gtag.js) - Google Analytics -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-D39YXHSX0V"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "G-D39YXHSX0V");
    </script>
    """
#st.components.v1.html(google_analytics_js)
fb_comments = """
        <div class="fb-comments" data-href="https://covid19.aipert.org" data-numposts="5" data-width=""></div>
        """
#st.components.v1.html(fb_comments)
st.components.v1.iframe('https://912-app-test-2mzhv9bgobnsxgnuga9n7e.streamlit.app/', height=1, scrolling=False)