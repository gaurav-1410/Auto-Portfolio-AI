import os
import pdfplumber
import requests
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
api_key = os.getenv("OPENROUTER_API_KEY")
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global to store extracted skills, text and job_desc
extracted_skills = ""
text = ""
job_desc = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global extracted_skills, text, job_desc
    response_text = ""
    suggested_projects = ""

    if request.method == 'POST':
        # If resume is uploaded
        if 'pdf_file' in request.files:
            uploaded_file = request.files['pdf_file']
            if uploaded_file and uploaded_file.filename.endswith('.pdf'):
                filename = secure_filename(uploaded_file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                uploaded_file.save(filepath)

                # Extract text from PDF using pdfplumber
                with pdfplumber.open(filepath) as pdf:
                    text = "".join([page.extract_text() or "" for page in pdf.pages])[:3000]

                # Build prompt to extract skills
                prompt = f"""
                    You are a highly intelligent AI assistant specialized in analyzing resumes and identifying professional capabilities.

                    Below is the full content of a candidate's resume:

                    {text}

                    Your task is to extract and list **only the skills** demonstrated in this resume. These skills may be mentioned across different sections such as:

                    - Work Experience
                    - Projects
                    - Education
                    - Certifications
                    - Technical Skills
                    - Tools and Technologies
                    - Extra-Curricular or Volunteering

                    👉 Provide a **clean, categorized bullet list** of the skills. Include both:
                    - **Technical skills** (e.g., programming languages, tools, software, technologies, frameworks)
                    - **Soft skills** (e.g., communication, problem-solving, leadership, adaptability)

                    Be concise, avoid repetition, and ensure all relevant skills are captured clearly.
                """

                response = query_openrouter(prompt)
                extracted_skills = response
                response_text = f"✅ Skills extracted successfully! Paste the job description below to compare."

        # If job description is submitted
        elif 'job_description' in request.form:
            job_desc = request.form['job_description']

            # Build prompt for skill gap & project suggestion
            prompt = f"""
            Resume Skills:
            {extracted_skills}

            Job Description:
            {job_desc}

            Based on the job description and skills, suggest:
            1. Additional skills the candidate should learn
            2. 2-3 project ideas to showcase those skills
            Please be concise and clear.
            """

            response_text = query_openrouter(prompt)

        # Generate Cover Letter
        elif 'generate_cover_letter' in request.form:
            response_text = write_cover_letter(text, job_desc)

    return render_template("index.html", skills=extracted_skills, response=response_text)

def write_cover_letter(text, job_desc):

    prompt = f"""
        You are an intelligent AI assistant specializing in resume analysis and professional writing.

        Below is the candidate’s resume:
        {text}

        Here is the job description:
        {job_desc}

        Write a concise and personalized **Cover Letter** using this structure:

        - **Greeting**: Use the recipient’s name if available; avoid "To whom it may concern" unless necessary.  
        - **Intro Paragraph**: Briefly introduce the candidate, mentioning education or professional experience.  
        - **Strong Opening**: Start with an engaging line to hook the reader.  
        - **Why Them**: Show genuine interest in the company and what excites the candidate about the role.  
        - **Why You**: Highlight the candidate's most relevant skill or achievement.  
        - **Fit & Personality**: Convey how the candidate thinks, works, and connects with others.  
        - **Call to Action**: Close with a polite, proactive note.  

        👉 Return only the **final cover letter**. Keep the tone professional yet natural.
    """
    
    response = query_openrouter(prompt)
    return response

def query_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error {response.status_code}: {response.text}"

if __name__ == '__main__':
    app.run(debug=True)


"""**E-commerce Analysis**: Use Streamlit to create a web-based dashboard to analyze sales 
data from a fictional e-commerce company. Apply linear regression and 
logistic regression to predict customer purchase behavior and recommend products. Use My SQL to store and query the data."""