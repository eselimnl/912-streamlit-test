import streamlit as st

st.title('My ESU Streamlit app 3')

user_input = st.text_input("Enter some text")
st.write('The user entered:', user_input)

google_analytics_js = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-D39YXHSX0V"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', 'G-D39YXHSX0V');
</script>
"""

# Embed Google Analytics script within iframe HTML content
iframe_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Streamlit App</title>
  {google_analytics_js}
</head>
<body>
  <iframe src="https://912-app-test-2mzhv9bgobnsxgnuga9n7e.streamlit.app/" width="100%" height="100%" frameborder="0"></iframe>
</body>
</html>
"""

st.components.v1.iframe(iframe_content, height=1, scrolling=False)