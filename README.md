# Docs Bot
This bot is a proof of concept bot that lets a user asks questions about DataMade how-to docs in natural language. It indexes DataMade how-to documentation in a Deep Lake vector database, retrieves similar documents based on the user's search query, and submits the related documents and questions to OpenAI's GPT4 API for a final answer.

It's based directly on [this tutorial](https://www.activeloop.ai/resources/lang-chain-gpt-4-for-code-understanding-twitter-algorithm/).

## Usage
Download requirements:
```
pip install -r requirements.txt
```

Add your config to the `.env` file.

Run the pipeline:
```
make all
```

You can change the questions in `chat.py`.
