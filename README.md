# 🧾 MultiLanguage Invoice Extractor

An AI-powered invoice analysis application built with **Streamlit, Google Gemini, and Python**.

The application allows users to upload an invoice image and ask questions about the invoice. Google Gemini analyzes the uploaded image along with the user's prompt and generates a response based on the invoice content.

---

## 🚀 Features

- 🧾 Upload invoice images
- 🖼️ Supports JPG, JPEG, and PNG
- 🤖 Analyze invoices using Google Gemini
- 💬 Ask questions about the uploaded invoice
- 🌍 Designed for multilingual invoice understanding
- ⚡ Interactive Streamlit interface
- 🔐 API key managed through environment variables
- 👁️ Multimodal AI — processes both text prompts and invoice images

---

## 🏗️ Architecture

```text
                ┌────────────────────┐
                │   Upload Invoice   │
                │    JPG/JPEG/PNG    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │    PIL / Image     │
                │   Image Loading    │
                └──────────┬─────────┘
                           │
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
         ▼                                   ▼
┌──────────────────┐               ┌──────────────────┐
│ System Prompt    │               │  User Question  │
│ Invoice Expert   │               │                  │
└────────┬─────────┘               └────────┬─────────┘
         │                                  │
         └────────────────┬─────────────────┘
                          │
                          ▼
                ┌────────────────────┐
                │    Google Gemini   │
                │  Multimodal Model  │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │   Generated Answer │
                └────────────────────┘
                           │
                           ▼
                ┌────────────────────┐
                │     Streamlit      │
                │      UI            │
                └────────────────────┘