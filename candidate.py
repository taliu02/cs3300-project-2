from typing import Optional
import gdown
import os
from datetime import datetime  # Importing the datetime class directly

from mathpix import extract_text
class JobCandidate:
    def __init__(self, data: list):
        self.timestamp = datetime.strptime(data[0], "%m/%d/%Y %H:%M:%S")
        self.name = data[1]
        self.email = data[2]
        self.resume_link = data[3]
        self.resume_text= self.parse_resume()
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
        return (f"Job Candidate: {self.name}\n"
                f"Applied on: {self.timestamp}\n"
                f"Email: {self.email}\n"
                f"Resume {self.resume_text}\n"
                f"Personal Website: {self.personal_website}\n"
                f"Visa Sponsorship: {self.visa_sponsorship}\n"
                f"Disability Status: {self.disability_status}\n"
                f"Ethnic Background: {self.ethnic_background}\n"
                f"Gender: {self.gender}\n"
                f"Military Service: {self.military_service}")

    def parse_resume(self):
        id=self.resume_link.split('=')[-1]
        pdf_path=os.path.join(os.getcwd(),"resume_pdfs", (str(id)+'.pdf'))
        if os.path.join(os.getcwd(),"resume_mmds", (str(id)+'.pdf.mmd')):
            return open(os.path.join(os.getcwd(),"resume_mmds", (str(id)+'.pdf.mmd')),"r").read()
        else:
            gdown.download(id=id, quiet=True, use_cookies=False, output=pdf_path)
            return extract_text(pdf_path)

    
