# Learning LangChain

A small collection of Python examples for learning LangChain with Google Gemini and Hugging Face models.

## Topics

- Basic LLM text generation
- Chat models
- Hugging Face inference endpoints
- Text embeddings
- Document similarity with cosine similarity

## Project Structure

```text
1-LLMs/
  1-llm-demo.py                 Basic Gemini text generation

2-Chat-Models/
  chatmodel_gemini.py           Gemini chat model
  chatmodel_huggface.py         Hugging Face chat model

3-Embedded-Models/
  embedding_huggface.py         Generate an embedding for text
  document_similarity.py        Find the most similar document

requirements.txt                Python dependencies
.env.example                    Environment variable template
```

## Setup

Create and activate a Python environment:

```powershell
conda create -n langenv python=3.12
conda activate langenv
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Create a local `.env` file and add your own API credentials:

```text
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_ACCESS_TOKEN=your_hugging_face_token
```

Never commit `.env` or expose API keys in source code. The repository ignores `.env` automatically.


The first Hugging Face embedding run may download the `sentence-transformers/all-MiniLM-L6-v2` model locally.

## Notes

- Google examples require a valid Google API key and an available Gemini model.
- The Hugging Face chat example requires a valid access token and a model supported by an enabled Hugging Face inference provider.
- Embedding examples use `sentence-transformers/all-MiniLM-L6-v2`.
