import streamlit as st
import datetime
from PIL import Image
import requests
from io import BytesIO

# Set the page configuration
st.set_page_config(page_title="Biography", page_icon="📋", layout="wide")

# Header Section
st.title("Biography 📋")
st.write("---")

# About Me Section
st.subheader("About Me")
about_me = st.text_area(
    " ",
    "I love playing computer games and exploring different genres. I find peace and inspiration watching sunsets by the ocean. I enjoy spending time outdoors, discovering new places, and taking photos of nature. I also love meeting new people and sharing stories. It's all about enjoying life's simple pleasures and embracing every moment!"
)

# Greeting Section
st.subheader(f"Hello! 👋 I'm")

# Main Section with Two Columns
left_column, right_column = st.columns([2, 1])  # Adjust width ratios: 2 parts text, 1 part image

# Left Column (Text Inputs)
with left_column:
    # Name
    name = st.text_input("Name", "Karen S. Sacote")

    # Age
    age = st.selectbox(
        "Age",
        [str(i) for i in range(18, 101)],  # Dynamic list from 18 to 100
        index=1  # Default is 19 years old (index 1)
    )

    # Birthday
    bday = st.date_input("Birthday", datetime.date(2005, 10, 9))  # Default is October 9, 2005

    # Gender
    gender_options = ["Male", "Female"]
    gender = st.radio("Gender", gender_options, index=1)  # Default is Female

    # Family Background
    st.subheader("Family Background")

    # Mother
    mother = st.text_input("Mother's Name", "Rowena S. Sacote")
    mbday = st.date_input("Mother's Birthday", datetime.date(1986, 8, 18))  # Default date

    # Father
    father = st.text_input("Father's Name", "Jerry E. Sacote")
    fbday = st.date_input("Father's Birthday", datetime.date(1980, 5, 23))  # Default date

    # Guardian
    guardian = st.text_input("Guardian", "N/A")  # Default is "N/A"

    st.write("---")

    # Educational Attainment
    st.subheader("Educational Attainment")
    hs = st.text_area("Elementary", "Mariano Espina Memorial Central Elementary School, Batch 2018")
    college = st.text_area("High School", "Surigao del Norte National High School, Batch 2024")
    st.write("---")

# Right Column (Profile Picture)
with right_column:
    # Default image URL
    default_image_url = (
        "https://scontent.fmnl9-7.fna.fbcdn.net/v/t1.15752-9/467467093_853919683605609_4072601454407834251_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeGcs1kf8CsJWxb568y1QKLwZCdPATon379kJ08BOiffvzYnTM7sir27KKDMAN43mo57PoJQfW7QNYslGXDt436m&_nc_ohc=qs1fu0IM6oYQ7kNvgFPsKL4&_nc_zt=23&_nc_ht=scontent.fmnl9-7.fna&oh=03_Q7cD1QHizxeWuiv4DCTyWzeKhA2AwNgBSKo_Je-0iiGYm4oBgA&oe=676C7D11"
    )

    # File uploader
    uploaded_image = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

    if uploaded_image:
        try:
            image = Image.open(uploaded_image)
            st.image(image, caption=f"Profile Picture: {name}", width=400)
        except Exception as e:
            st.error(f"Error displaying the uploaded image: {e}")
    else:
        try:
            # Fetch default image from URL
            response = requests.get(default_image_url)
            response.raise_for_status()  # Raise an error for invalid responses
            default_image = Image.open(BytesIO(response.content))
            st.image(default_image, caption=f"Profile Picture: {name}", width=400)
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the default image: {e}")

# Footer Section
st.subheader("Social Media Accounts")
fb = st.text_input("Facebook", "facebook.com/karen.sacote")
instagram = st.text_input("Instagram", "@karensacote_")
twitter = st.text_input("Twitter", "@KarenSacote")
youtube = st.text_input("YouTube", "Karen's Channel")
st.write("---")
