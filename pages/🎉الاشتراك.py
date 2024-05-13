import streamlit as st

# Set page configuration
st.markdown("""
<style>
html {
    direction: rtl;
}
body {
    background-color: #2E8BC0;
}

img{
width:250px;
}
.textsf{
 font-size:30px !important;
    font-weight: bold;
    width: 50%;
    align-self: center;
    }
button {
padding-top: 10px !important;
padding-bottom: 10px !important;
}
.big-font {
    font-size:30px !important;
    font-weight: bold;
    width: 50%;
    align-self: center;
}
.streamlit-container {
    align-items: center;
    justify-content: center;
}
</style>

""", unsafe_allow_html=True)
# Header Section
st.image("logo.png", use_column_width=True)
st.divider()

# Content Section
st.header("اختر خطتك")
st.write("فترة تجربة مجانية لمدة شهر!")

col1, col2 = st.columns(2)
with col1:
    st.info("الاشتراك السنوي\n" "12شهر 250 SAR")
    st.metric("SAR", "20.83 شهريًا", help="شهريًا")
    clicked = st.button("ادفع ←")
if clicked:
    st.switch_page("pages/💲الدفع.py")

with col2:
    st.info("الاشتراك الشهري")
    st.metric("SAR", "40")
    clickedd = st.button(":arrow_right: للخلف")
if clickedd:
    st.switch_page("pages/🏠الرئيسية.py")

