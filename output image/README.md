# 🛡️ Phishing Email Detection using Machine Learning  

This project detects **phishing emails** using Machine Learning and a Streamlit-based GUI.  
It analyzes the email content and classifies it as **Phishing** or **Safe**, based on suspicious words and trained ML models.  

---

## 🚀 Features  
- Detects phishing emails based on common suspicious words.  
- Trained ML model to classify email content.  
- Interactive **GUI built with Streamlit** for easy testing.  
- Modular structure with separate files for training, prediction, and GUI.  

---

## 📂 Project Structure  

📁 phishing-email-detector
┣ 📄 train_model.py # Train ML model on dataset
┣ 📄 predictor.py # Loads model & predicts email type
┣ 📄 email_gui.py # Streamlit GUI for testing
┣ 📄 suspicious_words.py # List of suspicious words
┣ 📄 phishing_model.pkl # Saved trained ML model
┣ 📄 vectorizer.pkl # Saved CountVectorizer/TF-IDF
┣ 📄 README.md # Documentation
┗ 📄 requirements.txt # Dependencies

Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


install dependencies

pip install -r requirements.txt


🏋️ Training the Model

If you want to retrain the model with your dataset:   python train_model.py

This will generate:

phishing_model.pkl → trained ML model

vectorizer.pkl → vectorizer used for text processing


🔮 Running Predictions

For command-line testing:

python predictor.py


It will ask for email content and return Phishing or Safe.





🖥️ Running the GUI

To launch the Streamlit GUI:

streamlit run email_gui.py

This will open the app in your browser where you can paste email text and check the result.


Requirements

Dependencies are listed in requirements.txt. Example:

scikit-learn
pandas
numpy
streamlit



Install with:

pip install -r requirements.txt


🤝 Contributing

Feel free to fork this repo, raise issues, or submit PRs to improve the project.


📜 License

This project is licensed under the MIT License.

 Author  
👨‍💻 Developed by **Yash Khedkar**  
🔗 GitHub: [yashkhedkar087](https://github.com/yashkhedkar087)  
🔗 LinkedIn: [Yash Khedkar](https://www.linkedin.com/in/yash-khedkar1907/)  
