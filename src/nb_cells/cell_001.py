# Auto-generated from notebook cell 1
def run(ctx: dict) -> dict:
    # Bring prior context into local scope
    locals().update(ctx)
    import os, re, math, random, json, time, gc, textwrap
    from dataclasses import dataclass
    import numpy as np


    import torch
    from transformers import (
        AutoTokenizer, AutoModelForCausalLM,
        DataCollatorForLanguageModeling,
        Trainer, TrainingArguments, EarlyStoppingCallback
    )
    from datasets import Dataset, DatasetDict
    from typing import Dict, Any

    if torch.cuda.is_available():

    # Push updated locals back to context
    ctx.update({k: v for k, v in locals().items() if k not in ["__name__", "__doc__", "__package__"]})
    return ctx
