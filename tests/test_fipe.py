from app.integrations.fipe_client import FipeClient
import asyncio

async def main(tipo_veiculo):
    fipe_cliente = FipeClient()
    try:
        response = await fipe_cliente.listar_marcas(tipo_veiculo)
        print(response)
    except Exception as e:
        print(f"Erro! {e}")
    finally:
        fipe_cliente.close()
        print("Cliente HTTP encerrado!")


asyncio.run(main("cars"))