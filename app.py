from openai import OpenAI
import streamlit as st


f=open("keys/.openai_key.txt")
key=f.read()
client = OpenAI(api_key=key)

st.balloons()
st.title("🖥 AI CODE REVIEWER")

prompt = st.text_area("Enter a your code here:",height=200)

if st.button("Generate")== True:
    st.snow()
    st.title("CODE REVIEWER")
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "given the code generate a report of BUGS and REVIEWED CODE"},
        {"role": "user", "content": prompt}
      ]
)

    st.write(response.choices[0].message.content)
