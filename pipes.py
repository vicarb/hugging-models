from transformers import pipeline

classifier = pipeline("text-generation", model="distilgpt2")
print(classifier)

res = classifier("today was a good day", max_length=50, num_return_sequences=2)

print(res)
