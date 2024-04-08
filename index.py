import os

from dotenv import load_dotenv

load_dotenv()



from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter



embeddings = OpenAIEmbeddings()


root_dir = './how-to'

docs = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())

        except Exception as e:
            pass

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

texts = text_splitter.split_documents(docs)

username = os.environ['ACTIVELOOP_USERNAME']

db = DeepLake(dataset_path=f"hub://{username}/how-to", embedding_function=embeddings)

db.add_documents(texts)
