import pathlib
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def load_split_pdf(file_path: pathlib.Path | str):
    with open(file_path) as f:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    return texts


if __name__ == "__main__":
    load_split_pdf("backend/pdfdata/paper.pdf")
