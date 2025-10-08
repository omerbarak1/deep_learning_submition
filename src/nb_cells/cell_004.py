# Auto-generated from notebook cell 4
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    dataset = Dataset.from_list(examples)
    dataset = dataset.train_test_split(test_size=0.1, seed=42)
    dataset = DatasetDict({
        "train": dataset["train"],
        "test": dataset["test"]
    })
    dataset

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
