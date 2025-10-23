# SENTIMENT-ANALYSIS-WITH-NLP-Python-program

COMPANY : CODTECH IT SOLUTIONS

NAME : Thangaraj P

INTERN ID : CT08DY1102

DOMAIN : MACHINE LEARNING

DURATION : 8 WEEKS

MENTOR : NEELA SANTHOSH

TASK DESCRIOTON : 

The main objective of this task was to perform Sentiment Analysis using Natural Language Processing (NLP) techniques to classify customer reviews as positive or negative.
This task focuses on understanding how text data can be transformed into numerical form using TF-IDF vectorization and then modeled using Logistic Regression, a popular algorithm for binary classification.
Through this exercise, I learned how to preprocess textual data, extract meaningful features, train a machine learning model, and evaluate its performance.

Tools and Technologies Used
•	Programming Language: Python
•	Libraries Used:
o	pandas – for loading and analyzing text data
o	numpy – for handling arrays and numerical operations
o	scikit-learn (sklearn) – for TF-IDF vectorization, model training, and evaluation
o	nltk (Natural Language Toolkit) – for text preprocessing (stopword removal, tokenization, etc.)
o	matplotlib & seaborn – for visualizing data distributions and confusion matrix
•	Editor/Platform: Jupyter Notebook (or alternatively VS Code with Jupyter extension)

Implementation Process
1.	Importing Libraries
I started by importing the required Python libraries for data handling, preprocessing, and model building.
2.	Loading the Dataset
I used a CSV dataset containing customer reviews and their sentiment labels (positive/negative). The dataset was read using pandas.read_csv(). Each review was represented as a text string, and the sentiment label was stored as 0 (negative) or 1 (positive).
3.	Exploratory Data Analysis (EDA)
Before training the model, I explored the dataset to understand its structure — checking for missing values, text length distribution, and the balance between positive and negative samples. I plotted sentiment distribution graphs using seaborn to visualize the dataset.
4.	Text Preprocessing
Since raw text data cannot be directly used in machine learning models, I performed several preprocessing steps:
o	Converted all reviews to lowercase
o	Removed punctuation and special characters
o	Removed stopwords (like the, is, and) using NLTK
o	Tokenized the text into words
o	Optionally applied stemming or lemmatization to reduce words to their base form
5.	TF-IDF Vectorization
I used TF-IDF (Term Frequency–Inverse Document Frequency) from sklearn.feature_extraction.text to convert the cleaned text into numerical feature vectors. TF-IDF measures how important a word is in a document relative to the entire dataset. This helps highlight meaningful words while reducing noise from common terms.
6.	Model Building with Logistic Regression
The feature vectors (X) and sentiment labels (y) were split into training (80%) and testing (20%) datasets using train_test_split().
A Logistic Regression model was trained using the training data. Logistic Regression is ideal for binary classification tasks like positive vs. negative sentiment.
7.	Model Prediction and Evaluation
After training, I used the model to predict sentiments on the test data. The results were evaluated using:
o	Accuracy Score – percentage of correct predictions
o	Confusion Matrix – to see how many positive/negative samples were correctly or incorrectly classified
o	Classification Report – showing precision, recall, and F1-score
8.	Visualization and Output
I visualized the confusion matrix using seaborn heatmap to make the results clearer.
The model achieved high accuracy (generally between 85–95%, depending on the dataset).
Finally, I saved the results and visualizations in the same project folder for submission.

Results and Analysis
The model successfully analyzed customer sentiments with high accuracy.
From the confusion matrix, I observed that the model correctly identified most of the positive and negative reviews.
The TF-IDF vectorization effectively captured the importance of key opinion words such as excellent, bad, love, and worst, which strongly influenced the classification outcome.
Overall, this task demonstrated how NLP combined with machine learning can convert unstructured text into valuable insights.
This kind of analysis helps companies understand customer feedback automatically and improve their products or services.

Applications
Sentiment Analysis has a wide range of real-world applications, such as:
•	E-commerce Platforms – Analyzing customer reviews to improve products
•	Social Media Monitoring – Tracking public opinion on brands, movies, or events
•	Finance Sector – Analyzing market sentiment to forecast stock trends
•	Customer Service – Automatically detecting negative feedback to prioritize responses
•	Politics & Public Relations – Measuring public sentiment on speeches, policies, or campaigns

Conclusion
Through this task, I gained a deep understanding of text preprocessing, feature extraction using TF-IDF, and modeling with Logistic Regression.
It helped me learn how machine learning can be applied to real-world text data to derive insights and make predictions.
I used Jupyter Notebook as my main platform because it allows running each cell step-by-step, viewing results instantly, and visualizing data clearly.
This task strengthened my skills in Natural Language Processing (NLP) and prepared me for more advanced projects involving chatbots, sentiment prediction, and opinion mining.


