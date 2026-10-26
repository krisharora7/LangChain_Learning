# LangChain Learning

A hands-on collection of Python examples covering LangChain, from its core building blocks to RAG pipelines, tool calling, and AI agents.

[**Explore the repository →**](https://github.com/krisharora7/LangChain_Learning)

---

## Why I built this

When I started learning LangChain, one of the biggest problems I faced was outdated tutorials. The syntax shown in a tutorial would often differ from the current API, and I had to jump between documentation, web searches, and LLMs just to get an example working.

It slowed down the learning process more than it should have.

So, I decided to organize my learnings into a single repository that I could use as a reference later. Each topic has its own folder, with practical code examples designed to make the concepts easier to understand and apply.

## What's inside?

The repository is organized by topic, so you can jump directly to the concept you're interested in.

### 1. LangChain fundamentals

| Topic                                                                                              | What you'll explore                                                    |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Models](https://github.com/krisharora7/LangChain_Learning/tree/main/models)                       | Working with LLMs and chat models                                      |
| [Prompts](https://github.com/krisharora7/LangChain_Learning/tree/main/prompts)                     | Prompt templates and structuring model inputs                          |
| [Structured Output](https://github.com/krisharora7/LangChain_Learning/tree/main/structured_output) | Getting predictable, structured responses from models                  |
| [Output Parsers](https://github.com/krisharora7/LangChain_Learning/tree/main/OuptutParsers)        | Parsing model responses into usable formats                            |
| [Chains](https://github.com/krisharora7/LangChain_Learning/tree/main/Chains)                       | Connecting components into workflows                                   |
| [Runnables](https://github.com/krisharora7/LangChain_Learning/tree/main/Runnables)                 | Composing and executing workflows using LangChain's Runnable interface |

### 2. Building RAG systems

Retrieval-Augmented Generation (RAG) lets an application retrieve relevant information from external documents or data sources and provide it to a language model as context.

These folders cover the building blocks involved in that process.

| Topic                                                                                            | What you'll explore                          |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| [Document Loaders](https://github.com/krisharora7/LangChain_Learning/tree/main/document_loaders) | Loading documents into LangChain             |
| [Text Splitters](https://github.com/krisharora7/LangChain_Learning/tree/main/text_splitters)     | Breaking documents into manageable chunks    |
| [Vector Stores](https://github.com/krisharora7/LangChain_Learning/tree/main/vector_store)        | Storing and searching vector representations |
| [Retrievers](https://github.com/krisharora7/LangChain_Learning/tree/main/retrievers)             | Retrieving relevant information for a query  |

### 3. Tools and AI agents

Once the fundamentals are clear, the next step is building systems that can interact with tools and perform tasks beyond generating text.

| Topic                                                                                    | What you'll explore                                          |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| [Tools](https://github.com/krisharora7/LangChain_Learning/tree/main/tools)               | Defining tools that an LLM-powered application can use       |
| [Tool Calling](https://github.com/krisharora7/LangChain_Learning/tree/main/tool_calling) | Letting models select and invoke tools                       |
| [Agents](https://github.com/krisharora7/LangChain_Learning/tree/main/agents)             | Building workflows where models decide which actions to take |

### 4. Running models locally

[**Ollama example →**](https://github.com/krisharora7/LangChain_Learning/blob/main/OLLAMA.py)

The repository also includes an example of using Ollama through LangChain to work with locally hosted language models, chat models, and embeddings.

---

## Getting started

### Prerequisites

- Python installed on your system
- Git
- API credentials for the examples that use hosted model providers
- [Ollama](https://ollama.com/) installed and a model downloaded if you want to run the local-model example

### 1. Clone the repository

```bash
git clone https://github.com/krisharora7/LangChain_Learning.git
cd LangChain_Learning
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your credentials

Some examples require provider-specific API keys. Set the appropriate environment variables for the model provider used in the example.

If you use a `.env` file, load it in your Python script with `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

Keep API keys and other secrets out of Git. Never commit your actual `.env` file.

### 5. Run an example

Navigate to the relevant topic folder and run the Python file you want to explore:

```bash
python path/to/example.py
```

Replace the path with the actual file you want to execute.

**Note:** Each example may have its own model, API key, local service, or input-data requirements. Check the code before running it.

---

## Tech stack

- **Python** — language used for the examples
- **LangChain** — building LLM-powered applications and workflows
- **LangGraph** — included in the project dependencies for exploring the broader ecosystem
- **Ollama** — running models locally
- **Model integrations** — OpenAI, Anthropic, Google Gemini, Groq, and Hugging Face

See [`requirements.txt`](https://github.com/krisharora7/LangChain_Learning/blob/main/requirements.txt) for the complete dependency list.

## How to use this repository

You don't need to go through every folder in one sitting.

- **Just starting with LangChain?** Begin with Models and Prompts, then move to Structured Output, Output Parsers, Chains, and Runnables.
- **Interested in RAG?** Explore Document Loaders, Text Splitters, Vector Stores, and Retrievers.
- **Want to build AI agents?** Start with Tools, continue with Tool Calling, and then explore Agents.
- **Want to experiment with local models?** Check out `OLLAMA.py`.

The idea is to understand a concept, run its example, modify it, and see how the behavior changes.

## A note on syntax

LangChain evolves quickly, and APIs can change between releases. These examples reflect the syntax used while building the repository, but individual examples may need adjustments as dependencies evolve.

If you find something outdated or have a better implementation, feel free to open an issue or contribute.

## Feedback and contributions

If this repository helps you learn something, feel free to star it. Suggestions, corrections, and improvements are welcome.

**Repository:** [krisharora7/LangChain_Learning](https://github.com/krisharora7/LangChain_Learning)

---

*Built while learning, organized for future reference.*
