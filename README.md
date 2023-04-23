<p align="center">
  <img src="https://i.imgur.com/hm20RaC.png" width="154">
  <h1 align="center">Python Resume Parser</h1>
  
  <p align="center"> This project is designed to assist in the <b>analysis</b> of resumes by automatically extracting relevant information, including job titles, responsibilities, dates of employment, and skills listed by the candidate.
<p>



</p>

## Class Documentation: ResumeParser

The ResumeParser class is a Python class that can parse a resume and extract information such as job titles, job history, and skills. The class requires either a filename or text input to initiate, and it will raise a ValueError if both inputs are missing.


## Class methods: 
`__init__(self, filename=None, text='', initialiseModel = True) -> None`: Initializes the class object with the input filename or text. It will raise an error if both inputs are missing.

```Python
sample = ResumeParser('resume.pdf') # Or ResumeParser('cv text goes here')
```

### get_role_titles:

`get_role_titles(self) -> list`: This method gets the role titles that the resume contains. It will load a JSON file of job titles and will match the job titles in the input text. It will return a list of matched job titles.

```Python
sample.get_role_titles() # [Software Engineer, Project Manager]
```
### get_role_history:

`get_role_history(self, skills = False) -> list`: This method will get the job history and the job descriptions in the resume. It will use the get_role_titles() method to find the job titles and then extract the job descriptions in between those job titles. It will return a list of dictionaries containing the `title`, `description`, `skills`, `start_date`, `end_date`, and `worked_period`.

```Python
sample = ResumeParser('resume.pdf')
sample.get_role_history()
# Output
# [
#   {
#     "title": "full stack developer",
#     "description": [
#       "feb 2022 - present • provided crucial support to a junior developer struggling with a complex project, offering guidance and troubleshooting assistance to help them overcome technical obstacles and achieve their objectives",
#       " • directed the successful development and launch of an exciting project, overseeing the entire development lifecycle from initial design to user feedback analysis",
#       " • led a team-wide effort to improve development processes, identifying areas for improvement and implementing new tools and methodologies to streamline workflows and improve project outcomes",
#       " • designed and developed a data dashboard panel in django that displayed key information to users, resulting in a 20% increase in user engagement",
#       " • developed a highly efficient backend using the django python framework, leveraging crud operations and advanced techniques to optimize performance and streamline development processes",
#       " • built a user settings page and email authentication system that improved user experience and boosted sign-ups by 25%",
#       " • refactored code with an emphasis on reusability, object orientation and reducing load on the database server, leading to a 15% improvement in website speed and performance",
#       " • successfully collaborated with a team of developers and designers to build and deploy multiple web applications on the django framework, resulting in a 40% increase in user acquisition and retention",
#       " • demonstrated expertise in django frameworks, using rest api, postgressql databases, as well as html, css, and javascript to develop visually appealing and user-friendly web pages",
#       " weprepfba remote zoho -"
#     ],
#     "skills": [
#       "support",
#       "server",
#       "html",
#       "javascript",
#       "django",
#       "design",
#       "database",
#       "python",
#       "databases",
#       "css",
#       "authentication",
#       "api",
#       "framework"
#     ],
#     "start_date": "None",
#     "end_date": "None",
#     "Worked Period": "None"
#   },
#]
```
### get_date:

`get_date(self, text="")` -> list: This method will get the date of a string and return the lowest and highest and the priod between as a datetime object .
```python
sample.get_date() # [May 2021, May 2022, 365]
```

### get_extract_skills:

`get_extract_skills(self, text = None) -> list`: This method will get the skills within the extracted resume. It will load a JSON file of skills and will match the skills in the input text. It will return a list of matched skills.
```python
sample.get_extract_skills() # ["Django", "Java", "React"] 
```

### _get_between_text:

`_get_between_text(self, text, list) -> list`: This private method gets the text in between the resume description. It will use the input list to find the starting and ending words of the job descriptions, then it will extract the text between those words.

```python
sample._get_between_text() 
# Output
# "feb 2022 - present • provided crucial support to a junior developer struggling with a complex project, offering guidance and troubleshooting assistance to help them overcome technical obstacles and achieve their objectives
# • directed the successful development and launch of an exciting project, overseeing the entire development lifecycle from initial design to user feedback analysis,
# • led a team-wide effort to improve development processes, identifying areas for improvement and implementing new tools and methodologies to streamline workflows and improve project outcomes,
# • designed and developed a data dashboard panel in django that displayed key information to users, resulting in a 20% increase in user engagement,
# • developed a highly efficient backend using the django python framework, leveraging crud operations and advanced techniques to optimize performance and streamline development processes,
# • built a user settings page and email authentication system that improved user experience and boosted sign-ups by 25%,
# • refactored code with an emphasis on reusability, object orientation and reducing load on the database server, leading to a 15% improvement in website speed and performance,
# • successfully collaborated with a team of developers and designers to build and deploy multiple web applications on the django framework, resulting in a 40% increase in user acquisition and retention,
# • demonstrated expertise in django frameworks, using rest api, postgressql databases, as well as html, css, and javascript to develop visually appealing and user-friendly web pages
# weprepfba remote zoho -"
```

### Note:

`The get_date(`) method has been commented out and not implemented.
The input skills in the `get_role_history()` method is not used in the method.
The `get_extract_skills()` method has a logical error where the text input is not assigned if provided as a parameter. It needs to be updated to text = text if text else self.source to fix this error.
The` _get_between_text()` method should be updated to not take in a list as an argument but rather a single job title.

