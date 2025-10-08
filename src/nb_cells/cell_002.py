# Auto-generated from notebook cell 2
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    def set_global_seeds(seed: int = 42):
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    set_global_seeds(42)

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
