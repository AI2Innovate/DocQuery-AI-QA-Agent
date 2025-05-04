from transformers import pipeline

def load_model():
    return pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")
