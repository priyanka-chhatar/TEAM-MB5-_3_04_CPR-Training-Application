import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Progress Tracking",
    page_icon="📊",
    layout="wide"
)

def main():
    st.title("📊 Progress Tracking & Analytics")
    st.markdown("Track your CPR training progress and identify areas for improvement")
    
    # Check if there's training data
    if 'training_sessions' not in st.session_state or not st.session_state.training_sessions:
        st.info("""
        🚀 *Start Training to See Your Progress!*
        
        Complete some training sessions to view your detailed analytics and progress tracking.
        """)
        
        if st.button("🎯 Start Training Session"):
            st.switch_page("training_simlulator.py")
        return
    
    # Create DataFrame from training sessions
    df = pd.DataFrame(st.session_state.training_sessions)
    df['date'] = pd.to_datetime(df['date'])
    
    # Overview metrics
    show_overview_metrics(df)
    
    # Progress charts
    show_progress_charts(df)
    
    # Detailed analytics
    show_detailed_analytics(df)
    
    # Recommendations
    show_recommendations(df)

def show_overview_metrics(df):
    """Display overview metrics"""
    st.header("📈 Overview")
    
    # Calculate metrics
    total_sessions = len(df)
    avg_score = df['score'].mean()
    total_compressions = df['compressions'].sum()
    best_score = df['score'].max()
    
    # Recent performance (last 7 days)
    recent_df = df[df['date'] >= datetime.now() - timedelta(days=7)]
    recent_sessions = len(recent_df)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Total Sessions",
            value=total_sessions,
            delta=f"+{recent_sessions} this week"
        )
    
    with col2:
        st.metric(
            label="Average Score",
            value=f"{avg_score:.1f}%",
            delta=f"{avg_score - 70:.1f}% vs target" if avg_score > 0 else "0%"
        )
    
    with col3:
        st.metric(
            label="Best Score",
            value=f"{best_score:.1f}%",
            delta="Personal Best" if best_score >= 90 else "Keep improving!"
        )
    
    with col4:
        st.metric(
            label="Total Compressions",
            value=f"{total_compressions:,}",
            delta=f"+{recent_df['compressions'].sum():,} this week" if not recent_df.empty else "+0"
        )
    
    with col5:
        # Calculate skill level
        if avg_score >= 90:
            skill_level = "Expert 🌟"
        elif avg_score >= 80:
            skill_level = "Advanced 👨‍⚕"
        elif avg_score >= 70:
            skill_level = "Intermediate 📚"
        else:
            skill_level = "Beginner 🚀"
        
        st.metric(
            label="Skill Level",
            value=skill_level,
            delta="Keep practicing!"
        )

