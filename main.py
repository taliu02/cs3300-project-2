import gspread
import os
from candidate import JobCandidate
from dotenv import load_dotenv
from compator import bubble_sort
from results import writeToSheets
sa = gspread.service_account(filename='service_creds.json')
sh = sa.open("Figma_swe")

wks = sh.worksheet("Sheet1")
data = wks.get_all_values()
os.environ["COMPARATOR_LLM"]="chat-bison"

# Load environment variables from the .env file
load_dotenv()
# destination_path = os.path.join(os.getcwd(), id)
candidates=[]
for i in range(1, len(data)):
    candidates.append(JobCandidate(data[i]))


sort_cand = bubble_sort(candidates)
for candidate in sort_cand:
    print(candidate.name)

#in the future
writeToSheets(candidates)

    





