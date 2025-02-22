# lottery-app
Flask-based lottery number generator.
# Deol's Lottery App

A Flask-based web application that generates random lottery numbers based on user-specified rows and balls. Built as a portfolio project to showcase web development skills with Python, Flask, and Gunicorn.

## Features
- **Custom Input**: Users specify the number of rows and balls per row (up to 50).
- **Visual Appeal**: Results displayed in gradient-styled buttons.
- **Replay Functionality**: "Wanna replay?" button for continuous generation.
- **Responsive Design**: Works seamlessly across all devices.

## Prerequisites
- **Python 3.x**: Ensure Python is installed (`python --version`).
- **pip**: Python package manager (`pip --version`).
- **Git**: For cloning the repository (`git --version`).

## Installation and Setup

### 1. Clone the Repository
Download the project files from GitHub:
```bash
git clone https://github.com/bhupinderdeol/lottery-app.git
cd lottery-app


pip install -r requirements.txt

This installs:

Flask (web framework)
gunicorn (WSGI server)
Alternatively, install manually:

bash
Wrap
Copy
pip install Flask gunicorn
3. Run the Application with Flask (Development)
For testing locally with Flask’s built-in server:

bash
Wrap
Copy
python app.py
Visit http://localhost:5000 in your browser.
Note: This is for development only—not production.
4. Run with Gunicorn (Production-Ready)
For a production-like setup, use Gunicorn:

bash
Wrap
Copy
gunicorn --bind 0.0.0.0:8000 app:app
Explanation:
--bind 0.0.0.0:8000: Binds to port 8000, accessible externally.
app:app: Refers to the Flask app instance in app.py.
Access at http://localhost:8000.
5. Optional: Expose Publicly with ngrok
To make it accessible online:

Install ngrok (e.g., paru -S ngrok on Arch-based systems like Garuda).
Run:
bash
Wrap
Copy
ngrok http 8000
Use the provided ngrok URL (e.g., https://bhupinder-lottery.ngrok-free.app).
Live Demo
Try it at http://deol.free.nf/lottery/ (redirects to an ngrok instance).

Project Structure
text
Wrap
Copy
lottery-app/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── index.html      # Homepage with input form
│   ├── results.html    # Results display with replay
├── static/             # Static assets
│   └── styles.css      # CSS with gradient buttons
└── requirements.txt    # Python dependencies
Tech Stack
Python: Core language.
Flask: Lightweight web framework.
HTML/CSS/JavaScript: Frontend rendering and styling.
Gunicorn: Production WSGI server.
Usage
Open the app in your browser (http://localhost:8000 or ngrok URL).
Enter the number of rows and balls.
Click "Generate Numbers" to see results.
Use "Wanna replay?" to generate new numbers.
Troubleshooting
Port in Use: Change port (e.g., gunicorn --bind 0.0.0.0:8080 app:app).
Dependencies Fail: Ensure pip is updated (pip install --upgrade pip).
Permission Issues: Fix folder ownership (sudo chown -R $USER:$USER .).
Author
Bhupinder Deol

LinkedIn
Email
License
This project is licensed under the MIT License—see the LICENSE file.

Contributing
Feel free to fork, submit issues, or create pull requests!
