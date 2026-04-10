```json
{
    "tools/supabase_integration.py": {
        "content": "
import logging
from typing import Dict, List
from pydantic import BaseModel
from supabase import create_client, Client
from logfire import configure, logger

configure(
    service_name=\"nondairy_butter_production_optimization_engine\"
)

logger = logger

class NondairyButterProductionOptimizationEngine(BaseModel):
    """Nondairy butter production optimization engine."""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool

class SupabaseIntegration:
    """Supabase integration class."""
    def __init__(self, url: str, key: str):
        """
        Initialize the Supabase integration.

        Args:
        - url (str): The URL of the Supabase instance.
        - key (str): The key for the Supabase instance.
        """
        self.url = url
        self.key = key
        self.supabase: Client = create_client(url, key)

    def insert_data(self, data: Dict[str, str]) -> None:
        """
        Insert data into the Supabase instance.

        Args:
        - data (Dict[str, str]): The data to be inserted.

        Raises:
        - Exception: If an error occurs during the insertion process.
        """
        try:
            self.supabase.from_('nondairy_butter_production').insert([data])
            logger.info(\"Data inserted successfully.\")
        except Exception as e:
            logger.error(f\"Error inserting data: {e}\")

    def retrieve_data(self) -> List[Dict[str, str]]:
        """
        Retrieve data from the Supabase instance.

        Returns:
        - List[Dict[str, str]]: The retrieved data.

        Raises:
        - Exception: If an error occurs during the retrieval process.
        """
        try:
            data = self.supabase.from_('nondairy_butter_production').select('*')
            logger.info(\"Data retrieved successfully.\")
            return data
        except Exception as e:
            logger.error(f\"Error retrieving data: {e}\")
            return []

def main() -> None:
    """Main function."""
    supabase_integration = SupabaseIntegration(
        url=\"https://your-supabase-instance.supabase.co\",
        key=\"your-supabase-key\"
    )
    data = {
        \"non_stationary_drift_index\": \"0.5\",
        \"stochastic_regime_switch\": \"True\"
    }
    supabase_integration.insert_data(data)
    retrieved_data = supabase_integration.retrieve_data()
    logger.info(f\"Retrieved data: {retrieved_data}\")

if __name__ == \"__main__\":
    main()
",
        "commit_message": "feat: implement specialized supabase_integration logic"
    }
}
```