def show_progress_charts(df):
    """Display progress charts"""
    st.header("📊 Progress Charts")
    
    # Score progression over time
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Score Progression")
        
        fig = go.Figure()
        
        # Add score line
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['score'],
            mode='lines+markers',
            name='Score',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=8)
        ))
        
        # Add target line
        fig.add_hline(y=80, line_dash="dash", line_color="green", 
                     annotation_text="Target: 80%")
        
        # Add trend line
        if len(df) > 1:
            z = np.polyfit(range(len(df)), df['score'], 1)
            p = np.poly1d(z)
            fig.add_trace(go.Scatter(
                x=df['date'],
                y=p(range(len(df))),
                mode='lines',
                name='Trend',
                line=dict(color='orange', width=2, dash='dot')
            ))
        
        fig.update_layout(
            title="Training Score Over Time",
            xaxis_title="Date",
            yaxis_title="Score (%)",
            yaxis=dict(range=[0, 100]),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Compressions per Session")
        
        fig = px.bar(
            df, 
            x='date', 
            y='compressions',
            title="Compressions Count by Session",
            color='score',
            color_continuous_scale='RdYlGn'
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance by difficulty and scenario
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Performance by Difficulty")
        
        difficulty_avg = df.groupby('difficulty')['score'].mean().reset_index()
        
        fig = px.bar(
            difficulty_avg,
            x='difficulty',
            y='score',
            title="Average Score by Difficulty Level",
            color='score',
            color_continuous_scale='RdYlGn'
        )
        
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Training Scenarios")
        
        scenario_counts = df['scenario'].value_counts()
        
        fig = px.pie(
            values=scenario_counts.values,
            names=scenario_counts.index,
            title="Training Sessions by Scenario"
        )
        
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

def show_detailed_analytics(df):
    """Show detailed analytics"""
    st.header("🔍 Detailed Analytics")
    
    # Time-based analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Training Frequency")
        
        # Group by date for frequency analysis
        daily_sessions = df.groupby(df['date'].dt.date).size().reset_index()
        daily_sessions.columns = ['date', 'sessions']
        
        fig = px.line(
            daily_sessions,
            x='date',
            y='sessions',
            title="Training Sessions per Day",
            markers=True
        )
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Performance Distribution")
        
        fig = px.histogram(
            df,
            x='score',
            nbins=20,
            title="Score Distribution",
            labels={'count': 'Number of Sessions', 'score': 'Score (%)'}
        )
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Correlation analysis
    st.subheader("📈 Performance Correlations")
    
    # Calculate correlation between compressions and score
    if len(df) > 1:
        correlation = df['compressions'].corr(df['score'])
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(
                df,
                x='compressions',
                y='score',
                color='difficulty',
                size='compressions',
                title="Compressions vs Score",
                trendline="ols"
            )
            
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.metric(
                "Correlation Coefficient",
                f"{correlation:.3f}",
                help="Correlation between number of compressions and score (-1 to 1)"
            )
            
            if correlation > 0.3:
                st.success("Strong positive correlation! More practice leads to better scores.")
            elif correlation > 0.1:
                st.info("Moderate correlation between practice and performance.")
            else:
                st.warning("Focus on technique quality over quantity.")

def show_recommendations(df):
    """Show personalized recommendations"""
    st.header("💡 Personalized Recommendations")
    
    # Calculate recent performance trends
    if len(df) >= 3:
        recent_scores = df.tail(3)['score'].tolist()
        avg_recent = np.mean(recent_scores)
        trend = "improving" if recent_scores[-1] > recent_scores[0] else "declining"
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Performance Insights")
            
            if avg_recent >= 90:
                st.success("""
                *🌟 Excellent Performance!*
                - You're performing at expert level
                - Consider teaching others or volunteering
                - Practice advanced scenarios to maintain skills
                """)
            elif avg_recent >= 80:
                st.info("""
                *👨‍⚕ Advanced Level*
                - Great job! You're above target performance
                - Focus on consistency across all scenarios
                - Practice team CPR scenarios
                """)
            elif avg_recent >= 70:
                st.warning("""
                *📚 Intermediate Level*
                - You're making good progress
                - Focus on compression rate consistency
                - Practice more challenging scenarios
                """)
            else:
                st.error("""
                *🚀 Keep Practicing!*
                - Focus on basic technique
                - Use metronome for rate training
                - Start with beginner scenarios
                """)
        
        with col2:
            st.subheader("📋 Action Items")
            
            # Generate specific recommendations
            recommendations = []
            
            # Scenario-based recommendations
            scenario_performance = df.groupby('scenario')['score'].mean()
            worst_scenario = scenario_performance.idxmin()
            best_scenario = scenario_performance.idxmax()
            
            if scenario_performance[worst_scenario] < 75:
                recommendations.append(f"🎯 Focus on '{worst_scenario}' scenarios (avg: {scenario_performance[worst_scenario]:.1f}%)")
            
            # Difficulty-based recommendations
            difficulty_performance = df.groupby('difficulty')['score'].mean()
            if 'Beginner' in difficulty_performance and difficulty_performance['Beginner'] < 80:
                recommendations.append("📚 Master beginner level before advancing")
            elif 'Advanced' not in difficulty_performance:
                recommendations.append("🚀 Try advanced difficulty to challenge yourself")
            
            # Frequency recommendations
            days_since_last = (datetime.now() - df['date'].max()).days
            if days_since_last > 7:
                recommendations.append("⏰ It's been a while! Practice regularly for best results")
            elif len(df[df['date'] >= datetime.now() - timedelta(days=7)]) < 3:
                recommendations.append("📅 Aim for 3+ sessions per week for optimal improvement")
            
            # Compression count recommendations
            avg_compressions = df['compressions'].mean()
            if avg_compressions < 50:
                recommendations.append("💪 Increase training duration for more practice")
            
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")
            
            if not recommendations:
                st.success("🎉 You're doing great! Keep up the excellent work!")
    
    # Training schedule suggestions
    st.subheader("📅 Suggested Training Schedule")
    
    current_level = "Beginner"
    if df['score'].mean() >= 90:
        current_level = "Expert"
    elif df['score'].mean() >= 80:
        current_level = "Advanced"
    elif df['score'].mean() >= 70:
        current_level = "Intermediate"
    
    schedules = {
        "Beginner": {
            "frequency": "3-4 times per week",
            "duration": "5-10 minutes per session",
            "focus": "Basic compression technique and rate"
        },
        "Intermediate": {
            "frequency": "2-3 times per week",
            "duration": "10-15 minutes per session",
            "focus": "Consistency and different scenarios"
        },
        "Advanced": {
            "frequency": "2 times per week",
            "duration": "15-20 minutes per session",
            "focus": "Advanced scenarios and team CPR"
        },
        "Expert": {
            "frequency": "1-2 times per week",
            "duration": "10-15 minutes per session",
            "focus": "Skill maintenance and teaching others"
        }
    }
    
    schedule = schedules[current_level]
    
    st.info(f"""
    *Recommended for {current_level} Level:*
    - *Frequency:* {schedule['frequency']}
    - *Duration:* {schedule['duration']}
    - *Focus:* {schedule['focus']}
    """)

if __name__ == "__main__":
    main()