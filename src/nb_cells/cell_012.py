# Auto-generated from notebook cell 12
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    save_dir = "correct-question-generator"
    trainer.model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)

    # Zip for download if you're on Colab
    from google.colab import files
    files.download("correct-question-generator.zip")

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
