import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="CPR Knowledge Quiz",
    page_icon="🧠",
    layout="wide"
)

# Quiz questions database
QUIZ_QUESTIONS = [
    {
        "question": "What is the correct compression rate for adult CPR?",
        "options": ["60-80 BPM", "80-100 BPM", "100-120 BPM", "120-140 BPM"],
        "correct": 2,
        "explanation": "The American Heart Association recommends 100-120 compressions per minute for effective CPR."
    },
    {
        "question": "How deep should chest compressions be for an adult?",
        "options": ["At least 1 inch (2.5 cm)", "At least 1.5 inches (3.8 cm)", "At least 2 inches (5 cm)", "At least 3 inches (7.6 cm)"],
        "correct": 2,
        "explanation": "Adult chest compressions should be at least 2 inches (5 cm) deep to be effective."
    },
    {
        "question": "What is the compression-to-ventilation ratio for single-rescuer adult CPR?",
        "options": ["15:2", "30:2", "5:1", "10:1"],
        "correct": 1,
        "explanation": "The standard ratio is 30 compressions to 2 rescue breaths for single-rescuer adult CPR."
    },
    {
        "question": "Where should you place your hands for adult chest compressions?",
        "options": ["Upper chest", "Lower chest", "Center of chest between nipples", "Left side of chest"],
        "correct": 2,
        "explanation": "Place the heel of your hand on the center of the chest between the nipples on the lower half of the breastbone."
    },
    {
        "question": "How often should you switch compressors during team CPR?",
        "options": ["Every 30 seconds", "Every 1 minute", "Every 2 minutes", "Every 5 minutes"],
        "correct": 2,
        "explanation": "Switch compressors every 2 minutes to prevent fatigue and maintain compression quality."
    },
    {
        "question": "What should you do if an AED becomes available during CPR?",
        "options": ["Continue CPR and ignore the AED", "Stop CPR immediately and use the AED", "Finish the current cycle then use the AED", "Use the AED only if CPR isn't working"],
        "correct": 2,
        "explanation": "Complete the current cycle of compressions, then apply the AED as soon as possible."
    },
    {
        "question": "For infant CPR, what is the preferred compression method for healthcare providers?",
        "options": ["One hand", "Two fingers", "Two thumbs encircling technique", "Palm of hand"],
        "correct": 2,
        "explanation": "Healthcare providers should use the two-thumb encircling technique for infant CPR as it provides better compression depth and consistency."
    },
    {
        "question": "What is the first step in the Chain of Survival?",
        "options": ["Early CPR", "Early defibrillation", "Early recognition and activation of emergency response", "Advanced life support"],
        "correct": 2,
        "explanation": "Early recognition of cardiac arrest and activation of the emergency response system is the first critical step."
    },
    {
        "question": "When should you NOT perform CPR?",
        "options": ["If the person is unconscious", "If the person is breathing normally", "If you don't know the person", "If you're not certified"],
        "correct": 1,
        "explanation": "Do not perform CPR if the person is conscious and breathing normally. CPR is only for unresponsive victims who are not breathing normally."
    },
    {
        "question": "What does 'hands-only CPR' mean?",
        "options": ["CPR using only one hand", "CPR without rescue breathing", "CPR without checking pulse", "CPR for trained professionals only"],
        "correct": 1,
        "explanation": "Hands-only CPR means continuous chest compressions without rescue breathing, recommended for untrained bystanders."
    },
    {
        "question": "How long should you check for breathing before starting CPR?",
        "options": ["No more than 5 seconds", "No more than 10 seconds", "No more than 15 seconds", "At least 30 seconds"],
        "correct": 1,
        "explanation": "Check for normal breathing for no more than 10 seconds. If the person is not breathing normally or only gasping, start CPR immediately."
    },
    {
        "question": "What is the correct hand position for infant chest compressions using the two-finger technique?",
        "options": ["Center of chest", "Just below the nipple line", "Upper chest", "Just above the nipple line"],
        "correct": 1,
        "explanation": "Place two fingers just below the nipple line on the lower half of the breastbone for infant CPR."
    }
]

