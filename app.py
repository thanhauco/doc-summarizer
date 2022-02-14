from src.summarize import summarize
txt = st.text_area('Text')
if st.button('Summarize'):
    st.write(summarize(txt))