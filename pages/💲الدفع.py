import streamlit as st
st.set_page_config(page_title="Profit Hub", layout="wide")
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
    height: auto;

    }
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


with st.form(key='profile_form'):
        st.markdown('<div class="big-font">اضف بطاقتك</div>', unsafe_allow_html=True)
        st.image("card.png", width=260, use_column_width=True)
        st.markdown('##')
        submit_button = st.form_submit_button('ادفع')
        st.markdown("###")
css="""
<style>
    [data-testid="stForm"] {
           background-color: #315D68;
           width:100%;
    align-self: center;
    }

    [data-testid="stHorizontalBlock"] {
           background-color: #b0e9e9;
            width:200%;
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
clickedd = st.button(":arrow_right: للخلف")
if clickedd:
    st.switch_page("pages/home.py")

