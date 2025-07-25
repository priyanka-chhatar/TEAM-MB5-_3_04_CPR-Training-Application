import streamlit as st
import plotly.express as px

# Page config
st.set_page_config(
    page_title="CPR Educational Content",
    page_icon="📚",
    layout="wide"
)

# ------------------ DATA FUNCTIONS ------------------

def get_cpr_steps():
    return [
        {"title": "Check Responsiveness", "description": "Tap the person and shout, 'Are you okay?'", "details": "If no response, begin CPR."},
        {"title": "Call Emergency Services", "description": "Call 911 or ask someone nearby.", "details": "Put phone on speaker."},
        {"title": "Open the Airway", "description": "Tilt head back, lift chin."},
        {"title": "Check for Breathing", "description": "Look, listen, and feel for up to 10 seconds."},
        {"title": "Start Chest Compressions", "description": "Push hard and fast in center of chest.", "details": "At least 2 inches deep at 100-120 BPM."},
        {"title": "Give Rescue Breaths (if trained)", "description": "2 breaths after 30 compressions.", "details": "Seal mouth and breathe in."},
        {"title": "Continue CPR", "description": "Repeat 30:2 cycle until help arrives."}
    ]

def get_cpr_content():
    return {
        "AHA": "2020 American Heart Association Guidelines: Focus on high-quality CPR...",
        "ERC": "European Resuscitation Council: Early recognition and defibrillation...",
        "ILCOR": "ILCOR: Global CPR science updates and harmonization."
    }

def get_emergency_scenarios():
    return [
        {
            "title": "Cardiac Arrest",
            "description": "Sudden loss of heart function, breathing, and consciousness.",
            "steps": ["Call 911", "Start CPR immediately", "Use AED if available"],
            "warning": "Begin CPR without delay."
        },
        {
            "title": "Choking",
            "description": "Blocked airway from object.",
            "steps": ["Ask if they're choking", "Perform Heimlich maneuver", "If unconscious, begin CPR"]
        },
        {
            "title": "Drowning",
            "description": "Water submersion injury.",
            "steps": ["Ensure scene safety", "Remove from water", "Check breathing", "Start CPR if needed"]
        }
    ]

# ------------------ MAIN APP ------------------

def main():
    st.title("📚 CPR Educational Content")
    st.markdown("Comprehensive guide to CPR techniques and emergency response")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🫀 Basic CPR", "👶 Infant CPR", "🚨 Emergency Response", "📖 Guidelines", "🎥 Interactive Guide"
    ])

    with tab1:
        show_basic_cpr()
    with tab2:
        show_infant_cpr()
    with tab3:
        show_emergency_response()
    with tab4:
        show_guidelines()
    with tab5:
        show_interactive_guide()

# ------------------ TAB FUNCTIONS ------------------

def show_basic_cpr():
    st.header("Adult CPR (Cardiopulmonary Resuscitation)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🎯 When to Perform CPR")
        st.write("""
        - Unconscious and unresponsive  
        - Not breathing normally  
        - No pulse (if trained to check)
        """)
        st.subheader("📋 Step-by-Step Instructions")
        steps = get_cpr_steps()
        for i, step in enumerate(steps, 1):
            with st.expander(f"Step {i}: {step['title']}"):
                st.write(step['description'])
                if 'details' in step:
                    st.info(step['details'])
    with col2:
        st.subheader("⚡ Key Numbers")
        st.metric("Compression Rate", "100–120 BPM")
        st.metric("Compression Depth", "2+ inches (5+ cm)")
        st.metric("Compression:Rescue Ratio", "30:2")
        st.metric("Hand Position", "Center of chest")
        st.subheader("⚠ Important Points")
        st.warning("""
        - Push hard and fast  
        - Allow full chest recoil  
        - Minimize interruptions  
        - Switch every 2 minutes if possible
        """)

def show_infant_cpr():
    st.header("👶 Infant CPR (Under 1 year)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🔍 Key Differences from Adult CPR")
        differences = [
            {"aspect": "Compression Method", "adult": "2 hands", "infant": "2 fingers or 2 thumbs"},
            {"aspect": "Compression Depth", "adult": "≥ 2 inches", "infant": "≥ 1.5 inches"},
            {"aspect": "Location", "adult": "Center of chest", "infant": "Below nipple line"},
            {"aspect": "Airway Opening", "adult": "Tilt head back", "infant": "Neutral position"}
        ]
        for diff in differences:
            st.write(f"**{diff['aspect']}**")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"👨 Adult: {diff['adult']}")
            with col_b:
                st.write(f"👶 Infant: {diff['infant']}")
            st.markdown("---")
    with col2:
        st.subheader("📊 Infant CPR Metrics")
        st.metric("Compression Rate", "100–120 BPM")
        st.metric("Depth", "≥ 1.5 inches (4 cm)")
        st.metric("Ratio", "30:2")
        st.error("Infants decline rapidly — call emergency services immediately!")

