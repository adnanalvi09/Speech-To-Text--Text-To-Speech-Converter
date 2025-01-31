import utils
import streamlit as st

def main():
    st.title("File Upload and Input Example")

    # File uploader
    uploaded_file = st.file_uploader("Upload PDF or DOCX file", type=["pdf", "docx"])

    # Button and input label
    if uploaded_file:
        if st.button("Process Uploaded File"):
            if(uploaded_file.name[-4:] == "docx"):
                text = utils.read_docx(uploaded_file)
            elif(uploaded_file.name[-4:] == ".pdf"):
                text = utils.read_pdf(uploaded_file)
            
            utils.text_to_speech(text)
    
    st.title("Press the Button to speak and convert to docx")
    if st.button("Press to speak"):
        processPlaceholder = st.empty()
        data = utils.recognize_speech(processPlaceholder)
        utils.write_to_docx(data , processPlaceholder)


if __name__ == "__main__":
    main()
