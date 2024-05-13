import streamlit as st
st.markdown("""
<style>
html {
    direction: rtl;
}
body {
    background-color: #2E8BC0;
}

img{
width: 1000px;
    object-fit: fill;
    height: auto;}
.textsf{
 font-size:30px !important;
    font-weight: bold;
    width: 50%;
    align-self: center;
    }
    .flex-around {
    display: flex;
    justify-content: space-around;
    margin: 40px;
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
.stButton > button{
background-color:#424D52;
border: 1px solid skyblue;
padding: 10px 10px;
height: 3em;
width: 8em;

}
</style>

""", unsafe_allow_html=True)
st.image("logo.PNG", use_column_width=True)
st.divider()
st.write("##")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image("raj.png")
with text_column:
    result = st.button("طلب تمويل", key="1")
    if result:
        st.switch_page("pages/Pay.py")
    st.write(
            """
تمويل يصل إلى مبلغ 20 مليون ريال.

 فترة سداد تبدأ من سنة وتصل حتى 20 سنة.
 
 هامش ربح منافس يبدأ من 6.5% ثابت سنوياً.


""",
            )
     
st.write("##")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image("tas.png")
with text_column:
    result2 = st.button("طلب تمويل", key="2")
    if result2:
         st.switch_page("pages/Pay.py")
    st.write(
            """
مبلغ التمويل من 10,000 إلى 250,000 ر.س

خيارات سداد مرنة حتى 5 سنوات

 مبلغ التمويل بحسابك البنكي خلال 48 ساعة في أيام العمل الرسمية ،
 متوافق مع الضوابط الشرعية
""")

            

st.write("##")
image_column, text_column = st.columns((1,2))
with image_column:
    st.image("bank.png")
with text_column:
    clicked = st.button("طلب تمويل")
    if clicked:
         st.switch_page("pages/Pay.py")
    st.write(
            """
اتفاقية تمويل تجمع بينك وبين بنك الرياض:

 مبلغ التمويل 100.00 ريال
 
قيمة القسط 8,500 ريال شهريا
معدل الربح السنوي 2%
""")
 

  
