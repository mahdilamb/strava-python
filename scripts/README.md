# Strava python

Python client for Strava API. Uses swagger's codegen for basing the API.

# Example usage

Set environment variables as required (`.env` file in root):

```ini
STRAVA_CLIENT_ID=??
STRAVA_CLIENT_SECRET=??
STRAVA_REDIRECT_URI=??


```

```python
from strava_python import auth, api, api_client

config = auth.get_config_for_tokens_local()
client = api_client.ApiClient(config)
data, status,headers = api.ActivitiesApi(client).get_logged_in_athlete_activities_with_http_info()
print(data)


```
