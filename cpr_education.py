"""
CPR Educational Content Database
Contains comprehensive information about CPR procedures, guidelines, and best practices
"""

def get_cpr_content():
    """Get comprehensive CPR educational content"""
    return {
        "overview": {
            "title": "Cardiopulmonary Resuscitation (CPR)",
            "description": """
            CPR is a life-saving technique that combines chest compressions and rescue breathing 
            to manually preserve brain function and blood circulation during cardiac arrest. 
            When performed correctly and promptly, CPR can double or triple the chances of survival.
            """,
            "importance": [
                "Maintains blood flow to vital organs",
                "Preserves brain function during cardiac arrest",
                "Buys time until professional medical help arrives",
                "Can be performed by trained bystanders"
            ]
        },
        "when_to_perform": {
            "indicators": [
                "Person is unresponsive to verbal or physical stimuli",
                "No normal breathing (not breathing or only gasping)",
                "No pulse (if trained to check)",
                "Signs of cardiac arrest"
            ],
            "do_not_perform": [
                "Person is conscious and responding",
                "Person is breathing normally",
                "Person has a pulse and is responsive",
                "Obvious signs of life"
            ]
        },
        "chain_of_survival": {
            "adult": [
                "Early recognition and activation of emergency response system",
                "Early high-quality CPR",
                "Early defibrillation",
                "Advanced life support",
                "Post-cardiac arrest care"
            ],
            "pediatric": [
                "Prevention of cardiac arrest",
                "Early high-quality CPR",
                "Early activation of emergency response",
                "Early advanced life support",
                "Post-cardiac arrest care"
            ]
        }
    }

def get_cpr_steps():
    """Get detailed CPR step-by-step instructions"""
    return [
        {
            "title": "Check Responsiveness",
            "description": "Tap the person's shoulders firmly and shout 'Are you okay?'",
            "details": "If no response, the person is unconscious. Look for normal breathing for no more than 10 seconds."
        },
        {
            "title": "Call for Help",
            "description": "Call 911 immediately and request an AED if available",
            "details": "If others are present, have someone call while you begin CPR. Time is critical."
        },
        {
            "title": "Position the Person",
            "description": "Place the person on their back on a firm surface",
            "details": "Tilt the head back slightly by lifting the chin. Ensure the airway is open."
        },
        {
            "title": "Hand Placement",
            "description": "Place the heel of one hand on the center of the chest between the nipples",
            "details": "Place your other hand on top, interlacing your fingers. Keep arms straight."
        },
        {
            "title": "Begin Compressions",
            "description": "Push hard and fast at least 2 inches deep at 100-120 compressions per minute",
            "details": "Allow complete chest recoil between compressions. Count out loud."
        },
        {
            "title": "Rescue Breathing",
            "description": "After 30 compressions, tilt head back, lift chin, and give 2 rescue breaths",
            "details": "Each breath should last 1 second and make the chest rise visibly."
        },
        {
            "title": "Continue Cycles",
            "description": "Continue with 30 compressions and 2 breaths until help arrives",
            "details": "If trained, switch with another rescuer every 2 minutes to prevent fatigue."
        }
    ]

