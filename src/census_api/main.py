# Add this file as a new addition to your local repository

from fastapi import FastAPI, HTTPException, Query
from typing import Dict
import schedule
from dotenv import load_dotenv
import os
from datetime import datetime

from .cache import CensusDataCache
from .fetcher import CensusDataFetcherImpl
from .processor import DataProcessor
from .exceptions import CensusAPIError

# Load environment variables
load_dotenv()

app = FastAPI(title="Philadelphia Census API")
cache = CensusDataCache()
