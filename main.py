from datetime import datetime
import json
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/feel-it-italian-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/feel-it-italian-sentiment")

file1 = open('input.csv', 'r', encoding='utf-8')
Lines = file1.readlines()
file1.close()

ris = ""

# Strips the newline character
for line in Lines:
    str = line.strip()
    data = json.loads(str)

    sentence = data["text"]
    inputs = tokenizer(sentence, return_tensors="pt")

    # Call the model and get the logits
    labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
    outputs = model(**inputs, labels=labels)
    loss, logits = outputs[:2]
    logits = logits.squeeze(0)

    # Extract probabilities
    proba = torch.nn.functional.softmax(logits, dim=0)

    # Unpack the tensor to obtain negative and positive probabilities
    negative, positive = proba
    data["tz_sa"] = datetime.now().isoformat()
    pos = np.round(positive.item(), 4)
    neg = np.round(negative.item(), 4)

    if pos > neg:
        data["sentiment"] = "positive"
        data["sentiment_value"] = pos
    else:
        data["sentiment"] = "negative"
        data["sentiment_value"] = neg

    tmp = json.dumps(data)
    ris += tmp + "\n"

f = open("output.csv", "w", encoding='utf-8')
f.write(ris)
f.close()