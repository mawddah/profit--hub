import streamlit as st

st.set_page_config(page_title="Profit Hub", layout="wide")

#css style
st.markdown("""
<style>
html {
    direction: rtl;
}
img{
width: 1000px;
    object-fit: fill;
    height: auto;

}
create_category_button > button{
padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)


st.image("logo.png", use_column_width=True)

st.divider()

search_query = st.text_input("", value="", max_chars=100)
search_button_clicked = st.button("🔍")

st.markdown("###")

def create_category_button(icon_path, target_url,name):
    st.image(icon_path, width=200)
    button = st.button("اختر هذه الفئه", key=target_url)
    if button:
        st.markdown(":white_check_mark:")
    return button

cols = st.columns(2)

with cols[0]:
    button1_clicked = create_category_button("icon1.png", "/handeMade", "Hande Made")
    button2_clicked = create_category_button("icon3.png", "/videoGames", "Video Games")
    button3_clicked = create_category_button("icon5.png", "/Fashion", "Fashion")

with cols[1]:
    button4_clicked = create_category_button("icon2.png", "/electricalAppliances", "Electrical Appliances")
    button5_clicked = create_category_button("icon4.png", "/foodIndustry", "Food Industry")
    button6_clicked = create_category_button("icon6.png", "/realEstate", "Real Estate")
st.markdown("###")
st.markdown("""
<style>
    .stButton > button {
        border: 2px solid skyblue;
        padding: 10px 20px;
    }
</style>
""", unsafe_allow_html=True)

if st.button("التالي ⬅️"):
    st.switch_page("pages/🏠ProfitHub.py")
