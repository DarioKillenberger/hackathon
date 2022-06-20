import streamlit as st
st.title('Careers Paths Story Game')
st.write("""You watch your team through the cameras. Where do you tell them to enter the museum""")

st.button("Through the roof", key=None, help=None, on_click=st.write("""test""")
)
st.radio("Choose one", ["Through the roof", "Through the main door", "Through the staff door"])


