import datetime
import os
import traceback
from config.dev import LOG_FILE
from config.settings import load_settings

# Logging configuration
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10 MB

# Default log level, can be set via settings
LOG_LEVEL = "INFO"  # Possible values: "DEBUG", "INFO", "ERROR"

def _write_log(message):
    """Schreibt eine Log-Nachricht in die Logdatei und rotiert bei Überschreitung der Maximalgröße."""
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        try:
            os.rename(LOG_FILE, str(LOG_FILE) + ".old")
        except Exception:
            pass  # Ignore rotation errors, continue logging
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_section(section):
    """Loggt einen neuen Abschnitt."""
    _write_log(f"\n=== [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SECTION: {section} ===")

def log_subsection(subsection):
    """Loggt einen neuen Unterabschnitt."""
    _write_log(f"-- [{datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] SUBSECTION: {subsection}")

def log_debug(message):
    """Loggt eine Debug-Nachricht, wenn der Log-Level DEBUG ist."""
    if LOG_LEVEL == "DEBUG":
        _write_log(f"[DEBUG {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_info(message):
    """Loggt eine Info-Nachricht, wenn der Log-Level INFO oder DEBUG ist."""
    if LOG_LEVEL in ("INFO", "DEBUG"):
        _write_log(f"[INFO {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_error(message):
    """Loggt eine Fehlermeldung."""
    _write_log(f"[ERROR {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")

def log_exception(message, exc=None):
    """Loggt eine Exception mit optionalem Traceback."""
    _write_log(f"[ERROR {datetime.datetime.now().isoformat(sep=' ', timespec='seconds')}] {message}")
    if exc is not None:
        _write_log(traceback.format_exc())

def setup_logging():
    """Initialisiert das Logging und lädt den Log-Level aus den Einstellungen."""
    global LOG_LEVEL
    try:
        settings = load_settings()
        LOG_LEVEL = settings.get("log_level", LOG_LEVEL)
    except Exception:
        pass  # Use default if settings not available
    log_section("Logging started")

def log_header():
    """Loggt den Start der Anwendung."""
    _write_log("\n==================== CSNova Application Start ====================\n")

def log_call(func):
    """Decorator für automatisches Logging von Funktionsaufrufen und Exceptions."""
    def wrapper(*args, **kwargs):
        log_info(f"Calling {func.__name__}")
        try:
            result = func(*args, **kwargs)
            log_info(f"{func.__name__} finished successfully")
            return result
        except Exception as e:
            log_exception(f"Error in {func.__name__}: {e}", e)
            raise
    return wrapper