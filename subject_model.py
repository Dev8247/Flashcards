from transformers import pipeline

# List of possible subjects
SUBJECT_LABELS = [
    "Physics", "Chemistry", "Biology", "Math",
    "History", "Geography", "Computer Science", "Economics"
]

# Load pre-trained zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_subject(text: str) -> str:
    result = classifier(text, SUBJECT_LABELS)
    return result["labels"][0]  # Most likely subject
