
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Resume(BaseModel):
    name: str
    education: str
    experience: str
    skills: str
    projects: str

class JDRequest(BaseModel):
    job_description: str
    resume: Resume

@app.post("/generate")
async def generate_cover_letter(data: JDRequest):
    prompt = f"""
You are an AI assistant helping to write cover letters. Based on the following job description and resume, generate a professional, personalized cover letter:

Job Description:
{data.job_description}

Resume:
Name: {data.resume.name}
Education: {data.resume.education}
Experience: {data.resume.experience}
Skills: {data.resume.skills}
Projects: {data.resume.projects}

Cover Letter:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional career assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return {"cover_letter": response['choices'][0]['message']['content']}