def get_emergency_scenarios():
    """Get different emergency scenarios and responses"""
    return [
        {
            "title": "Witnessed Cardiac Arrest",
            "description": "You see someone suddenly collapse and become unresponsive",
            "steps": [
                "Ensure the scene is safe",
                "Check responsiveness by tapping shoulders and shouting",
                "Call 911 immediately",
                "Check for normal breathing (no more than 10 seconds)",
                "Begin CPR if no normal breathing",
                "Continue until emergency services arrive"
            ],
            "warning": "Time is critical - begin CPR within 4-6 minutes for best outcomes"
        },
        {
            "title": "Drowning Victim",
            "description": "Unresponsive person pulled from water",
            "steps": [
                "Remove victim from water safely",
                "Check responsiveness",
                "Call 911",
                "Check for breathing and pulse",
                "Begin CPR if needed (may require modified positioning)",
                "Be prepared for vomiting - turn head to side if needed"
            ],
            "warning": "Water in lungs may make rescue breathing less effective initially"
        },
        {
            "title": "Choking Leading to Unconsciousness",
            "description": "Person who was choking becomes unconscious",
            "steps": [
                "Lower person to ground carefully",
                "Call 911",
                "Open mouth and look for visible object",
                "Remove object only if clearly visible",
                "Begin CPR with chest compressions",
                "Check mouth before each rescue breath"
            ],
            "warning": "Do not perform blind finger sweeps - may push object deeper"
        },
        {
            "title": "Infant Emergency",
            "description": "Infant (under 1 year) is unresponsive",
            "steps": [
                "Tap foot and shout to check responsiveness",
                "Call 911 or have someone else call",
                "Check for breathing (no more than 10 seconds)",
                "Use 2-finger or 2-thumb compression technique",
                "Compress at least 1.5 inches deep",
                "Use gentle head tilt for rescue breathing"
            ],
            "warning": "Infant physiology requires modified techniques - get trained specifically"
        },
        {
            "title": "Elderly Person Collapse",
            "description": "Elderly person collapses, possibly due to medical condition",
            "steps": [
                "Approach carefully and check responsiveness",
                "Be aware of possible spine injuries",
                "Call 911 and mention age and any known medical conditions",
                "Check for medical alert jewelry",
                "Begin CPR if indicated",
                "Be gentle but effective with compressions"
            ],
            "warning": "Elderly persons may have fragile ribs - compressions may cause breaks but continue CPR"
        }
    ]

def get_age_specific_guidelines():
    """Get age-specific CPR guidelines"""
    return {
        "adult": {
            "age_range": "8 years and older",
            "compression_depth": "At least 2 inches (5 cm), no more than 2.4 inches (6 cm)",
            "compression_rate": "100-120 per minute",
            "compression_technique": "Two hands, heel of palm",
            "hand_position": "Center of chest, lower half of breastbone",
            "compression_ventilation_ratio": "30:2",
            "rescue_breath_duration": "1 second each",
            "special_considerations": [
                "Allow complete chest recoil",
                "Minimize interruptions",
                "Switch rescuers every 2 minutes"
            ]
        },
        "child": {
            "age_range": "1 year to puberty (approximately 8 years)",
            "compression_depth": "At least 1/3 chest diameter (approximately 2 inches or 5 cm)",
            "compression_rate": "100-120 per minute",
            "compression_technique": "One or two hands (depending on child size)",
            "hand_position": "Center of chest, lower half of breastbone",
            "compression_ventilation_ratio": "30:2 (single rescuer), 15:2 (two rescuers)",
            "rescue_breath_duration": "1 second each",
            "special_considerations": [
                "Use appropriate force for child's size",
                "Head tilt-chin lift may be less pronounced",
                "Consider child's fear and trauma"
            ]
        },
        "infant": {
            "age_range": "Under 1 year",
            "compression_depth": "At least 1/3 chest diameter (approximately 1.5 inches or 4 cm)",
            "compression_rate": "100-120 per minute",
            "compression_technique": "Two fingers or two thumbs (healthcare providers)",
            "hand_position": "Just below nipple line, lower half of breastbone",
            "compression_ventilation_ratio": "30:2 (single rescuer), 15:2 (two rescuers)",
            "rescue_breath_duration": "1 second each",
            "special_considerations": [
                "Support head and neck",
                "Gentle head tilt (neutral position)",
                "Cover mouth and nose with your mouth for rescue breathing",
                "Two-thumb technique preferred for healthcare providers"
            ]
        }
    }

