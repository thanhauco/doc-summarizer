import openai
def get_completion(prompt):
    return openai.Completion.create(engine='text-davinci-002', prompt=prompt)