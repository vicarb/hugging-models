from transformers import pipeline

classifier = pipeline("sentyment-analysis")
print(classifier)

res = classifier("hello today was a good day")

print(res)
