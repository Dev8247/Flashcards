# 📚 Smart Flashcard Backend

This is a FastAPI-based backend for a smart flashcard system that automatically detects the subject of a flashcard using a pre-trained transformer model.

---

## 🚀 Features

- Add flashcards with just a question and answer
- Automatically infers subject (e.g., "Physics", "Biology") using **zero-shot learning**
- Fetch a shuffled mix of flashcards across different subjects
- Uses Hugging Face's `facebook/bart-large-mnli` model for classification

---
