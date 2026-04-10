```json
{
    "utils/data_preprocessing.py": {
        "content": "
import logging
from typing import List, Tuple
import torch
from pydantic import BaseModel
from logfire import Logfire

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Logfire
logfire = Logfire()
logfire.configure(service_name=\"nondairy_butter_production\")

class DataPreprocessingConfig(BaseModel):
    """
    Configuration for data preprocessing.
    
    Attributes:
    - non_stationary_drift_index (float): Index for non-stationary drift detection.
    - stochastic_regime_switch (bool): Flag for stochastic regime switch.
    """
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

def detect_non_stationary_drift(data: List[float], config: DataPreprocessingConfig) -> Tuple[bool, float]:
    """
    Detect non-stationary drift in the data.
    
    Args:
    - data (List[float]): Input data.
    - config (DataPreprocessingConfig): Configuration for data preprocessing.
    
    Returns:
    - Tuple[bool, float]: Whether non-stationary drift is detected and the corresponding index.
    """
    try:
        # Calculate the non-stationary drift index
        non_stationary_drift_index = torch.std(torch.tensor(data))
        logger.info(f\"Non-stationary drift index: {non_stationary_drift_index}\")
        logfire.info(\"Non-stationary drift index calculated\")
        
        # Check if non-stationary drift is detected
        if non_stationary_drift_index > config.non_stationary_drift_index:
            return True, non_stationary_drift_index
        else:
            return False, non_stationary_drift_index
    except Exception as e:
        logger.error(f\"Error detecting non-stationary drift: {e}\")
        logfire.error(\"Error detecting non-stationary drift\")
        return False, 0.0

def apply_stochastic_regime_switch(data: List[float], config: DataPreprocessingConfig) -> List[float]:
    """
    Apply stochastic regime switch to the data.
    
    Args:
    - data (List[float]): Input data.
    - config (DataPreprocessingConfig): Configuration for data preprocessing.
    
    Returns:
    - List[float]: Data with stochastic regime switch applied.
    """
    try:
        # Apply stochastic regime switch
        if config.stochastic_regime_switch:
            # Simulate stochastic regime switch using PyTorch
            switched_data = torch.tensor(data) + torch.randn(len(data))
            logger.info(\"Stochastic regime switch applied\")
            logfire.info(\"Stochastic regime switch applied\")
            return switched_data.tolist()
        else:
            return data
    except Exception as e:
        logger.error(f\"Error applying stochastic regime switch: {e}\")
        logfire.error(\"Error applying stochastic regime switch\")
        return data

if __name__ == \"__main__\":
    # Simulation of the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    config = DataPreprocessingConfig(non_stationary_drift_index=1.5, stochastic_regime_switch=True)
    
    # Detect non-stationary drift
    drift_detected, drift_index = detect_non_stationary_drift(data, config)
    print(f\"Non-stationary drift detected: {drift_detected}, index: {drift_index}\")
    
    # Apply stochastic regime switch
    switched_data = apply_stochastic_regime_switch(data, config)
    print(f\"Data with stochastic regime switch: {switched_data}\")
",
        "commit_message": "feat: implement specialized data_preprocessing logic"
    }
}
```