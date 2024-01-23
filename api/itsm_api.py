import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, RequestException
class ITSM_API:
    def __init__(self, email, api_token, base_url):
        self.auth = HTTPBasicAuth(email, api_token)
        self.base_url = base_url
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    def create_issue(self, summary, project_key, issue_type,description):
         url = f"{self.base_url}/issue/"
         adf_description = {
             "version": 1,
             "type": "doc",
             "content": [
                 {
                     "type": "paragraph",
                     "content": [
                         {
                             "type": "text",
                             "text": description
                         }
                    ]
                }
            ]
         } 
         data = {
             "fields": {
             "summary": summary,
             "description": adf_description,
             "project": {
                 "key": project_key
             },
             "issuetype": {
                "name": issue_type
             }
           }
         }
         try:
              response = requests.post(url, json=data, headers=self.headers, auth=self.auth)
              response.raise_for_status()  # Raises an HTTPError if the status is 4xx or 5xx
              return response.json()
         except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            return {"error": str(http_err)}
         except RequestException as req_err:
            print(f"Network error occurred: {req_err}")  # Log the error
            return {"error": str(req_err)}
         except Exception as err:
            print(f"An unexpected error occurred: {err}")  # Log the error
            return {"error": "An unexpected error occurred"}
     
     #ISSUE DETAILS
    def get_issue_details(self, issue_key):
        """Get details of an issue given its key."""
        url = f"{self.base_url}/issue/{issue_key}"
        try:
            response = requests.get(url, headers=self.headers, auth=self.auth)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except RequestException as req_err:
            print(f"Network error occurred: {req_err}")
            return {"error": str(req_err)}
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
            return {"error": "An unexpected error occurred"}
