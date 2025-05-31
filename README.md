# Women’s Health Chatbot 🤖🌸

This repository contains code, data, and deployment instructions to create a **domain-specific chatbot** focused on women’s health topics, including periods, pregnancy, breast cancer, menopause, fertility, and more.

![women's health](women%27s%20health.png)




The chatbot is **fine-tuned on a custom dataset** using Hugging Face Transformers, and deployed via a **Gradio** web UI for easy interaction.

---

## 💡 Overview

Model: DialoGPT (small/medium)

Fine-tuning method: LoRA (memory-efficient parameter tuning)

Dataset: Custom JSON file with question-answer pairs (small size ~10 KB)

Goal: Make the chatbot respond based on the domain-specific dataset

---

## 💡 Important Notes

The dataset is very small (only a few examples). Fine-tuning a large model like DialoGPT on such a small dataset leads to overfitting and repeated answers.

LoRA reduces training costs but cannot compensate for lack of data.

For better results, use a larger dataset or consider retrieval-based approaches.

DialoGPT is optimized for open-domain dialogue, so it may not perfectly fit closed-domain QA tasks.



----
## 💡 LImitations

Small dataset causes limited generalization.

Model may repeat answers or return unrelated responses.

For production or better accuracy, increase dataset size or use retrieval-based models.

