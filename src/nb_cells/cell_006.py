# Auto-generated from notebook cell 6
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    def tokenize_with_labels_fixed(batch):
        full_texts   = [f"{inp}\n{out}{tokenizer.eos_token}" for inp, out in zip(batch["input"], batch["output"])]
        prefix_texts = [f"{inp}\n" for inp in batch["input"]]

        enc_full = tokenizer(full_texts, truncation=True, max_length=400, padding="max_length")
        enc_pref = tokenizer(prefix_texts, truncation=True, max_length=400, padding="max_length", add_special_tokens=False)

        labels = []
        for ids, pref in zip(enc_full["input_ids"], enc_pref["input_ids"]):
            L = min(len(pref), len(ids))
            lab = list(ids)
            for i in range(L):
                lab[i] = -100
            labels.append(lab)

        enc_full["labels"] = labels
        return enc_full

    tokenized = dataset.map(
        tokenize_with_labels_fixed,
        batched=True,
        remove_columns=dataset["train"].column_names
    )


    from transformers import DataCollatorForLanguageModeling
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
