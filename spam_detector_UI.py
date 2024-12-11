import streamlit as st
import pickle

# Load the pre-trained model and vectorizer
model = pickle.load(open('spam_mod.pkl', 'rb'))
vec = pickle.load(open('ct_vec.pkl', 'rb'))


def load_css(file_path):
    with open(file_path, "r") as f:
        return f"<style>{f.read()}</style>"
    
css_styles = load_css("style.css")

st.markdown(css_styles, unsafe_allow_html=True)


def main():
    st.title("Intelligent Spam Email Detection System")
    st.write("This Machine Learning application is designed for accurately classifying spam emails")
    st.subheader("Classification")
    
    # Get user input for email classification
    user_input = st.text_area("Enter an email to classify", height=70)

    if st.button("Classify"):
        if user_input:
            data = [user_input]
            user_vec = vec.transform(data)  # Transform input email text
            result = model.predict(user_vec)  # Predict spam or not

            if result[0] == 0:
                st.success("This is not a spam email")
            else:
                st.error("This is a spam email")
        else:
            st.write("Please enter an email to classify...")


if __name__ == "__main__":
    main()
