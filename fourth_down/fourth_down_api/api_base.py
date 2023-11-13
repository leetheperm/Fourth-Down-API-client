from .environment import FourthDownEnvironment
from dataclasses import dataclass, field
from time import perf_counter
import requests


@dataclass
class ApiRequest:
    path: str
    params: dict = field(default_factory=dict)
    headers: dict = field(default_factory=dict)
    verbose: bool = False


class ApiBase:
    def __init__(self, endpoint: FourthDownEnvironment, headers: dict[str, str] = {}) -> None:
        if isinstance(endpoint, FourthDownEnvironment):
            self._endpoint: str = endpoint.value
        else:
            self._endpoint: str = endpoint.strip().lstrip("/")
        self.headers = headers

    def _get(self, request: ApiRequest) -> str:
        start_time = perf_counter()

        r = requests.get(
            f"{self._endpoint}/{request.path.lstrip('/')}",
            params=request.params,
            headers={**request.headers})
        duration = perf_counter() - start_time
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
        if request.verbose:
            print(f"Request url: {r.url}")
            print(f"Duration: {duration:.3f}s")
            print(f"Status: {r.status_code}")
            return r.text

