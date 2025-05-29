import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini client
genai.configure(api_key=GOOGLE_API_KEY)

# Let user optionally set temperature
try:
    temperature = float(input("Enter temperature (e.g., 0.7): ").strip())
except ValueError:
    temperature = 0.7  # Default if user input is invalid
    print("Using default temperature: 0.7")

# Initialize chat session with model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": temperature,
        "top_p": 1,
        "max_output_tokens": 2048,
    }
)

chat = model.start_chat(history=[])

# First turn
user_input1 = input("\nYou: ")
response1 = chat.send_message(user_input1)
print("\nGemini:", response1.text)

# Second turn
user_input2 = input("\nYou: ")
response2 = chat.send_message(user_input2)
print("\nGemini:", response2.text)

# (Optional) Third turn — Bonus
continue_chat = input("\nWould you like to continue chatting? (yes/no): ").strip().lower()
while continue_chat == "yes":
    user_input = input("\nYou: ")
    response = chat.send_message(user_input)
    print("\nGemini:", response.text)
    continue_chat = input("\nContinue? (yes/no): ").strip().lower()
