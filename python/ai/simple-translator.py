import argparse
import os
import sys

from openai import OpenAI


# ============================================================
# 1. API CLIENT
# ============================================================

# Ambil API key dari environment variable.
# Kalau tidak ada, fallback ke hardcode (untuk testing).
#
# Cara set environment variable:
#   export OPENAI_API_KEY="sk-or-v1-xxxxx"
#
# Atau pakai file .env (lihat komentar di bawah).

OPENAI_API_KEY = ""


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
)


# ============================================================
# 2. ARGUMENT PARSER
# ============================================================

parser = argparse.ArgumentParser(
    description="Translator Bahasa Indonesia → Bahasa Inggris via OpenRouter"
)
parser.add_argument(
    "--message",
    "-m",
    required=True,
    help="Teks Bahasa Indonesia yang ingin diterjemahkan",
)
args = parser.parse_args()


# ============================================================
# 3. REQUEST KE AI
# ============================================================

# Pakai router "openrouter/free" supaya otomatis memilih
# model gratis yang sedang aktif. Ini menghindari error 404
# karena model spesifik dinonaktifkan.
#
# Kalau ingin pakai model spesifik, ganti dengan:
#   model="nvidia/nemotron-3.5-lightning:free"
#   model="google/gemma-3-27b-it:free"
#   model="qwen/qwen3-32b:free"
#   model="meta-llama/llama-3.1-8b-instruct:free"

try:
    response = client.responses.create(
        model="openrouter/free",
        instructions=(
            "You are a professional translator. "
            "Translate Indonesian to English accurately and naturally. "
            "Output ONLY the translation, without any additional explanation."
        ),
        input=args.message,
    )

    result = response.output_text.strip()

    if not result:
        print("⚠️ Model tidak mengembalikan hasil. Coba lagi atau ganti model.")
        sys.exit(1)

    print(result)

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
