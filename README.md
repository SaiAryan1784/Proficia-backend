# Proficia Backend

Proficia Backend is a dynamic MCQ test generator built using Streamlit and integrated with the Groq API. This tool allows users to create multiple-choice question tests on various technology stacks and difficulty levels. Users can generate tests, select answers, and evaluate their scores interactively.

## Features
- **Customizable Test Generation**:
  - Choose from popular technology stacks like React, Python, Node.js, and Django.
  - Set difficulty levels: Beginner, Intermediate, or Advanced.
- **Dynamic User Interaction**:
  - Answer questions directly on the interface.
  - Submit responses to calculate and display scores.
- **Seamless API Integration**:
  - Uses the Groq API to generate MCQs in real-time.

## Demo
Check out the live deployment of the project: [Proficia Backend on Streamlit](https://proficia-backend-sai.streamlit.app/).

## How It Works
1. Select a technology stack and difficulty level from the sidebar.
2. Click on **Generate Test** to create an MCQ test dynamically.
3. Answer each question using the radio buttons provided.
4. Submit the test to calculate your score, displayed as `Correct Answers / Total Questions`.

## Technologies Used
- **Backend**: Groq API for generating questions.
- **Frontend**: Streamlit for interactive UI.
- **Programming Language**: Python.

## Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SaiAryan1784/Proficia-backend.git
   cd Proficia-backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the app in your browser at `http://localhost:8501`.

## Future Enhancements
- Add more technology stack options.
- Implement timed tests for better evaluation.
- Include a leaderboard for competitive scoring.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
