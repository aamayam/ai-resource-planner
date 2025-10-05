import logging

def setup_logger(name):
    """
    Sets up and returns a logger with custom formatting.
    
    Args:
        name: Logger name (typically __name__ from the module)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicating handlers if already exists
    if not logger.handlers:
        # Create handler
        handler = logging.StreamHandler()
        
        # Create formatter
        formatter = logging.Formatter(
            fmt='\033[1m%(name)s:\033[0m %(levelname)s - %(asctime)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    return logger