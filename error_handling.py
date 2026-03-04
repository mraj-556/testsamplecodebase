def safe_execute(func):
    try:
        return func()
    except Exception as e:
        log_error(f"Execution failed: {str(e)}")
        raise

def log_error(message):
    # Custom error logging implementation
    print(f"[ERROR] {message}")