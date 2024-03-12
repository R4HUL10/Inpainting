import streamlit as st
from PIL import Image

def main():
    st.title("Semantic Image Inpainting")

    st.write("Please upload a normal image and a masked image.")

    # Upload the normal image
    normal_image = st.file_uploader("Upload Normal Image", type=["jpg", "jpeg", "png"])

    # Upload the masked image
    masked_image = st.file_uploader("Upload Masked Image", type=["jpg", "jpeg", "png"])

    if normal_image and masked_image:
        st.image(normal_image, caption='Normal Image', use_column_width=True)
        st.image(masked_image, caption='Masked Image', use_column_width=True)

        if st.button("Submit"):
            # Process the images here
            # You can perform any processing or analysis here
            # For demonstration, we'll just display the images again
            st.write("Processing the images...")

            # Convert uploaded images to PIL Image objects
            normal_img = Image.open(normal_image)
            masked_img = Image.open(masked_image)

            # Display processed images
            st.write("Processed Normal Image")
            st.image(normal_img, use_column_width=True)

            st.write("Processed Masked Image")
            st.image(masked_img, use_column_width=True)

if __name__ == "__main__":
    main()
