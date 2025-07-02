import sqlite3
from typing import List, Dict

# Connect to SQLite and create table if not exists
conn = sqlite3.connect("flashcard.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        question TEXT,
        answer TEXT,
        subject TEXT
    )
''')
conn.commit()

def add_flashcard(student_id: str, question: str, answer: str, subject: str):
    cursor.execute('''
        INSERT INTO flashcards (student_id, question, answer, subject)
        VALUES (?, ?, ?, ?)
    ''', (student_id, question, answer, subject))
    conn.commit()

def get_mixed_flashcards(student_id: str, limit: int) -> List[Dict]:
    cursor.execute('''
        SELECT subject FROM flashcards
        WHERE student_id = ?
        GROUP BY subject
    ''', (student_id,))
    subjects = [row[0] for row in cursor.fetchall()]

    results = []
    for subject in subjects:
        cursor.execute('''
            SELECT question, answer, subject FROM flashcards
            WHERE student_id = ? AND subject = ?
            ORDER BY RANDOM()
            LIMIT 1
        ''', (student_id, subject))
        row = cursor.fetchone()
        if row:
            results.append({
                "question": row[0],
                "answer": row[1],
                "subject": row[2]
            })
        if len(results) >= limit:
            break

    return results
