"""Email sending functionality for AI News Agent"""

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Dict, List


class EmailSender:
    """Sends formatted emails using SMTP"""
    
    def __init__(self, config_manager):
        self.config = config_manager
        self.logger = logging.getLogger('ai_news_agent.email_sender')
        
        # Get email configuration
        email_config = self.config.get_email_config()
        smtp_config = email_config.get('smtp', {})
        
        self.smtp_server = smtp_config.get('server', 'smtp.gmail.com')
        self.smtp_port = smtp_config.get('port', 587)
        self.use_tls = smtp_config.get('use_tls', True)
        
        # Get credentials
        credentials = email_config.get('credentials', {})
        self.username = credentials.get('username')
        self.password = credentials.get('password')
        
        # Get recipients
        self.recipients = email_config.get('recipients', [])
        
        if not self.username or not self.password:
            raise ValueError("Email credentials not found in configuration")
        
        if not self.recipients:
            raise ValueError("No email recipients configured")
    
    def send_email(self, email_content: Dict[str, str]) -> bool:
        """
        Send email with the provided content
        
        Args:
            email_content: Dictionary with 'subject', 'html_body', 'text_body'
            
        Returns:
            True if email sent successfully, False otherwise
        """
        try:
            self.logger.info("Preparing to send email")
            
            # Create message
            msg = self._create_message(email_content)
            
            # Send email
            self._send_via_smtp(msg)
            
            self.logger.info(f"Email sent successfully to {len(self.recipients)} recipients")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
            return False
    
    def _create_message(self, email_content: Dict[str, str]) -> MIMEMultipart:
        """Create MIME message from email content"""
        
        # Create multipart message
        msg = MIMEMultipart('alternative')
        
        # Set headers
        msg['Subject'] = email_content['subject']
        msg['From'] = self.username
        msg['To'] = ', '.join([recipient['email'] for recipient in self.recipients])
        
        # Create text and HTML parts
        text_part = MIMEText(email_content['text_body'], 'plain', 'utf-8')
        html_part = MIMEText(email_content['html_body'], 'html', 'utf-8')
        
        # Attach parts
        msg.attach(text_part)
        msg.attach(html_part)
        
        return msg
    
    def _send_via_smtp(self, msg: MIMEMultipart):
        """Send message via SMTP"""
        
        self.logger.debug(f"Connecting to SMTP server: {self.smtp_server}:{self.smtp_port}")
        
        # Create SMTP session
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            
            # Enable TLS if configured
            if self.use_tls:
                server.starttls()
                self.logger.debug("TLS enabled")
            
            # Login
            server.login(self.username, self.password)
            self.logger.debug("SMTP login successful")
            
            # Send email to all recipients
            recipient_emails = [recipient['email'] for recipient in self.recipients]
            
            for recipient_email in recipient_emails:
                try:
                    # Create individual message for each recipient
                    individual_msg = MIMEMultipart('alternative')
                    individual_msg['Subject'] = msg['Subject']
                    individual_msg['From'] = msg['From']
                    individual_msg['To'] = recipient_email
                    
                    # Copy content
                    for part in msg.walk():
                        if part.get_content_type() in ['text/plain', 'text/html']:
                            individual_msg.attach(part)
                    
                    # Send
                    server.send_message(individual_msg)
                    self.logger.debug(f"Email sent to: {recipient_email}")
                    
                except Exception as e:
                    self.logger.error(f"Failed to send to {recipient_email}: {e}")
                    continue
    
    def test_email_connection(self) -> bool:
        """Test email connection and credentials"""
        try:
            self.logger.info("Testing email connection")
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                
                server.login(self.username, self.password)
                
            self.logger.info("Email connection test successful")
            return True
            
        except Exception as e:
            self.logger.error(f"Email connection test failed: {e}")
            return False
    
    def send_test_email(self) -> bool:
        """Send a test email to verify everything is working"""
        try:
            test_content = {
                'subject': 'AI News Agent - Test Email',
                'html_body': '''
                <html>
                <body>
                    <h2>🤖 AI News Agent Test</h2>
                    <p>This is a test email to verify that your AI News Agent is configured correctly.</p>
                    <p>If you're receiving this, everything is working properly!</p>
                    <p><strong>AI News Agent</strong></p>
                </body>
                </html>
                ''',
                'text_body': '''
AI News Agent Test

This is a test email to verify that your AI News Agent is configured correctly.

If you're receiving this, everything is working properly!

AI News Agent
                '''
            }
            
            return self.send_email(test_content)
            
        except Exception as e:
            self.logger.error(f"Failed to send test email: {e}")
            return False
