from fpl import FPL
import aiohttp
import asyncio
from datetime import datetime
import pandas as pd
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        for i in range(1,39):
            fixtures = await fpl.get_fixtures_by_gameweek(i, True)
            # print(type(fixtures))
            for fixture in fixtures:
                date = fixture["kickoff_time"]
                date = date.replace('Z','')
                date_time = date.split('T')
                fixture["kickoff_time"] = date_time
                # print(date_time)
            df = pd.DataFrame(fixtures)
            df.to_csv("Gameweeks/GameWeek"+str(i))





asyncio.get_event_loop().run_until_complete(main())