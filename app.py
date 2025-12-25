import streamlit as st

st.sidebar.title("More")

st.header("Welcome to VNU")
st.title("Information about you")
st.subheader("Let's do a quick survey!")
st.text("It will only take a minute")
st.image("http://i.pravatar.cc?u=8","image",width=200)

fah = []



name = st.text_input("Fill in your name: ")
age = st.text_input("Fill in your age: ")
language = st.radio("Select your language", ["Janpanese","Russian","English","Vietnamese","Spanish"])
st.write("What are your hobbies?")
football = st.checkbox("Footbal")
chess = st.checkbox("Chess")
basketball = st.checkbox("Basketball")
volleyball = st.checkbox("Volleyball") 
fah.extend([football,chess,basketball,volleyball])
gender = st.selectbox("Your gender is ",["Male","Female"])
subject = st.multiselect("Select subjects that you are currently studying",["Math","Phylosophy","Physics","Chemistry","History","Economy","Psycology","PE","Literature"])
clickSubmit = st.button("Submit")
hobbyNumber = 0
if clickSubmit:
    st.markdown(f"""
             Your name is <strong>{name}</strong> and you are <strong>{age}</strong> years old, <strong>{gender}</strong> <br />
             Your language is <strong>{language}</strong> <br />
             """,True)
    for item in fah:
        if item:
            hobbyNumber +=1
    if hobbyNumber == 0:
        st.markdown(f"You have <strong>no</strong> hobby <br />",True)
    if hobbyNumber == 1:
        st.markdown(f"You have <strong>one</strong> hobby <br />",True)
    if hobbyNumber > 1:
        st.markdown(f"You have <strong>{hobbyNumber}</strong> hobbies <br />",True)
    st.markdown(f"Subjects that you are currently studying: <strong>{', '.join(subject)}</strong>",True)
    st.table(fah)