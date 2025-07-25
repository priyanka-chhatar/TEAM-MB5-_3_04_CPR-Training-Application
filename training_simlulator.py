import streamlit as st
import time
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import threading
import queue

st.set_page_config(
    page_title="CPR Training Simulator",
    page_icon="🫀",
    layout="wide"
)

# Initialize session state for training
if 'training_active' not in st.session_state:
    st.session_state.training_active = False
if 'compressions' not in st.session_state:
    st.session_state.compressions = []
if 'compression_count' not in st.session_state:
    st.session_state.compression_count = 0
if 'training_start_time' not in st.session_state:
    st.session_state.training_start_time = None
if 'metronome_active' not in st.session_state:
    st.session_state.metronome_active = False
if 'target_rate' not in st.session_state:
    st.session_state.target_rate = 110  # BPM

def calculate_score(compressions, target_rate=110):
    """Calculate training score based on compression timing"""
    if len(compressions) < 2:
        return 0
    
    # Calculate intervals between compressions
    intervals = [compressions[i] - compressions[i-1] for i in range(1, len(compressions))]
    
    # Target interval in seconds
    target_interval = 60 / target_rate
    
    # Calculate accuracy
    accuracy_scores = []
    for interval in intervals:
        # Score based on how close to target interval
        deviation = abs(interval - target_interval)
        score = max(0, 100 - (deviation / target_interval) * 100)
        accuracy_scores.append(score)
    
    return np.mean(accuracy_scores) if accuracy_scores else 0

def reset_training():
    """Reset training session"""
    st.session_state.training_active = False
    st.session_state.compressions = []
    st.session_state.compression_count = 0
    st.session_state.training_start_time = None
    st.session_state.metronome_active = False

def main():
    st.title("🫀 CPR Training Simulator")
    
    # Training configuration
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("⚙ Training Settings")
        
        difficulty = st.selectbox("Difficulty Level", 
                                ["Beginner", "Intermediate", "Advanced"],
                                key="difficulty_select")
        
        scenario = st.selectbox("Scenario", [
            "Basic Adult CPR",
            "Infant CPR", 
            "Emergency Response",
            "Team CPR"
        ], key="scenario_select")
        
        st.session_state.target_rate = st.slider("Target Rate (BPM)", 
                                                100, 120, 110)
        
        training_duration = st.slider("Training Duration (minutes)", 
                                    1, 10, 2)
        
        # Metronome toggle
        metronome_enabled = st.checkbox("Enable Metronome", 
                                      value=st.session_state.metronome_active)
        
        if metronome_enabled != st.session_state.metronome_active:
            st.session_state.metronome_active = metronome_enabled
    
    with col1:
        st.subheader("🎯 Training Area")
        
        # Training status
        if st.session_state.training_active:
            elapsed_time = time.time() - st.session_state.training_start_time
            remaining_time = max(0, (training_duration * 60) - elapsed_time)
            
            if remaining_time > 0:
                # Progress bar
                progress = elapsed_time / (training_duration * 60)
                st.progress(progress)
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Compressions", st.session_state.compression_count)
                with col_b:
                    current_rate = calculate_current_rate()
                    st.metric("Current Rate", f"{current_rate:.0f} BPM")
                with col_c:
                    st.metric("Time Left", f"{remaining_time:.0f}s")
                
                # Compression button
                if st.button("💥 COMPRESS", key="compress_btn", type="primary", 
                           help="Click to perform compression"):
                    perform_compression()
                    st.rerun()
                
                # Real-time feedback
                show_realtime_feedback()
                
                # Auto-end training when time is up
                if remaining_time <= 0:
                    end_training_session()
                    st.rerun()
            else:
                end_training_session()
                st.rerun()
        else:
            # Start training button
            if st.button("🚀 Start Training", type="primary", key="start_btn"):
                start_training()
                st.rerun()
            
            # Instructions
            st.info(f"""
            *Instructions for {scenario}:*
            
            1. Click 'Start Training' to begin
            2. Click the 'COMPRESS' button at {st.session_state.target_rate} BPM
            3. Maintain steady rhythm for {training_duration} minutes
            4. Follow real-time feedback for improvement
            
            *Target*: {st.session_state.target_rate} compressions per minute
            """)
    
    # Training history and analytics
    if st.session_state.compressions or 'training_sessions' in st.session_state:
        st.markdown("---")
        show_training_analytics()

