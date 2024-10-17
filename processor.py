# Add this file as a new addition to your local repository

class DataProcessor:
    # ... existing code ...

    def calculate_demographics(self, data: Dict) -> Dict:
        # Process raw census data into structured format
        total_pop = int(data.get("B01003_001E", 0))
        white_pop = int(data.get("B02001_002E", 0))
        black_pop = int(data.get("B02001_003E", 0))

        return {
            "total_population": total_pop,
            "demographics": {
                "white_percentage": round((white_pop / total_pop) * 100, 2),
                "black_percentage": round((black_pop / total_pop) * 100, 2),
                "other_percentage": round(((total_pop - white_pop - black_pop) / total_pop) * 100, 2)
            }
        }
