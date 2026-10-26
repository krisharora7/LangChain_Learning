from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
text = '''# Python

Python is a popular programming language.

## Variables

Variables are used to store data.

## Functions

Functions are reusable blocks of code.

# Machine Learning

Machine learning allows computers to learn from data.

## Supervised Learning

Supervised learning uses labeled data.

## Unsupervised Learning

Unsupervised learning uses unlabeled data.'''
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0
)
result = splitter.split_text(text)
print(len(result))
print(result)