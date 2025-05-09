# Trang 71

import streamlit as st
import numpy as np

# Cấu hình giao diện
st.set_page_config(page_title="Đánh giá sai biệt màu", layout="centered")
st.title("So sánh sự sai biệt màu giữa 2 màu (theo không gian Lab)")

# Đánh giá Delta E
def evaluate_delta_e(de):
    if de < 1.5:
        return "Rất ít khác biệt - RẤT TỐT"
    elif de < 3.5:
        return "Rất khó phân biệt - KHÁ TỐT"
    elif de < 5:
        return "Có thể phân biệt"
    else:
        return "Rất khác biệt - KHÔNG ĐẠT"

# Giao diện nhập màu
col1, col2 = st.columns(2)

with col1:
    st.subheader("Màu 1 (Lab)")
    L1 = st.number_input("L1", 0.0, 100.0, 50.0)
    a1 = st.number_input("a1", -128.0, 127.0, 0.0)
    b1 = st.number_input("b1", -128.0, 127.0, 0.0)

with col2:
    st.subheader("Màu 2 (Lab)")
    L2 = st.number_input("L2", 0.0, 100.0, 55.0, key="L2")
    a2 = st.number_input("a2", -128.0, 127.0, 10.0, key="a2")
    b2 = st.number_input("b2", -128.0, 127.0, 5.0, key="b2")

# Tính ΔE
if st.button("So sánh"):
    deltaE = np.linalg.norm(lab1 - lab2)
    quality = evaluate_delta_e(deltaE)

    st.markdown("### Kết quả:")
    st.write(f"**Màu 1 (Lab):** L={L1:.2f}, a={a1:.2f}, b={b1:.2f}")
    st.write(f"**Màu 2 (Lab):** L={L2:.2f}, a={a2:.2f}, b={b2:.2f}")
    st.success(f"**ΔE = {deltaE:.2f} → {quality}**")
