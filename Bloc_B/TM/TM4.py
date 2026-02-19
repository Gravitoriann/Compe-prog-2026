## This is the template for TM3, full problem in the rulebook ##
import itertools as it
def convert(name):
    if name == "Station1":
        return "Station0"
    if name == "Station2":
        return "Station1"
    if name == "Station3":
        return "Station2"
    if name == "Station4":
        return "Station3"
def vert(name):
    if name == "Station0":
        return "Station1"
    if name == "Station1":
        return "Station2"
    if name == "Station2":
        return "Station3"
    if name == "Station3":
        return "Station4"

def solve(instructions: list[str]):
    """
    Find the full 2D matrix describing the metro stations

    Parameters:
        instructions list[str]: Sequence of instructions to give info on the metro station and their relationships
        
    Returns:
        list[list[str]]: THe full array of the informations on each metro station
    """
    informations = []
    lines = ["Bleu", "Vert", "Orange", "Jaune", "Rose"]
    stations = ["Snowdon", "Berri-UQAM", "Vendôme", "Licorne", "Atwater"]
    bags = ["Sac à dos", "Tote bag", "Sac à main", "Bandoulière", "Sac plastique"]
    drinks = ["Tea", "Jus", "Coffee", "Eau", "Lait"]
    fares =["Weekend illimité", "Soirée illimité", "Aucun", "1 passage", "Mensuel"]
    places ={}
    places["Station1"] = []
    places["Station2"] = []
    places["Station3"] = []
    places["Station4"] = []
    places["Station0"] = []
    print(places)
    for line in instructions:
        if "=" in line:
            split =line.index("=")
            if line[:split-1] in places.keys():
                places[line[:split-1]].append(line[split+2:])
        if "->" in line:
            split =line.index("->")
            if line[:split-1] in places.keys():
                places[vert(line[:split-1])].append(line[split+2:])
    #while "Aucun" not in places.values():
        for line in instructions:
            if "=" in line:
                split = line.index("=")
                for key in places.keys():
                    if line[:split-1] in places[key]:
                        if line[split+2:] not in places[key]:
                            places[key].append(line[split+2:])
            if "->" in line:
                split = line.index("->")
                for key in places.keys():
                    if line[:split-1] in places[key]:
                        a = vert(key)
                        if line[split + 3:] not in places[a]:
                            places[a].append(line[split+3:])
                    if line[:split+3] in places[key]:
                        a = convert(key)
                        if line[split-1:] not in places[a]:
                            places[a].append(line[split-1:])
                if line[:split-1] in places.keys():
                    b = convert(line[:split-1])
                    if line[split + 3:] not in places[b]:
                        places[b].append(line[split+3:])
                if line[:split+3] in places.keys():
                    b = vert(line[:split+3])
                    if line[split-1:] not in places[b]:
                        places[b].append(line[split-1:])



        print(places)

    opt_lines = it.permutations(lines)
    opt_stations = it.permutations(stations)
    opt_bags = it.permutations(bags)
    opt_drinks = it.permutations(drinks)
    opt_fares = it.permutations(fares)
    for a in opt_lines:
        for b in opt_stations:
            for c in opt_bags:
                for d in opt_drinks:
                    for f in opt_fares:
                        places["Station0"] = [a[0],b[0],c[0],d[0],f[0]]
                        places["Station1"] = [a[1],b[1],c[1],d[1],f[1]]
                        places["Station2"] = [a[2],b[2],c[2],d[2],f[2]]
                        places["Station3"] = [a[3],b[3],c[3],d[3],f[3]]
                        places["Station4"] = [a[4],b[4],c[4],d[4],f[4]]
                        for line in instructions:
                            if "=" in line:
                                split = line.index("=")
                                if line[:split - 1] in places.keys():
                                    if line[split+2] not in places[:line[split-1]]:
                                        break
                                for key in places.keys():
                                    if line[:split - 1] in places[key]:
                                        if line[split + 2:] not in places[key]:
                                            break
                            if "->" in line:
                                split = line.index("->")
                                for key in places.keys():
                                    if line[:split - 1] in places[key]:
                                        a = vert(key)
                                        if line[split + 3:] not in places[a]:
                                            places[a].append(line[split + 3:])
                                    if line[:split + 3] in places[key]:
                                        a = convert(key)
                                        if line[split - 1:] not in places[a]:
                                            places[a].append(line[split - 1:])
                                if line[:split - 1] in places.keys():
                                    b = convert(line[:split - 1])
                                    if line[split + 3:] not in places[b]:
                                        places[b].append(line[split + 3:])
                                if line[:split + 3] in places.keys():
                                    b = vert(line[:split + 3])
                                    if line[split - 1:] not in places[b]:
                                        places[b].append(line[split - 1:])

    
    return informations


instructions = [
        "Vendôme = Orange",
        "Licorne = Soirée illimité",
        "Snowdon = Sac à dos",
        "Vert -> Rose",
        "Vert = Coffee",
        "Sac à main = Mensuel",
        "Jaune = Bandoulière",
        "Station2 = Lait",
        "Station0 = Berri-UQAM",
        "Weekend-illimité -> Sac à dos",
        "Bandoulière -> 1 passage",
        "Sac plastique = Jus",
        "Atwater = Tote bag",
        "Berri-UQAM -> Bleu",
        "Eau -> Sac à dos"]
print(solve(instructions))