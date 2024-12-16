import streamlit as st
import numpy as np
import pandas as pd
import module_interpolation as inter

def calculate_li(x0, y0, x1, y1, x):
    st.write(f"{inter.linear_interpolation(x0, y0, x1, y1, x)}")
    # return str(y0 + (y1 - y0) * (x - x0) / (x1 - x0))

def calculate_qi(x0, y0, x1, y1, x2, y2, x):
    st.write(f"{inter.quadratic_interpolation(x0, y0, x1, y1, x2, y2, x)}")

st.write("# Interpolation Calculator")

# Linier Interpolation
st.write("## Linier Interpolation")
st.write("Input here")

li_inputx0, li_inputy0, li_inputx = st.columns(3)
li_inputx1, li_inputy1, _ = st.columns(3)

x0 = li_inputx0.number_input("x0", value=None, format="%0.5f",placeholder="type a number")
y0 = li_inputy0.number_input("y0", value=None, format="%0.5f",placeholder="type a number")
x1 = li_inputx1.number_input("x1", value=None, format="%0.5f",placeholder="type a number")
y1 = li_inputy1.number_input("y1", value=None, format="%0.5f",placeholder="type a number")
x = li_inputx.number_input("x", value=None, format="%0.5f",placeholder="type a number")

if not x0 or not y0 or not x1 or not y1 or not x:
    st.write("please fill all the input")
else:
    calculate_li(x0, y0, x1, y1, x)

# Quadratic Interpolation
st.write("## Quadratic Interpolation")
st.write("Input here")

qi_inputx0, qi_inputy0, _ = st.columns(3)
qi_inputx1, qi_inputy1, qi_inputx  = st.columns(3)
qi_inputx2, qi_inputy2, _  = st.columns(3)

x0 = qi_inputx0.number_input("x0", value=None, format="%0.5f", placeholder="type a number", key=1)
y0 = qi_inputy0.number_input("y0", value=None, format="%0.5f",placeholder="type a number", key=2)
x1 = qi_inputx1.number_input("x1", value=None, format="%0.5f",placeholder="type a number", key=3)
y1 = qi_inputy1.number_input("y1", value=None, format="%0.5f",placeholder="type a number", key=4)
x2 = qi_inputx2.number_input("x2", value=None, format="%0.5f",placeholder="type a number", key=5)
y2 = qi_inputy2.number_input("y2", value=None, format="%0.5f",placeholder="type a number", key=6)
x = qi_inputx.number_input("x", value=None, format="%0.5f",placeholder="type a number", key=7)

if not x0 or not y0 or not x1 or not y1 or not x2 or not y2 or not x:
    st.write("please fill all the input")
else:
    calculate_qi(x0, y0, x1, y1, x2, y2, x)

# Polinomial Newton
st.write("## Polinomial Newton")
st.write("Input here")

pn_size, _ , _ = st.columns(3)

xsize = pn_size.number_input("Data size", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
if xsize > 0:
    data = [{"x": 0.0, "y": 0.0} for _ in range(int(xsize))]
    
    df = pd.DataFrame(data)

    st.write("### Masukkan data (editable)")
    edited_df = st.data_editor(df)

    # if st.button("Calculate"):  # Tombol untuk memulai perhitungan
    
    # Ambil nilai x dan y dari dataframe
    x_points = edited_df['x'].to_numpy()
    y_points = edited_df['y'].to_numpy()

    # Nilai x yang ingin diestimasi
    x_interpolate = st.number_input("Masukkan nilai x untuk interpolasi", value=0.0, help="Masukkan nilai x")

    # Hitung interpolasi
    result = inter.newton_polynomial(x_points, y_points, x_interpolate)

    st.write(f"### Hasil interpolasi pada x = {x_interpolate}: {result}")