import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from colour import sRGB_to_XYZ, XYZ_to_Lab

st.set_page_config(layout="wide")
st.title("Dải màu quang phổ (400nm - 700nm) và thông tin màu")

# Hàm chuyển bước sóng (nm) sang RGB
def wavelength_to_rgb(wavelength):
    gamma = 0.8
    if 380 <= wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif 440 < wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif 490 < wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif 510 < wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif 580 < wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif 645 < wavelength <= 700:
        attenuation = 0.3 + 0.7 * (700 - wavelength) / (700 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = G = B = 0.0

    return int(R * 255), int(G * 255), int(B * 255)

# Tạo phổ màu
wavelengths = np.arange(400, 701, 1)
colors = [wavelength_to_rgb(wl) for wl in wavelengths]

# Hiển thị dải màu
fig, ax = plt.subplots(figsize=(10, 1))
for i, color in enumerate(colors):
    ax.axvspan(i, i + 1, color=np.array(color) / 255)

ax.set_xlim(0, len(wavelengths))
ax.set_xticks(np.linspace(0, len(wavelengths), 7))
ax.set_xticklabels(np.linspace(400, 700, 7, dtype=int))
ax.set_yticks([])
ax.set_title("Phổ ánh sáng khả kiến (400 - 700nm)")
st.pyplot(fig)

# Lựa chọn bước sóng
selected_wavelength = st.slider("Chọn bước sóng (nm):", 400, 700, 550)

# Tính màu
r, g, b = wavelength_to_rgb(selected_wavelength)
rgb_norm = np.array([r, g, b]) / 255.0
xyz = sRGB_to_XYZ(rgb_norm)
lab = XYZ_to_Lab(xyz)

# Hiển thị màu và thông tin
st.markdown(f"### Thông tin tại {selected_wavelength} nm")
st.color_picker("Màu tương ứng", f'#{r:02X}{g:02X}{b:02X}', disabled=True)
st.write(f"**RGB:** R={r}, G={g}, B={b}")
st.write(f"**Lab:** L={lab[0]:.2f}, a={lab[1]:.2f}, b={lab[2]:.2f}")
