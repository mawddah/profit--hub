from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np


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
col1, col2, col3, col4 = st.columns(4)

with col1:
    pass
with col2:
    button1 = st.button("اشترك")
if button1:
    st.switch_page("pages/sub.py")
with col3:
    button2 = st.button("طلب تمويل")
if button2:
    st.switch_page("pages/🏦طلب تمويل.py.py")
with col4:
    pass
st.divider()
    
imge1 = Image.open("Picture1.png")
imge2 = Image.open("Picture2.png")
imge3 = Image.open("Picture3.png")
imge5 = Image.open("Picture5.png")


    
with st.container():
    st.markdown('<p class="big-font">تصفح واستثمر!</p>', unsafe_allow_html=True)
    
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge1)
        
    with text_column:
        st.subheader("Simple Home")
        st.write(
            """

انطلاقاً من جدة نختص بالمشاريع السكنية والتجارية , والواجهات السياحية
""",
            )
     
        result = st.button("استثمر", key="1")
        if result:
            st.write(':confetti_ball:')
        st.markdown('<i class="bi bi-bookmark-heart"></i>', unsafe_allow_html=True)
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge2)
        with text_column:
            st.subheader("متجر روشيه")
            st.write(
            """
متجر روشيه يقدم الستر المحبوكة بسعر رمزي والتصميم بطلب العميل .
""")
            result2 = st.button("استثمر", key="2")
            if result2:
                st.write(':confetti_ball:')
            

    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imge3)
    with text_column:
        st.subheader("Crème")
        st.write(
            """

صناعه منزليه للمخبوزات بمختلف الانواع . 

""")
        clicked = st.button("استثمر")
        if clicked:
            st.switch_page("pages/تفاصيل اكثر.py")
            

 
