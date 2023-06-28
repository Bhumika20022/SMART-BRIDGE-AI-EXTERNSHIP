# SMART-BRIDGE-AI-EXTERNSHIP
FAKE NEWS DETECTION SYSTEM 
Fake news has become a significant concern in the digital age, spreading misinformation and influencing public opinion. To address this issue, researchers have developed various techniques to detect and combat fake news. One such approach involves using Long Short-Term Memory (LSTM) networks combined with a Flask-based website.

LSTM is a type of recurrent neural network (RNN) that is particularly effective in modeling sequential data, making it suitable for analyzing text. The basic idea behind using LSTMs for fake news detection is to train the model on a large dataset of labeled news articles, distinguishing between real and fake news.

Here's an overview of the steps involved in using LSTMs and a Flask website for fake news detection:

Dataset Preparation: Gather a dataset of labeled news articles, where each article is classified as either real or fake. This dataset will serve as the training data for the LSTM model.

Preprocessing: Clean the text data by removing stop words, punctuation, and other irrelevant information. Perform tokenization and convert the text into numerical representations suitable for training the LSTM.

LSTM Model Training: Build an LSTM model using a deep learning framework like TensorFlow or PyTorch. Train the model on the preprocessed dataset, allowing it to learn patterns and features indicative of fake news.

Model Evaluation: Assess the performance of the trained LSTM model using evaluation metrics such as accuracy, precision, recall, and F1 score. This step helps determine the model's effectiveness in distinguishing between real and fake news.

Flask Website Development: Create a web application using the Flask framework, a popular Python web framework. Design the website's front-end, including forms for users to enter news article text.

Integration: Integrate the trained LSTM model into the Flask web application. When a user submits an article, the model processes the text and predicts whether it is real or fake news.

Display Results: Present the prediction results to the user on the Flask website. This can be done by showing a binary classification (real or fake) or providing a probability score indicating the likelihood of the news being fake.

Continuous Improvement: As new fake news detection techniques emerge or as more labeled data becomes available, retrain the LSTM model to enhance its accuracy and adapt it to evolving patterns of misinformation.

By combining LSTM models with a Flask website, users can easily access and utilize the fake news detection system. This approach provides a user-friendly interface for users to input news articles and receive instant predictions, contributing to the fight against fake news dissemination.

It's important to note that the effectiveness of fake news detection systems depends on various factors, including the quality and representativeness of the training dataset, the design of the LSTM model, and the ongoing efforts to update and refine the system.

By 
     Bhumika S (20BEC1100) 
     Md Nameer Uddin Haider  (20BEC1029)
     Ajay Krishnan (20BEC1355)
     Mridul Negi (20BEC1126)
   

