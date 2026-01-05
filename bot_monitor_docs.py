import requests
import hashlib
import schedule
import time
import os
from datetime import datetime

# ================= CONFIGURAÇÕES =================
BOT_TOKEN = "8363564066:AAGT4m4I-kLa_WkDWe7u31uoPS6fZnPchrE"
CHAT_ID = "167753189"
DOC_ID = "1DZv3vwfuipKGdlq_BIOYNTT9HQEopqo6IZxJ4iDw2tg"
CHECK_INTERVAL_MINUTES = 60
HASH_FILE = "last_hash.txt"
# =================================================

def get_doc_text():
    url = f"https://docs.google.com/document/d/{DOC_ID}/export?format=txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def calculate_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }
    requests.post(url, json=payload)

def check_for_updates():
    try:
        text = get_doc_text()
        current_hash = calculate_hash(text)

        last_hash = None
        if os.path.exists(HASH_FILE):
            with open(HASH_FILE, "r") as f:
                last_hash = f.read().strip()

        if current_hash != last_hash:
            now = datetime.now().strftime("%d/%m/%Y %H:%M")
            send_telegram_message(
                f"📄 Documento do Internato CLM atualizado\n"
                f"🕒 {now}\n"CHECK_INTERVAL_MINUTES = 60

                f"🔗 https://docs.google.com/document/d/{DOC_ID}"
            )
            with open(HASH_FILE, "w") as f:
                f.write(current_hash)

    except Exception as e:
        send_telegram_message(f"⚠️ Erro ao verificar o documento:\n{e}")

schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(check_for_updates)

print("🤖 Bot iniciado. Monitorando alterações no Google Docs...")

while True:
    schedule.run_pending()
    time.sleep(10)
