# Google-Form-generator
Welcome to the Google Form Generator project! This Python-based tool allows you to easily generate Google Forms using the ChatGPT API and Google Forms API. With just a few simple steps, you can create a customized Google Form by providing the form title, and the generated link will be provided to you.
## How to Use

Follow these steps to set up and use the Google Form Generator:

### 1. Obtain ChatGPT API Key

Before you begin, you need to obtain an API key for the ChatGPT API. If you don't have one, you can sign up on the OpenAI website. Once you have the API key, enter it as `API_KEY` in the `.env` file in the root directory of the project.

### 2. Create a Google Cloud Project

In order to host the Google Forms API and collect data, you'll need to create a Google Cloud project. Follow these steps to create a project:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project drop-down at the top of the page and click "New Project."
3. Provide a name for your project and select your desired organization.
4. Click "Create" to create the project.

### 3. Set Up Google Forms API

To set up the Google Forms API for your project, follow these steps:

1. In your Google Cloud project, navigate to the "APIs & Services" > "Dashboard" section.
2. Click on the "+ ENABLE APIS AND SERVICES" button.
3. Search for "Google Forms API" and enable it for your project.

### 4. Download API Credentials

After enabling the Google Forms API, you need to download the API credentials:

1. In the "APIs & Services" > "Credentials" section, click on the "Create credentials" button.
2. Select "OAuth client ID."
3. Choose "Web application" as the application type.
4. Provide a name for the client ID and add the authorized redirect URIs (e.g., `http://localhost:8080`).
5. Click "Create" to generate the credentials.
6. Download the credentials JSON file and rename it to `client_secrets.json`.

### 5. Run the Project

Now you're ready to run the Google Form Generator:

1. Clone this GitHub repository to your local machine.
2. Navigate to the project directory using the terminal.
3. Install the required dependencies by running: `pip install -r requirements.txt`.
4. Make sure you've added your ChatGPT API key to the `.env` file.
5. Place the `client_secrets.json` file (downloaded in Step 4) in the project directory.
6. Run the `main.py` file using Python: `python main.py`.

### Note

Remember to keep your API keys and credentials secure. Avoid sharing them publicly or committing them to version control.

For more information on creating a Google Forms API, you can refer to the [Google Forms API documentation](https://developers.google.com/forms/api/guides).
