# Spam_Email_Classification_using_NLP_and_ML
Email is a vital part of modern communication, but spam emails create major challenges, wasting time and posing security risks like phishing and malware. This project addresses the shortcomings of traditional spam filters by using NLP and Machine Learning to build an adaptive system that accurately classifies emails as spam or legitimate. The solution enhances security, prevents phishing attacks, and ensures important emails aren't mistakenly flagged. It can be integrated into email platforms to benefit individuals and organizations, improving productivity and communication. By automating spam detection, this project helps make email safer, more efficient, and stress-free for everyone.

![image alt](https://github.com/Tridibesh-033/Spam_Email_Classification_using_NLP_and_ML/blob/main/diagram.png?raw=true)

## Proposed Methodology:
Proposed Methodology
1.	Dataset Collection: Dataset contained 5,572 entries; duplicates removed, reduced to ~5,100.
2.	
3.	Text Preprocessing:
           Tokenization, lowercasing, and noise removal (punctuation/special characters).
           Removed stopwords using NLTK and top 5 frequent words using Counter.
  	       Applied stemming (PorterStemmer) and lemmatization (WordNetLemmatizer).
  	
4.	Data Splitting: Split dataset into 80% training and 20% testing.
5.	
6.	Vectorization: Converted text to numerical data using CountVectorizer.
7.	
8.	Model Training & Evaluation:
          Trained Naive Bayes (~99% accuracy), SVM (97%), Random Forest (96%).
          Selected Naive Bayes for simplicity and performance.
  	
10.	Model Deployment:
          Saved model and vectorizer as pickle files.
          Built a user-friendly interface using Streamlit.
   	
This methodology ensures accurate, scalable, and user-friendly spam email classification.




