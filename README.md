# Forsico IO AI Flask Application

This is a Flask application for handling logs and generating text based on given tasks. 
It uses the Flask framework, SQLAlchemy for database interaction, and `transformers` for generating text in English or Turkish.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3.8+
- Pip

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
   ```bash git clone https://github.com/yourusername/forsico_io_ai.git```

2. Navigate to the project directory:
   ```bash cd forsico_io_ai```

3. Install the required packages:
   ```bash  pip install -r requirements.txt```



### API Endpoints
   * `POST /generate` - Generates tasks based on the provided description.
   * `POST /logs` - Generates tasks based on the provided description.
   * `GET /logs/<log_id>` - Generates tasks based on the provided description.
   * `PUT /logs/<log_id>` - Generates tasks based on the provided description.
   * `DELETE /logs/<log_id>` - Generates tasks based on the provided description.

### Running the Application
    To run the application, use the following command:

    1- pip install virtualenv

    2- virtualenv myenv

    3- source myenv/bin/activate

    4- python app.py