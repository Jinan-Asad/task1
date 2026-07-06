import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
from splitter import split_text
# مسار قاعدة المعرفة
KNOWLEDGE_BASE_PATH = "Knowledge Base"


# ----------- قراءة الملفات -----------

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def load_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()


# ----------- تحميل كل الملفات -----------

def load_documents():
    documents = []

    for file in os.listdir(KNOWLEDGE_BASE_PATH):
        file_path = os.path.join(KNOWLEDGE_BASE_PATH, file)

        if file.endswith(".txt") or file.endswith(".md"):
            text = load_txt(file_path)

        elif file.endswith(".pdf"):
            text = load_pdf(file_path)

        elif file.endswith(".docx"):
            text = load_docx(file_path)

        elif file.endswith(".csv"):
            text = load_csv(file_path)

        else:
            continue

        documents.append({
            "file": file,
            "content": text
        })

    return documents


# ----------- تقسيم النصوص -----------

def load_and_split():
    documents = load_documents()

    all_chunks = []

    for doc in documents:
        chunks = split_text(doc["content"])

        for chunk in chunks:
            all_chunks.append({
                "file": doc["file"],
                "text": chunk
            })

    return all_chunks