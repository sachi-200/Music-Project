# ============================================================
# Test Carnatic Rāga Classifier from Hugging Face Space
# ============================================================

# 1️⃣ Install required library (only once)
# pip install gradio_client

from gradio_client import Client, file

# 2️⃣ Create a client for the Hugging Face Space
client = Client("jeevster/carnatic-raga-classifier")

# 3️⃣ Run prediction on your own WAV file
result = client.predict(
    k=5,                                      # number of top ragas to display
    audio=file("valli3.wav"),               # <-- replace with your own local audio file
    api_name="/predict"                       # the endpoint name from the Space
)

# 4️⃣ Print results
print("🎶 Prediction Result:")
print(result)