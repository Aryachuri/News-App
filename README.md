# News App — Python News Aggregator

A simple Python-based command-line news application that fetches the latest news articles using the [NewsData.io API](https://newsdata.io/). Users can select a news category and language to retrieve relevant news articles directly in their terminal.

## Features

- 📰 **Latest News:** Fetch news articles using the NewsData.io API.
- 🗂️ **Category-Based Filtering:** Browse news across different categories.
- 🌐 **Multilingual Support:** Read news in English, Hindi, Russian, and Korean.
- 🔍 **Keyword Search:** Retrieve news based on a selected topic or search query.
- 🔄 **Duplicate Filtering:** Uses the API's duplicate-removal parameter.
- ⚠️ **Error Handling:** Handles unsuccessful API responses and empty search results.
- 💻 **Interactive CLI:** Navigate through a menu-driven terminal interface.

## News Categories

The application provides the following menu options:

1. Business
2. Sports
3. Politics
4. Food
5. Lifestyle
6. Crime
7. Breaking News
8. Domestic News
9. Education
10. Environment
11. Exit

*Note: The availability of individual categories depends on the NewsData.io API and its supported category values.*

## Languages Supported

| Language | API Code |
|---|---|
| English | `en` |
| Hindi | `hi` |
| Russian | `ru` |
| Korean | `ko` |

## Technologies Used

- **Programming Language:** Python
- **API Integration:** NewsData.io REST API
- **HTTP Requests:** Requests library
- **Data Handling:** JSON
- **Interface:** Command-Line Interface (CLI)

## How It Works

1. The application displays a menu of news categories.
2. The user selects a category.
3. The user chooses a preferred language.
4. Python sends an HTTP GET request to the NewsData.io API with the selected parameters.
5. The API returns a JSON response containing news articles.
6. The application displays each article's title and description in the terminal.
7. Users can continue browsing other categories or exit the application.

## Project Structure

```text
News-App/
├── news_app.py
└── README.md
```

*Replace `news_app.py` with the actual name of your Python file if it differs. Add any other project files or folders that exist in your repository.*

## Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip
- An API key from NewsData.io

### 1. Clone the Repository

```bash
git clone https://github.com/Aryachuri/News-App.git
cd News-App
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install requests
```

### 4. Configure Your API Key

Obtain an API key from [NewsData.io](https://newsdata.io/).

For safer configuration, store the API key in an environment variable instead of hardcoding it in your source code.

For example, in Git Bash:

```bash
export NEWSDATA_API_KEY="your_api_key"
```

In your Python file, retrieve it using:

```python
import os

api_key = os.getenv("NEWSDATA_API_KEY")
```

Then use `api_key` as the value of the `apikey` parameter in your request.

On Windows Command Prompt, you can set the variable for the current session using:

```cmd
set NEWSDATA_API_KEY=your_api_key
```

### 5. Run the Application

```bash
python news_app.py
```

Select a news category and language from the displayed menu to begin browsing.

## Example Usage

```text
1. To Read Business Related News
2. To Read Sports Related News
3. To Read Politics Related News
...
11. Exit

Enter the option for which you want to read the news: 2

1. English
2. Hindi
3. Russian
4. Korean

Enter the language in which you want to read the news: 1

News 1
Title: Example news headline
Description: Example news description
------------------------------------------------------------
```

*The headline and description above are illustrative examples, not live news results.*

## Error Handling

The application includes basic handling for:

- Unsuccessful API responses.
- Empty news results.
- Missing results in the API response.

Network exceptions, request timeouts, and invalid user input can be handled in future improvements.

## Future Improvements

- 🖥️ Develop a graphical interface using Flask or React.
- 🔎 Add a custom keyword search option.
- 🔗 Display article URLs so users can read full articles.
- 🖼️ Display news thumbnails and source information.
- ⭐ Allow users to save favorite articles.
- 📰 Add pagination to browse additional results.
- 🛡️ Improve API error handling and secure API key management.
- 📦 Add a `requirements.txt` file for easier installation.

## Learning Outcomes

This project demonstrates practical experience with:

- Python functions and loops.
- Conditional statements and pattern matching.
- REST API integration using the Requests library.
- HTTP GET requests and query parameters.
- JSON response handling.
- User input and menu-driven applications.
- Basic API error handling.

## Author

**Arya Churi**

GitHub: [Aryachuri](https://github.com/Aryachuri)

## Disclaimer

This project is intended for educational purposes. News articles and their availability are provided by NewsData.io and are subject to its API terms, usage limits, and licensing conditions.
