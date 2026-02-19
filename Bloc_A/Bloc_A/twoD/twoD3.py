## This is the template for 2D3, full problem in the rulebook ##
def solve(noise: list[str]) -> int:
    """
    Compute the perimeter of the biggest noise bloc

    Parameters:
        noise [str]: The surface of the noise

    Returns:
        int: The perimeter of the biggest noise bloc
    """
    largest_perimeter = 0
    ### YOUR CODE GOES HERE ###
    coord = {}
    for row in range(len(noise[0])):
        for col in range(len(noise)):
            coord[row, col] = noise[row][col]
    print(coord)

    island = []
    for item in coord.keys():
        if coord[item] == "#":
            island.append(item)
            break
    while True:
        temp = []
        for item in island:
            if item[0] == 0:

            if item[0] == len
            for x in range((item[0])-1,item[0]+2,2 ):

                #dropped





    return largest_perimeter
solve([ ".......##....##.....",
  "##.........########.",
  "###....###.#####....",
  ".##....##.#..##....#",
  "#####..#...#..#...##",
  "#####..##..#....###.",
  "....##.##.......##..",
  "....#.####....######",
  "##..#.#####..##.#.##",
  ".#..##.##....#..#...",
  "...##.###....####.##",
  "....##.#####......##",
  ".#..##....##.......#",
  "...#.#..#..#........",
  ".##..#..##........##",
  ".#...#.....#.##.##..",
  "#....##.....####..#.",
  "####....###.#######.",
  ".##.....#.#..##..#..",
  ".###..###...###....." ]
        )