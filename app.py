import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Prince's Portfolio", page_icon=":rocket:", layout="wide")

# --- PROFILE SECTION ---
with st.container():
    st.title("👨‍💻 Prince Jaiswal")
    st.subheader("Computer Science Student | ML & Software Enthusiast | NIT Hamirpur")
    st.write("Aspiring Software Engineer passionate about building intelligent systems and solving real-world problems with code.")

    # Optional profile image
    # image = Image.open("assets/profile.png")
    # st.image(image, width=120)

# --- PROJECTS SECTION ---
with st.container():
    st.write("---")
    st.header("🧠 Projects")
    st.write("Some of the projects I've worked on:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔍 Intent Classifier App")
        st.write("Deep learning powered chatbot intent classifier using LSTM and Streamlit.")
        st.markdown("[View Demo](https://your-deployed-intent-app.streamlit.app)")

    with col2:
        st.subheader("🌊 Flood Prediction System")
        st.write("Flood risk analysis for Bihar using GIS and machine learning techniques.")
        st.markdown("[Read Report](https://link-to-report.com)")

# --- SKILLS SECTION ---
with st.container():
    st.write("---")
    st.header("🛠️ Skills & Tools")
    st.write("""
    - 💻 Languages: Python, C++, JavaScript
    - 🤖 ML/DL: TensorFlow, scikit-learn, Keras
    - 🛠️ Tools: Git, Streamlit, Google Colab, VS Code
    - 📊 Others: SQL, HTML/CSS, PowerPoint, Excel
    """)

# --- CONTACT SECTION ---
with st.container():
    st.write("---")
    st.header("📬 Get in Touch")
    st.write("Want to connect or collaborate? Reach out!")

    st.markdown("""
    - 📧 Email: [prince@example.com](mailto:prince@example.com)
    - 🔗 GitHub: [github.com/princekumar](https://github.com/princekumar)
    - 💼 LinkedIn: [linkedin.com/in/princekumar](https://linkedin.com/in/princekumar)
    """)
