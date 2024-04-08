import os

from langchain.document_loaders import TextLoader


root_dir = './how-to'

docs = []

for dirpath, dirnames, filenames in os.walk(root_dir):

    for file in filenames:

        try:

            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')

            docs.extend(loader.load_and_split())

        except Exception as e:

            pass
