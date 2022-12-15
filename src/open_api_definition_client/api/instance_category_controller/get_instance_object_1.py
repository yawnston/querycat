from http import HTTPStatus
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    schema_id: int,
    object_key: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/instances/{schemaId}/object/{objectKey}".format(
        client.base_url, schemaId=schema_id, objectKey=object_key
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    schema_id: int,
    object_key: int,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        schema_id (int):
        object_key (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
        object_key=object_key,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    schema_id: int,
    object_key: int,
    *,
    client: Client,
) -> Response[Any]:
    """
    Args:
        schema_id (int):
        object_key (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        schema_id=schema_id,
        object_key=object_key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)