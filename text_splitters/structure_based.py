from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)
text = '''My name is Nitish
I am 35 years old

I live in gurgaon
how are you'''
result = splitter.split_text(text)
print(result)