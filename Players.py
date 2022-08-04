from fpl import FPL
import aiohttp
import asyncio
import pandas as pd
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(return_json=True)
        for player in players:
            file_name = str(player["first_name"]) + str(player["second_name"])+str(player["code"])
            file_name = file_name.replace(" ","")
            print(player)
            df = pd.DataFrame([player])
            df.to_csv("Players/"+file_name)


if __name__ == "__main__":
    asyncio.run(main())
