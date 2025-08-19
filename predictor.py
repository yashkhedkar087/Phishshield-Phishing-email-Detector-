import joblib
import sys

# Step 1: Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Step 2: Take multi-line user input
print("\n📧 Enter the email content you want to check (Press Ctrl+Z then Enter to finish):\n")
email_text = sys.stdin.read()

# Step 3: Vectorize input
email_vector = vectorizer.transform([email_text])

# Step 4: Predict
prediction = model.predict(email_vector)[0]
probability = model.predict_proba(email_vector)[0]

# Step 5: Show result
label = "Phishing Email 🚨" if prediction == 1 else "Safe Email ✅"
confidence = max(probability) * 100

print(f"\n🔍 Prediction: {label}")
print(f"📊 Confidence: {confidence:.2f}%")
