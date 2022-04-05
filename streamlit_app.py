from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import docx2txt
Skills_Lab_Supplies_Inventory.docx
https://github.com/LinkHere/CEU-SOM-INVENTORY/blob/16f6a046ee624297e1885cc99b6639b238d1b1aa/Skills_Lab_Supplies_Inventory.docx
# extract text
text = docx2txt.process("https://github.com/LinkHere/CEU-SOM-INVENTORY/blob/main/Skills_Lab_Supplies_Inventory.docx?raw=true")

st.text(text)

