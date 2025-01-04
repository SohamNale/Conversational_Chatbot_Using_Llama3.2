# Conversational Chatbot using Ollama Llama 3.2

This project implements a conversational chatbot using the Ollama Llama 3.2 model, which runs locally on your system. The interface of the bot is created using Gradio, allowing users to interact with the chatbot through audio input and receive audio responses.

## Features

- Converts audio input to text using Google Speech Recognition.
- Interacts with the Ollama Llama 3.2 API to generate responses based on the conversation history.
- Converts text responses to audio using Google Text-to-Speech (gTTS).
- Provides a user-friendly interface with Gradio for seamless interaction.

## Requirements

- Python 3.6+
- `requests`
- `gradio`
- `speech_recognition`
- `gtts`
- `tempfile`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SohamNale/Conversational_Chatbot_Using_Llama3.2.git
    cd Conversational_Chatbot_Using_Llama3.2
    ```

2. Install the required packages:
    ```sh
    pip install requests gradio speechrecognition gtts
    ```

## Usage

1. Ensure that the Ollama Llama 3.2 API is running locally on your system at `http://localhost:11434`.

2. Run the chatbot:
    ```sh
    python conversational_chat_bot.py
    ```

3. Open the Gradio interface in your web browser. You can speak to the assistant using your microphone and receive audio responses.

## File Structure

- [conversational_chat_bot.py](http://_vscodecontentref_/0): Main script for the chatbot, including functions for audio-to-text, text-to-audio, and interaction with the Ollama API.

## Functions

### [audio_to_text(audio_file)](http://_vscodecontentref_/4)

Converts audio input to text using Google Speech Recognition.

### [text_to_audio(text)](http://_vscodecontentref_/5)

Converts text to audio using Google Text-to-Speech (gTTS).

### [llama_chat(audio_file, history=[])](http://_vscodecontentref_/6)

Interacts with the Ollama API to generate responses based on the conversation history.

## Gradio Interface

The Gradio interface consists of:

- An audio input component for recording user queries.
- A submit button to send the query to the chatbot.
- A clear button to reset the conversation.
- A chatbot component to display the conversation history.
- An audio output component to play the assistant's response.

## Acknowledgements

- [Gradio](https://gradio.app/)
- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)
- [Ollama Llama](https://ollama.com/)
