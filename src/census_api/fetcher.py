# Add this file as a new addition to your local repository

from abc import ABC, abstractmethod
from typing import Dict, List
import requests
from .exceptions import CensusAPIError

class CensusDataFetcher(ABC):
    # ... existing code ...

    @abstractmethod
    async def fetch_demographic_data(self, year: int) -> Dict:
        # ... existing method ...
