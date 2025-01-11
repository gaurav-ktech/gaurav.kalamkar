import streamlit as st

# Set the page title
st.set_page_config(page_title="Professional Scroll Lock Title")

# HTML and CSS for the animated title with BlackChancery font and scroll lock
st.markdown("""
    <style>
        /* Load BlackChancery font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Black+Chancery&display=swap');

        /* Keyframe animation for fade-in and slide-up */
        @keyframes fadeInSlideUp {
            0% {
                opacity: 50;
                transform: translateY(30px);
            }
            100% {
                opacity: 1;
                transform: translateY(5);
            }
        }

        /* Style for the fixed and animated title */
        .animated-title {
            font-family: 'Black Chancery', cursive; /* Applying the custom font */
            font-size: 2.5em;
            font-weight: 300;
            color: 	#87CEEB	; /* Elegant color */
            text-align: center;
            position: center;
            top: 50px;  /* Positioning title a bit below the top */
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;  /* Make sure it's above other elements */
            animation: fadeInSlideUp 2s ease-out;
            width: 0%;
            padding: 10px 0;
            background: rgba(255, 255, 255, 0.9); /* light background for contrast */

        }

        /* Body content styling to simulate scrolling */
        .content {
            margin-top: 120px;  /* Add margin to avoid overlap with the fixed title */
            padding: 20px;
        }
    </style>

    <div class="animated-title">
       WELCOME TO GAURAV KALAMKAR COMPUTER HARDWARE WORKS
    </div>

    <div class="content">
        <!-- Simulate some content on the page -->
        <h2>Scroll Down</h2>
  
    </div>
""", unsafe_allow_html=True)
# Create a button and handle the action when it is clicked
if st.button("CLICK ME "):
    st.write("HEY user you are on my website!")
st.write("High & low budget pc build")

# Display an image
st.image("E:\pythonProject\gaurav1.jpg")

import streamlit as st

# Title of the app
st.title("")

# Ask a question
st.write("HEY user Do you like COMPUTER?")

# Create Yes and No buttons
if st.button("Yes"):
    st.write("Thanks for answer!")
elif st.button("No"):
    st.write("error!")


# Contact Information
st.markdown("### Contact Information")
st.write("""
- **Email**:  kalamkargaurav6666@gmail.com  # Email for hardware releted WORKS
- **Phone**:7028220581 # CONTACT For hardware WORKS
- **instagram**: [https://www.instagram.com/___gaurav___0112/)  
- **whatsapp**: 7028220581 # whats your problame click your problame image and send mi
""")

# Summary Section
st.markdown("### Summary")
st.write("""
An enthusiastic and skilled [COMPUTER HARDWARE] with experience in [ V]. Passionate about building solutions that are scalable and efficient.
Highly motivated, results-oriented, and eager to contribute to a growing team.ll
""")

# Skills Section
st.markdown("### Skills")
st.write("""
- **COMPUTER Repairing 
- **LAPTOP Repairing
- **language**: python & java
""")

# Education Section
st.markdown("### Education")
st.write("""
**Diploma in hardware & Networking**  
& python and html
""")

st.title("PROFESSIONAL CPU/COMPUTER BUILD")
st.image("build.jpg")

st.title("PROFESSIONAL REPAIRING  COMPUTER/LAPTOP & HARDWARE")
st.image("repair.jpg")