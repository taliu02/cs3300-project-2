from typing import Optional
import gdown
import os,datetime
from mathpix import extract_text
class JobCandidate:
    def __init__(self, data: list):
        self.timestamp = datetime.strptime(data[0], "%m/%d/%Y %H:%M:%S")
        self.name = data[1]
        self.email = data[2]
        self.resume_link = data[3]
        self.resume_text=""
        self.cover_letter = data[4]
        self.linkedin = data[5]
        self.github = data[6]
        self.personal_website = data[7]
        self.visa_sponsorship = data[8]
        self.disability_status = data[9]
        self.ethnic_background = data[10]
        self.gender = data[11]
        self.military_service = data[12]

    def __str__(self):
        return f"Job Candidate: {self.name}"

    def parse_resume(self) -> bool:
        id=self.resume_link.split('=')[-1]
        pdf_path=os.path.join(os.getcwd(),"resume_pdfs", (str(id)+'.pdf'))
        gdown.download(id=id, quiet=True, use_cookies=False, output=pdf_path)
        self.resume_text=extract_text((str(id)+'.pdf'))
        return True
    
    
    
    def __lt__(self, other):
        if not isinstance(other, JobCandidate):
            return NotImplemented
        return self.timestamp < other.timestamp

    def __eq__(self, other):
        return False