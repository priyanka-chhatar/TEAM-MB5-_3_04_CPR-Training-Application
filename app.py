import streamlit as st
import time
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="CPR Training Simulator",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'training_sessions' not in st.session_state:
    st.session_state.training_sessions = []
if 'current_session' not in st.session_state:
    st.session_state.current_session = None
if 'user_level' not in st.session_state:
    st.session_state.user_level = 'Beginner'

def main():
    st.title("🫀 Interactive CPR Training Application")
    st.markdown("---")
    
    # Main dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Training Sessions",
            value=len(st.session_state.training_sessions),
            delta=f"+{len([s for s in st.session_state.training_sessions if s['date'].date() == datetime.now().date()])}"
        )
    
    with col2:
        avg_score = np.mean([s['score'] for s in st.session_state.training_sessions]) if st.session_state.training_sessions else 0
        st.metric(
            label="Average Score",
            value=f"{avg_score:.1f}%",
            delta=f"{avg_score - 70:.1f}%" if avg_score > 0 else "0%"
        )
    
    with col3:
        total_compressions = sum([s['compressions'] for s in st.session_state.training_sessions])
        st.metric(
            label="Total Compressions",
            value=total_compressions,
            delta=f"+{sum([s['compressions'] for s in st.session_state.training_sessions if s['date'].date() == datetime.now().date()])}"
        )
    
    with col4:
        st.metric(
            label="Current Level",
            value=st.session_state.user_level,
            delta="Improving" if avg_score > 80 else "Practice More"
        )
    
    st.markdown("---")
    
    # Quick start section
    st.header("🚀 Quick Start")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Start Training")
        difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"])
        scenario = st.selectbox("Training Scenario", [
            "Basic Adult CPR",
            "Infant CPR",
            "Emergency Response",
            "Team CPR"
        ])
        
        if st.button("🎯 Start Training Session", type="primary"):
            st.session_state.current_session = {
                'difficulty': difficulty,
                'scenario': scenario,
                'start_time': datetime.now()
            }
            st.switch_page("training_simlulatorpy")
    
    with col2:
        st.subheader("Learn CPR")
        st.write("Access comprehensive educational content about CPR techniques and procedures.")
        if st.button("📚 Educational Content"):
            st.switch_page("Educational_Content.py")
        
        st.write("Test your knowledge with interactive quizzes.")
        if st.button("🧠 Knowledge Quiz"):
            st.switch_page("knowledge_quiz.py")
    
    # Recent performance chart
    if st.session_state.training_sessions:
        st.markdown("---")
        st.header("📊 Recent Performance")
        
        # Create performance chart
        recent_sessions = st.session_state.training_sessions[-10:]  # Last 10 sessions
        df = pd.DataFrame(recent_sessions)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['score'],
            mode='lines+markers',
            name='Score',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Training Session Scores",
            xaxis_title="Date",
            yaxis_title="Score (%)",
            yaxis=dict(range=[0, 100]),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # CPR Quick Facts
    st.markdown("---")
    st.header("💡 CPR Quick Facts")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        *Compression Rate*
        100-120 compressions per minute
        """)
    
    with col2:
        st.warning("""
        *Compression Depth*
        At least 2 inches (5 cm) for adults
        """)
    
    with col3:
        st.success("""
        *Hand Position*
        Center of chest, between nipples
        """)

if __name__ == "__main__":
    main()