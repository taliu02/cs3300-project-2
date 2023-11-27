import openai;
import json, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
from candidate import JobCandidate

def getContent(resumeA: str, resumeB: str) -> str:
    return (
        "Given the following two SWE candidates, choose between the two. Here is the rubric: "
        + get_rubric()
        + "Candidate A: "
        + "\nRESUME:\n" +resumeA+"\nEND Resume\n"
        + " END OF Candidate A"
        + "\n\nCandidate B: "
        + "\nRESUME:\n" +resumeB+"\nEND Resume\n"
        + " END OF Candidate B"
    )



def compare_resumes(content:str):
    choice =0
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": content}],
        functions=[
            {
                "name": "selectCanidate",
                "description": "choose between the two canidates",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "choice_num": {
                        "type": "integer",
                        "description": "1 for Candidate A is the best fit, 2 for Candidate B is the best fit",
                        "required": ["choice_num"],
                        },
                        "justifcation": {
                        "type": "string",
                        "description": "justifcation for why you chose the candidate",
                        "required": ["justifcation"],
                        },
                    }
                },
            }
        ],
        function_call="auto",

    )

    message = response["choices"][0]["message"]

    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])
        if function_name == "selectCanidate":
            choice = (int(function_args["choice_num"]))
            print(function_args["justifcation"])
            
    return choice
    

def get_rubric():
    text = open("rubric.txt","r").read()
    return "\nRubric:\n" +str(text)+"\nEND Rubric\n"





def comp(candidateA:JobCandidate, candidateB:JobCandidate, rub_id:int=0 ) -> int:
    comp_table= json.load(open("comparisons.json","r"))
    tag= (candidateA.email+"#"+candidateB.email+"#"+str(rub_id))
    inv_tag= (candidateB.email+"#"+candidateA.email+"#"+str(rub_id))

    else:
        choice = compare_resumes(getContent(candidateA, candidateB), candidateA.name, candidateB.name)   
        comp_table[tag]=choice
        comp_table[inv_tag]=choice*-1

        json.dump(comp_table, open("comparisons.json","w"))
        return choice

def bubble_sort(candidates: list) -> list:
    n = len(candidates)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if comp(candidates[j], candidates[j+1]) > 0:
                candidates[j], candidates[j+1] = candidates[j+1], candidates[j]
                swapped = True
        if not swapped:
            break
    return candidates

