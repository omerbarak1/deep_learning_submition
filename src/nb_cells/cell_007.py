# Auto-generated from notebook cell 7
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    training_args = TrainingArguments(
        output_dir="correct-question-generator",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        gradient_accumulation_steps=1,
        warmup_steps=50,
        logging_steps=50,
        save_steps=300,
        eval_steps=300,
        eval_strategy="steps",
        save_strategy="steps",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        learning_rate=5e-4,
        lr_scheduler_type="linear",
        weight_decay=0.01,
        fp16=torch.cuda.is_available(),
        report_to=None,
        seed=42
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        tokenizer=tokenizer,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"],
        data_collator=data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
    )

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
