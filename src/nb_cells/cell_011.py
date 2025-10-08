# Auto-generated from notebook cell 11
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    # ==== Quick test (fixed) — anti-repetition + self-contained helpers ====
    import re, torch, random
    from typing import Dict, Any
    from collections import OrderedDict

    # If these helpers already exist earlier, you can delete these re-definitions.
    def create_student_vector_string(student_state: Dict[str, Dict[str, float]]) -> str:
        mastery = student_state.get("mastery", {})
        psychology = student_state.get("psychology", {})
        learning_style = student_state.get("learning_style", {})
        interests = student_state.get("interests", {})
        goals = student_state.get("goals", {})
        parts = []
        parts.append("mastery: " + ", ".join([f"{k}={float(v):.2f}" for k, v in mastery.items()]))
        parts.append("psychology: " + ", ".join([f"{k}={float(v):.2f}" for k, v in psychology.items()]))
        parts.append("learning_style: " + ", ".join([f"{k}={float(v):.2f}" for k, v in learning_style.items()]))
        parts.append("interests: " + ", ".join([f"{k}={float(v):.2f}" for k, v in interests.items()]))
        parts.append("goals: " + ", ".join([f"{k}={float(v):.2f}" for k, v in goals.items()]))
        return " | ".join(parts)

    def make_input_v2(student_state: Dict[str, Any], topic: str, difficulty: int) -> str:
        return f"STUDENT: {create_student_vector_string(student_state)} | TOPIC: {topic} | DIFFICULTY: {difficulty}"

    def make_state_v2(
        mastery: Dict[str, float] = None,
        psychology: Dict[str, float] = None,
        learning_style: Dict[str, float] = None,
        interests: Dict[str, float] = None,
        goals: Dict[str, float] = None,
    ):
        _mastery = {"fractions": 0.40, "geometry": 0.55, "percentages": 0.45, "algebra": 0.50, "statistics": 0.50}
        _psych = {"attention_level": 0.60, "anxiety_sensitivity": 0.30, "patience": 0.70, "impulsivity": 0.40, "motivation": 0.65}
        _style = {"visual": 0.50, "verbal": 0.50, "kinesthetic": 0.50}
        _ints  = {"sports": 0.30, "puzzles": 0.30, "history": 0.30, "music": 0.30, "science": 0.30, "art": 0.30}
        _goals = {"grades": 0.50, "understanding": 0.60, "speed": 0.50, "creativity": 0.50}
        if mastery: _mastery.update(mastery)
        if psychology: _psych.update(psychology)
        if learning_style: _style.update(learning_style)
        if interests: _ints.update(interests)
        if goals: _goals.update(goals)
        r2 = lambda d: {k: round(float(v), 2) for k, v in d.items()}
        return {"mastery": r2(_mastery), "psychology": r2(_psych), "learning_style": r2(_style), "interests": r2(_ints), "goals": r2(_goals)}

    # --- Tail trimming: cut repetitive tail and keep 1–3 clean sentences ---
    def trim_repetitive_tail(text: str, max_sentences: int = 3) -> str:
        text = re.sub(r'\s+', ' ', text).strip()
        text = re.sub(r'([?!\.])\1{1,}', r'\1', text)   # "????" -> "?"
        parts = re.split(r'(?<=[\.\!\?])\s+', text)
        clean, seen_norm = [], set()
        for s in parts:
            s = s.strip()
            if not s:
                continue
            norm = re.sub(r'\d+', '<NUM>', s.lower())
            # stop if we already saw a very similar sentence
            if norm in seen_norm:
                break
            # after we already kept at least one good sentence, stop when generic "create/make/need..." repeats start
            if len(clean) >= 30 and re.match(r'^(create|make|need|can you|design)\b.*\b(level|question)\b', s.lower()):
                break
            clean.append(s)
            seen_norm.add(norm)
            if len(clean) >= max_sentences:
                break
        return " ".join(clean).strip()

    @torch.inference_mode()
    def generate_prompt_v2(model, tokenizer, student_state: Dict[str, Any],
                           topic: str = "fractions", difficulty: int = 2,
                           max_new_tokens: int = 80,
                           temperature: float = 0.7,
                           top_p: float = 0.9, top_k: int = 50,
                           repetition_penalty: float = 1.15,
                           no_repeat_ngram_size: int = 5,
                           do_sample: bool = True) -> str:
        model.eval()
        prefix = make_input_v2(student_state, topic, difficulty)
        inputs = tokenizer([prefix], return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
            model = model.cuda()
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p, top_k=top_k,
            do_sample=do_sample,
            repetition_penalty=repetition_penalty,
            no_repeat_ngram_size=no_repeat_ngram_size,
            pad_token_id=tokenizer.eos_token_id
        )
        decoded = tokenizer.decode(out[0], skip_special_tokens=True)
        gen = decoded[len(prefix):].strip()
        return trim_repetitive_tail(gen, max_sentences=3)

    # ----- Example runs -----
    state1 = make_state_v2(
        mastery={"fractions": 0.10, "algebra": 0.95},
        psychology={"anxiety_sensitivity": 0.90, "attention_level": 0.45, "patience": 0.60},
        learning_style={"visual": 0.90, "verbal": 0.35, "kinesthetic": 0.25},
        interests={"music": 0.92, "science": 0.55, "sports": 0.10},
        goals={"understanding": 0.80, "creativity": 0.65, "speed": 0.35}
    )

    state2 = make_state_v2(
        mastery={"geometry": 0.88, "fractions": 0.40},
        psychology={"anxiety_sensitivity": 0.20, "motivation": 0.85},
        learning_style={"kinesthetic": 0.85, "visual": 0.40, "verbal": 0.30},
        interests={"puzzles": 0.85, "art": 0.20},
        goals={"speed": 0.85, "grades": 0.70}
    )

    tests = [
        ("fractions", 1, state1),
        ("geometry", 4, state2),
        ("statistics", 3, make_state_v2())
    ]

    for i, (topic, diff, st) in enumerate(tests, 1):
        gen = generate_prompt_v2(trainer.model, tokenizer, st, topic=topic, difficulty=diff,
                                 max_new_tokens=100, temperature=0.7, top_p=0.9, do_sample=True)

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
