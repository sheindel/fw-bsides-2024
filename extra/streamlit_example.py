import os
import streamlit as st
import subprocess

def hello_world_pressed():
    st.write("You clicked the button! Nice!")

st.button("Hello World", on_click=hello_world_pressed)

ping_count = st.slider("Pick a number", 0, 100, 4)

def run():
    # run ping and capture stdout
    subprocess_result = subprocess.run(["ping", "-c", str(ping_count), "google.com"], stdout=subprocess.PIPE)
    ping_text = subprocess_result.stdout.decode("utf-8").replace("\n", "  \n")
    times = []
    for line in ping_text.split("\n"):
        print(line)
        if "time=" in line:
            times.append(line.split(" ")[7].split("=")[1])
    
    # st.write(f"Average time: {sum(times)/len(times)}")
    st.scatter_chart(times)
    

st.button("Ping Google", on_click=run)