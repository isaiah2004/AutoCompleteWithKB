# region import
from langchain_openai import ChatOpenAI

# from langchain_community import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

import os
import dotenv

# endregion

"""
A simple library for generating the next sentence in a document using LangChain and OpenAI.
"""
# Load environment variables from .env file
dotenv.load_dotenv()


def initialize_chat_template():
    """
    Initializes and returns a ChatPromptTemplate configured for autocompletion.

    Returns:
        ChatPromptTemplate: A configured chat prompt template.
    """
    template = [
        ("system", "You are a helpful AI bot. You do AutoComplete"),
        (
            "human",
            """
            You are an autocompletion model that is helping me write.
            This is the current document. {document}
            Please write the next sentence.
            Return the remaining sentence and the next sentence only. Return in plain text no decorators.
        """,
        ),
    ]
    return ChatPromptTemplate.from_messages(template)


def get_next_sentence(document, api_key=None):
    """
    Generates the next sentence based on the provided document using LangChain and OpenAI.

    Args:
        document (str): The document to generate the next sentence for.
        api_key (str): The OpenAI API key. If None, attempts to read from environment variable.

    Returns:
        str: The generated next sentence.
    """
    if api_key is None:
        try:
            api_key = os.environ.get("OPENAI_API_KEY")
        except:
            raise ValueError("OpenAI API key not provided or found in environment variables.")

    model = ChatOpenAI(api_key=api_key)
    chat_template = initialize_chat_template()
    chat_template_chain = chat_template | model
    response = chat_template_chain.invoke({"document": document})
    return response.content


if __name__ == "__main__":
    # Example usage
    document = "In a Land of Myth, and a Time of Magic, the destiny of a great Kingdom rests on the shoulders"
    print(f"Document:   {document}")
    print(f"Completion: {get_next_sentence(document)}")
