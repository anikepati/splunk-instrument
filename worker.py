import logging
import time  # For simulation

logger = logging.getLogger(__name__)  # Inherits Splunk config from main

def monitor_security_events():
    logger.info("Starting security event monitoring.", extra={'module': 'worker', 'phase': 'init'})
    
    # Simulate extensive real-time logging (e.g., in a loop for ongoing ops)
    for i in range(5):
        time.sleep(1)  # Simulate real-time delay
        logger.debug(f"Debug: Scanning network iteration {i}", extra={'ip': '192.168.1.100', 'port': 443})
        logger.info("Info: User login attempt.", extra={'user_id': 'admin', 'source_ip': '10.0.0.5'})
        logger.warning("Warning: Suspicious activity detected.", extra={'threat_level': 'medium', 'anomaly_score': 0.75})
        print(f"This print redirects to Splunk: Potential breach alert {i}")  # Handles legacy print
        if i % 3 == 0:
            logger.error("Error: Intrusion detected!", extra={'event_type': 'intrusion', 'details': 'Unauthorized access'})
    
    logger.critical("Critical: System breach confirmed.", extra={'alert': 'high_priority', 'response_needed': True})
