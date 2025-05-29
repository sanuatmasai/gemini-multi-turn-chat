# Context-Aware Gemini Chat

A simple interactive console chatbot that uses Google's Gemini AI API to maintain context-aware conversations. The bot remembers previous messages in the conversation and allows users to adjust model parameters like temperature for different response styles.

## What the Script Does

This chatbot provides:

- **Context Preservation**: Maintains conversation history across multiple turns so Gemini can reference earlier messages
- **Interactive Console Chat**: Simple text-based interface using Python's `input()` and `print()`
- **Configurable Parameters**: Allows users to set temperature values to control response creativity
- **Multi-turn Conversations**: Supports minimum 2 turns with optional extended chatting
- **Real-time API Integration**: Direct communication with Google's Gemini 2.0 Flash model

**Key Features:**
1. **First Turn**: User provides initial input, receives Gemini response
2. **Second Turn**: User provides follow-up, Gemini responds with full context awareness
3. **Extended Chat (Bonus)**: Optional continued conversation with persistent context
4. **Temperature Control**: User can specify creativity level (0.0 = focused, 1.0 = creative)

## Setup and Dependencies

### Prerequisites
- Python 3.7+
- Google AI API key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation Steps

1. **Clone or download the script**:
   ```bash
   # If using git
   git clone https://github.com/your-username/gemini-chat.git
   cd gemini-chat
   
   # Or simply download gemini_chat.py
   ```

2. **Install required packages**:
   ```bash
   pip install google-generativeai>=0.3.1 python-dotenv>=1.0.1
   ```

3. **Set up environment variables**:
   Create a `.env` file in the same directory as the script:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Get your API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

### File Structure

```
gemini-chat/
├── gemini_chat.py    # Main script
├── .env              # Environment variables (create this)
├── README.md         # This file
├── requirements.txt  # Dependencies (optional)
└── .gitignore       # Git ignore file (optional)
```

## How to Run

1. **Ensure setup is complete** (API key in `.env` file, dependencies installed)

2. **Run the script**:
   ```bash
   python gemini_chat.py
   ```

3. **Follow the prompts**:
   ```
   Enter temperature (e.g., 0.7): 0.9
   
   You: Hello, can you help me write a story about a robot?
   
   Gemini: [Response about robot story]
   
   You: Make it more dramatic and add a villain
   
   Gemini: [Context-aware response incorporating previous story discussion]
   
   Would you like to continue chatting? (yes/no): yes
   
   You: [Additional input...]
   ```

4. **Expected Output**: The script will print Gemini's responses after each turn, with the final response being the last message from the AI.

## Usage Examples

### Example 1: Creative Writing
```bash
$ python gemini_chat.py
Enter temperature (e.g., 0.7): 0.9

You: Tell me about quantum physics
Gemini: Quantum physics is the fascinating study of matter and energy at the smallest scales...

You: Can you explain it using a simple analogy?
Gemini: Great question! Think of quantum physics like a cosmic game of hide-and-seek...
```

### Example 2: Technical Discussion
```bash
$ python gemini_chat.py
Enter temperature (e.g., 0.7): 0.3

You: What are the benefits of using Docker?
Gemini: Docker provides several key benefits for software development...

You: How does it compare to virtual machines?
Gemini: Excellent follow-up! Compared to the virtual machines we just discussed...
```

## Model Configuration

The script allows you to configure several parameters:

- **Temperature** (0.0-1.0): Controls response creativity
  - `0.0-0.3`: Focused, deterministic responses
  - `0.4-0.7`: Balanced creativity and consistency
  - `0.8-1.0`: Highly creative, varied responses

- **Model**: Uses `gemini-2.0-flash` for fast, efficient responses
- **Max Output Tokens**: Set to 2048 for comprehensive responses
- **Top-p**: Set to 1 for full vocabulary consideration

## Error Handling

The script includes basic error handling:

- **Invalid Temperature**: Defaults to 0.7 if non-numeric input is provided
- **API Key Missing**: Will fail gracefully with clear error message
- **Network Issues**: Google's client library handles most connection errors

## Requirements File

If you prefer using a requirements file, create `requirements.txt`:
```
google-generativeai>=0.3.1
python-dotenv>=1.0.1
```

Then install with:
```bash
pip install -r requirements.txt
```

## Security Notes

⚠️ **Important**: 
- Never commit your `.env` file to version control
- Keep your API key secure and don't share it
- The `.env` file should be added to `.gitignore`

## Features Demonstrated

✅ **Multi-turn conversation with context preservation**  
✅ **Console-based input/output**  
✅ **Model parameter configuration (temperature)**  
✅ **Proper API initialization and chat session management**  
✅ **Extended conversation support (bonus feature)**  
✅ **Error handling for user inputs**  
