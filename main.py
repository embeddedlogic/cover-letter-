from openai import OpenAI
client = OpenAI()

# Questions to get information for the cover letter
name = input("What's your first and last name? ").title()
job = input("What is the desired job title? ").title()
company = input("What company are you applying to? ").title()
skills = input("Please name all your skills (separate with commas): ").title()
motivation = input("Why do you want this job? ").title()
years_of_experience = input("How many years of experience do you have in this field? ")
degree = input("What degree or education do you have? ").title()
achievements = input("What are your top achievements? (separate with commas): ").title()
location = input("Where are you located? (City, Country): ").title()

# Prompt for the AI
cover_letter_prompt = f"""
Write a professional cover letter based on all the information given. Also make sure to tailor the letter to the compant and the job position. The word count should be between 300 and 400 words

Applicant Name: {name}
Job Title: {job}
Company: {company}
Skills: {skills}
Motivation: {motivation}
Years of Experience: {years_of_experience}
Degree/Education: {degree}
Achievements: {achievements}
Location: {location}

Make the cover letter professional, clear, and tailored to the company.
"""

# Send request to OpenAI
response = client.responses.create(
    model="gpt-4.1-mini",
    input=cover_letter_prompt
)

cover_letter = response.output_text
#Here we print the generated cover letter and also save it to a file named "cover_letter.txt"
print("\nGenerated Cover Letter:\n")
print(cover_letter)


with open("cover_letter.txt", "w") as file:
    file.write(cover_letter)

print("\nCover letter saved as cover_letter.txt")