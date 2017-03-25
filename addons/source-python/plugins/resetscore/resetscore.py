## IMPORTS

from commands import CommandReturn
from commands.say import SayCommand
from messages import SayText2
from players.entity import Player
from translations.strings import LangStrings

## GLOBALS

strings = LangStrings('resetscore')


## SAY REGISTERS

@SayCommand(['!rs', '/rs', '!resetscore', '/resetscore'])
def _resetscrore_say_command(command, index, team_only=None):
    player = Player(index)
    if player.kills != 0 and player.deaths != 0: 
        player.kills = 0
        player.deaths = 0
        SayText2(strings['Resetscore']).send(player.index)
    else:
        SayText2(strings['Already']).send(player.index)

    return CommandReturn.BLOCK