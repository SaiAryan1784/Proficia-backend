import streamlit as st
from groq import Groq  # Using the Groq SDK
import json

# Initialize Groq Client
client = Groq(api_key="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")

# Generate MCQ prompt
def generate_mcq_prompt(tech_stack, difficulty):
    return (f"Generate 5 multiple-choice questions (MCQ) for {tech_stack} "
            f"at {difficulty} difficulty. Each question must have exactly 4 options, "
            f"with one correct answer explicitly marked."
            f"Return output in JSON format with keys: 'question', 'options', 'correct_answer'.")

# Call Groq API via SDK
def call_groq_api(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Specify the model
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        # Extract the generated content
        response_text = completion.choices[0].message.content
        return response_text
    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")

# Parse JSON output from Groq AI
def parse_json_output(ai_output):
    try:
        # Extract JSON block from the response
        json_start = ai_output.find("[")
        json_end = ai_output.rfind("]") + 1
        if json_start == -1 or json_end == -1:
            raise ValueError("JSON block not found in AI output.")
        
        json_data = ai_output[json_start:json_end]
        # Parse JSON data
        parsed_questions = json.loads(json_data)
        return parsed_questions
    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing JSON output: {str(e)}")
    except Exception as e:
        raise Exception(f"Error extracting JSON: {str(e)}")

# Streamlit UI
st.title("Dynamic MCQ Test Generator")
st.sidebar.header("Test Settings")

tech_stack = st.sidebar.selectbox("Select Technology Stack", ["React", "Python", "Node.js", "Django"])
difficulty = st.sidebar.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

# Generate test button
if st.button("Generate Test"):
    st.info("Generating your test, please wait...")
    prompt = generate_mcq_prompt(tech_stack, difficulty)

    try:
        raw_test = call_groq_api(prompt)
        mcqs = parse_json_output(raw_test)

        if not mcqs:
            st.warning("No questions were generated. Please try again.")
        else:
            st.session_state["mcqs"] = mcqs
            st.session_state["user_answers"] = {idx: None for idx in range(len(mcqs))}
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display test if generated
if "mcqs" in st.session_state:
    mcqs = st.session_state["mcqs"]
    user_answers = st.session_state["user_answers"]

    st.subheader("Generated Test")
    for idx, mcq in enumerate(mcqs):
        st.markdown(f"**Q{idx + 1}: {mcq['question']}**")
        user_answers[idx] = st.radio(
            f"Select an option for Question {idx + 1}",
            mcq["options"],
            key=f"q{idx + 1}"
        )

    # Submit button
    if st.button("Submit Test"):
        score = 0
        for idx, mcq in enumerate(mcqs):
            correct_option = mcq["correct_answer"]
            if user_answers[idx] == correct_option:
                score += 1
        st.success(f"Your Score: {score}/{len(mcqs)}")