def initialize_quiz_state():
    """Initialize quiz session state"""
    if 'quiz_active' not in st.session_state:
        st.session_state.quiz_active = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    if 'quiz_results' not in st.session_state:
        st.session_state.quiz_results = []
    if 'show_explanation' not in st.session_state:
        st.session_state.show_explanation = False

def start_quiz(num_questions=10, difficulty="Mixed"):
    """Start a new quiz session"""
    # Select random questions
    selected_questions = random.sample(QUIZ_QUESTIONS, min(num_questions, len(QUIZ_QUESTIONS)))
    
    st.session_state.quiz_questions = selected_questions
    st.session_state.current_question = 0
    st.session_state.user_answers = []
    st.session_state.quiz_active = True
    st.session_state.show_explanation = False

def main():
    initialize_quiz_state()
    
    st.title("🧠 CPR Knowledge Quiz")
    st.markdown("Test your CPR knowledge with interactive quizzes")
    
    if not st.session_state.quiz_active:
        show_quiz_setup()
    else:
        show_quiz_question()

def show_quiz_setup():
    """Show quiz configuration and start options"""
    st.header("📋 Quiz Setup")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Choose Your Quiz")
        
        quiz_type = st.selectbox(
            "Quiz Type:",
            ["General CPR Knowledge", "Adult CPR", "Infant/Child CPR", "Emergency Response", "AED Usage"]
        )
        
        num_questions = st.slider("Number of Questions:", 5, 15, 10)
        
        difficulty = st.selectbox(
            "Difficulty Level:",
            ["Mixed", "Beginner", "Intermediate", "Advanced"]
        )
        
        if st.button("🚀 Start Quiz", type="primary"):
            start_quiz(num_questions, difficulty)
            st.rerun()
    
    with col2:
        st.subheader("📊 Quiz Statistics")
        
        if 'quiz_results' in st.session_state and st.session_state.quiz_results:
            total_quizzes = len(st.session_state.quiz_results)
            avg_score = sum([r['score'] for r in st.session_state.quiz_results]) / total_quizzes
            best_score = max([r['score'] for r in st.session_state.quiz_results])
            
            st.metric("Quizzes Taken", total_quizzes)
            st.metric("Average Score", f"{avg_score:.1f}%")
            st.metric("Best Score", f"{best_score:.1f}%")
        else:
            st.info("Take your first quiz to see statistics!")
    
    # Recent quiz results
    if 'quiz_results' in st.session_state and st.session_state.quiz_results:
        st.markdown("---")
        st.subheader("📈 Recent Results")
        
        recent_results = st.session_state.quiz_results[-5:]  # Last 5 quizzes
        
        for i, result in enumerate(reversed(recent_results), 1):
            score_color = "🟢" if result['score'] >= 80 else "🟡" if result['score'] >= 60 else "🔴"
            st.write(f"{score_color} *Quiz {len(st.session_state.quiz_results) - i + 1}:* {result['score']:.1f}% - {result['date'].strftime('%m/%d/%Y %H:%M')}")

def show_quiz_question():
    """Display current quiz question"""
    current_q = st.session_state.current_question
    total_q = len(st.session_state.quiz_questions)
    question_data = st.session_state.quiz_questions[current_q]
    
    # Progress bar
    progress = (current_q + 1) / total_q
    st.progress(progress)
    st.write(f"Question {current_q + 1} of {total_q}")
    
    # Question
    st.subheader(f"❓ {question_data['question']}")
    
    # Answer options
    if not st.session_state.show_explanation:
        selected_answer = st.radio(
            "Select your answer:",
            options=range(len(question_data['options'])),
            format_func=lambda x: question_data['options'][x],
            key=f"question_{current_q}"
        )
        
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("✅ Submit Answer"):
                st.session_state.user_answers.append(selected_answer)
                st.session_state.show_explanation = True
                st.rerun()
        
        with col2:
            if st.button("❌ End Quiz"):
                end_quiz()
                st.rerun()
    
    else:
        # Show explanation and results
        show_answer_explanation(question_data, current_q)

