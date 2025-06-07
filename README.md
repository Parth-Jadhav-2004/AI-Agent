# AI News Agent

An intelligent daily news agent that scrapes AI-related articles, summarizes them using Google's Gemini API, and sends professional email digests.

## Features

- 🌐 **Web Scraping**: Automatically scrapes AI news from multiple reputable sources
- 🤖 **AI Summarization**: Uses Google's Gemini API for intelligent article summarization
- 📧 **Professional Emails**: Sends beautifully formatted HTML email digests
- ⏰ **Automated Scheduling**: Configurable daily scheduling
- 🔧 **Highly Configurable**: Easy configuration through YAML files
- 📊 **Comprehensive Logging**: Detailed logging for monitoring and debugging

## Quick Start

### 1. Installation

```bash
# Clone or download the project
cd "AI Agent"

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

1. **Copy environment file:**
   ```bash
   copy .env.example .env
   ```

2. **Get Gemini API Key:**
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Create a new API key
   - Add it to your `.env` file

3. **Configure Email:**
   - For Gmail: Enable 2FA and create an [App Password](https://support.google.com/accounts/answer/185833)
   - Add your email and app password to `.env`

4. **Update Recipients:**
   - Edit `config/config.yaml`
   - Update the recipients section with your email details

### 3. Test Setup

```bash
# Test the configuration
python main.py
```

## Configuration

### Main Configuration (`config/config.yaml`)

```yaml
# News Sources - Add or remove sources as needed
news_sources:
  - name: "AI News"
    url: "https://www.artificialintelligence-news.com/"
    enabled: true

# Email Recipients
email:
  recipients:
    - email: "your-email@example.com"
      name: "Your Name"

# Scheduling
scheduling:
  daily_time: "08:00"  # 24-hour format
  timezone: "UTC"
```

### Environment Variables (`.env`)

```bash
GEMINI_API_KEY=your_gemini_api_key_here
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
```

## Usage

### Run Once (Manual)
```bash
python main.py
```

### Scheduled Execution

#### Option 1: Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for daily at your preferred time
4. Set action to start your Python script

#### Option 2: Python Scheduler (Keep Running)
Modify `main.py` to use the scheduler:

```python
from src.scheduler.news_scheduler import NewsScheduler

def main():
    config = ConfigManager()
    logger = setup_logging(config)
    
    orchestrator = NewsOrchestrator(config)
    scheduler = NewsScheduler(config)
    
    # Schedule daily task
    scheduler.schedule_daily_task(orchestrator.run_daily_process)
    scheduler.start_scheduler()
    
    # Keep running
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        scheduler.stop_scheduler()
```

## Project Structure

```
AI Agent/
├── src/
│   ├── scrappers/          # Web scraping modules
│   ├── summarizer/         # Gemini API integration
│   ├── email/              # Email formatting and sending
│   ├── scheduler/          # Task scheduling
│   ├── config_manager.py   # Configuration management
│   └── orchestrator.py     # Main coordination logic
├── config/
│   └── config.yaml         # Main configuration file
├── logs/                   # Application logs
├── main.py                 # Entry point
└── requirements.txt        # Dependencies
```

## Customization

### Adding New News Sources

Edit `config/config.yaml`:

```yaml
news_sources:
  - name: "Your News Source"
    url: "https://example.com/ai-news"
    enabled: true
```

### Modifying Email Template

Edit `src/email/email_formatter.py` to customize the HTML template.

### Changing Summarization Prompts

Edit `src/summarizer/gemini_summarizer.py` to modify the Gemini prompts.

## Troubleshooting

### Common Issues

1. **"Gemini API key not found"**
   - Ensure your `.env` file has the correct API key
   - Verify the key is valid at [Google AI Studio](https://makersuite.google.com/)

2. **Email sending fails**
   - For Gmail: Ensure you're using an App Password, not your regular password
   - Check that 2FA is enabled on your Google account
   - Verify SMTP settings in `config.yaml`

3. **No articles found**
   - Check if the news sources are accessible
   - Verify your internet connection
   - Look at logs in `logs/ai_news_agent.log`

### Enable Debug Logging

Edit `config/config.yaml`:

```yaml
logging:
  level: "DEBUG"
```

## API Keys

### Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/)
2. Sign in with your Google account
3. Click "Get API Key"
4. Create a new API key
5. Copy and paste into your `.env` file

### Email App Password (Gmail)
1. Enable 2-factor authentication on your Google account
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new app password for "Mail"
4. Use this password in your `.env` file (not your regular Google password)

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the logs in `logs/ai_news_agent.log`
2. Verify your configuration files
3. Test your API keys and email settings
4. Create an issue with detailed error information

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
