from app.core.config import config
import httpx

class FipeClient:
    def __init__(self):
        self._client = httpx.AsyncClient(
            base_url = config.FIPE_API_URL,
            timeout = config.FIPE_API_TIMEOUT
        )

    async def close(self):
        await self._client.aclose()

    async def listar_marcas(self, tipo_veiculo: str):
        response = await self._client.get(f"/{tipo_veiculo}/brands")
        response.raise_for_status()
        return response.json()