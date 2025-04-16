# FridayProject9
# AI Prompt GUI Application
This is a simple Python desktop application that provides a graphical user interface (GUI) to interact with an AI completion service (like OpenAI's GPT). You can enter a prompt, submit it, and view the AI's response.

## Features
- Input text box for prompts.

- Submit button to trigger AI completion.

- Output text box to display the AI's response.

- Uses a .env file to securely store the API key.

# How to Set Up and Run the AI Prompt App
Follow these steps to get the Python application running on your computer:

## 1. Prerequisites:
- Python: Make sure you have Python installed. You can download it from python.org. Version 3.7 or higher is recommended.

- OpenAI API Key: You need an API key from OpenAI.

- Go to the OpenAI Platform website.

- Sign up or log in.

- Navigate to the API keys section (usually under your account settings).

- Create a new secret key. Important: Copy this key immediately and save it somewhere secure. You won't be able to see it again after closing the window. Treat this key like a password!

## 2. Save the Code:
- Copy the Python code for the GUI (e.g., from a file named ai_prompt_app.py).

- Save it in a directory on your computer. If cloning from Git, this is already done.

## 3. Create the .env File:
- In the same directory where you saved ai_prompt_app.py, create a new text file.

- Name this file exactly .env (dot env). Make sure your system doesn't automatically add .txt at the end.

- Open the .env file with a simple text editor.

- Add the following line, replacing "YOUR_API_KEY_HERE" with the actual API key you got from OpenAI:

- OPENAI_API_KEY="YOUR_API_KEY_HERE"

- Save and close the .env file. Do not share this file or commit it to public repositories like GitHub, as it contains your secret key. (Add .env to your .gitignore file if using Git).

## 4. Install Required Libraries:
- Open your terminal or command prompt.

- Navigate (cd) to the directory where you saved ai_prompt_app.py and .env.

- Run the following command to install the necessary Python libraries:

- pip install openai python-dotenv
(Note: Depending on your Python setup, you might need to use pip3 instead of pip)

## 5. Run the Application:
- While still in the same directory in your terminal or command prompt, run the script using Python:

  python ai_prompt_app.py
  (Or python3 ai_prompt_app.py if needed)

## 6. Use the App:
- A window titled "AI Prompt Interface" should appear.

- Type your question or instruction into the top box ("Enter your prompt:").

- Click the "Submit Prompt" button.

- Wait a moment while the app contacts the OpenAI API.

- The AI's response will appear in the bottom box ("AI Response:").

## Troubleshooting:
API Key Error: If you get an error about the API key, double-check that your .env file is named correctly, is in the same folder as the script, and contains the correct key in the format OPENAI_API_KEY="your_key". Also ensure you have funds or credits in your OpenAI account if required.

Library Not Found: If you get an error like ModuleNotFoundError, make sure you ran the pip install command correctly (Step 4).

Other Errors: If the AI response shows an error, it might be related to the specific prompt, the chosen model, or temporary issues with the OpenAI service.
