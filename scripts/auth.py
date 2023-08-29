import functools
import os
import threading
from typing import Callable, Literal, ParamSpec, Sequence, TypeAlias, TypeVar
import urllib.parse
from dotenv import load_dotenv
from oauthlib.oauth2 import WebApplicationClient
import webbrowser
from http import server
import requests
import pydantic

from strava_python import configuration

load_dotenv()
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

STRAVA_REDIRECT_URI = os.getenv("STRAVA_REDIRECT_URI")

T = TypeVar("T")
P = ParamSpec("P")

Scope: TypeAlias = Literal[
    "read",
    "read_all",
    "profile:read_all",
    "profile:write",
    "activity:read",
    "activity:read_all",
    "activity:write",
]


class TokenResponse(pydantic.BaseModel, extra="allow"):
    token_type: str
    expires_at: int
    expires_in: int
    refresh_token: str
    access_token: str


def requires_auth(fn: Callable[P, T]) -> Callable[P, T]:
    """Decorator for a function to check the keys have been set."""
    if None in (STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, STRAVA_REDIRECT_URI):
        raise ValueError("Please set the client id and/or redirect url")
    return fn


@functools.cache
def _urls(
    scopes: Sequence[Scope],
    state: str = "test",
    approval_prompt: Literal["auto", "force"] = "auto",
):
    auth_client = WebApplicationClient(STRAVA_CLIENT_ID)

    url = auth_client.prepare_request_uri(
        "https://www.strava.com/oauth/authorize",
        redirect_uri=STRAVA_REDIRECT_URI,
        scope=scopes,
        state=state,
        approval_prompt=approval_prompt,
    )
    return url, lambda code: auth_client.prepare_request_body(
        code=code,
        redirect_uri=STRAVA_REDIRECT_URI,
        client_id=STRAVA_CLIENT_ID,
        client_secret=STRAVA_CLIENT_SECRET,
    )


@requires_auth
def authorize_url(scopes: Sequence[Scope]):
    return _urls(scopes)[0]


def token_url(code: str):
    return _urls(None)[1](code)


@requires_auth
def get_config_for_tokens_local(
    scopes: Sequence[Scope] = ("activity:read",),
    auto_open: bool = True,
):
    url = authorize_url(scopes)
    if auto_open:
        webbrowser.open(url)
    code = None
    host = urllib.parse.urlparse(STRAVA_REDIRECT_URI).netloc.split(":", maxsplit=1)
    address, port = host

    class AuthClient(server.BaseHTTPRequestHandler):
        def do_GET(self):
            path = urllib.parse.urlsplit(self.path)
            if path.netloc not in ("/", ""):
                self.send_error(404)
                return
            try:
                nonlocal code
                code = urllib.parse.parse_qs(path.query)["code"][0]
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(
                    bytes(
                        """<html>
    <head>
        
    </head>
    <body>You can now close this tab...
        <script type='text/javascript'>
                window.opener && window.opener.location.reload(true);
                window.close();
        </script>
    </body>
</html>""",
                        "utf-8",
                    )
                )
            except Exception as e:
                self.send_error(500)
            finally:
                server_closer = threading.Thread(
                    target=tmp_server.shutdown, daemon=True
                )
                server_closer.start()

    tmp_server = server.HTTPServer((address, int(port)), AuthClient)
    tmp_server.serve_forever()
    data = token_url(code)
    response = TokenResponse.model_validate_json(
        requests.post("https://www.strava.com/oauth/token", data=data).text
    )

    config = configuration.Configuration()
    config.access_token = response.access_token
    #TODO: refresh_token
    return config
