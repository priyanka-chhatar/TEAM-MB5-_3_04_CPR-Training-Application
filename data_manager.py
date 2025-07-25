import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class CPRDataManager:
    """Manage CPR training data and analytics"""
    
    def __init__(self):
        self.sessions = []
        self.quiz_results = []
        
    def add_training_session(self, session_data):
        """Add a training session to the database"""
        session_data['id'] = len(self.sessions) + 1
        session_data['date'] = datetime.now()
        self.sessions.append(session_data)
        
    def add_quiz_result(self, quiz_data):
        """Add a quiz result to the database"""
        quiz_data['id'] = len(self.quiz_results) + 1
        quiz_data['date'] = datetime.now()
        self.quiz_results.append(quiz_data)
        
    def get_sessions_df(self):
        """Get training sessions as DataFrame"""
        if not self.sessions:
            return pd.DataFrame()
        
        return pd.DataFrame(self.sessions)
    
    def get_quiz_df(self):
        """Get quiz results as DataFrame"""
        if not self.quiz_results:
            return pd.DataFrame()
        
        return pd.DataFrame(self.quiz_results)
    
    def calculate_user_level(self):
        """Calculate user skill level based on performance"""
        if not self.sessions:
            return "Beginner"
        
        recent_sessions = self.sessions[-10:]  # Last 10 sessions
        avg_score = np.mean([s.get('score', 0) for s in recent_sessions])
        
        if avg_score >= 90:
            return "Expert"
        elif avg_score >= 80:
            return "Advanced"
        elif avg_score >= 70:
            return "Intermediate"
        else:
            return "Beginner"
    
    def get_progress_metrics(self):
        """Get overall progress metrics"""
        if not self.sessions:
            return {
                "total_sessions": 0,
                "average_score": 0,
                "total_compressions": 0,
                "best_score": 0,
                "current_level": "Beginner"
            }
        
        df = self.get_sessions_df()
        
        return {
            "total_sessions": len(self.sessions),
            "average_score": df['score'].mean() if 'score' in df.columns else 0,
            "total_compressions": df['compressions'].sum() if 'compressions' in df.columns else 0,
            "best_score": df['score'].max() if 'score' in df.columns else 0,
            "current_level": self.calculate_user_level()
        }
    
    def get_recent_performance(self, days=7):
        """Get performance data for recent days"""
        if not self.sessions:
            return []
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_sessions = [s for s in self.sessions if s.get('date', datetime.now()) >= cutoff_date]
        
        return recent_sessions
    
    def get_performance_by_scenario(self):
        """Get performance breakdown by scenario"""
        if not self.sessions:
            return {}
        
        df = self.get_sessions_df()
        
        if 'scenario' not in df.columns:
            return {}
        
        scenario_performance = df.groupby('scenario').agg({
            'score': ['mean', 'count'],
            'compressions': 'sum'
        }).round(2)
        
        return scenario_performance.to_dict()
    
    def get_performance_by_difficulty(self):
        """Get performance breakdown by difficulty"""
        if not self.sessions:
            return {}
        
        df = self.get_sessions_df()
        
        if 'difficulty' not in df.columns:
            return {}
        
        difficulty_performance = df.groupby('difficulty').agg({
            'score': ['mean', 'count'],
            'compressions': 'sum'
        }).round(2)
        
        return difficulty_performance.to_dict()
    
    def get_learning_curve(self):
        """Calculate learning curve progression"""
        if len(self.sessions) < 3:
            return None
        
        df = self.get_sessions_df()
        
        # Calculate moving average of scores
        window_size = min(5, len(df))
        df['moving_avg'] = df['score'].rolling(window=window_size).mean()
        
        # Calculate trend
        x = np.arange(len(df))
        y = df['score'].values
        z = np.polyfit(x, y, 1)
        trend_slope = z[0]
        
        return {
            "trend_slope": trend_slope,
            "improvement_rate": "Improving" if trend_slope > 0 else "Declining" if trend_slope < -1 else "Stable",
            "sessions_data": df[['date', 'score', 'moving_avg']].to_dict('records')
        }
    
    def generate_recommendations(self):
        """Generate personalized training recommendations"""
        recommendations = []
        
        if not self.sessions:
            recommendations.append({
                "type": "info",
                "message": "Start with basic CPR training to establish baseline skills"
            })
            return recommendations
        
        metrics = self.get_progress_metrics()
        recent_performance = self.get_recent_performance()
        
        # Frequency recommendations
        if len(recent_performance) < 2:
            recommendations.append({
                "type": "warning",
                "message": "Practice more frequently - aim for 2-3 sessions per week"
            })
        
        # Score-based recommendations
        avg_score = metrics['average_score']
        
        if avg_score < 60:
            recommendations.append({
                "type": "error",
                "message": "Focus on basic technique - review educational content"
            })
        elif avg_score < 80:
            recommendations.append({
                "type": "warning",
                "message": "Good progress! Focus on compression rate consistency"
            })
        elif avg_score >= 90:
            recommendations.append({
                "type": "success",
                "message": "Excellent skills! Consider advanced scenarios or teaching others"
            })
        
        # Scenario-specific recommendations
        scenario_performance = self.get_performance_by_scenario()
        if scenario_performance:
            # Find weakest scenario
            worst_scenarios = []
            for scenario, data in scenario_performance.items():
                if isinstance(data, dict) and 'score' in data and 'mean' in data['score']:
                    if data['score']['mean'] < 75:
                        worst_scenarios.append(scenario)
            
            if worst_scenarios:
                recommendations.append({
                    "type": "info",
                    "message": f"Practice these scenarios: {', '.join(worst_scenarios)}"
                })
        
        return recommendations
    
    def export_data(self):
        """Export all data for backup or analysis"""
        return {
            "sessions": self.sessions,
            "quiz_results": self.quiz_results,
            "exported_at": datetime.now().isoformat()
        }
    
    def import_data(self, data):
        """Import data from backup"""
        if 'sessions' in data:
            self.sessions = data['sessions']
        if 'quiz_results' in data:
            self.quiz_results = data['quiz_results']

