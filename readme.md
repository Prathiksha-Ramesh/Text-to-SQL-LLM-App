# Text to SQL LLM App

This application leverages a language learning model to translate natural language queries into SQL commands, facilitating easy interaction with databases for users who are not proficient in SQL.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

The Text to SQL LLM App simplifies database querying by allowing users to input questions or commands in plain English, which the system then translates into executable SQL queries. This tool is particularly useful for data analysts and business professionals looking to extract insights from data without deep SQL knowledge.

## Features

- **Natural Language Understanding**: Converts natural language into SQL commands using advanced NLP models.
- **User-Friendly Interface**: Features a simple, intuitive interface for users to input their queries and view results.
- **AI-Driven Insights**: Enhances query capabilities with AI, providing suggestions for optimizing queries and understanding complex data patterns.

## Installation

### Prerequisites

- Python 3.8+
- Git

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/text-to-sql-llm-app.git
   cd text-to-sql-llm-app
```
2. **Create a virtual environment**:

``` bash 
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
``` 
3. **Install the required dependencies:**
``` bash 
pip install -r requirements.txt
```
4. **Set up environment variables:** Copy the `.env.example` file to create a `.env` file and adjust the variables accordingly.

## Usage
To start the application, run:
``` bash 
streamlit run app.py

``` 

Navigate to the provided local web address to interact with the application.

## Project Structure
- `app.py`: Main application script for the Streamlit interface.
- `sql.py`: Contains the logic for converting text to SQL.
requirements.txt: Lists all project dependencies.
- `.env`: Environment variable configuration file.
-`.gitignore`: Specifies intentionally untracked files to ignore.

## Dependencies
Key dependencies include:

- `streamlit`: For the web interface.
- `transformers`: For leveraging pre-trained NLP models.
- `sqlalchemy`: For database interaction.
- `python-dotenv`: For managing environment variables.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or have encountered issues, please open an issue or submit a pull request.