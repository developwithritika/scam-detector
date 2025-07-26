from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample dataset
texts = [
    # Scam examples
    "Congratulations you have won a lottery claim your prize now",
    "Urgent action required verify your account immediately",
    "Aapne lottery jeet liya click here to claim",
    "Your loan has been approved please send your details",
    "You are the lucky draw winner transfer fees to receive prize",
    "Bank se call hai your account will be blocked send OTP",
    # Safe examples
    "Hey are we still meeting tomorrow?",
    "Don't forget to bring your notebook to class.",
    "Happy birthday have a great day!",
    "Can you send me the report by evening?",
    "I attached the photos from our trip.",
    "Please review the document when you get time."
]

labels = [
    1, 1, 1, 1, 1, 1,  # 1 = Scam
    0, 0, 0, 0, 0, 0   # 0 = Safe
]

# Create a text classification pipeline
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# Train the model
model.fit(texts, labels)

# Save the model to a file
joblib.dump(model, "scam_model.pkl")

print("✅ Model trained and saved as 'scam_model.pkl'")
