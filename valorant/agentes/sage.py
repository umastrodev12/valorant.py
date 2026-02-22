import aiohttp
import asyncio

class Sage:
    def __init__(self):
        self.url = "https://playvalorant.com/pt-br/agents/sage/"
        self.color = 0x3b4acc

    
    async def catch_sage_agent(self, session):
        async with session.get(self.url) as response:
            html = await response.text()

            base = {
                "Sage",
                "Como uma verdadeira fortaleza chinesa, Sage traz segurança para si mesma e para a equipe aonde quer que vá. Capaz de reviver aliados e rechaçar investidas agressivas, ela oferece um centro de calmaria em meio ao caos da batalha.",
                "Função: Sentinela"
            }
