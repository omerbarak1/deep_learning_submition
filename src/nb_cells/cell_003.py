# Auto-generated from notebook cell 3
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    # ==== Data Synthesis ====
    import random

    def generate_synthetic_student():
        """Generate a random student profile with expanded features."""
        return {
            "mastery": {k: round(random.uniform(0, 1), 2) for k in
                        ["fractions", "geometry", "percentages", "algebra", "statistics"]},
            "psychology": {k: round(random.uniform(0, 1), 2) for k in
                           ["attention_level", "anxiety_sensitivity", "patience", "impulsivity", "motivation"]},
            "learning_style": {k: round(random.uniform(0, 1), 2) for k in
                               ["visual", "verbal", "kinesthetic"]},
            "interests": {k: round(random.uniform(0, 1), 2) for k in
                          ["sports", "puzzles", "history", "music", "science", "art"]},
            "goals": {k: round(random.uniform(0, 1), 2) for k in
                      ["grades", "understanding", "speed", "creativity"]}
        }

    def create_varied_prompts(student_state, topic, difficulty):
        """Create diverse question prompts using exact student parameters."""
        mastery = student_state["mastery"]
        psychology = student_state["psychology"]
        learning_style = student_state["learning_style"]
        interests = student_state["interests"]
        goals = student_state["goals"]

        # Get exact values
        topic_mastery = mastery.get(topic, 0.5)
        anxiety = psychology.get("anxiety_sensitivity", 0.5)
        attention = psychology.get("attention_level", 0.5)
        patience = psychology.get("patience", 0.5)
        motivation = psychology.get("motivation", 0.5)

        # Learning preferences
        visual_pref = learning_style.get("visual", 0.5)
        verbal_pref = learning_style.get("verbal", 0.5)
        kinesthetic_pref = learning_style.get("kinesthetic", 0.5)
        dominant_style = max(learning_style, key=learning_style.get)

        # Goals and interests
        creativity_goal = goals.get("creativity", 0.5)
        understanding_goal = goals.get("understanding", 0.5)
        speed_goal = goals.get("speed", 0.5)
        top_interest = max(interests, key=interests.get)

        # Create VERY different prompt structures (12+ styles)
        prompt_styles = []

        # 1) Direct instruction
        prompt_styles.append(
            f"Generate {topic} question: difficulty={difficulty}, mastery={topic_mastery:.2f}, "
            f"anxiety={anxiety:.2f}, style={dominant_style}, interest={top_interest}"
        )

        # 2) Narrative
        prompt_styles.append(
            f"A student loves {top_interest} and has {topic_mastery:.2f} mastery in {topic} with {anxiety:.2f} anxiety. "
            f"They learn best through {dominant_style} methods. Create a level {difficulty} question that excites them."
        )

        # 3) Problem-solving (for anxious students)
        if anxiety > 0.7:
            prompt_styles.append(
                f"Challenge: Help an anxious student (anxiety={anxiety:.2f}) with {topic_mastery:.2f} {topic} mastery. "
                f"Design a confidence-building level {difficulty} question using {dominant_style} approach and {top_interest} context."
            )

        # 4) Teacher briefing
        prompt_styles.append(
            f"Teacher briefing: Student profile shows {topic_mastery:.2f} {topic} mastery, {anxiety:.2f} anxiety, "
            f"{attention:.2f} attention span. Prefers {dominant_style} learning and enjoys {top_interest}. "
            f"Need level {difficulty} question."
        )

        # 5) Adaptive (weak/strong mastery)
        if topic_mastery < 0.3:
            prompt_styles.append(
                f"Struggling student alert: {topic} mastery only {topic_mastery:.2f}, anxiety at {anxiety:.2f}. "
                f"Needs gentle level {difficulty} question with {dominant_style} methods and {top_interest} motivation."
            )
        elif topic_mastery > 0.8:
            prompt_styles.append(
                f"Advanced student ready: {topic} mastery {topic_mastery:.2f}, low anxiety {anxiety:.2f}, "
                f"creativity goal {creativity_goal:.2f}. Needs challenging level {difficulty} question with {top_interest} themes."
            )

        # 6) Learning-focused (visual/kinesthetic)
        if visual_pref > 0.7:
            prompt_styles.append(
                f"Visual learner needs {topic} question: mastery={topic_mastery:.2f}, anxiety={anxiety:.2f}, "
                f"visual_pref={visual_pref:.2f}. Level {difficulty} with diagrams and {top_interest} imagery."
            )
        elif kinesthetic_pref > 0.7:
            prompt_styles.append(
                f"Hands-on learner profile: {topic} mastery {topic_mastery:.2f}, kinesthetic preference {kinesthetic_pref:.2f}, "
                f"anxiety {anxiety:.2f}. Create level {difficulty} manipulative-based question with {top_interest} activities."
            )

        # 7) Goal-oriented (creativity)
        if creativity_goal > 0.7:
            prompt_styles.append(
                f"Creative student seeking: {topic} exploration at level {difficulty}. Current mastery: {topic_mastery:.2f}, "
                f"anxiety: {anxiety:.2f}, creativity drive: {creativity_goal:.2f}. Incorporate {top_interest} and {dominant_style} methods."
            )

        # 8) Interest-first (very high interest)
        if interests[top_interest] > 0.8:
            prompt_styles.append(
                f"{top_interest.title()} enthusiast needs {topic} question! Mastery: {topic_mastery:.2f}, anxiety: {anxiety:.2f}, "
                f"learning style: {dominant_style}. Make level {difficulty} question that connects {topic} to {top_interest}."
            )

        # 9) Conversational
        buckets = ['struggling with', 'getting better at', 'excelling in']
        idx = min(int(topic_mastery * 2), 2)
        prompt_styles.append(
            f"I have a student who's {buckets[idx]} {topic} (mastery: {topic_mastery:.2f}). "
            f"They have {anxiety:.2f} anxiety and love {top_interest}. "
            f"Can you create a level {difficulty} question using {dominant_style} methods?"
        )

        # 10) Concise
        prompt_styles.append(
            f"Student: {topic}={topic_mastery:.2f}, anxiety={anxiety:.2f}, {dominant_style} learner, loves {top_interest}. "
            f"Need level {difficulty} question."
        )

        return prompt_styles

    def create_student_vector_string(student_state):
        """Convert student state to comprehensive vector string."""
        mastery = student_state.get("mastery", {})
        psychology = student_state.get("psychology", {})
        learning_style = student_state.get("learning_style", {})
        interests = student_state.get("interests", {})
        goals = student_state.get("goals", {})

        parts = []
        parts.append("mastery: " + ", ".join([f"{k}={v:.2f}" for k, v in mastery.items()]))
        parts.append("psychology: " + ", ".join([f"{k}={v:.2f}" for k, v in psychology.items()]))
        parts.append("learning_style: " + ", ".join([f"{k}={v:.2f}" for k, v in learning_style.items()]))
        parts.append("interests: " + ", ".join([f"{k}={v:.2f}" for k, v in interests.items()]))
        parts.append("goals: " + ", ".join([f"{k}={v:.2f}" for k, v in goals.items()]))
        return " | ".join(parts)

    # ---- Build examples ----
    examples = []
    topics = ["fractions", "geometry", "percentages", "algebra", "statistics"]
    N_EXAMPLES = int(os.environ.get("N_EXAMPLES", "2500"))

    for i in range(N_EXAMPLES):
        student_state = generate_synthetic_student()
        topic = random.choice(topics)
        difficulty = random.randint(1, 5)

        input_vector = create_student_vector_string(student_state)
        input_text = f"STUDENT: {input_vector} | TOPIC: {topic} | DIFFICULTY: {difficulty}"

        prompt_options = create_varied_prompts(student_state, topic, difficulty)
        output_prompt = random.choice(prompt_options)

        examples.append({
            "input": input_text,
            "output": output_prompt,
            "topic": topic,
            "difficulty": str(difficulty)
        })

        if (i + 1) % 500 == 0:

    sample = examples[0]

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
