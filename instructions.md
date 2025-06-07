# AI Agent Development Prompt: Daily AI News Summarizer and Emailer with Gemini API

## Objective
Develop an AI agent that:
1. Scrapes recent AI-related news articles from specified websites.
2. Summarizes the articles using the Gemini API.
3. Formats the summaries into a professional email.
4. Sends the email daily to a user-specified email address at a scheduled time.

The solution should be reliable, maintainable, and user-friendly, with error handling and logging for robustness.

## Project Requirements

### 1. Web Scraping
- **Target Websites**: Scrape AI news from reputable sources, such as:
  - https://www.artificialintelligence-news.com/
  - https://www.theverge.com/ai-artificial-intelligence
  - https://techcrunch.com/category/artificial-intelligence/
  - Allow for easy addition of new sources in the future.
- **Data to Extract**:
  - Article title.
  - Publication date (to ensure only recent articles, e.g., within the last 24 hours).
  - Article summary or first paragraph (if a summary is not explicitly provided).
  - URL to the full article.
- **Scraping Method**:
  - Use a Python-based web scraping library (e.g., BeautifulSoup or Scrapy).
  - Respect website terms of service and robots.txt.
  - Implement rate limiting to avoid overwhelming servers.
  - Handle dynamic content (JavaScript-rendered pages) using tools like Selenium or Playwright if needed.

### 2. News Summarization
- **Summary Generation**:
  - Use the **Gemini API** (provided by Google) to generate concise summaries (50–100 words per article).
  - Ensure summaries are factual, capturing the main points without introducing errors or bias.
  - If the article provides a summary, refine it for clarity and brevity using the Gemini API rather than generating a new one.
- **Input**: Raw article text or extracted summary.
- **Output**: A clear, concise summary with proper grammar and professional tone.
- **Gemini API Integration**:
  - Use the Gemini API client library for Python (e.g., `google-generativeai`).
  - Configure API access with a user-provided API key stored securely (e.g., in environment variables).
  - Craft prompts for Gemini to produce summaries, e.g.:
    - "Summarize the following article in 50–100 words, focusing on the main points and maintaining a professional tone: [article text]"
  - Handle API rate limits and errors (e.g., retry logic for failed requests).
  - Include fallback logic (e.g., use extracted summary if API fails).

### 3. Email Formatting
- **Email Structure**:
  - **Subject Line**: “Daily AI News Digest – [Date]”
  - **Header**: Professional greeting (e.g., “Dear [User Name],” or “Hello AI Enthusiast,” if no name is provided).
  - **Body**:
    - Brief introduction (e.g., “Here’s your daily roundup of the latest AI news.”).
    - List 3–5 articles with:
      - Article title (hyperlinked to the original URL).
      - Gemini-generated summary (50–100 words).
      - Publication source and date.
    - Organized in a clean, readable format (e.g., bullet points or numbered list).
  - **Footer**: Closing statement (e.g., “Stay informed, [Your AI Agent Name]”) and an unsubscribe option.
- **Styling**:
  - Use HTML for professional formatting (e.g., bold titles, proper spacing, hyperlinks).
  - Ensure compatibility with major email clients (e.g., Gmail, Outlook).
  - Keep the design minimalistic yet visually appealing.

### 4. Email Delivery
- **Scheduling**:
  - Send the email daily at a user-specified time (default: 8:00 AM local time).
  - Use a scheduling library (e.g., Python’s `schedule` or a cron job) to automate daily execution.
- **Email Service**:
  - Use a reliable email-sending service (e.g., SMTP with Gmail, SendGrid, or AWS SES).
  - Allow users to specify their email address during setup.
  - Support multiple recipients if needed.
- **Security**:
  - Securely store email credentials (e.g., using environment variables or a secrets manager).
  - Include an unsubscribe mechanism compliant with email regulations (e.g., CAN-SPAM).

### 5. Technical Requirements
- **Programming Language**: Python (preferred for its robust libraries).
- **Libraries/Tools**:
  - Web scraping: BeautifulSoup, Scrapy, or Selenium.
  - Summarization: Gemini API via `google-generativeai` Python library.
  - Email handling: `smtplib`, SendGrid, or AWS SES.
  - Scheduling: `schedule` library or cron jobs.
  - Logging: Python’s `logging` module for debugging and monitoring.
- **Error Handling**:
  - Handle scraping failures (e.g., website downtime, blocked requests).
  - Manage Gemini API rate limits and errors (e.g., HTTP 429, authentication issues).
  - Ensure email delivery errors are logged and retried if appropriate.
