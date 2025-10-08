# Auto-generated from notebook cell 8
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    # --- Hard-kill W&B in this runtime (no restart needed) ---
    import os, sys, types

    # כבה שירותים חיצוניים
    os.environ["WANDB_DISABLED"] = "true"
    os.environ["WANDB_MODE"] = "offline"
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

    # נקה import קודם אם נטען
    if "wandb" in sys.modules:
        del sys.modules["wandb"]

    # הזרק מודול דמה שמבטל כל קריאה ל-wandb
    wandb = types.SimpleNamespace(
        init=lambda *a, **k: None,
        log=lambda *a, **k: None,
        watch=lambda *a, **k: None,
        finish=lambda *a, **k: None,
        run=None,
        config={}
    )
    sys.modules["wandb"] = wandb

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
