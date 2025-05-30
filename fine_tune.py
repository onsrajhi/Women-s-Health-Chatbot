from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.training_args import TrainingArguments
from transformers.trainer import Trainer

# Load your dataset, specify split to get a Dataset (not DatasetDict)
dataset = load_dataset("json", data_files="data/merged_data.json", split="train")

# Preprocess the dataset to merge prompt and response into a single text field
def preprocess(examples):
    # Format: "User: prompt\nBot: response"
    examples["text"] = [f"User: {p}\nBot: {r}" for p, r in zip(examples["prompt"], examples["response"])]
    return examples

dataset = dataset.map(preprocess, batched=True)

# Load tokenizer and model
model_name = "mistralai/Mistral-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenization function
def tokenize_fn(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512)

tokenized_dataset = dataset.map(tokenize_fn, batched=True)

# Set training arguments
training_args = TrainingArguments(
    output_dir="./fine_tuned_women_health_bot",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    logging_steps=10,
    save_steps=100,
    evaluation_strategy="no",  # or "steps" if you add eval_dataset later
    learning_rate=2e-5,
    weight_decay=0.01,
    fp16=True,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train the model
trainer.train()
