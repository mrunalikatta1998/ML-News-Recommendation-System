# ML-News-Recommendation-System
=======
# News Classification System

## Overview
This project focuses on developing a machine-learning-driven system for classifying news articles. The system integrates traditional classification algorithms such as SVM (Support Vector Machines) and Naive Bayes with advanced deep learning techniques like BERT. The goal is to enhance accuracy and deliver relevant news through a user-friendly web application that provides real-time, category-based news browsing.

## Project Objectives
- Develop a robust machine-learning model for news classification.
- Improve accuracy using a hybrid approach with both traditional and advanced models.
- Implement a user-friendly web application for real-time news delivery.
- Ensure scalability to handle large datasets and adapt to user preferences.

## Technologies Used
- **Frontend:** React
- **Backend:** Python (Django Framework)
- **Machine Learning Frameworks:**
  - Scikit-learn (for SVM, Logistic Regression, Naive Bayes)
  - Transformers (for BERT)
- **Database:** SQLite

## Data Collection
- Data Sources:
  - Zenodo (for training data)
  - News API and Currents API (for real-time news retrieval)
- Collection Methods:
  - Automated web scraping (using BeautifulSoup)
  - API integration for dynamic content

## Data Preprocessing
- Cleaning: Removal of HTML tags, special characters, and noise.
- Normalization: Lowercasing, stop-word removal, and stemming/lemmatization.
- Vectorization: Text transformed into numerical vectors using TF-IDF.
- Dataset Splitting: Stratified sampling for training, validation, and testing.

## Machine Learning Models
1. **Naive Bayes:**   
2. **Logistic Regression:**
3. **Support Vector Machines (SVM):**
4. **BERT (Bidirectional Encoder Representations from Transformers):**

   ## Model Evaluation
- Metrics:
  - **Precision:** 0.88 (for BERT model)
  - **Recall:** Measures true positive rate.
  - **F1 Score:** Harmonic mean of precision and recall.

## System Architecture
- Data is collected through APIs and web scraping.
- Processed through four machine learning models (Naive Bayes, Logistic Regression, SVM, BERT).
- Results are presented via a user-friendly web interface.

## System Features
- Real-time news classification and recommendation.
- Adaptive learning to track and adjust user preferences.
- User-friendly dashboard for categorized news browsing.

## Achievements
- Achieved 0.88 precision using BERT for news classification.
- Built a scalable system capable of handling large datasets.
- Deployed a fully functional web application.

## Challenges
- High computational demands for training BERT.
- Managing data quality and diversity.
- Complex implementation due to multi-model integration.

## Future Improvements
- Implement personalized news recommendation based on user behavior.
- Add a news summarization feature to enhance user experience.
- Optimize models for better resource utilization and faster processing.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/kanchNaik/newsRecommendationClassification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd newsRecommendationClassification
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend (Django server):
   ```bash
   python manage.py runserver
   ```
5. Navigate to the frontend directory and start React:
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Contributors
- Kanchan Naik
- Mrunali Katta
- Prasad Shimpatwar
- Yashasvi Kanchugantla

## References
1. Hong, J.-H., & Cho, S.-B. (2008). "A probabilistic multi-class strategy of one-vs.-rest support vector machines."
2. Yang, F.-J. (2018). "An implementation of naive bayes classifier."
3. Google. "bert-base-uncased," Hugging Face.
4. Raza, S., & Ding, C. (2020). "A survey on news recommender systems."
