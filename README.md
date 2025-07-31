# 📧 Spam Email Classification

A machine learning-based system to intelligently detect and classify spam emails using Natural Language Processing (NLP) techniques. The model is deployed using Streamlit for an interactive and user-friendly web interface.

![image alt](https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML/blob/main/diagram.png?raw=true)

## 🚀 Features
- Preprocessing with:
  - Lowercasing
  - Punctuation removal
  - Stopword removal
  - Frequent word elimination
  - Stemming & Lemmatization
  - Feature extraction using `CountVectorizer`

- Multiple model training:
  - Multinomial Naive Bayes
  - Random Forest
  - Support Vector Machine (SVM)

- Highest Accuracy Achieved: **~98.7%** (Naive Bayes)
- Lightweight Streamlit UI for spam email detection
- Model and vectorizer serialized with `pickle`

## 🧠 Algorithms Used
| Model              | Accuracy     |
|--------------------|--------------|
| Naive Bayes        | 98.7%        |
| Random Forest      | 96.8%        |
| SVM (Linear)       | 97.8%        |

## 📂 Project Structure

<img width="428" height="118" alt="{F1340397-7A71-4D58-9572-A2FAAC092B1A}" src="https://github.com/user-attachments/assets/508ed456-061a-4961-beac-e4b9ca4a417d" />

## 🧹 Preprocessing Steps
1. Text normalization: Lowercase conversion
2. Punctuation removal using `string.punctuation`
3. Stopwords removal using NLTK
4. Frequent word filtering (`call`, `im`, `get`, etc.)
5. Stemming (Porter Stemmer)
6. Lemmatization (WordNet Lemmatizer)
7. Train-test split using `sklearn`

## Proposed Methodology:
### Dataset Collection: 
Dataset contained 5,572 entries; duplicates removed, reduced to ~5,100.   
### Text Preprocessing:
Tokenization, lowercasing, and noise removal (punctuation/special characters).
Removed stopwords using NLTK and top 5 frequent words using Counter.
Applied stemming (PorterStemmer) and lemmatization (WordNetLemmatizer).
### Data Splitting: 
Split dataset into 80% training and 20% testing.
### Vectorization: 
Converted text to numerical data using CountVectorizer.
### Model Training & Evaluation:
Trained Naive Bayes (~99% accuracy), SVM (97%), Random Forest (96%).
Selected Naive Bayes for simplicity and performance. 	
### Model Deployment:
Saved model and vectorizer as pickle files.
Built a user-friendly interface using Streamlit.

## 🖥️ How to Run Locally
### 1. Clone the Repository
git clone https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML.git

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Streamlit App
streamlit run spam_detector_UI.py

### Streamlit User Application
![image alt](https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML/blob/main/Screenshot%20(209).png?raw=true)

## Classify Spam and Ham Email
![image alt](https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML/blob/main/Screenshot%20(210).png?raw=true)

![image alt](https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML/blob/main/Screenshot%20(211).png?raw=true)

## 👨‍💻 Author
Tridibesh Debnath
B.Tech (CSE - Data Science)
🔗 LinkedIn : https://www.linkedin.com/in/tridibesh-debnath-46b37924a/
📧 tridibeshdebnath@gmail.com
