from core.pdfExtract import pdfMine
from core.skills import exSkills
from core.edu import exEdu
from core.emailE import exEmail
from core.phone import exPhone
import pandas as pd
from core.name import exName
import sys 

df = pd.read_csv('Book.csv')
edu_main = df['education'].tolist()
skill_main = df['skills'].tolist()
main_edu =["BTech","BSc","BEngg"]
resume_text = pdfMine("./resumes/resume1.pdf")
email = exEmail(resume_text)
phone = exPhone(resume_text)
name = exName(resume_text)
skills = exSkills(resume_text)
edu = exEdu(resume_text)

x = {
    # "education":edu,
    "skills":skills,
    "name":name,
    "email":email,
    "phone":phone,
    "education":edu,
}
flagEdu =False
flagSkill = False
if(any(x[0] in edu_main for x in edu)):
	flagEdu = True
if(all(x in skills for x in skill_main)):
	flagSkill = True
if(all([flagEdu,flagSkill])):
	print("Selected")
else:
	print("Not Selected")

print(x)
