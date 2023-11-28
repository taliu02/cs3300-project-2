import openai;
import json, os,sys
from dotenv import load_dotenv
load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
import openai; openai.api_key = "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"
from Candidate import JobCandidate


import litellm
from litellm import completion


import xml.etree.ElementTree as ET







def printc(obj, color="cyan"):
    color_code = {
        "black": "30", "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36", "white": "37"
    }
    colored_text = f"\033[{color_code[color]}m{obj}\033[0m" if color in color_code else obj
    print(colored_text)



LLM=os.environ.get("COMPARATOR_LLM","chat-bison")
# LLM=os.environ.get("COMPARATOR_LLM","gpt-3.5-turbo-1106")
def getContent(candidateA, candidateB) -> str:
    return (
        "Given the following two candidates, choose between the two. Here is the rubric: "
        + get_rubric()
        + "Candidate A: "
        + "\nRESUME:\n" +candidateA.resume_text+"\nEND Resume\n"
        + "\nGITHUB:\n" +candidateA.github_text+"\nEND GITHUB\n"
        + " END OF Candidate A"
        + "\n\nCandidate B: "
        + "\nRESUME:\n" +candidateB.resume_text+"\nEND Resume\n"
        + "\nGITHUB:\n" +candidateB.github_text+"\nEND GITHUB\n"
        + " END OF Candidate B"

    )