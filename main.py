import logging
from splunkInstrumentor import instrument  # Import the setup
import worker  # Import other modules

# One-time setup at startup (add this line)
instrument()

# Your app code (no further changes needed)
logger = logging.getLogger(__name__)

logger.info("Cybersecurity application starting.", extra={'event_type': 'startup', 'system': 'prod'})

# Simulate cybersecurity operations
worker.monitor_security_events()

logger.info("Application finished.", extra={'event_type': 'shutdown', 'status': 'success'})
