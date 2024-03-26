import streamlit as st
import torch
from StableDiffusionWrapper import generate_images

st.title("Image Generation Server 🎨")


# Streamlit interface
text_prompt = st.text_area("Enter text prompt:")

if st.button("Generate Images"):
  if text_prompt:
    generated_image = generate_images(text_prompt)
    st.write("Generated Images:")
    st.image(generated_image)

    if generated_image:
      if st.button("Download Images") :
        generated_image.save(f"{text_prompt}.png")