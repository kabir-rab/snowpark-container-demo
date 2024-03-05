from flask import Flask, request, jsonify, render_template, current_app
from flask_cors import CORS
import modules.chat_gpt_data_generator as gpt
import modules.snowflake_writer as sf
import logging


app = Flask(__name__)
app.config["DEBUG"] = True
app.logger.debug(f"App started")
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Snowflake London Meetup</h1>
                <p>Snowpark Container Demo!</p>'''

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        request_json = request.form
        open_ai_api_key = "[YOUR_API_KEY]"
        columns = request_json['columns'] #["FIRST_NAME","LAST_NAME","AGE","ADDRESS","COUNTRY"]
        rows_number = request_json['noofrec']
        db = request_json['db_name']
        schema = request_json['schema_name']
        table = request_json['table_name']

        generator = gpt.ChatGptDataGenerator(columns, rows_number, open_ai_api_key)
        current_app.logger.info(generator.get_df())
        

        df = generator.get_df()  
        result = sf.snowflake_writer(df, db, schema, table)
        current_app.logger.info(result)
        
        return jsonify(result)
    
    except ValueError as ver:
        current_app.logger.error(jsonify(ver.args[0]))
        return jsonify(ver.args[0]), 403
    except Exception as err:
        current_app.logger.error(err)
        return str(err), 500

@app.route('/generateData')
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) #ssl_context='adhoc' for using https