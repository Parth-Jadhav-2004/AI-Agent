"""
AI News Agent - Main Entry Point
Daily AI news scraper, summarizer, and emailer using Gemini API
"""

import logging
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from config_manager import ConfigManager
from logger_config import setup_logging
from orchestrator import NewsOrchestrator

def main():
    """Main entry point for the AI News Agent"""
    try:
        # Initialize configuration
        config = ConfigManager()
        
        # Setup logging
        logger = setup_logging(config)
        logger.info("Starting AI News Agent")
        
        # Initialize orchestrator
        orchestrator = NewsOrchestrator(config)
        
        # Run the daily news process
        orchestrator.run_daily_process()
        
        logger.info("AI News Agent completed successfully")
        
    except Exception as e:
        logging.error(f"Fatal error in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()