- **Configuration**:
  - Use a configuration file (e.g., JSON or YAML) for:
    - Target websites.
    - Email recipient(s).
    - Email sending time.
    - Gemini API key and email service credentials.
- **Logging**:
  - Log key actions (e.g., articles scraped, summaries generated, emails sent).
  - Save logs to a file for troubleshooting.

### 6. User Experience
- **Setup**:
  - Provide a simple setup script or interface for users to input:
    - Email address(es).
    - Preferred delivery time.
    - Gemini API key (with instructions to obtain it from Google).
    - Optional: Custom news sources.
  - Allow users to start/stop the service easily.
- **Output**:
  - Deliver a professional, polished email that is easy to skim.
  - Ensure Gemini-generated summaries are engaging and informative.

### 7. Scalability and Maintenance
- **Modularity**:
  - Structure the code in modular components (e.g., scraper, summarizer, email formatter, scheduler).
  - Make it easy to update scraping logic or switch to another summarization API if needed.
- **Extensibility**:
  - Allow users to add new news sources via the configuration file.
  - Support multiple languages for summaries if requested in the future.
- **Monitoring**:
  - Implement basic monitoring to alert the developer if the agent fails (e.g., no articles scraped for 24 hours).

## Deliverables
1. **Source Code**:
   - Well-documented Python code with clear comments explaining each module.
   - Organized into functions or classes for modularity.
   - Include a `README.md` with setup instructions, dependencies, and usage.
2. **Configuration File**:
   - A sample configuration file (e.g., `config.yaml`) with placeholders for:
     - Website URLs.
     - Email settings (recipient, SMTP server, credentials).
     - Gemini API key.
3. **Sample Output**:
   - A mock-up of the email format (HTML and plain text versions).
   - Example summaries for 3–5 articles generated using the Gemini API.
4. **Setup Instructions**:
   - Step-by-step guide to install dependencies, configure the agent, and run it.
   - Instructions for obtaining a Gemini API key from Google (e.g., via Google Cloud Console).
   - Instructions for scheduling (e.g., using cron or a cloud scheduler).
5. **Error Handling and Logging**:
   - Include robust error handling for all components.
   - Set up logging to a file with timestamps and error details.

## Constraints
- **Ethical Considerations**:
  - Adhere to website scraping policies and robots.txt.
  - Ensure Gemini-generated summaries are accurate and do not misrepresent original content.
  - Comply with email regulations (e.g., CAN-SPAM for unsubscribe options).
- **Performance**:
  - Scrape and process articles within a reasonable time (e.g., under 5 minutes for 5 articles).
  - Optimize Gemini API calls to stay within rate limits and cost constraints.
- **Dependencies**:
  - Use open-source libraries where possible (except for Gemini API, which requires a Google account).
  - Ensure compatibility with common operating systems (Linux, macOS, Windows).

## Example Workflow
1. At 8:00 AM daily, the agent runs.
2. Scrapes 3–5 recent articles from specified AI news websites.
3. Summarizes each article using the Gemini API.
4. Formats the summaries into a professional HTML email.
5. Sends the email to the user’s email address via the configured service.
6. Logs the process (articles scraped, summaries generated, email status).

## Success Criteria
- The agent successfully scrapes and summarizes 3–5 articles daily using the Gemini API without errors.
- Emails are delivered on schedule with professional formatting and accurate content.
- The system is easy to set up and maintain, with clear documentation.
- Errors are logged, and the system recovers gracefully from failures.

## Additional Notes
- If Claude Sonnet 4 cannot directly execute code, provide a detailed implementation plan with pseudocode for each module (scraper, Gemini API summarizer, emailer, scheduler).
- Suggest specific libraries (e.g., BeautifulSoup for scraping, `google-generativeai` for Gemini API, SendGrid for email).
- Include instructions for obtaining a Gemini API key (e.g., via Google Cloud Console at https://makersuite.google.com/).
- Ensure the solution is beginner-friendly for users with basic Python knowledge.
- Assume the user has a Google account for accessing the Gemini API; provide fallback logic (e.g., use extracted summary) if API access fails.

## Output Format
Provide the following:
1. A detailed implementation plan with pseudocode for each module.
2. Sample Python code snippets for key components (e.g., scraper, Gemini API integration, email formatter).
3. A sample configuration file (`config.yaml`).
4. A sample HTML email template.
5. A `README.md` with setup and usage instructions, including how to obtain a Gemini API key.

Please begin developing the AI agent based on this prompt. If you need clarification on any requirement, assume reasonable defaults and document your assumptions.