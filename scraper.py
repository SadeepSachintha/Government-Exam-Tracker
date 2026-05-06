import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

API_URL = "https://applications.doenets.lk/doe_application/frontend/list-exams"

def fetch_ongoing_exams():
    """
    Fetches the list of ongoing exams from the DOE API.
    Returns a list of dictionaries if successful, or an empty list if there's an error.
    """
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://applications.doenets.lk/exams'
    }
    
    try:
        response = requests.get(API_URL, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Check if response is actually JSON. Sometimes if empty, it might be different.
        data = response.json()
        
        if 'data' in data and isinstance(data['data'], list):
            return data['data']
        else:
            logger.warning(f"Unexpected JSON structure: {data}")
            return []
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching exams: {e}")
        return []
    except ValueError as e:
        logger.error(f"Error parsing JSON (Response might be XML or empty): {e}")
        return []

if __name__ == "__main__":
    # Test the fetch logic
    exams = fetch_ongoing_exams()
    print(f"Found {len(exams)} exams.")
    for ex in exams:
        print(ex.get('name'))
