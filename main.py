from core.pdfExtract import pdfMine
from core.skills import exSkills
from core.edu import exEdu
from core.emailE import exEmail
from core.phone import exPhone

from core.name import exName
import sys 




resume_text = pdfMine("./resumes/resume1.pdf")
email = exEmail(resume_text)
phone = exPhone(resume_text)
name = exName(resume_text)
skills = exSkills(resume_text)
# edu = exEdu(resume_text)

x = {
    # "education":edu,
    "skills":skills,
    "name":name,
    "email":email,
    "phone":phone,

}

print(x)



