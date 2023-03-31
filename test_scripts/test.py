from proton import ProtonDB
import argparse, sys

parser = argparse.ArgumentParser(description="Herramienta para consultar estados de juegos de steam en ProtonDB")

parser.add_argument("-g", "--game", action="store", dest="game", help="Titulo del juego")
parser.add_argument("-l", "--list", action="store_true", dest="list")
args = parser.parse_args()

if args.game:
    proton_api = ProtonDB()
    game_id, title = proton_api.get_game_id(args.game)
    if not game_id:
        print("Juego no encontrado")
        sys.exit(1)
    rating, note = proton_api.get_game_reports(game_id)
    print("Game:",title,"\nRating:",rating, "\nRandom Notes:",note)
    
elif args.list:
    proton_api = ProtonDB()
    proton_api.get_games()
