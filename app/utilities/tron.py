from tronpy import AsyncTron


async def get_tron_info(address):

    async with AsyncTron(network='nile') as client:
        bandwidth = await client.get_bandwidth(addr=address)
        account_inf = await client.get_account(addr=address)
        return (
            f'bandwidth: {bandwidth}, '
            f'energy: {account_inf["net_window_size"]}, '
            f'balance: {account_inf["balance"]}'
        )
