import streamlit as st

st.set_page_config(layout="wide")

st.title("To-do App")
content = """
To-do App was a first project, which evolved over time, i tried basics of python on this project
. At first command line interface was created, then we appended desktop GUI version and lastly made web application
for this project. Under picture of desktop GUI you can find link to repository with all the files that
led to the desktop version, including command line interface version. You can also see web version, link
to its source code and link to the website.
This app is supposed to allow user to add todos and tick them as completed once done, web version however
collects all the todos into one text file which it displays, so the todo list can have more contributors.
Its not a bug though, its a feature, thats makes this web app a brand new social media.
"""
st.info(content)

col1, col2 = st.columns(2)

with col1:
    st.image("project_examples/todoappgui.png")
    st.write(f"[Source Code](https://github.com/S1fam/todo-app)")

with col2:
    st.image("project_examples/todoappweb.png")
    st.write(f"[Source Code](https://github.com/S1fam/to-do-webapp)")
    st.write(f"[Website](https://s1fam-to-do-webapp-web-g9wtl9.streamlit.app)")


st.title("Web portfolio")
content = """
Portfolio app is this project you're looking at, it is supposed to showcase my projects, allow you to contact me, 
give access to source codes of the projects and show them visually here on page project_examples. You can also
find other projects here.
"""
st.info(content)

col3, col4 = st.columns(2)

with col3:
    st.image("images/2.png")
    st.write(f"[Source Code](https://github.com/S1fam/Portfolio)")

with col4:
    st.image("project_examples/portfolio.png")
    st.write(f"[Website](https://s1fam-portfolio-home-at8i55.streamlit.app)")


st.title("PDF export")
content = """
PDF export is an app that connects pdf generation in python using fpdf module and reading files from
csv file. the csv file contains order of topics, names of topics and amount of pages each topic should get
it generated pdf file with topic as title and with amount of blank pages it gets from csv file.
bellow you can find example of csv file, and pdf output, link to a source code aswell as to whole pdf output
"""
st.info(content)

col5, col6 = st.columns(2)

with col5:
    st.image("project_examples/PDFcsv.png")
    st.write(f"[Source Code](https://github.com/S1fam/PDF-export)")

with col6:
    st.image("project_examples/PDFcsvoutput.png")
    st.write(f"[pdf output](https://github.com/S1fam/PDF-export/blob/master/output.pdf)")


st.title("Excel to PDF")
content = """
This is an app that creates PDF invoices out of Excel files.
the file is programmed for certain amount of columns (5), with exact names, if you want to use this code you might
need to edit it first or use defined number of columns and names in excel file.
you can find example of an invoice bellow aswell as example of generated pdf table for the invoice
"""
st.info(content)

col7, col8 = st.columns(2)

with col7:
    st.image("project_examples/ExcelInvoice.png")
    st.write(f"[Source Code](https://github.com/S1fam/ExcelToPDF)")

with col8:
    st.image("project_examples/PdfInvoice.png")
    st.write(f"[pdf output](https://github.com/S1fam/ExcelToPDF/blob/master/PDFs/10003-2023.1.18.pdf)")
