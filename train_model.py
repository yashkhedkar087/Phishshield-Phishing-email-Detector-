# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load the dataset
df = pd.read_csv("Phishing_Email.csv")

# Step 2: Clean data
df.dropna(inplace=True)
df['Email Text'] = df['Email Text'].astype(str)

# Step 3: Convert labels to 1 (Phishing) and 0 (Safe)
df['label'] = df['Email Type'].apply(lambda x: 1 if 'Phishing' in x else 0)

# Step 4: Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(df['Email Text'])
y = df['label']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Step 8: Save model & vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Model and vectorizer saved as 'model.pkl' and 'vectorizer.pkl'")
