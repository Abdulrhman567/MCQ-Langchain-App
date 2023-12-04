import streamlit as st
from qustions_answers_generator import LangchainModel


def generate_quiz(user_topic, user_number_of_questions):
    """
    This function takes two parameters: user_topic and user_number_of_questions
    and makes an instance of the langchain OpenAI Chat model and passes the parameters to this model so it can generate the specified number of questions about the specified topic with multi-choice answers and the correct answer for each question and returns the output of the model in Json format (Python dict).
    """
    langchain_model = LangchainModel(user_topic, user_number_of_questions)
    model_response_output = langchain_model.generate_langchain_quiz()
    return dict(model_response_output)


# Making Headings
st.title("MCQ Quizes")

# Creating a Side bar
with st.sidebar:
    # Setting values for the user topic and the number of questions that the user selects
    picked_topic = st.text_input(label="**Pick a Topic:**", max_chars=75, placeholder="Enter Text")
    pick_number_of_q = st.number_input(label="**Pick a Number:**", min_value=1, max_value=20, value="min", step=1, placeholder="Enter Number")
    # Creaing a toggle to make the user in fully control of the initilization of the quiz after the user enters the topic of quiz and the number of the questions
    create_quiz_toggle = st.toggle(label="**Take Quiz**", key="create_quize")
    if not picked_topic:
        st.warning("Please pick a topic before you proceed...", icon="⚠️")

# Runs the quiz
if create_quiz_toggle:
    if picked_topic:
        score = 0
        # Generate the quiz
        model_ouput = generate_quiz(user_topic=picked_topic, user_number_of_questions=pick_number_of_q)
        st.subheader(f"{picked_topic} Quiz")
        # displaying the questions and making it interactalbe inside a Form
        with st.form(key="questions_form"):
            # Displaying the questions and there answers 
            for question in model_ouput['questions']:
                question_radio = st.radio(label=f"**{question['question_num']}- {question['questions']}**", options=question['answers'], index=None, key=f"question_{question['question_num']}")

            # A submit button for the user to submit all the answers the user selected 
            submit_form_btn = st.form_submit_button("Submit Answer")
        if submit_form_btn:
            # Displaying the Correct answer and the user score after submiting the answers
            with st.container(border=True):
                st.subheader("Correct Answers")
                for answer_idx in range(len(model_ouput["questions"])):
                    if st.session_state.get(f"question_{answer_idx + 1}") == model_ouput["questions"][answer_idx]["correct_answer"]:
                        score += 1
                    
                    st.write(f"Q{answer_idx + 1} Correct answer: **{model_ouput['questions'][answer_idx]['correct_answer']}**")
                
            with st.container(border=True):
                st.subheader("Quiz Results")
                st.write(f"You got **{score}/{len(model_ouput['questions'])} correct**, Congrats🥳")
                st.write(f"You got {len(model_ouput['questions']) - score}/{len(model_ouput['questions'])} incorrect, It's okey as long as you learn from your mistakes👍")
    else:
        st.error("No topic found, please enter a topic before you proceed...", icon="⛔")
else:
    st.write("**To Generate a Quiz specifiy a Topic for the Quiz and a Number of questions Then Take the quiz by pressing the toggle and happy learning👍😁**")
