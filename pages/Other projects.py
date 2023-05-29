import streamlit as st

st.set_page_config(layout="wide")

st.title("Company Website")
content = """
this app is supposed to be demontration website for fictional company, to run this app on web you have to clone
the repository and have python on your computer. 
then to run it go to terminal and enter command: streamlit run Home.py 
(make sure you see (venv) in your terminal and correct path to Home.py file)
you can see the looks bellow, as well as link to source code
"""
st.info(content)

col1, col2 = st.columns(2)

with col1:
    st.image("other_projects/Company_web.png")
    st.write(f"[Source Code](https://github.com/S1fam/CompanyWebsite)")

with col2:
    st.image("other_projects/Company_contact.png")


st.title("PDF export lined")
content = """
PDF export is an app that connects pdf generation in python using fpdf module and reading files from
csv file. the csv file contains order of topics, names of topics and amount of pages each topic should get
it generated pdf file with topic as title and with amount of blank pages it gets from csv file.
bellow you can find example of csv file, and pdf output, link to a source code aswell as to whole pdf output.
I have this project on project_examples aswell, this version only generates the pdf documents with lines
to say, write on.
"""
st.info(content)

col3, col4 = st.columns(2)

with col3:
    st.image("other_projects/PDFcsv.png")
    st.write(f"[Source Code](https://github.com/S1fam/PDF-export-lined)")

with col4:
    st.image("other_projects/PDFcsvoutput.png")
    st.write(f"[pdf output](https://github.com/S1fam/PDF-export-lined/blob/master/output.pdf)")


st.title("Text to PDF")
content = """
this code takes text files in folder "files", uses their name as a header and puts their content into pdf file. 
It takes multiple text files and puts them into one PDF document. you can see the files bellow, aswell as
content of two of them and the final pdf output. there is link to the whole pdf aswell as to source code on GitHub
"""
st.info(content)

col5, col6 = st.columns(2)

with col5:
    st.image("other_projects/TextFilenames.png")
    st.image("other_projects/TextContents1.png")
    st.image("other_projects/TextContents2.png")
    st.write(f"[Source Code](https://github.com/S1fam/TextToPDF)")

with col6:
    st.image("other_projects/TextToPDF1.png")
    st.image("other_projects/TextToPDF2.png")
    st.write(f"[pdf output](https://github.com/S1fam/TextToPDF/blob/master/output.pdf)")


st.title("NASA API - Image of the day")
content = """
This app creates a simple webpage using streamlit. website displays content using NASA API. 
it requests astronomic picture of the day to get the image of the day, its title and description. 
it saves the image using its url and displays it on webpage. 
To use this app all you have to do is create your API key on NASA webpage for free. 
To run this app import you API key to code in line 5 and in terminal run: streamlit run Home.py
Bellow you can find image of two versions of web GUI, first with only one column and second with two columns.
You can also find link to source code here
"""
st.info(content)

col7, col8 = st.columns(2)

with col7:
    st.image("other_projects/NasaAPIWeb.png")
    st.write(f"[Source Code](https://github.com/S1fam/NasaAPI-image-of-day)")

with col8:
    st.image("other_projects/NasaAPIWebWide.png")
