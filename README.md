# Snowpark Container Demo with Python Flask

This is a Python Flask application designed to generate dummy data using OpenAI's Large Language Model and store it in a Snowflake database table.

## Setup and Deployment

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Folder Structure

```
project
│   README.md
│   app.py
│   Dockerfile
│   requirements.txt
│
└───templates
│       form.html
│
└───modules
    │   chat_gpt_data_generator.py
    │   snowflake_writer.py
```

### How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/kabir-rab/snowpark-container-demo.git
   cd snowpark-container-demo
   ```

2. Set up environment variables:

   Create a `.env` file in the project root directory and define the following variables:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

3. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

4. Access the application in your web browser:

   Open [http://localhost:5000](http://localhost:5000) to access the application.

## Usage

### Endpoints

- `/`: Home endpoint to test if the server is running.
- `/api/generate`: Endpoint to generate dummy data and store it in the Snowflake database.
- `/generateData`: Endpoint to render the form for inputting Snowflake table details.

### How to Use

1. Access the `/generateData` endpoint to fill in the Snowflake table details.
2. Submit the form to `/api/generate` endpoint to generate and store dummy data.
3. Check the logs for information about the process.

## License

[MIT License](LICENSE)
