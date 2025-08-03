import streamlit as st
import cv2
import numpy as np

st.markdown("# Captura")

# Opencv webcam capture
# if st.button("Camera"):
#     camera = cv2.VideoCapture(0)
#     win_name = "Pressione Espaço para capturar a imagem"
#     st.write(win_name)
#     while camera.isOpened():
#         ret, frame = camera.read()
#         cv2.imshow(win_name, frame)
#         cv2.setWindowProperty(win_name, cv2.WND_PROP_TOPMOST, 1.0)
#         press = cv2.waitKey(1)
#         if press == ord(" "):
#             camera.release()
#             st.session_state.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             st.switch_page('pages/ajustes.py')
#         elif press == 27:
#             camera.release()
#     cv2.destroyAllWindows()


def to_opencv_im(bytes_data):
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_GRAYSCALE)
    st.session_state.frame = cv2_img
    st.switch_page('pages/ajustes.py')

cam_disabled = True
if st.button("Camera 📷"):
    cam_disabled = False

img_file_buffer = st.camera_input("Caputar com webcam", disabled=cam_disabled)
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    to_opencv_im(bytes_data)


upload_file = st.file_uploader("Upload de Imagem")
if upload_file is not None:
    bytes_data = upload_file.getvalue()
    to_opencv_im(bytes_data)