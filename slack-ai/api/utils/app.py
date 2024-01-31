from dotenv import load_dotenv
from embedchain import App
from embedchain.models.data_type import DataType
from embedchain.chunkers.base_chunker import BaseChunker

from .slack_chunker import SlackChunker
from .slack_loader import SlackLoader

load_dotenv(".env")

loader = SlackLoader()
chunker = SlackChunker()
chunker.set_data_type(DataType.SLACK)

# Uncomment this line if you want to use HuggingFace LLMs
# app_config = {
#     "app": {
#         "config": {
#             "name": "slack-ai"
#         }
#     },
#     "llm": {
#         "provider": "huggingface",
#         "config": {
#             "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
#             "temperature": 0.1,
#             "max_tokens": 250,
#             "top_p": 0.1
#         }
#     },
#     "embedder": {
#         "provider": "huggingface",
#         "config": {
#             "model": "sentence-transformers/all-mpnet-base-v2"
#         }
#     }
# }

app_config = {
    "app": {
        "config": {
            "id": "slack-ai-app",
            "log_level": "DEBUG"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-3.5-turbo",
        },
    },
    # "vectordb": {
    #     "provider": "chroma",
    #     "config": {
    #         "dir": "db",
    #         "allow_reset": "true"
    #     }
    # },
    # "embedder": {
    #     "provider": "openai",
    #     "config": {
    #         "model": "text-embedding-3-small"
    #     }
    # }
}


ec_app = App.from_config(config=app_config)
