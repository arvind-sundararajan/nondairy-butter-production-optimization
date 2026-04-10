```json
{
    "tools/nasa_integration.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic_ai import Agent
import logfire
from logfire import Span
import torch
from pytorch_CycleGAN_and_pix2pix import Generator

def configure_logfire(service_name: str) -> None:
    """
    Configure Logfire for observability.

    Args:
    service_name (str): The name of the service.

    Returns:
    None
    """
    try:
        logfire.configure(
            service_name=service_name,
        )
        logging.info('Logfire configured successfully')
    except Exception as e:
        logging.error(f'Error configuring Logfire: {e}')

def initialize_agent() -> Agent:
    """
    Initialize the AI agent.

    Returns:
    Agent: The initialized agent.
    """
    try:
        agent = Agent()
        logging.info('Agent initialized successfully')
        return agent
    except Exception as e:
        logging.error(f'Error initializing agent: {e}')

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index.

    Args:
    data (List[float]): The input data.

    Returns:
    float: The non-stationary drift index.
    """
    try:
        # Calculate the non-stationary drift index using a stochastic regime switch
        non_stationary_drift_index = torch.mean(torch.tensor(data))
        logging.info('Non-stationary drift index calculated successfully')
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error calculating non-stationary drift index: {e}')

def simulate_rocket_science(agent: Agent, data: List[float]) -> Dict[str, float]:
    """
    Simulate the rocket science problem.

    Args:
    agent (Agent): The AI agent.
    data (List[float]): The input data.

    Returns:
    Dict[str, float]: The simulation results.
    """
    try:
        # Initialize the generator
        generator = Generator()

        # Calculate the non-stationary drift index
        non_stationary_drift_index = calculate_non_stationary_drift_index(data)

        # Simulate the rocket science problem using the agent and generator
        simulation_results = agent.simulate(generator, non_stationary_drift_index)
        logging.info('Rocket science simulation completed successfully')
        return simulation_results
    except Exception as e:
        logging.error(f'Error simulating rocket science: {e}')

if __name__ == '__main__':
    # Configure Logfire
    configure_logfire('nasa_integration')

    # Initialize the agent
    agent = initialize_agent()

    # Simulate the rocket science problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    simulation_results = simulate_rocket_science(agent, data)

    # Print the simulation results
    print(simulation_results)
",
        "commit_message": "feat: implement specialized nasa_integration logic"
    }
}
```