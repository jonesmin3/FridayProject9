import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import openai
from dotenv import load_dotenv

# --- Configuration ---
# Load environment variables from a .env file
# This file should contain your OPENAI_API_KEY
load_dotenv()

# --- OpenAI API Setup ---
try:
    # Attempt to get the API key from environment variables
    # Correct way to load the key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file or environment variables.")
    # You might want to specify a model, e.g., "gpt-3.5-turbo" or "gpt-4"
    # If using newer versions of the openai library (>= 1.0.0), client initialization is different:
    # client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except ValueError as e:
    messagebox.showerror("API Key Error", str(e))
    # Exit if the API key is missing, as the core functionality depends on it.
    exit()
except ImportError:
    messagebox.showerror("Import Error", "The 'openai' or 'python-dotenv' library is not installed.\nPlease install them using: pip install openai python-dotenv")
    exit()


# --- Function to Get Completion ---
def get_ai_completion():
    """
    Retrieves the prompt from the input box, sends it to the OpenAI API,
    and displays the response in the output box.
    Handles potential API errors.
    """
    prompt = prompt_entry.get("1.0", tk.END).strip() # Get text from input box

    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return

    # Indicate processing
    output_text.configure(state='normal') # Enable editing to insert text
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Generating response...")
    output_text.configure(state='disabled') # Disable editing
    window.update_idletasks() # Update the GUI to show the message

    try:
        # --- Using OpenAI API (older versions < 1.0.0) ---
        # response = openai.Completion.create(
        #   engine="text-davinci-003", # Or another suitable model
        #   prompt=prompt,
        #   max_tokens=150 # Adjust as needed
        # )
        # completion = response.choices[0].text.strip()

        # --- Using OpenAI API (newer versions >= 1.0.0 with ChatCompletion) ---
        # Initialize client if not done globally (adjust based on your openai library version)
        client = openai.OpenAI(api_key=openai.api_key) # Assumes API key was loaded correctly

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # A common and capable chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250 # Limit response length
        )
        completion = response.choices[0].message.content.strip()
        # --- End API Call ---


        # Display the completion
        output_text.configure(state='normal') # Enable editing
        output_text.delete("1.0", tk.END)      # Clear "Generating..." message
        output_text.insert(tk.END, completion) # Insert the AI response
        output_text.configure(state='disabled')# Disable editing again

    except openai.AuthenticationError:
         messagebox.showerror("API Error", "Authentication failed. Please check your API key in the .env file.")
         output_text.configure(state='normal')
         output_text.delete("1.0", tk.END)
         output_text.insert(tk.END, "Error: Invalid API Key.")
         output_text.configure(state='disabled')
    except openai.RateLimitError:
         messagebox.showerror("API Error", "Rate limit exceeded. Please wait and try again later or check your usage plan.")
         output_text.configure(state='normal')
         output_text.delete("1.0", tk.END)
         output_text.insert(tk.END, "Error: Rate limit exceeded.")
         output_text.configure(state='disabled')
    except Exception as e:
        # Catch any other unexpected errors during the API call
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        output_text.configure(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        output_text.configure(state='disabled')

# --- GUI Setup ---
window = tk.Tk()
window.title("AI Prompt Interface")
window.geometry("600x500") # Set initial window size

# Configure grid layout
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1) # Input prompt row
window.rowconfigure(3, weight=3) # Output text row

# Input Label
prompt_label = tk.Label(window, text="Enter your prompt:")
prompt_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

# Input Text Area (using Text widget for potential multi-line input)
prompt_entry = scrolledtext.ScrolledText(window, height=5, wrap=tk.WORD)
prompt_entry.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

# Submit Button
submit_button = tk.Button(window, text="Submit Prompt", command=get_ai_completion)
submit_button.grid(row=2, column=0, padx=10, pady=10)

# Output Label
output_label = tk.Label(window, text="AI Response:")
output_label.grid(row=3, column=0, padx=10, pady=(5, 0), sticky="w")

# Output Text Area (read-only)
output_text = scrolledtext.ScrolledText(window, height=15, wrap=tk.WORD, state='disabled') # Start disabled
output_text.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

# --- Start the GUI Event Loop ---
window.mainloop()
