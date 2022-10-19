from langchain.prompts import PromptTemplate
template = PromptTemplate(input_variables=['text'], template='Summarize: {text}')