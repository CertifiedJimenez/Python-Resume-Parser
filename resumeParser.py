from dateutil import parser
from datetime import datetime
import json
import re

class ResumeParser:

    def __init__(self, filename=None, text='', initialiseModel = True) -> None:
        if not filename and not text:
            raise ValueError("Please provide either a filename or a text")
        elif filename:
            self.source = ''
        elif text:
            self.source = text

    def get_role_titles(self) -> list:
        """
        This will get the role title that resume 
        contains.
        """
        with open('./data/job-titles.json') as f:
            self.data = json.load(f)
        title_list = self.data['job-titles']
        matched = []
        text = self.source.lower()

        escaped_title_list = '|'.join(map(re.escape, title_list))
        pattern = re.compile(r'\b({})\b'.format(escaped_title_list), re.IGNORECASE)
        matched = [match.group(0) for match in pattern.finditer(text) if len(match.group(0).split(' ')) > 1]

        return matched


    def get_role_history(self, skills = False) -> list:
        """
        This will get the role followed by the responsability 
        in the resume.
        """
        title = self.get_role_titles()
        history = self._get_between_text(self.source, title)
        output = [{'title': title[index], 'description': list(history[index].split('.')), 
                   'skills': self.get_extract_skills(history[index]), 
                   'start_date': self.get_date(history[index])[0],
                   'end_date': self.get_date(history[index])[1],
                   'Worked Period': self.get_date(history[index])[3],
                   } for index in range(len(title)-1)]
        return output
        
    def get_date(self, text="") -> list:
        """
        Get the date of a string and return the lowest and highest 
        as datetime object.
        """  

        # # Use regular expression to find all dates in the text
        # date_list = re.findall(r'\b\w{3}\s*\d{4}\b', text)

        # # If only one date is found, return it
        # if len(date_list) == 1:
        #     return parser.parse(date_list[0]).strftime("%d/%m/%Y")

        # # Parse all dates and return the earliest and latest dates
        # dates = [parser.parse(date).date() for date in date_list]
        # earliest_date = min(dates) if date_list else None
        # latest_date = max(dates) if date_list else None
        # worked_period = latest_date - earliest_date if earliest_date and latest_date else None

        # print(dates)


        # # Convert dates to datetime objects
        # earliest_date = datetime.combine(earliest_date, datetime.min.time()) if earliest_date else None
        # latest_date = datetime.combine(latest_date, datetime.min.time()) if latest_date else None        
        # return [earliest_date, latest_date, str(worked_period.days) + ' days' if worked_period else None]

    def get_extract_skills(self, text = None) -> list:
        """
        This will get the skills within the extracted resume.
        """
        text if text else self.source 
        with open('./data/skills.json') as f:
            self.qualifications = json.load(f)
        pattern = re.compile(r'\b(' + '|'.join(self.qualifications.keys()) + r')\b', flags=re.IGNORECASE)
        extracted_qualifications = list(set(pattern.findall(text)))
        return extracted_qualifications

    def _get_between_text(self, text, list) -> list:
        """
        Gets the text in between the resume description.
        """
        text = text.lower()
        title_list = list
        
        words_between_titles = []
        for i in range(len(title_list)-1):
            start_word = title_list[i]
            end_word = title_list[i+1]
            words_between = text.split(start_word)[1].split(end_word)[0].strip()
            words_between_titles.append(words_between)

        last_word = title_list[-1]
        last_word_index = text.rfind(last_word)
        if last_word_index != -1:
            words_after_last = text[last_word_index+len(last_word):].strip()
            words_between_titles.append(words_after_last)

        return words_between_titles


# TODO: - Remove any charatachers like - ! for the title searching

sample = ResumeParser(text = """
WePrepFBA Remote Zoho - Full Stack Developer Feb 2022 - May 2022 • Developed a warehouse management system that tracks incoming orders using SQL, Python, and Django, resulting in improved efficiency and meeting project requirements. • I leveraged the powerful combination of HTMX and Bootstrap4 to architect and develop the frontend for a comprehensive warehouse management system, demonstrating my proficiency in cutting-edge web development technologies. • Adapted quickly to new technologies, learning Deluge within 3 days and proposing using Django instead to better meet the aim for project requirements. • Collaborated effectively with cross-functional teams to troubleshoot and solve technical issues, resulting in a 25% decrease in project turnaround time. • Implemented various features, such as order tracking, inv
""")

print(sample.get_date())

