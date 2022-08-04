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
            file_name = file_name.replace(" ", "")
            csvdf = pd.read_excel("Players/"+file_name+".xlsx")
            df = pd.DataFrame([player])

            vertical_concat = pd.concat([csvdf, df], axis=0)
            vertical_concat.to_excel("Players/"+file_name+".xlsx")
            # df.to_excel("Players/" + file_name+".xlsx")


if __name__ == "__main__":
    asyncio.run(main())
