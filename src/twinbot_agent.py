
import os
from dotenv import load_dotenv
from ollama_telegrambot_api.agent import TelegramAgent
# Load .env file
load_dotenv()

# SPECIFIC CONFIGURATIONS - PLEASE CHANGE ACCORDINGLY
# It is needed to create an .env file with the TELEGRAM_TOKEN
# Need to create a Telegrambot and get the token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# This is the chat_id (user or group) of the person who will receive the notifications
NOTIFICATION_TELEGRAM_ID = os.getenv("NOTIFICATION_TELEGRAM_ID")
# It is important to specify the right model
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL")
# URL is the standard URL for the Ollama API
OLLAMA_URL: str = os.getenv("OLLAMA_URL")

# STANDARD CONFIGURATIONS - CHANGE ONLY IF NECESSARY
# Logger name - Name of the logger file
LOGGER_NAME: str = "ollama_chatbot"
# Logger directory path - Path to the directory where the log file will be stored
LOGGER_DIRECTORY_PATH: str = "/app/logs/"

# Disclaimer messages are sent to users to inform them about the bot's capabilities and limitations
DISCLAIMER_MESSAGE = (
    "<b>✨ Didac's Digital Twinbot ✨</b>\n\n"
    "Welcome 👋 to the Twinbot! This AI-powered assistant 🤖 is a proof of concept 🚀, created using Ollama 🦙 and trained on data inspired by my real-life experiences 🌟.\n\n"
    "To ensure safety and privacy 🔒, the dataset has been carefully curated 🧐 to avoid sharing sensitive personal information 🤫.\n\n"
    "You can interact with the Twinbot 💬 by asking any question ❓ you'd like to know about me 🤔.\n\n"
    "<i>As this is an experimental 🧪 setup running on compact, energy-efficient 🔋 hardware — specifically a Raspberry Pi 5 💻 without a GPU 🧠 — execution times may be slightly longer ⏳.</i>\n\n"
    "Thank you 🙏 for your patience, and enjoy the experience! 😉"
)
# Minimum time between disclaimer messages (in seconds)
MIN_TIME_BETWEEN_DISCLAIMERS = 3 * 24 * 60 * 60  # 3 days

def main() -> None:
    Agent = TelegramAgent(
        ollama_url=OLLAMA_URL,
        ollama_model=OLLAMA_MODEL,
        logger_name=LOGGER_NAME,
        telegram_token=TELEGRAM_TOKEN,
        notification_telegram_id = NOTIFICATION_TELEGRAM_ID,
        disclaimer_message=DISCLAIMER_MESSAGE,
        min_time_between_disclaimers=MIN_TIME_BETWEEN_DISCLAIMERS,
        logger_directory_path=LOGGER_DIRECTORY_PATH,
    )
    Agent.run()

if __name__ == '__main__':
    main()