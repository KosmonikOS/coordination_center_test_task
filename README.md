## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Set up

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add the following configurations:
```plaintext
OPENAI_API_KEY=<API_key>
OPENAI_BASE_URL=<URL_to_OpenAI_compatible_API>
OPENAI_MODEL=<Model_to_use>
OPENAI_TEMPERATURE=0.0
TEMPLATE_PATH=templates/template.docx
```

5. Run Streamlit client from the root directory:
```bash
streamlit run src/app.py
```