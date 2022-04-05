from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import docx2txt
# extract text
text = docx2txt.process("https://combinatronics.com/LinkHere/CEU-SOM-INVENTORY/main/Skills_Lab_Supplies_Inventory.docx")

st.text(text)