def get_common_mistakes():
    """Get common CPR mistakes and how to avoid them"""
    return {
        "compression_mistakes": [
            {
                "mistake": "Insufficient depth",
                "problem": "Compressions less than 2 inches deep for adults",
                "solution": "Push hard enough to compress chest at least 2 inches",
                "impact": "Reduced blood flow and effectiveness"
            },
            {
                "mistake": "Incorrect rate",
                "problem": "Too fast (>120 BPM) or too slow (<100 BPM)",
                "solution": "Use metronome or count aloud to maintain 100-120 BPM",
                "impact": "Reduced cardiac output and blood circulation"
            },
            {
                "mistake": "Incomplete recoil",
                "problem": "Not allowing chest to return to normal position",
                "solution": "Completely release pressure between compressions",
                "impact": "Prevents blood from refilling the heart"
            },
            {
                "mistake": "Wrong hand position",
                "problem": "Hands too high, too low, or off-center",
                "solution": "Place heel of hand on center of chest between nipples",
                "impact": "Ineffective compressions, possible injury"
            }
        ],
        "breathing_mistakes": [
            {
                "mistake": "Excessive ventilation",
                "problem": "Breathing too fast or with too much force",
                "solution": "Give breaths slowly over 1 second each",
                "impact": "Reduces blood return to heart, gastric inflation"
            },
            {
                "mistake": "Inadequate seal",
                "problem": "Poor mouth-to-mouth seal allowing air to escape",
                "solution": "Ensure good seal and watch for chest rise",
                "impact": "Ineffective ventilation"
            },
            {
                "mistake": "Over-extension of head",
                "problem": "Tilting head too far back, especially in infants",
                "solution": "Use appropriate head position for age",
                "impact": "May close airway instead of opening it"
            }
        ],
        "general_mistakes": [
            {
                "mistake": "Delayed recognition",
                "problem": "Taking too long to recognize cardiac arrest",
                "solution": "Check responsiveness and breathing quickly (max 10 seconds)",
                "impact": "Delays life-saving intervention"
            },
            {
                "mistake": "Frequent interruptions",
                "problem": "Stopping compressions too often or for too long",
                "solution": "Minimize interruptions, continue compressions during most procedures",
                "impact": "Reduces perfusion pressure and survival chances"
            },
            {
                "mistake": "Rescuer fatigue",
                "problem": "Not switching rescuers when tired",
                "solution": "Switch every 2 minutes or when quality decreases",
                "impact": "Degraded compression quality over time"
            }
        ]
    }

def get_legal_considerations():
    """Get legal considerations for CPR"""
    return {
        "good_samaritan_laws": {
            "description": "Laws that protect people who give reasonable assistance to those in peril",
            "coverage": [
                "Protection from liability when acting in good faith",
                "Applies to trained and untrained rescuers",
                "Covers emergency situations outside of work duties",
                "Generally requires reasonable care without gross negligence"
            ],
            "limitations": [
                "May not apply if acting outside scope of training",
                "Does not protect against grossly negligent acts",
                "May vary by state or jurisdiction",
                "Professional rescuers may have different standards"
            ]
        },
        "consent": {
            "expressed_consent": "Conscious person gives verbal or written permission",
            "implied_consent": "Unconscious person assumed to want life-saving care",
            "special_situations": [
                "Minors: parent/guardian consent preferred when possible",
                "Medical alert jewelry indicating DNR orders",
                "Advanced directives or living wills"
            ]
        },
        "duty_to_act": {
            "general_public": "No legal duty to provide care in most jurisdictions",
            "professionals": "Healthcare workers may have duty to act",
            "special_relationships": "Lifeguards, coaches may have duty in their work environment"
        }
    }

def get_cpr_statistics():
    """Get CPR effectiveness statistics"""
    return {
        "survival_rates": {
            "out_of_hospital_cardiac_arrest": {
                "overall": "10.8%",
                "with_bystander_cpr": "16.3%",
                "without_bystander_cpr": "7.2%"
            },
            "in_hospital_cardiac_arrest": {
                "overall": "25.8%",
                "with_immediate_response": "40%+"
            }
        },
        "time_factors": {
            "brain_death_begins": "4-6 minutes without oxygen",
            "cpr_within_2_minutes": "Survival rate up to 80%",
            "cpr_within_4_minutes": "Survival rate 40-50%",
            "cpr_after_10_minutes": "Survival rate less than 5%"
        },
        "quality_factors": {
            "adequate_compression_depth": "Only 24% of bystanders achieve proper depth",
            "adequate_compression_rate": "37% maintain proper rate",
            "hands_only_cpr_effectiveness": "Equally effective as conventional CPR for first 6-8 minutes"
        },
        "demographics": {
            "cardiac_arrests_per_year": "Over 350,000 out-of-hospital in US",
            "bystander_cpr_rate": "40.2% nationally",
            "witnessed_arrests": "Better outcomes than unwitnessed"
        }
    }