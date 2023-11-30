import openai
import json, os,sys
from dotenv import load_dotenv
load_dotenv()
from litellm import completion
from mathpix import extract_text
import gradio
def printc(obj, color="cyan"):
    color_code = {
        "black": "30", "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36", "white": "37"
    }
    colored_text = f"\033[{color_code[color]}m{obj}\033[0m" if color in color_code else obj
    print(colored_text)

def get_prompt(candidate, chat_history, question):
    return ('Given the details of a candidate, the previous chat history, and a question, answer the question as if you are the candidate. Keep the answers short and to the point.\n'
    +"I want you to be honest, if asked if you know something only answer from the candidates perspective"
    + 'Candidate Details:\n\n' + str(candidate) + '\nEnd Candidate Details\n'
    + 'Chat History:\n\n' + chat_history + '\nEnd Chat History\n'
    + 'Question:\n\n' + question + '\nEnd Question\n')

def chat_with_candidate(candidate, model = os.environ.get('CHAT_LLM', 'gpt-4')):
    chat_history = ''
    print('You are now chatting with ' + candidate.name +" using "+model+ ' \nType in your question or type QUIT to stop.')

    while True:
        print('User:')
        question = input()
        print()
        if question.strip().upper() == 'QUIT':
            break
        prompt = get_prompt(candidate, chat_history, question)
        messages = [{ 'content': prompt, 'role': 'user'}]
        response = completion(model = model, messages = messages)['choices'][0]['message']['content']
        printc(('Response:\n' + response + '\n'),"green")
        chat_history += 'User:\n' + question + '\nResponse:\n' + response