```json
{
    "agents/tool_calling.py": {
        "content": "
import logging
from pydantic_ai import Agent
from logfire import configure, logger
from typing import Dict, List

configure(
    service_name=\"nondairy_butter_production\",
    # Sending to Logfire is on by default regardless of the OTEL env vars.
)

logger = logging.getLogger(__name__)

def stochastic_regime_switch(
    non_stationary_drift_index: float, 
    regime_switch_probability: float
) -> Dict[str, float]:
    """
    Calculate the stochastic regime switch based on non-stationary drift index and regime switch probability.

    Args:
    - non_stationary_drift_index (float): The non-stationary drift index.
    - regime_switch_probability (float): The regime switch probability.

    Returns:
    - Dict[str, float]: A dictionary containing the stochastic regime switch result.
    """
    try:
        result = {
            'stochastic_regime_switch': non_stationary_drift_index * regime_switch_probability
        }
        logger.info(f\"Stochastic regime switch result: {result}\")
        return result
    except Exception as e:
        logger.error(f\"Error in stochastic regime switch: {e}\")
        return {}

def tool_calling(
    agent: Agent, 
    tool_name: str, 
    input_data: List[float]
) -> Dict[str, str]:
    """
    Call a tool using the given agent and input data.

    Args:
    - agent (Agent): The agent to use for the tool call.
    - tool_name (str): The name of the tool to call.
    - input_data (List[float]): The input data for the tool call.

    Returns:
    - Dict[str, str]: A dictionary containing the tool call result.
    """
    try:
        result = agent.call_tool(tool_name, input_data)
        logger.info(f\"Tool call result: {result}\")
        return result
    except Exception as e:
        logger.error(f\"Error in tool call: {e}\")
        return {}

def simulate_rocket_science(
    non_stationary_drift_index: float, 
    regime_switch_probability: float, 
    tool_name: str, 
    input_data: List[float]
) -> Dict[str, str]:
    """
    Simulate the rocket science problem using the given parameters.

    Args:
    - non_stationary_drift_index (float): The non-stationary drift index.
    - regime_switch_probability (float): The regime switch probability.
    - tool_name (str): The name of the tool to call.
    - input_data (List[float]): The input data for the tool call.

    Returns:
    - Dict[str, str]: A dictionary containing the simulation result.
    """
    try:
        stochastic_regime_switch_result = stochastic_regime_switch(
            non_stationary_drift_index, 
            regime_switch_probability
        )
        tool_calling_result = tool_calling(
            Agent(), 
            tool_name, 
            input_data
        )
        logger.info(f\"Simulation result: {stochastic_regime_switch_result}, {tool_calling_result}\")
        return {
            'simulation_result': 'success'
        }
    except Exception as e:
        logger.error(f\"Error in simulation: {e}\")
        return {}

if __name__ == '__main__':
    non_stationary_drift_index = 0.5
    regime_switch_probability = 0.2
    tool_name = 'nondairy_butter_production_tool'
    input_data = [1.0, 2.0, 3.0]
    simulate_rocket_science(
        non_stationary_drift_index, 
        regime_switch_probability, 
        tool_name, 
        input_data
    )
",
        "commit_message": "feat: implement specialized tool_calling logic"
    }
}
```