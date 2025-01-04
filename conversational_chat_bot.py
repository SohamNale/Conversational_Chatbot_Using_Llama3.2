import requests
import json
import gradio as gr
import speech_recognition as sr
from gtts import gTTS
import tempfile

OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Function to convert audio input to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Error with speech recognition service: {e}"

# Function to convert text to audio output
def text_to_audio(text):
    tts = gTTS(text)
    audio_path = tempfile.mktemp(suffix=".mp3")
    tts.save(audio_path)
    return audio_path

# Function to interact with the Ollama API
def llama_chat(audio_file, history=[]):
    # Convert audio to text
    user_message = audio_to_text(audio_file)
    if "Error" in user_message or "could not understand" in user_message:
        return history, None  # Skip showing error message directly

    # Append user message to conversation history
    history.append((user_message, None))  # Placeholder for assistant reply

    # Create the prompt with conversation history
    prompt = "You are a friendly conversational chatbot. You help user with any queries or question. Give short and appropriate answer to user needs no need for lengthy responses.\n\n"
    for user_msg, assistant_msg in history:
        prompt += f"User: {user_msg}\n"
        if assistant_msg:
            prompt += f"Assistant: {assistant_msg}\n"

    # Define payload for Ollama API
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 500,
        "top_p": 0.9
    }

    # Send request to Ollama API
    try:
        response = requests.post(
            OLLAMA_API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        if response.status_code == 200:
            response_data = response.json()
            assistant_reply = response_data.get("response", "No response available.")
            history[-1] = (user_message, assistant_reply)

            # Convert text response to audio
            audio_response = text_to_audio(assistant_reply)
            return history, audio_response
        else:
            error_message = f"Error: {response.status_code} - {response.text}"
            history[-1] = (user_message, error_message)
            return history, None

    except requests.exceptions.RequestException as e:
        error_message = f"Request failed: {str(e)}"
        history[-1] = (user_message, error_message)
        return history, None

# Gradio interface with Blocks
with gr.Blocks() as chat_interface:
    with gr.Row():
        with gr.Column():
            input_audio = gr.Audio(label="Speak to the Assistant", sources="microphone", type="filepath",recording=True)
            submit_button = gr.Button("Submit")
            clear_button = gr.Button("Clear")
            
        with gr.Column():
            chatbot = gr.Chatbot(label="Conversation")
            output_audio = gr.Audio(type="filepath", label="Assistant's Response (Audio)", autoplay=True)

    # Define actions for buttons
    submit_button.click(
        llama_chat,
        inputs=[input_audio, chatbot],
        outputs=[chatbot, output_audio]
    )

    # Clear button to reset conversation
    clear_button.click(lambda: ([], None), outputs=[chatbot, output_audio])

# Launch the interface
chat_interface.launch()