class PerformanceAnalyzer:
    """Advanced analytics for CPR performance"""
    
    @staticmethod
    def analyze_compression_rhythm(compression_times, target_rate=110):
        """Analyze compression rhythm patterns"""
        if len(compression_times) < 3:
            return None
        
        # Calculate intervals
        intervals = np.diff(compression_times)
        target_interval = 60 / target_rate
        
        # Statistical analysis
        mean_interval = np.mean(intervals)
        std_interval = np.std(intervals)
        cv = std_interval / mean_interval  # Coefficient of variation
        
        # Rhythm consistency score
        consistency = max(0, 100 - (cv * 100))
        
        # Rate accuracy
        actual_rate = 60 / mean_interval
        rate_accuracy = max(0, 100 - abs(actual_rate - target_rate) / target_rate * 100)
        
        return {
            "mean_interval": mean_interval,
            "std_interval": std_interval,
            "coefficient_of_variation": cv,
            "consistency_score": consistency,
            "actual_rate": actual_rate,
            "rate_accuracy": rate_accuracy,
            "target_rate": target_rate
        }
    
    @staticmethod
    def detect_fatigue_patterns(session_data):
        """Detect signs of fatigue during training"""
        if len(session_data) < 30:  # Need sufficient data
            return None
        
        # Split session into segments
        segment_size = len(session_data) // 3
        
        segments = [
            session_data[:segment_size],
            session_data[segment_size:2*segment_size],
            session_data[2*segment_size:]
        ]
        
        segment_scores = []
        for segment in segments:
            if len(segment) > 5:
                analyzer = PerformanceAnalyzer()
                analysis = analyzer.analyze_compression_rhythm(segment)
                if analysis:
                    segment_scores.append(analysis['rate_accuracy'])
        
        if len(segment_scores) == 3:
            # Check for declining performance
            decline = segment_scores[0] - segment_scores[-1]
            fatigue_detected = decline > 10  # 10% decline indicates fatigue
            
            return {
                "fatigue_detected": fatigue_detected,
                "performance_decline": decline,
                "segment_scores": segment_scores
            }
        
        return None