import streamlit as st
import pandas as pd
import module_ludec as ludec

st.write("# LU Decomposition")

# LU Decomposition
st.write("Input here")
pn_size, _ , _ = st.columns(3)

xsize = pn_size.number_input("Data size", value=0, min_value=0, step=1, help="Masukkan jumlah titik data")
if xsize > 0:
    data = [{f"{i}": 0.0 for i in range(int(xsize))} for _ in range(int(xsize))]
    
    df = pd.DataFrame(data)

    st.write("### Masukkan data (editable)")
    edited_df = st.data_editor(df)

    matrix = edited_df.to_numpy()
    P, L, U = ludec.lu_decomposition(matrix)

    if st.button("Calculate"):  # Tombol untuk memulai perhitungan
        print(P)
        l_df = pd.DataFrame(L, columns=(i for i in range(len(L))))
        st.write("Lower Triangle")
        st.table(l_df)
        u_df= pd.DataFrame(U, columns=(i for i in range(len(U))))
        st.write("Upper Triangle")
        st.table(u_df)
