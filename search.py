import os
from dotenv import load_dotenv
load_dotenv()

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

username = os.environ['ACTIVELOOP_USERNAME']

db = DeepLake(dataset_path=f"hub://{username}/how-to", embedding=OpenAIEmbeddings())

retriever = db.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 10

model = ChatOpenAI(model='gpt-4')

qa = ConversationalRetrievalChain.from_llm(model,retriever=retriever)

# questions = [
#     "What is DataMade's preferred deployment service?",
#     "What are the commands for modifying an encrypted file with blackbox?",
#     "Can you share an example of code where a map is made with react leaflet?",
#     "Show an example of using GeoJSON in a a map with react leaflet.",
# ]

questions = [
    'What should my dockerfile look like in my django app?'
]

chat_history = []

for question in questions:
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    print(f"-> **Question**: {question} \n")
    print(f"**Answer**: {result['answer']} \n")
