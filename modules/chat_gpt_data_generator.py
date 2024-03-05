import openai
from pandas import json_normalize
import json
from openai import  OpenAIError


class ChatGptDataGenerator:
    def __init__(self, columns, rows_number, openai_key):
        self.column_list = columns
        self.rows_number=rows_number
        self.openai_key=openai_key
        self.df=None
        self.generate_data()

    def get_df(self):
        return self.df
            
    def get_json(self):
        return self.df.to_json()
    
    def generate_data(self):
        try:
            openai.api_key = self.openai_key
            basic_query= "generate data for"+ str(self.rows_number)+ "rows with the features of "+str(self.column_list)+" in a JSON format"
            answer = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': basic_query}])
            answer = answer['choices'][0]['message']['content']
            dict = json.loads(answer)
            self.df= json_normalize(dict)
            
        except OpenAIError as e:
            # Handle all OpenAI API errors
            return e