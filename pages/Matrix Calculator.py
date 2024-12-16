import streamlit as st
import numpy as np
import pandas as pd
import module_matriks as matrix

# Pages
def add():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")
    col2.write("### Masukkan data matrix B")

    r1_size, c1_size = col1.columns(2)
    r2_size, c2_size = col2.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    x2size = r2_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=1)
    y2size = c2_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=2)

    if (x1size and y1size) or (x2size and y2size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        data2 = [{f"{i}": 0.0 for i in range(int(y2size))} for _ in range(int(x2size))]
        
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        edited_df1 = col1.data_editor(df1, key=3)
        edited_df2 = col2.data_editor(df2, key=4)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.add_matrices(edited_df1.to_numpy(), edited_df2.to_numpy())
            print(result)

            result_df = pd.DataFrame(result)
            st.write("Result")
            st.table(result_df)
def substract():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")
    col2.write("### Masukkan data matrix B")

    r1_size, c1_size = col1.columns(2)
    r2_size, c2_size = col2.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    x2size = r2_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=1)
    y2size = c2_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=2)

    if (x1size and y1size) or (x2size and y2size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        data2 = [{f"{i}": 0.0 for i in range(int(y2size))} for _ in range(int(x2size))]
        
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        edited_df1 = col1.data_editor(df1, key=3)
        edited_df2 = col2.data_editor(df2, key=4)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.subtract_matrices(edited_df1.to_numpy(), edited_df2.to_numpy())
            print(result)

            result_df = pd.DataFrame(result, columns=(i for i in range(len(result))))
            st.write("Result")
            st.table(result_df)
def multiply():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")
    col2.write("### Masukkan data matrix B")

    r1_size, c1_size = col1.columns(2)
    r2_size, c2_size = col2.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    x2size = r2_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=1)
    y2size = c2_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data", key=2)

    if (x1size and y1size) or (x2size and y2size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        data2 = [{f"{i}": 0.0 for i in range(int(y2size))} for _ in range(int(x2size))]
        
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        edited_df1 = col1.data_editor(df1, key=3)
        edited_df2 = col2.data_editor(df2, key=4)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.multiply_matrices(edited_df1.to_numpy(), edited_df2.to_numpy())
            print(result)

            result_df = pd.DataFrame(result)
            st.write("Result")
            st.table(result_df)
def determinant():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")

    r1_size, c1_size = col1.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    if (x1size and y1size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        
        df1 = pd.DataFrame(data1)

        edited_df1 = col1.data_editor(df1, key=3)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.determinant(edited_df1.to_numpy())
            
            st.write(f"Result : {result}")
def inverse():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")

    r1_size, c1_size = col1.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    if (x1size and y1size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        
        df1 = pd.DataFrame(data1)

        edited_df1 = col1.data_editor(df1, key=3)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.inverse_matrix(edited_df1.to_numpy())
            print(result)

            result_df = pd.DataFrame(result)
            st.write("Result")
            st.table(result_df)
def transpose():
    col1, col2 = st.columns(2)

    col1.write("### Masukkan data matrix A")

    r1_size, c1_size = col1.columns(2)

    x1size = r1_size.number_input("row", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
    y1size = c1_size.number_input("column", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")

    if (x1size and y1size):
        data1 = [{f"{i}": 0.0 for i in range(int(y1size))} for _ in range(int(x1size))]
        
        df1 = pd.DataFrame(data1)

        edited_df1 = col1.data_editor(df1, key=3)

        if st.button("Calculate"):  # Tombol untuk memulai perhitungan
            
            result = matrix.transpose_matrix(edited_df1.to_numpy())
            print(result)

            result_df = pd.DataFrame(result)
            st.write("Result")
            st.table(result_df)

st.set_page_config(
    page_title="Matrix Calculator",
    page_icon=":wave:"
)

st.markdown("# Calculate matrix")

options = ["Add", "Substract", "Multiply", "Determinant", "Inverse", "Transpose"]
selection = st.pills("Operations", options, selection_mode="single")

if selection == "Add":
    add()
elif selection == "Substract":
    substract()
elif selection == "Multiply":
    multiply()
elif selection == "Determinant":
    determinant()
elif selection == "Inverse":
    inverse()
elif selection == "Transpose":
    transpose()