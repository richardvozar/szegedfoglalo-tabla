import json
from pathlib import Path

class ReadQuestionsJson:
    topic_dict = {
        'questions': 'questions',
        'questions2': 'questions2',
        'TTIK': 'questions_TTIK',
        'AJTK': 'questions_AJTK',
        'GTK': 'questions_GTK',
        'BTK': 'questions_BTK',
        'SZAOK': 'questions_SZAOK'
    }

    def read_questions(self, topic='questions'):
        json_file = Path(__file__).parent.absolute() / 'questions' / f'{self.topic_dict[topic]}.json'
        with open(json_file, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data






