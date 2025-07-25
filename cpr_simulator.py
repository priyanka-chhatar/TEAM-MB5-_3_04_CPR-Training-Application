import time
import numpy as np
from datetime import datetime

class CPRSimulator:
    def __init__(self):
        self.compressions = []
        self.start_time = None
        self.target_rate = 110  # BPM
        self.is_active = False
        
    def start_session(self, target_rate=110):
        """Start a new CPR training session"""
        self.compressions = []
        self.start_time = time.time()
        self.target_rate = target_rate
        self.is_active = True
        
    def add_compression(self):
        """Record a compression"""
        if self.is_active:
            current_time = time.time()
            self.compressions.append(current_time)
            return current_time - self.start_time
        return None
    
    def get_current_rate(self, window_size=10):
        """Calculate current compression rate based on recent compressions"""
        if len(self.compressions) < 2:
            return 0
        
        # Use last N compressions for rate calculation
        recent_compressions = self.compressions[-window_size:]
        if len(recent_compressions) < 2:
            return 0
        
        time_span = recent_compressions[-1] - recent_compressions[0]
        if time_span == 0:
            return 0
        
        # Calculate rate in BPM
        rate = (len(recent_compressions) - 1) / time_span * 60
        return rate
    
    def get_compression_intervals(self):
        """Get intervals between compressions"""
        if len(self.compressions) < 2:
            return []
        
        intervals = []
        for i in range(1, len(self.compressions)):
            interval = self.compressions[i] - self.compressions[i-1]
            intervals.append(interval)
        
        return intervals
    
    def calculate_rate_accuracy(self):
        """Calculate accuracy of compression rate"""
        if len(self.compressions) < 2:
            return 0
        
        intervals = self.get_compression_intervals()
        target_interval = 60 / self.target_rate  # Target interval in seconds
        
        # Calculate how close each interval is to target
        accuracy_scores = []
        for interval in intervals:
            deviation = abs(interval - target_interval)
            # Score decreases with deviation from target
            score = max(0, 100 - (deviation / target_interval) * 100)
            accuracy_scores.append(score)
        
        return np.mean(accuracy_scores) if accuracy_scores else 0
    
    def calculate_rhythm_consistency(self):
        """Calculate consistency of compression rhythm"""
        intervals = self.get_compression_intervals()
        
        if len(intervals) < 3:
            return 0
        
        # Calculate coefficient of variation (lower is better)
        mean_interval = np.mean(intervals)
        std_interval = np.std(intervals)
        
        if mean_interval == 0:
            return 0
        
        cv = std_interval / mean_interval
        # Convert to consistency score (0-100)
        consistency = max(0, 100 - (cv * 100))
        
        return consistency
    
    def get_overall_score(self):
        """Calculate overall performance score"""
        if len(self.compressions) < 2:
            return 0
        
        rate_accuracy = self.calculate_rate_accuracy()
        rhythm_consistency = self.calculate_rhythm_consistency()
        
        # Weight the scores
        overall_score = (rate_accuracy * 0.6) + (rhythm_consistency * 0.4)
        
        return overall_score
    
    def get_feedback(self):
        """Get real-time feedback based on performance"""
        if len(self.compressions) < 2:
            return "Start compressions", "info"
        
        current_rate = self.get_current_rate()
        target_rate = self.target_rate
        
        # Rate feedback
        rate_diff = abs(current_rate - target_rate)
        
        if rate_diff <= 5:
            rate_feedback = f"✅ Excellent rate: {current_rate:.0f} BPM"
            rate_type = "success"
        elif rate_diff <= 10:
            rate_feedback = f"⚠ Good rate: {current_rate:.0f} BPM (Target: {target_rate})"
            rate_type = "warning"
        else:
            if current_rate < target_rate:
                rate_feedback = f"❌ Too slow: {current_rate:.0f} BPM - Speed up!"
            else:
                rate_feedback = f"❌ Too fast: {current_rate:.0f} BPM - Slow down!"
            rate_type = "error"
        
        # Rhythm feedback
        if len(self.compressions) >= 5:
            consistency = self.calculate_rhythm_consistency()
            
            if consistency > 80:
                rhythm_feedback = "🎵 Excellent rhythm consistency!"
                rhythm_type = "success"
            elif consistency > 60:
                rhythm_feedback = "🎵 Good rhythm - maintain consistency"
                rhythm_type = "warning"
            else:
                rhythm_feedback = "🎵 Focus on maintaining steady rhythm"
                rhythm_type = "error"
        else:
            rhythm_feedback = "🎵 Building rhythm pattern..."
            rhythm_type = "info"
        
        return {
            "rate": {"message": rate_feedback, "type": rate_type},
            "rhythm": {"message": rhythm_feedback, "type": rhythm_type}
        }
    
    def end_session(self):
        """End the training session"""
        self.is_active = False
        
        session_data = {
            "compressions": len(self.compressions),
            "duration": time.time() - self.start_time if self.start_time else 0,
            "target_rate": self.target_rate,
            "actual_rate": self.get_current_rate(),
            "rate_accuracy": self.calculate_rate_accuracy(),
            "rhythm_consistency": self.calculate_rhythm_consistency(),
            "overall_score": self.get_overall_score(),
            "timestamp": datetime.now()
        }
        
        return session_data
    
    def get_metronome_interval(self):
        """Get the interval for metronome beats"""
        return 60 / self.target_rate
    
    def should_metronome_beat(self, current_time):
        """Check if metronome should beat now"""
        if not self.start_time:
            return False
        
        elapsed = current_time - self.start_time
        interval = self.get_metronome_interval()
        
        # Check if we're close to a beat time
        beat_number = elapsed / interval
        next_beat_time = (int(beat_number) + 1) * interval
        
        return abs(elapsed - next_beat_time) < 0.1  # 100ms tolerance

class TrainingScenario:
    """Different CPR training scenarios"""
    
    SCENARIOS = {
        "Basic Adult CPR": {
            "description": "Standard adult CPR with 30:2 compression-ventilation ratio",
            "target_rate": 110,
            "compression_depth": "At least 2 inches (5 cm)",
            "hand_position": "Center of chest between nipples",
            "special_instructions": "Allow complete chest recoil between compressions"
        },
        "Infant CPR": {
            "description": "CPR for infants under 1 year",
            "target_rate": 110,
            "compression_depth": "At least 1.5 inches (4 cm)",
            "hand_position": "Two fingers just below nipple line",
            "special_instructions": "Use gentle head tilt for airway opening"
        },
        "Emergency Response": {
            "description": "High-stress emergency scenario",
            "target_rate": 115,
            "compression_depth": "At least 2 inches (5 cm)",
            "hand_position": "Center of chest between nipples",
            "special_instructions": "Focus on rapid response and calling for help"
        },
        "Team CPR": {
            "description": "Team-based CPR with role rotation",
            "target_rate": 110,
            "compression_depth": "At least 2 inches (5 cm)",
            "hand_position": "Center of chest between nipples",
            "special_instructions": "Practice communication and smooth transitions"
        }
    }
    
    @classmethod
    def get_scenario(cls, scenario_name):
        """Get scenario details"""
        return cls.SCENARIOS.get(scenario_name, cls.SCENARIOS["Basic Adult CPR"])
    
    @classmethod
    def get_all_scenarios(cls):
        """Get list of all available scenarios"""
        return list(cls.SCENARIOS.keys())