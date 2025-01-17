# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import typing_extensions

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FlatfileEnvironment
from .resources.agents.client import AgentsClient, AsyncAgentsClient
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.cells.client import AsyncCellsClient, CellsClient
from .resources.documents.client import AsyncDocumentsClient, DocumentsClient
from .resources.environments.client import AsyncEnvironmentsClient, EnvironmentsClient
from .resources.events.client import AsyncEventsClient, EventsClient
from .resources.files.client import AsyncFilesClient, FilesClient
from .resources.guests.client import AsyncGuestsClient, GuestsClient
from .resources.jobs.client import AsyncJobsClient, JobsClient
from .resources.records.client import AsyncRecordsClient, RecordsClient
from .resources.secrets.client import AsyncSecretsClient, SecretsClient
from .resources.sheets.client import AsyncSheetsClient, SheetsClient
from .resources.snapshots.client import AsyncSnapshotsClient, SnapshotsClient
from .resources.spaces.client import AsyncSpacesClient, SpacesClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.versions.client import AsyncVersionsClient, VersionsClient
from .resources.workbooks.client import AsyncWorkbooksClient, WorkbooksClient


class Flatfile:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FlatfileEnvironment = FlatfileEnvironment.PRODUCTION,
        x_disable_hooks: typing_extensions.Literal["true"],
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            x_disable_hooks=x_disable_hooks,
            token=token,
            httpx_client=httpx.Client(timeout=timeout),
        )
        self.spaces = SpacesClient(client_wrapper=self._client_wrapper)
        self.agents = AgentsClient(client_wrapper=self._client_wrapper)
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.cells = CellsClient(client_wrapper=self._client_wrapper)
        self.documents = DocumentsClient(client_wrapper=self._client_wrapper)
        self.environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        self.events = EventsClient(client_wrapper=self._client_wrapper)
        self.files = FilesClient(client_wrapper=self._client_wrapper)
        self.guests = GuestsClient(client_wrapper=self._client_wrapper)
        self.jobs = JobsClient(client_wrapper=self._client_wrapper)
        self.records = RecordsClient(client_wrapper=self._client_wrapper)
        self.secrets = SecretsClient(client_wrapper=self._client_wrapper)
        self.sheets = SheetsClient(client_wrapper=self._client_wrapper)
        self.snapshots = SnapshotsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.versions = VersionsClient(client_wrapper=self._client_wrapper)
        self.workbooks = WorkbooksClient(client_wrapper=self._client_wrapper)


class AsyncFlatfile:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FlatfileEnvironment = FlatfileEnvironment.PRODUCTION,
        x_disable_hooks: typing_extensions.Literal["true"],
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            x_disable_hooks=x_disable_hooks,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout),
        )
        self.spaces = AsyncSpacesClient(client_wrapper=self._client_wrapper)
        self.agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.cells = AsyncCellsClient(client_wrapper=self._client_wrapper)
        self.documents = AsyncDocumentsClient(client_wrapper=self._client_wrapper)
        self.environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        self.events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        self.files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        self.guests = AsyncGuestsClient(client_wrapper=self._client_wrapper)
        self.jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        self.records = AsyncRecordsClient(client_wrapper=self._client_wrapper)
        self.secrets = AsyncSecretsClient(client_wrapper=self._client_wrapper)
        self.sheets = AsyncSheetsClient(client_wrapper=self._client_wrapper)
        self.snapshots = AsyncSnapshotsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.versions = AsyncVersionsClient(client_wrapper=self._client_wrapper)
        self.workbooks = AsyncWorkbooksClient(client_wrapper=self._client_wrapper)
