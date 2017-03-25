## IMPORTS

from configobj import ConfigObj

from commands import CommandReturn
from commands.client import ClientCommand
from commands.say import SayCommand
from messages import SayText2
from paths import CFG_PATH
from players.entity import Player
from translations.strings import LangStrings

from .info import info

## GLOBALS

ini_file = CFG_PATH / info.name + '.ini'
ini_config = ConfigObj(ini_file)
strings = LangStrings('resetscore')
ALREADY_MSG = SayText2(strings['Already'])
RESETSCORE_MSG = SayText2(strings['Resetscore'])

## INI CREATION
if not ini_file.isfile():
    # Add the public commands
    ini_config['public_commands'] = ['!rs', '!resetscore']
    ini_config.comments['public_commands'] = strings[
        'Public'
    ].get_string().splitlines()

    # Add the private commands
    ini_config['private_commands'] = ['/rs', '/resetscore']
    ini_config.comments['private_commands'] = [
        ''
    ] + strings['Private'].get_string().splitlines()

    # Add the client commands
    ini_config['client_commands'] = ['rs', 'resetscore']
    ini_config.comments['client_commands'] = [
        ''
    ] + strings['Client'].get_string().splitlines()

    ini_config.write()

## COMMAND REGISTERS

@SayCommand(ini_config['public_commands'] + ini_config['private_commands'])
@ClientCommand(ini_config['client_commands'])
def _resetscrore_say_command(command, index, team_only=None):
    player = Player(index)
    if player.kills != 0 or player.deaths != 0: 
        player.kills = 0
        player.deaths = 0
        RESETSCORE_MSG.send(player.index)
    else:
        ALREADY_MSG.send(player.index)

    if command[0] in ini_config['private_commands'] or team_only is None:
        return CommandReturn.BLOCK