def show_emergency_response():
    st.header("🚨 Emergency Response Protocol")
    scenarios = get_emergency_scenarios()
    for scenario in scenarios:
        with st.expander(f"🚨 {scenario['title']}"):
            st.write(scenario['description'])
            if 'steps' in scenario:
                st.subheader("Response Steps:")
                for i, step in enumerate(scenario['steps'], 1):
                    st.write(f"{i}. {step}")
            if 'warning' in scenario:
                st.warning(scenario['warning'])

def show_guidelines():
    st.header("📖 Official CPR Guidelines")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏥 AHA Guidelines")
        st.write("""
        **Key Points:**  
        - Compression rate: 100–120/min  
        - Depth: ≥2 inches for adults  
        - Full recoil and minimal pauses  
        - Compression-only CPR for untrained
        """)
    with col2:
        st.subheader("🌍 International Standards")
        st.write("""
        - *ERC, ILCOR, UK Resuscitation Council*  
        - Early recognition and CPR  
        - Quick defibrillation  
        - Post-resuscitation care
        """)
    st.subheader("📊 CPR Effectiveness Statistics")
    locations = ['Hospital', 'Home', 'Public', 'Workplace']
    survival_rates = [25, 12, 10, 15]
    fig = px.bar(
        x=locations,
        y=survival_rates,
        title="Survival Rates by Location",
        labels={'x': 'Location', 'y': 'Survival Rate (%)'},
        color=survival_rates,
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig, use_container_width=True)

def show_interactive_guide():
    st.header("🎥 Interactive CPR Guide")
    technique = st.selectbox("Choose CPR Technique:", [
        "Adult CPR", "Child CPR", "Infant CPR", "Compression-Only CPR"
    ])
    if technique == "Adult CPR":
        show_adult_cpr_guide()
    elif technique == "Child CPR":
        show_child_cpr_guide()
    elif technique == "Infant CPR":
        show_infant_cpr_visual()
    else:
        show_compression_only_guide()

    st.markdown("---")
    st.subheader("🎵 Rhythm Training")
    col1, col2 = st.columns([2, 1])
    with col1:
        bpm = st.slider("Target BPM", 100, 120, 110)
        if st.button("🎵 Start Metronome"):
            st.session_state.metronome_bpm = bpm
            st.success(f"Metronome set to {bpm} BPM")
    with col2:
        st.info(f"""
        *Current BPM:* {st.session_state.get('metronome_bpm', 110)}  
        *Interval:* {60 / st.session_state.get('metronome_bpm', 110):.2f} sec
        """)

def show_adult_cpr_guide():
    st.subheader("👨 Adult CPR Technique")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Hand Position:**\n- Heel of one hand on center of chest\n- Interlock fingers\n- Straight arms over chest")
    with col2:
        st.info("**Compression Technique:**\n- Push hard and fast\n- At least 2 inches deep\n- Full recoil")

def show_child_cpr_guide():
    st.subheader("🧒 Child CPR Technique (1–8 years)")
    st.write("""
    - Use 1 or 2 hands  
    - Depth: ≥1/3 chest (~2 inches)  
    - Ratio: 30 compressions to 2 breaths  
    """)

def show_infant_cpr_visual():
    st.subheader("👶 Infant CPR Guide")
    technique = st.radio("Choose technique:", ["Two-Finger", "Two-Thumb (preferred)"])
    if technique == "Two-Finger":
        st.info("""
        - Place 2 fingers below nipple line  
        - Compress at least 1.5 inches  
        - Allow full recoil
        """)
    else:
        st.info("""
        - Encircle chest with both hands  
        - Use thumbs for compressions  
        - Support back with fingers
        """)

def show_compression_only_guide():
    st.subheader("🫀 Compression-Only CPR")
    st.success("Ideal for untrained bystanders.")
    st.write("""
    - Call 911  
    - Push hard and fast in center of chest  
    - No rescue breaths  
    - Continue until help arrives
    """)
    st.warning("Effective for first few minutes of cardiac arrest.")

# ------------------ RUN ------------------

if __name__ == "__main__":
    main()
