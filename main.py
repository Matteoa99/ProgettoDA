import json
from datetime import datetime

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/feel-it-italian-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/feel-it-italian-sentiment")

# Read data from input file
file = open('input.csv', 'r', encoding='utf-8')
Lines = file.readlines()
file.close()

ris = ""

# Predict sentiment and update json for each line
for line in Lines:
    data = json.loads(line.strip())

    inputs = tokenizer(data["text"], return_tensors="pt")

    # Call the model and get the logits
    labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
    outputs = model(**inputs, labels=labels)
    loss, logits = outputs[:2]
    logits = logits.squeeze(0)

    # Extract probabilities
    proba = torch.nn.functional.softmax(logits, dim=0)

    # Unpack the tensor to obtain negative and positive probabilities
    negative, positive = proba

    pos = np.round(positive.item(), 4)
    neg = np.round(negative.item(), 4)

    # Update json content
    data["tz_sa"] = datetime.now().isoformat()
    if pos > neg:
        data["sentiment"] = "positive"
        data["sentiment_value"] = pos
    else:
        data["sentiment"] = "negative"
        data["sentiment_value"] = neg

    # Create result string
    ris += json.dumps(data) + "\n"

# Write data into output file
file = open("output.csv", "w", encoding='utf-8')
file.write(ris)
file.close()