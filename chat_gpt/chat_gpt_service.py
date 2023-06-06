import os
import openai
from chat_gpt.chat_gpt_model import MessageRequestDTO


# openai.organization = os.getenv('ORGANIZATION_ID')
# openai.api_key = os.getenv('OPENAI_API_KEY')

openai.organization = "org-UNpHbA1sru4gIudRB5W1moxH"
openai.api_key = "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"


class ChatGptService:

    @classmethod
    def get_ai_model_answer(cls,data:MessageRequestDTO):
        return openai.Completion.create(
            prompt=data.question,
            model=data.model_id,
            temperature=data.temperature,
            max_tokens=data.max_tokens
        )

    @classmethod
    def list_models(cls):
        return openai.Model.list()