def calculate_current_rate():
    """Calculate current compression rate"""
    if len(st.session_state.compressions) < 2:
        return 0
    
    # Use last 10 compressions for rate calculation
    recent_compressions = st.session_state.compressions[-10:]
    if len(recent_compressions) < 2:
        return 0
    
    time_span = recent_compressions[-1] - recent_compressions[0]
    if time_span == 0:
        return 0
    
    rate = (len(recent_compressions) - 1) / time_span * 60
    return rate

def perform_compression():
    """Record a compression"""
    current_time = time.time()
    st.session_state.compressions.append(current_time)
    st.session_state.compression_count += 1

def start_training():
    """Start training session"""
    st.session_state.training_active = True
    st.session_state.training_start_time = time.time()
    st.session_state.compressions = []
    st.session_state.compression_count = 0

def show_realtime_feedback():
    """Show real-time feedback during training"""
    if len(st.session_state.compressions) >= 2:
        current_rate = calculate_current_rate()
        target_rate = st.session_state.target_rate
        
        # Rate feedback
        if abs(current_rate - target_rate) <= 5:
            st.success(f"✅ Excellent rate: {current_rate:.0f} BPM")
        elif abs(current_rate - target_rate) <= 10:
            st.warning(f"⚠ Good rate: {current_rate:.0f} BPM - Target: {target_rate} BPM")
        else:
            if current_rate < target_rate:
                st.error(f"❌ Too slow: {current_rate:.0f} BPM - Speed up!")
            else:
                st.error(f"❌ Too fast: {current_rate:.0f} BPM - Slow down!")
        
        # Rhythm consistency
        if len(st.session_state.compressions) >= 5:
            recent_intervals = [st.session_state.compressions[i] - st.session_state.compressions[i-1] 
                              for i in range(-4, 0)]
            consistency = 1 - (np.std(recent_intervals) / np.mean(recent_intervals))
            
            if consistency > 0.9:
                st.success("🎵 Excellent rhythm consistency!")
            elif consistency > 0.7:
                st.warning("🎵 Good rhythm - maintain consistency")
            else:
                st.error("🎵 Focus on maintaining steady rhythm")

def end_training_session():
    """End training session and save results"""
    if st.session_state.compressions:
        # Calculate final score
        score = calculate_score(st.session_state.compressions, st.session_state.target_rate)
        
        # Save session data
        session_data = {
            'date': datetime.now(),
            'compressions': st.session_state.compression_count,
            'score': score,
            'difficulty': st.session_state.get('difficulty_select', 'Beginner'),
            'scenario': st.session_state.get('scenario_select', 'Basic Adult CPR'),
            'target_rate': st.session_state.target_rate
        }
        
        if 'training_sessions' not in st.session_state:
            st.session_state.training_sessions = []
        
        st.session_state.training_sessions.append(session_data)
        
        # Show results
        st.success(f"🎉 Training Complete! Final Score: {score:.1f}%")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Compressions", st.session_state.compression_count)
        with col2:
            avg_rate = calculate_current_rate()
            st.metric("Average Rate", f"{avg_rate:.0f} BPM")
        with col3:
            st.metric("Score", f"{score:.1f}%")
        
        # Performance feedback
        if score >= 90:
            st.balloons()
            st.success("🌟 Outstanding performance! You're ready for emergency situations.")
        elif score >= 75:
            st.success("👍 Good job! Keep practicing to improve consistency.")
        else:
            st.warning("💪 Keep practicing! Focus on maintaining the target rate.")
    
    reset_training()

def show_training_analytics():
    """Show training analytics and progress"""
    st.subheader("📊 Training Analytics")
    
    if st.session_state.compressions:
        # Real-time compression chart
        fig = go.Figure()
        
        # Plot compressions over time
        times = [t - st.session_state.training_start_time for t in st.session_state.compressions]
        
        fig.add_trace(go.Scatter(
            x=times,
            y=[1] * len(times),
            mode='markers',
            marker=dict(size=10, color='red'),
            name='Compressions',
            yaxis='y'
        ))
        
        # Add target rate line
        if len(times) > 1:
            target_intervals = np.arange(0, times[-1], 60/st.session_state.target_rate)
            fig.add_trace(go.Scatter(
                x=target_intervals,
                y=[1.1] * len(target_intervals),
                mode='markers',
                marker=dict(size=8, color='green', symbol='diamond'),
                name='Target Rate',
                yaxis='y'
            ))
        
        fig.update_layout(
            title="Compression Timing",
            xaxis_title="Time (seconds)",
            yaxis_title="",
            showlegend=True,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()