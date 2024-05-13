import streamlit as st

st.markdown("""
<style>
html {
    direction: rtl;
}
.main > .block-container {
    background: linear-gradient(to bottom left, #81a1b1, #11353c);
    font-size:2rem;
    color:white;
    letter-spacing: 2px;
    font-family: Sans-Serif;
}

img{
    width: 1000px;
    object-fit: fill;
    height: auto;
}

h1 {
    color: white;
    text-align: center;
    font-family: Serif;
}

p {
    padding: 20px;
    font-size: 2rem !important;
    font-family: Serif;
}

hr {
    border-bottom: 2px solid rgb(244 245 249);
    margin: 5px 50px;
}

.bottom-card {
    border: 2px solid #315d68;
    border-top: 60px solid #315d68;
    border-radius: 30px;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
    margin: 20px 50px;
}

.flex-around {
    display: flex;
    justify-content: space-around;
    margin: 30px;
}
.stButton{
    display: flex  !important;
    justify-content: center  !important;
  
}

 button, button p{
    background-color:#315d68 !important;
    border-radius: 20px  !important;
    color:white !important;
}
</style>
""", unsafe_allow_html=True)

st.image("Picture33.png")
# Main container
with st.container():
    # Header section with logo and menu icon
    st.markdown("<h1>Crème</h1>", unsafe_allow_html=True)
    st.markdown("""
صناعة منزلية للمخبوزات بمختلف الأنواع مثل الكعك، الكوكيز، الكب كيك، والخبز الطازج. ويتوفر لدينا ايضا خيارات صحية مثل المخبوزات الخالية من الجلوتين او السكر.
    """)
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("""
     <div class="bottom-card">
    <div class="flex-around">
    <span> سعر الاستثمار </span>
    <span> 1000 SAR </span>
    </div>
    <div class="flex-around">
    <span> نسبة الربح</span>
    <span> 2% </span>
    </div>
    </div>
    """, unsafe_allow_html=True)

# Streamlit native button for navigation
if st.button("استثمر"):
    st.switch_page("pages/Pay.py")
# Debugging
