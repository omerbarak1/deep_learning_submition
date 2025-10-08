# Auto-generated from notebook cell 9
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    # ודא שאין Callback של W&B
    try:
        from transformers.integrations import WandbCallback
        trainer.remove_callback(WandbCallback)
    except Exception as e:


    train_result = trainer.train()
    trainer.save_model("correct-question-generator")
    metrics_train = train_result.metrics
    metrics_eval = trainer.evaluate()


    eval_loss = metrics_eval.get("eval_loss", None)
    if eval_loss is not None:
        try:
            ppl = math.exp(eval_loss)
        except OverflowError:

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
