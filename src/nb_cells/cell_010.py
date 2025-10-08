# Auto-generated from notebook cell 10
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    def synth_state(
        fractions=0.40, geometry=0.35,
        percentages=0.60, algebra=0.2, probability=0.50
        anxiety_sensitivity=0.30, patience=0.70, learning_style="visual",
        interests=("music", "coding"), goals="improve problem solving"
    ):
        mastery = {
            "fractions": fractions,
            "geometry": geometry,
            "percentages": percentages,
            "algebra": algebra,
            "probability": probability,

        }
        psychology = {"anxiety_sensitivity": anxiety_sensitivity, "patience": patience}
        return {
            "mastery": {k: round(v, 2) for k, v in mastery.items()},
            "psychology": {k: round(v, 2) for k, v in psychology.items()},
            "learning_style": learning_style,
            "interests": list(interests),
            "goals": goals
        }

    def make_input_from_state(st: Dict[str, Any], topic: str, difficulty: str):
        return (
            f"STUDENT_STATE: {create_student_vector_string(st)}\n"
            f"TOPIC: {topic}\n"
            f"DIFFICULTY: {difficulty}\n"
            f"QUESTION_PROMPT:"
        )

    @torch.inference_mode()
    def generate_prompt_v2(model, tokenizer, student_state: Dict[str, Any],
                           topic: str = "fractions", difficulty: int = 2,
                           max_new_tokens: int = 80,     # קצר = פחות חזרות
                           temperature: float = 0.7,
                           top_p: float = 0.9, top_k: int = 50,
                           repetition_penalty: float = 1.15,
                           no_repeat_ngram_size: int = 5,
                           do_sample: bool = True) -> str:
        model.eval()
        text = f"STUDENT: {create_student_vector_string(student_state)} | TOPIC: {topic} | DIFFICULTY: {difficulty}"
        inputs = tokenizer([text], return_tensors="pt")
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
        gen = decoded[len(text):].strip()

        # ✂️ חיתוך הזנב החזרתי
        gen = trim_repetitive_tail(gen, max_sentences=3)
        return gen

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
