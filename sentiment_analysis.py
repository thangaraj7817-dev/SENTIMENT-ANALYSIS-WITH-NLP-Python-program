from textblob import TextBlob
import os

# Step 1: Input from user or dataset
text = input("Enter a sentence or review: ")

# Step 2: Analyze sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# Step 3: Classify sentiment
if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😠"
else:
    sentiment = "Neutral 😐"

# Step 4: Display result
print(f"Sentiment: {sentiment}")
print(f"Polarity Score: {polarity}")

# Step 5: Save output to file
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "sentiment_output.txt")

with open(file_path, "w") as file:
    file.write(f"Input Sentence: {text}\n")
    file.write(f"Polarity Score: {polarity}\n")
    file.write(f"Sentiment: {sentiment}\n")

print(f"✅ Output saved to {file_path}")
