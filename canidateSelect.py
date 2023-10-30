import openai
import json, os
openai.api_key = os.environ.get("OPENAI_API_KEY")

def getContent():
    return "Given the following two SWE canidates,choose between the two, here is the rubic"+get_rubric()+"Canidate A:"+getResume("resumeA.txt")+"END OF Canidate A"+"\n\nCanidate B:"+getResume("resumeB.txt")+"END OF Canidate B"



def run_conversation():
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": getContent()}],
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
        max_new_tokens=30,
    )

    message = response["choices"][0]["message"]

    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])
        if function_name == "selectCanidate":
            selectCanidate(int(function_args["score_num"]),str(function_args["justifcation"]))
    

    
def selectCanidate(score_num, justifcation):
    print("score_num: ", score_num)
    print("justifcation: ", justifcation)
    if score_num == 1:
        printc("Candidate A is the best fit", "cyan")
    elif score_num == 2:
        printc("Candidate B is the best fit", "magenta")
    
    
    

def getResume(name): 
    text = open(name,"r").read()
    
    return "\nRESUME:\n" +str(text)+"\nEND Resume\n"

def jobPosting(): 
    text = open("posting.txt","r").read()
    return "\nPOSTING:\n" +str(text)+"\nEND POSTING\n"

def get_rubric():
    # text = open("rubric.txt","r").read()
    # return "\nRubric:\n" +str(text)+"\nEND Rubric\n"
    return """
    Educational Background
    Institution
    - **Top Tier** (e.g., MIT, Stanford, Harvard, etc.)
    - **Second Tier**
    - **Other Institutions**

    Degree
    - PhD in Computer Science or related field
    - Master's in Computer Science or related field
    - Bachelor's in Computer Science or related field
    - Other degrees or no formal degree

    GPA (if provided)
    - **4.0 - 3.7**: Outstanding
    - **3.6 - 3.3**: Above Average
    - **3.2 - 2.9**: Average
    - **Below 2.9**: Below Average

    Work Experience and Years of Experience
    - **5+ years**: Senior
    - **3-5 years**: Mid-Level
    - **1-3 years**: Junior
    - **<1 year**: Entry Level

    Relevance of Experience
    - Directly related to the role
    - Partially related
    - Unrelated

    Companies Worked At
    - **Top Tech Companies** (e.g., Google, Apple, Facebook, etc.)
    - **Start-ups**
    - **Non-tech Corporates**
    - **Others**

    Projects
    Complexity and Scale
    - Large-scale projects with significant impact
    - Mid-sized projects
    - Small projects or class assignments

    Relevance to Position
    - Directly related to the role
    - Partially related
    - Unrelated

    Technical Skills and Programming Languages
    - List of languages known (e.g., Python, Java, C++, etc.)

    Frameworks and Technologies
    - List of relevant frameworks/technologies 

    Open-source, research, projects
    - Personal projects, contributions to open source, publications, etc.
    
    
    """

def printc(obj, color="cyan"):
    color_code = {
        "black": "30", "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36", "white": "37"
    }
    colored_text = f"\033[{color_code[color]}m{obj}\033[0m" if color in color_code else obj
    print(colored_text)
    








if __name__ == "__main__":

    run_conversation()