import streamlit as st
import cv2
from PIL import Image
import funcoes as f
import numpy as np


class ImageSettings:
    def __init__(self):
        self.rotation = 0
        self.scale = 1.0
        self.shear_v = 0.0
        self.shear_h = 0.0
        self.brightness = 0
        self.contrast = 1.0
        self.intensity = 1.0
        self.negative = False

    def apply(self, src):
        res = f.rotation(self.rotation, src)
        res = f.scale(self.scale, res)
        res = f.shear(self.shear_h, self.shear_v, res)
        res = f.brightness(self.brightness, res)
        res = f.contrast(self.contrast, res)
        res = f.intensity(self.intensity, res)
        if(self.negative):
            res = f.negative(res)
        return res


if "img_settings" not in st.session_state:
    st.session_state.img_settings = ImageSettings()

st.write("# Ajustes")

if "frame" in st.session_state:
    original = st.session_state.frame
    res = st.session_state.img_settings.apply(original)
    ow, oh = original.shape
    rw, rh = res.shape

    # tw = max(ow,rw)
    # th = max(oh,rh)

    img = Image.fromarray(original)
    edited = Image.fromarray(res)
    with st.container(border=True):
        st.image(img, caption=f"Original {ow}x{oh}")
        st.image(edited, caption=f"Modificada {rw}x{rh}", width=None)
        _, buffer = cv2.imencode(".jpg", res)
        
        st.download_button("Download", data=buffer.tobytes(), file_name="editada.jpg", type="primary")
else:
    st.switch_page("pages/captura.py")

with st.sidebar:
    settings = st.session_state.img_settings
    rotation = st.slider("🔄 Rotação", max_value=360, value=settings.rotation)
    scale = st.slider("🔍 Escala", max_value=2.0, min_value=0.1, value=settings.scale)
    st.write("🪞 Cisalhamento")
    shear_h = st.slider(
        "Horizontal", max_value=1.0, min_value=-1.0, value=settings.shear_h
    )
    shear_v = st.slider(
        "Vertical", max_value=1.0, min_value=-1.0, value=settings.shear_v
    )
    brightness = st.slider("🌞 Brilho", max_value=255, min_value=0, value=settings.brightness)
    contrast = st.slider("🌗 Contraste", max_value=2.0, min_value=0.1, value=settings.contrast)
    intensity = st.slider("🎚️ Intensidade", max_value=2.0, min_value=0.1, value=settings.intensity)
    negative = st.checkbox("⚫ Negativo", value=settings.negative)
    if st.button("Aplicar"):
        settings.rotation = rotation
        settings.scale = scale
        settings.shear_h = shear_h
        settings.shear_v = shear_v
        settings.brightness = brightness
        settings.contrast = contrast
        settings.intensity = intensity
        settings.negative = negative
        st.rerun()