def show_answer_explanation(question_data, current_q):
    """Show explanation for the current question"""
    user_answer = st.session_state.user_answers[current_q]
    correct_answer = question_data['correct']
    
    # Show user's answer
    st.write("*Your Answer:*")
    if user_answer == correct_answer:
        st.success(f"✅ Correct! {question_data['options'][user_answer]}")
    else:
        st.error(f"❌ Incorrect: {question_data['options'][user_answer]}")
        st.success(f"✅ Correct Answer: {question_data['options'][correct_answer]}")
    
    # Show explanation
    st.info(f"*Explanation:* {question_data['explanation']}")
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if current_q < len(st.session_state.quiz_questions) - 1:
            if st.button("➡ Next Question"):
                st.session_state.current_question += 1
                st.session_state.show_explanation = False
                st.rerun()
        else:
            if st.button("🏁 Finish Quiz"):
                end_quiz()
                st.rerun()
    
    with col2:
        if st.button("❌ End Quiz Early"):
            end_quiz()
            st.rerun()

def end_quiz():
    """End quiz and show results"""
    if st.session_state.user_answers:
        # Calculate score
        correct_answers = 0
        total_questions = len(st.session_state.user_answers)
        
        for i, user_answer in enumerate(st.session_state.user_answers):
            if user_answer == st.session_state.quiz_questions[i]['correct']:
                correct_answers += 1
        
        score = (correct_answers / total_questions) * 100
        
        # Save quiz result
        quiz_result = {
            'score': score,
            'correct': correct_answers,
            'total': total_questions,
            'date': datetime.now()
        }
        
        st.session_state.quiz_results.append(quiz_result)
        
        # Show results
        show_quiz_results(quiz_result)
    
    # Reset quiz state
    st.session_state.quiz_active = False
    st.session_state.current_question = 0
    st.session_state.user_answers = []
    st.session_state.show_explanation = False

def show_quiz_results(result):
    """Display quiz results"""
    st.balloons() if result['score'] >= 80 else None
    
    st.header("🎉 Quiz Complete!")
    
    # Score display
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Score", f"{result['score']:.1f}%")
    
    with col2:
        st.metric("Correct Answers", f"{result['correct']}/{result['total']}")
    
    with col3:
        if result['score'] >= 90:
            grade = "A+ 🌟"
        elif result['score'] >= 80:
            grade = "A 😊"
        elif result['score'] >= 70:
            grade = "B 👍"
        elif result['score'] >= 60:
            grade = "C 📚"
        else:
            grade = "D 💪"
        
        st.metric("Grade", grade)
    
    # Performance feedback
    if result['score'] >= 90:
        st.success("""
        🌟 *Outstanding!* You have excellent CPR knowledge. 
        You're well-prepared for emergency situations!
        """)
    elif result['score'] >= 80:
        st.success("""
        😊 *Great job!* You have solid CPR knowledge. 
        Review the questions you missed to improve further.
        """)
    elif result['score'] >= 70:
        st.warning("""
        👍 *Good effort!* You have basic CPR knowledge. 
        Study the educational content and retake the quiz.
        """)
    elif result['score'] >= 60:
        st.warning("""
        📚 *Keep studying!* Review the CPR guidelines and 
        educational materials before retaking the quiz.
        """)
    else:
        st.error("""
        💪 *More practice needed!* Spend time with the educational 
        content and training simulator before retaking the quiz.
        """)
    
    # Detailed review
    st.subheader("📝 Question Review")
    
    for i, (question, user_answer) in enumerate(zip(st.session_state.quiz_questions[:len(st.session_state.user_answers)], st.session_state.user_answers)):
        correct = user_answer == question['correct']
        
        with st.expander(f"Question {i+1}: {'✅' if correct else '❌'} {question['question']}"):
            st.write(f"*Your answer:* {question['options'][user_answer]}")
            st.write(f"*Correct answer:* {question['options'][question['correct']]}")
            st.info(f"*Explanation:* {question['explanation']}")
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Take Another Quiz"):
            st.rerun()
    
    with col2:
        if st.button("📚 Study Educational Content"):
            st.switch_page("edu_contentt.py")
    
    with col3:
        if st.button("🎯 Practice Training"):
            st.switch_page("training_simlulator.py")

if __name__ == "__main__":
    main()