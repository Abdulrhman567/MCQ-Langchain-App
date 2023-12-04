from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field
from typing import List
import json
import os

# API_key (use whatever is your API key that you got after creating your OpenAI account)
API_KEY = os.environ.get("API_KEY_SEP")


class MultipleChoiceQuestions(BaseModel):
    question_num: int = Field(description="the number of the questoin")
    questions: str = Field(description="questions related to the topic chosen by the user")
    answers: List[str] = Field(description="answers of the question")
    correct_answer: str = Field(description="the correct answer of the question")


class Questions(BaseModel):
    questions: List[MultipleChoiceQuestions]


class LangchainModel:
    def __init__(self, user_text, questions_num) -> None:
    # Prompt Templates
        self.user_text = user_text
        self.questions_num = questions_num
        self.chat = ChatOpenAI(temperature=0, api_key=API_KEY)
    
    def generate_langchain_quiz(self):
        """
        This function uses the Integration between Langchain and OpenAI Completion API to generate number of questions and there answers by making a very specific template that gets passed to the OpenAI chat model to get the output as a message and parse it using the Pydentic (Json) parser to get the output in Json format and returns it.
        """
        self.prompt_template = ("""You are a quiz generator that are going to generate {number_of_questions} differant types of multi-choice quesions about {text} and give the correct answer out of each question. Format each question as:
        \n{format_instructions}\n
        """)
        
        parser = PydanticOutputParser(pydantic_object=Questions)

        # Prompts
        system_message_prompt = SystemMessagePromptTemplate.from_template(self.prompt_template, partial_variables={"format_instructions": parser.get_format_instructions()})
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

        output_response = self.chat(chat_prompt.format_prompt(number_of_questions=self.questions_num, text=self.user_text).to_messages())

        output_in_json = json.loads(output_response.content)
        return output_in_json
