from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import docx2txt
# extract text
text = docx2txt.process("https://github.com/LinkHere/CEU-SOM-INVENTORY/blob/main/Skills_Lab_Supplies_Inventory.docx?raw=true")

st.text(text)

