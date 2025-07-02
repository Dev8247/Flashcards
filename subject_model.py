from transformers import pipeline

# subjects
SUBJECT_LABELS = [
    "Physics", "Chemistry", "Biology", "Math",
    "History", "Geography", "Computer Science", "Economics"
]

# pre-trained classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_subject(text: str) -> str:
    result = classifier(text, SUBJECT_LABELS)
    return result["labels"][0]  
