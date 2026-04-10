```json
{
    "config/logging.py": {
        "content": "
import logging
from pydantic import BaseModel
from logfire import configure, logger
from typing import Optional

class LoggingConfiguration(BaseModel):
    """Logging configuration model."""
    service_name: str
    log_level: str
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

def configure_logging(config: LoggingConfiguration) -> None:
    """
    Configure logging with the given configuration.

    Args:
    - config (LoggingConfiguration): Logging configuration.

    Returns:
    - None
    """
    try:
        configure(
            service_name=config.service_name,
            log_level=config.log_level
        )
        logger.info('Logging configured successfully.')
    except Exception as e:
        logger.error(f'Error configuring logging: {str(e)}')

def log_non_stationary_drift(index: float) -> None:
    """
    Log non-stationary drift index.

    Args:
    - index (float): Non-stationary drift index.

    Returns:
    - None
    """
    try:
        logger.info(f'Non-stationary drift index: {index}')
    except Exception as e:
        logger.error(f'Error logging non-stationary drift index: {str(e)}')

def log_stochastic_regime_switch(switch: bool) -> None:
    """
    Log stochastic regime switch.

    Args:
    - switch (bool): Stochastic regime switch.

    Returns:
    - None
    """
    try:
        logger.info(f'Stochastic regime switch: {switch}')
    except Exception as e:
        logger.error(f'Error logging stochastic regime switch: {str(e)}')

def simulate_rocket_science() -> None:
    """
    Simulate the 'Rocket Science' problem.

    Returns:
    - None
    """
    try:
        config = LoggingConfiguration(
            service_name='rocket_science',
            log_level='INFO',
            non_stationary_drift_index=0.5,
            stochastic_regime_switch=True
        )
        configure_logging(config)
        log_non_stationary_drift(config.non_stationary_drift_index)
        log_stochastic_regime_switch(config.stochastic_regime_switch)
    except Exception as e:
        logger.error(f'Error simulating rocket science: {str(e)}')

if __name__ == '__main__':
    simulate_rocket_science()
",
        "commit_message": "feat: implement specialized logging logic"
    }
}
```