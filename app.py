import json
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# similarity model
sim_model = SentenceTransformer("all-MiniLM-L6-v2")

# local AI model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
ai_model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# load dataset
with open("dataset.json") as f:
    data = json.load(f)

# load knowledge file
with open("knowledge.txt") as f:
    knowledge = f.readlines()

# encode knowledge once
knowledge_embeddings = sim_model.encode(knowledge, convert_to_tensor=True)


# ---------------- AI Generator ----------------
def ai_generate(query):
    inputs = tokenizer(query, return_tensors="pt").to(ai_model.device)
    output = ai_model.generate(**inputs, max_new_tokens=120)
    return tokenizer.decode(output[0], skip_special_tokens=True)


# ---------------- Chatbot Logic ----------------
def chatbot(query):

    # SECURITY GUARDRAILS
    blocked = ["password", "otp", "pin", "cvv", "card number"]
    if any(word in query.lower() for word in blocked):
        return "Sorry, I cannot assist with sensitive or confidential information."

    # -------- DATASET SEARCH --------
    query_embedding = sim_model.encode(query, convert_to_tensor=True)

    best_score = 0
    best_answer = None

    for item in data:
        emb = sim_model.encode(item["instruction"], convert_to_tensor=True)
        score = util.cos_sim(query_embedding, emb)

        if score > best_score:
            best_score = score
            best_answer = item["output"]

    if best_score > 0.75:
        return best_answer

    # -------- RAG SEARCH --------
    scores = util.cos_sim(query_embedding, knowledge_embeddings)[0]
    best_idx = scores.argmax()

    if scores[best_idx] > 0.55:
        return knowledge[best_idx]

    # -------- AI FALLBACK --------
    return ai_generate(query)


# ---------------- RUN BOT ----------------
print("\nBFSI Assistant Ready. Type 'exit' to quit.\n")

while True:
    q = input("You: ")
    if q.lower() == "exit":
        break
    print("Bot:", chatbot(q))