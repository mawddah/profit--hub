import streamlit as st

# Custom CSS to inject for styling the interface
st.markdown("""
<style>
html {
    direction: rtl;
}
.main {
background-color: #020606;
}

img{
    width: 1000px;
    object-fit: fill;
    height: 150px;}
p{
    font-size:1.7rem !important;

}
.big-font {
    font-size:2.5rem !important;
    width:100%;
    font-weight: bold;
    font-family: Inter;
}
.st-bv {
    font-size: 2rem;
}
.streamlit-container {
    align-items: center;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.image("logo.png")
    st.markdown('##')
  

    # Form for user input
    with st.form(key='profile_form'):
        st.markdown('<div class="big-font">انشاء حساب</div>', unsafe_allow_html=True)
        st.markdown('##')
        username = st.text_input('اسم المستخدم')
        email = st.text_input('البريد الإلكتروني')
        password = st.text_input('كلمة المرور', type='password')
        confirm_password = st.text_input('تأكيد كلمة المرور', type='password')
        
        # Button for submission
        st.markdown('##')
        submit_button = st.form_submit_button('إنشاء حساب')
        st.markdown('##')
        st.markdown('<span> لديك حساب  <a href="pages/home.py" target="self">تسجيل الدخول</a></span>', unsafe_allow_html=True)
css="""
<style>
    [data-testid="stForm"] {
           background-color: #315D68;
           width:100%;
    align-self: center;
    }

    [data-testid="stHorizontalBlock"] {
           background-color: #b0e9e9;
            width:100%;
    align-self: center;
    }
    
     [data-testid="baseButton-secondaryFormSubmit"] {
     width:100%;
     background-color: #031014;
     text-align: center;
     align-self: center;
     
    }
    [type=button]{
        background-color: #99cbcbcf;
        color: white;
    }
</style>
"""
st.write(css, unsafe_allow_html=True)

#Handling the form submission
if submit_button:
    if password == confirm_password:
        st.success("تم انشاء حساب بنجاح!")
        st.switch_page("pages/webPage.py")
    else:
        st.error("كلمة السر غير متطابقة!")
