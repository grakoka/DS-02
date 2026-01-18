import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from analytics import log_info, log_error

class Research:
    def create_report(self):
        try:
            log_info("Creating the report")

            log_info("Report created successfully")

            self.send_telegram_message("The report has been successfully created")
        except Exception as e:
            log_error(f"Error creating report: {str(e)}")
            self.send_telegram_message("The report hasn’t been created due to an error")

    def send_telegram_message(self, message):
        log_info(f"Preparing to send message: {message}")
        
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
        
        try:
            response = requests.post(url, data=data)
            log_info(f"Response from Telegram: {response.status_code} {response.text}")

            if response.status_code == 200:
                log_info("Message sent to Telegram successfully")
            else:
                log_error(f"Failed to send message to Telegram: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            log_error(f"Error sending message to Telegram: {e}")

if __name__ == '__main__':
    research = Research()
    research.create_report()
