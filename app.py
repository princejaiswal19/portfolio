import streamlit as st
from base64 import b64encode

def web_portfolio():
    # Page configuration
    st.set_page_config(page_title="Prince Jaiswal's Portfolio", page_icon="🎓")

    # Custom styling
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    @keyframes fadeInZoom {
        0% {opacity: 0; transform: scale(0.9);}
        100% {opacity: 1; transform: scale(1);}
    }
    .title {
        animation: fadeInZoom 1s ease-in-out;
    }
    .box img {
        width: 300px;
        height: 200px;
        border-radius: 50%;
        animation: slowTilt 2s ease-in-out infinite;
    }
    @keyframes slowTilt {
        0%, 100% {transform: rotate(0deg);}
        50% {transform: rotate(5deg);}
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.write("""
    <div class="title" style="text-align: center;">
        <span style='font-size: 32px;'>Hello! My name is Prince Jaiswal</span> 👋
    </div>
    """, unsafe_allow_html=True)

    # Load image
    with open("IMG_20230720_192947.jpg", "rb") as img_file:
        img = "data:image/png;base64," + b64encode(img_file.read()).decode()

    # Load PDF
    with open("AHILYA TRADERS.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display image
    st.write(f"""
    <div style="display: flex; justify-content: center;">
        <div class="box">
            <img src="{img}">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write("""
    <div class="subtitle" style="text-align: center; font-size: 20px;">
        Deep Learning Enthusiast | AI/ML Developer
    </div>
    """, unsafe_allow_html=True)

    # Social media links
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/princejaiswal22", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub": ["https://github.com/princejaiswal22", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
        "Twitter": ["https://twitter.com/princejaiswal22", "https://cdn-icons-png.flaticon.com/128/733/733579.png"]
    }

    social_icons_html = [
        f"<a href='{url}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{icon}' alt='{platform}' style='width: 25px; height: 25px;'></a>"
        for platform, (url, icon) in social_icons_data.items()
    ]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>
    """, unsafe_allow_html=True)

    # About section
    st.subheader("About Me")
    st.markdown("""
    - 🧠 I am a **Computer Science student** at NIT Hamirpur passionate about AI and Deep Learning.
    - 💡 Currently working on intent classification using LSTM in Colab.
    - 💻 Skilled in Python, Streamlit, TensorFlow, Keras, and NLP.
    - 📈 Actively involved in CSEC and organizing hackathons like HACK 5.0.
    - 🛠️ I love building ML apps and deploying them using Streamlit.
    - 📫 Reach me at princejaiswal22@gmail.com
    - 🌍 Based in India.
    """)

    # Resume download button
    st.download_button(label="📄 Download My Resume", data=pdf_bytes, file_name="Prince_Jaiswal_Resume.pdf", mime="application/pdf")

    # Goodbye message
    st.write("##")
    st.write("""
    <div class="subtitle" style="text-align: center; font-size: 18px;">✨ Thanks for visiting! Have a great day! ✨</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
