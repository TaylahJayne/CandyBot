from candybot.interface import database
from candybot.commands.framework import Command, ArgumentSpec


class CreditsCommand(Command):
    name = "credits"
    help = "Shows CandyBot credits."
    aliases = []
    examples = [""]
    argument_spec = ArgumentSpec([], False)
    clean = False
    admin = False
    ignore = False

    title = ":bow: CandyBot Credits"
    donate_link = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4MA3ZWKYSYNB6"

    async def _run(self):
        donators = database.get_donators()
        donators = [f"**{x}**" for x in donators]
        donators_str = "\n".join(donators)
        credits_str = ":candy: CandyBot Created By **Super#0010**\n" \
                      f":moneybag: Please consider donating [here]({self.donate_link}) to support CandyBot!\n" \
                      f":heart: CandyBot supported by:\n{donators_str}"
        await self.send(credits_str)

