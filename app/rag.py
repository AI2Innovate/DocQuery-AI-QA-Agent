from app.model import load_model
from app.ingest import search_context

model = load_model()

def get_answer(question: str):
    context = search_context(question)
    prompt = f"""
    You are a helpful assistant. Use the following context to answer:
    Context: {context}
    Question: {question}
    Answer:
    """
    response = model(prompt, max_length=256, do_sample=True)
    return response[0]['generated_text']
