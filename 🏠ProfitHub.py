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
    font-size:1.6rem !important;

}
.big-font {
    font-size:2.5rem !important;
    width:100%;
    font-weight: bold;
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


show_pages(
    [
        Page("ProfitHub.py", "تسجيل الدخول", ":bust_in_silhouette:"),
        Page("pages/signup.py", "انشاء حساب", ":pencil:"),
        Page("pages/home.py", "الرئيسية", ":house:"),
        Page("pages/webPage.py", "التفضيلات", ":star:"),
        Page("pages/sub.py", "اشترك", ":tada:"),
        Page("pages/fund.py", "تمويل", ":bank:"),
        Page("pages/info.py", "."),
        Page("pages/Pay.py", "."),

     ]
    )

# Main container
with st.container():
    st.image("logo.png")
    st.markdown('##')
  

    # Form for user input
    with st.form(key='profile_form'):
        st.markdown('####')
        st.markdown('<div class="big-font">تسجيل الدخول</div>', unsafe_allow_html=True)
        st.markdown('##')
        username = st.text_input('اسم المستخدم')
        password = st.text_input('كلمة المرور', type='password')
        
        
        # Button for submission
        st.markdown('##')
        submit_button = st.form_submit_button(label="تسجيل الدخول")
        st.markdown('##')
        st.markdown('ليس لديك حساب <a href="pages/signup.py" target="_self">انشاء حساب</a>', unsafe_allow_html=True)
css="""
<style>
    [data-testid="stForm"] {
           background-color: #315D68;
           width:100%;
    align-self: center;
    }

    [data-testid="stHorizontalBlock"] {
           background-color: #b0e9e9;
            width:150%;
    align-self: center;
    }
    
     [data-testid="baseButton-secondaryFormSubmit"] {
     width:100%;
    text-align: center;
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
     st.success("تم انشاء حساب بنجاح!")
     st.switch_page("pages/webPage.py")
