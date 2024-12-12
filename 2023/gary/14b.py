def read_data(data):
  grid = []
  for line in data.splitlines():
    grid.append(list(line))
  return grid

def pprint(grid):
  for line in grid:
    print(''.join(line))

def tilt_north_south(grid, dir='n'):
  while True:
    change = False
    for i in range(len(grid)-1):
      for j in range(len(grid[i])):
        if dir == 'n' and grid[i][j] == '.' and grid[i+1][j] == 'O':
          grid[i][j] = 'O'
          grid[i+1][j] = '.'
          change = True
        elif dir == 's' and grid[i][j] == 'O' and grid[i+1][j] == '.':
          grid[i][j] = '.'
          grid[i+1][j] = 'O'
          change = True
    if not change: break
  return grid

def tilt_east_west(grid, dir='e'):
  while True:
    change = False
    for i in range(len(grid)):
      for j in range(len(grid[i])-1):
        if dir == 'e' and grid[i][j] == 'O' and grid[i][j+1] == '.':
          grid[i][j] = '.'
          grid[i][j+1] = 'O'
          change = True
        elif dir == 'w' and grid[i][j] == '.' and grid[i][j+1] == 'O':
          grid[i][j] = 'O'
          grid[i][j+1] = '.'
          change = True
    if not change: break
  return grid

def cycle(grid):
  grid = tilt_north_south(grid, 'n')
  grid = tilt_east_west(grid, 'w')
  grid = tilt_north_south(grid, 's')
  grid = tilt_east_west(grid, 'e')
  return grid

def weight(grid):
  N = len(grid)
  w = 0
  for i in range(N):
    for j in range(N):
      if grid[i][j] == 'O':
        w += N-i
  return w

def hash_grid(grid):
  return hash(tuple( (''.join(line) for line in grid) ))

def main():
  T = 1000000000
  grid = read_data(data2)
  times = {}
  weights = {}
  time = 1
  print(0, weight(grid), hash_grid(grid))
  while True:
    grid = cycle(grid)
    h = hash_grid(grid)
    w = weight(grid)
    if h in times:
      start = times[h]
      break
    times[h] = time
    weights[time] = w
    time += 1
  print(weights[start + (T - start) % (time - start)])



data1 = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

data2 = """\
#...#...O....OO.#O.O........#.OO.#.O..O.O.#.#..O#..O...#.#......#..O.....O.###O..OO.#.....O.O.......
O.#..#..O.O...O..#OO#...#.#.OO....O.#.....O.#OOO.#O.#O#O.......O......O.OO.#.#.........O..#.....#...
....O..O..O#...#O#......O...##O#.O.....#O..##..O...#O..O.O..#.O..O..#.....OO....O.O.O...O......#.O.O
##O....O....#.OOO...O.#....O#.O#OO....O....O#...O..O#O.#..O.OO...O..O..#.#O..OO.O...O..#.#OO#.......
.O.O#OO..#...#..........O#.O..##.O..OO.O...#........O##.OOOO..#.#....O..O#O.#O.##..OO..O...#..O##...
OO...O##.....#...O.#O.....#.OOO.#.##...##...##.O.....##....O..O..#..#..OO...#..........OO..#.O#...O.
.OO#..#.O.O##...O....O...O....#.O.O..#.OO........O..O..O..###..O...O#..#..#......OO.O..#O....O##.#..
#O.O..O#...O..O.O.O...#.....O..O......O....OO.OO..O#.O#..#.O......#..O...#.O.##.#....O.OO.#...O...O#
.#.O.....O...O...O...O.#.........OO.....#................O....O..#..........##.O#.OO..O###..#.......
#O...#O..O#.......O...#..O...OO..#...O........#....O#..OO...O.O..#.OOO.....O..O.#...O.OO#.OO#.OO.O#.
......#.O...O...O.O...#...#O.O#....#.O..###..O....#.#.O.OO#....O#.....O...#.O......##......#O..#OO..
#OO.##...#..O....#...#...OO...........OO.O.OOOO...#...#O..#...#O#.O.O......O....O..#.O..O...#O#.O.O.
#...O.OO...#.#.OO...O#O....OO....#O....O.O#..#....O...##..O..O.#..#..#...........O...OO#.#..O.....O#
..#..O.O#.....O....O#..#........OO#.#...#O.O....O#....O#...O..#....OO#.O.#........#O....O.O...##O.#O
....#O.....O#...O.......O.......OO..#.....#...O##.O.......#O#....O...O..O.O.......#.....#..#.O.O.O..
.....O.....O.O.O#O.O##.....OOO#...#O.O#O.....#.O#..........O#O.....O.OOO..##.#O....O.O.....#.O.O#O.#
O#O....O.#.......O.O.OO.#..#...#O#..O...O.......O.#........#O#....O....O.#...#.O.#O...O.#.........O.
........O.O...O.#O....#..O....#O.....OO#..O.O..####..#...O..O...OOO.#OO..#....#...OO..O.....#O..O..#
O#...##...#..#O#..#O#..O#....OO..O#O#.....OOOOOO#.#.O.O..O.OO.O........O...#.#......OO#...#..#.#...#
..OO.O..OO.OO....#........#O.#...#O....#...O.OO...O#..O......O.###....#O......#.....####...#..#.#OO.
..O.O..O#....#.O.#.#.#.O#..O.......OO.........##.O.....#OOO..O#..#OO#.....O...OO.O.O...#...OO#.O.#..
O...#........###..##..O#.#O.O..O.#OO.OO...#....#O.O#O..OO...##....O......OO..#...#.......#...#......
..O..#.O#...OO#O.O#....#.....O#..O..O#..O.O..O.#O.O.#O.#OO..#........#.#O..#O....O..#...#OO#...#.O.O
..#O..O.....#....O.O...O.#O.#.O#.O......#........OO...O....#.O........O#.OO#..........O.O..OOOOO#.#.
O..##.##...........O##.#...#.O.#.OO..O.O...OO#.#..#...O..O....#..#..#...O###......O#.#O#..O.#....O.#
#.O.O.O.###.##......#.OO...OO.O..OOO.O.OOO.....##..O#...O......O.#O..#...#...OO..O#......O....##.O.#
#...#.O.O....O..#...#........##O#O#O..##O.#......O...OO#O...OOOO#O..OO##..#......O.#O.#.O#.OO...O..#
#..#........#O.#O.#...O...O....#OO...O....#...O..#......#..O..O...##........O..#.O..#.#OO..OO.O##.O.
..#...#...OO.#.O#O.O.##..#..##..O#...O#....#..O....OO.OOO..O#.#....O.......OO.#.O#.....O.#O.O.#.....
.......O...O..O...#.O..OO...O.....O.O#..#OO#.O...O..O#O..O..#.OO.......O..O....OOOO..O.#.O#O#..O.##.
.####...O.....#...#......#.O...........O......O.#O.....O.#......#.#...O...#......#..O#.....O.O..O..#
O....O...#OO##.O.O...O....O..O......O.O..O..O..O#O..O.O#O.#O.#..OO.....#.O.#O#..##.#.O.O...OO....#..
....#.O..O..#...#....O............O.O.#O.#.O...O....O.#.OO....O..O##...O##......O....O...OO........#
.#O...O..O.O.#O.......O###OO.O.O.O.....##O..OO...#.O..#OO..#...#...#.O.O###.....#O#..##.#O.....O....
..#.###.#..##......#..#.#OO..O......O..#OOO.#O...#....OO.##O...O..#.#O....#OO....O.#.......#....O...
#OO...#......#..#........#.OO.##....#...OOOO..O#O..O.#..#O........#O.OO#..........OO..OO....O..#O.#.
..##.##.O....#.##O..#...###..O##.#.#......O#O..###..##......O...#.....##.#...........O.O.O....O.#...
...O.#..#......#.OO..#..O##...O..O...OO##...OO.O#....O.O.#.O.....O..#..O..#...O..#O.....O.O..O.O#.##
O......###OOO#.#.....OO...O.....O.##.....OO..........OO#O#.O.#.#O....O..#O.#..........##O...#O....O.
..#...#...OO.OO#.....OO...O.O.O.##.##O##..O.#.O#..O.O.....OOOO....#....O.O.#..##OO.O#..#O.O.#...O...
.#.OO.##....O..O...O..#.##.O#OO..#.....OO.........O.OOO.#..O....O....OOO.#.OO..O..#...O#OO.OO##.#.O.
.#.OO.O#.O.O.....#O..O.O..O......O.#O...O..O...##.O#..#.O.....O...O....OO.OOO..OO.O...OO..#.#..OOO#.
.#..O.#.O..#.OOO....#O#O#............##.#.O...O....O.OO..#.O....O#O#.O.#...#....#..OO.O.O#.#.....O.O
O....O.O#....O..#.......O..#O.##.#...O..O.......O#.#.....#..#..O......O..O.....#............##OO....
O#.O...O.##O..OO..O.O.O.#O.O..##..O#.#..#O..O#O...#...OO..#.O.O....OO..O..#..O.......O.O#....O..#.O#
#.O..##......#..O#O..........##O#.#O..O#.#..#.O..##O.O.#.OO....O#..........O..#.##..#..O.#...#O.OO..
.O..#....OO...O.......#...#...O.##...O..O.O.........OO#O.OO.O..O...O.##.....##.....##O..#......O....
#..O.O..OO....O.O#.#O#........O..OO#.OO#O.O..O..#......O#...##.......#..##..O.#..#.O.O...#....#.O...
#..O.#...OO#.OO#.O.OO.O##.#....OO....#........#.O.O....O.#..O#..#....#.O#..O#..O.....OO..OOOO.....O.
.O..OO#.O#OO..#O..O.#......O..O..O.#O.#..#.#.O..O.O..O.....##.OO..#O.#............O#...#......O.OO.#
O......##OO....O...O......#...O..O.#...OO#O..O.OOO..O.....O...#.##..OOO.##...O.O....O#O....##...#...
..OO..#.O.O..#O.O...O...#...O.O#.##O....##...###O..O...O.O##..........###...O...O..#...#.#.....O....
#..OO....O..#O..OO...OO.............O.O..OOO.O.#.....O#O....#O.....#.O..O....O..O....O..O....O.#....
OO.O##..O...#O........#O...#OOOO.O..O....O...O..O..O#.O.O..##.##..O.#O...O#...#..O...O...OO.......O.
#..O#..O...O.#......#OO.OO.O.#...O...O#...#...O..##O#....#......#.....#..#O...#.O.O..............O#.
##..OO#..........#.O..OOOOO..#...#....#.#..O#O...O....#.O.#O#OO.#......#...O........O...O#....#....O
.....O...O#....O..O..OO.O..#...O.#..#..#...O#..#O....O.#.....#O....O...##....#..#......###.O.....O#.
#...O#..O..O#..OO....#.#...#O#..#.....#..#..................OO....O......OO.........O###O#....OO.O..
O#...O.O.O..##.....##....#....#......#...O.#...O..##...O..O...##..#....#..O..O#...##..O.O..OOO..#...
..#.......#.O..O..#O....#...#.....OOO#...O#...O#.#.#O.....O#O.#.O.#.O......O.#..O.O..O#......O.O..O#
...O.#.#..O.#..###..#...#.....O..O.....OO#..O..#.O..#....OOO...........#.......#..OO..OO#.#O....#O..
.O.O...#....#.#O..#..OO#..#....OO....#O..O#.#..#..O.#..O.#O#..OO........#O.#...OO....OO......#.#O...
OO.O.O#..#.#.#.O.OOO...#....O..O##...O.OO#.#.....O.....#.....O....#.........O...O..........OOO.O.OOO
......O...O...###....##.O.O..OOO..O.O......O.#.......#..O..........O#..#..#O.#.##.....###.#O#O#O..#.
O..#..#O.OO.......#.OO...#OO..OO.O#O.....#.#.O..OOO.OO.##O.O#...#.O......#..#O#O...O#..........O.O#.
OO#...O..#..O.#..O........O.....O.....O........O..#....###..O..O..#...O...#.#.##.......O..#.O#O#O...
.......O..O...O...O.OO#.O.#..OO............O.O.O.#..OO#....##O.....O#.....O##O.....O.#...###O.....#.
.....O....OO..O..#O.....O#..O..O.#.#O#.#O#....O.#O..O#.O#.OO......#.O#..O.O...O...#...#..O....#...#O
#...#....#..O..#.O..#.##O..#O..#..OOO.#..##.....OO.O.....OOO.#..O.#.##O#..O.#..#.#.#....#O#...##....
.OO.O..###....#O....O..#.O.#.......#....O###..O.#......O#....#........O...#O..#..#.........O......##
O#......O#.....#.O....#..#.O.#O.......OO#...#..#.#O.#.O.##......#.#.#..O#O.#...O......O..OOO..OO.###
#O.#.O...O.....O....#OO##...OO..#...OO.#O.OOO.O..#O....O............#....#....#...........O.OOO#.OO.
.O.O.#OO#O.O.OO#..O..#....O.#..O...O....O.#OO#O...##.......O...O.....#.O...#...O.##O...OOO.O........
.O#..O.......#..##..OO#.....O.#.OO#...#O.O..O......O..OO.#...#.#............O#O.OO.......O#........#
.OO#..O##...........O.OO.....#.##....O#.#.#O..O...O..#..#..O.......#......#.#...........###O##......
...#...#.....O........OO..#.#...O.#.....#.OO.....#.O.#OO......#OO..#.....#..O##..O..#...O.O.......O#
O...O...#O..#O#O.......#..#O....#OO....#.#O.....O....O##.#...O.......#.....#........#O.O...O...O....
..#.....OO.#.OO....O#O....O#O...O.O...#O.##....##O...#..##O#.OO#O..OOO.#.#......O.OO.O..O.O.OO.#O.#.
.......O.....##...O#.#O.#....O.....O........#...#.OO...#...OO........#OO#...#..OO..O...#....O#.#OO.O
..#..O.OO....O...#.......OO.O.##...#...O...#.O#.OO#....O...O..O###.O.###O..#....##.O.##....O..##...#
.......OOO.....OO..#..O..#O.OOO#O.....O.O#.....O....###..O#..OO..O....###O.OO...#..#.O....#.O.O..#OO
.#...#.........#.###..#...#.#...#O.#..O#O#OOOO#.#.O.....O.#....#..O......#OO....O..O.O.#.O......O..O
O.O....O....O..O......O...#.....O##....OOO.....#.OO.#..O....O..O.O#.O#.OO......#....#......OO......O
..#O.#O.....O...#O...##.O#..O...#..##.O.O.O....#.....#.O#O.....#............O....#.#...#....###...#.
.O..O...OO.....#...........##...O#.O##O........OO..O.###O.#..#..#.O..O.......O....#O.#.........#...#
..##.O....O...O.O.O#O...#O..#..#.#.O...#O.O.O.....#....#...........O...O....O....OO#O.#.O....#..O..O
.#O#....O.....O#O..O##O#..O..O.O.....O........#.#......O#..O..OO.OO#.....OO........O......O#...O.#..
....#.....O..#......O...##.O.O.#..#.....O.O..#.O#.#O...##....O.......#O..O.....#..#.....#.....#.....
.OO....OOO.OO....O...#.......O......#O.#O..O.O#O..............O.#......#.#.......#....#.O....#.#O.#.
OO...OO.#.O#OO#........##.O.....#..#O.#....O..O..O.O#..........O..O.O....#..O.......O....O....O.OO.O
O.#O.......O#.#...#........O...O.O....O#OO....O.O.O...#.#.O#...#O#O.....##..O#O...#O....O....O#OOO.#
.OO#..#..O..........##.O.#OO#..O.O.#...#....O..O#.O..#.#.....O.O..#..OO..##O#...O.O.O#........O.....
.O............#.O...#...#....###.O#.#.#....O.....OO...#O.#.O..O##...#O.#O..OO#..#.O#.#.....O#.......
#..O#..#.OOO#O...O.O..O..#OOO....#...........O##...OOO##O....O.O...O..O#O.........O.OO.....O....O...
.#....#OO..##O..#O##O.#O....#......O.OO..........##.OO#O...#.....O.O.....O#..OO.#........O..O.O..O..
....O.##...#.O.........O.OO....#....##O..#O.......#..O.##O#..#O..#.....O.O#O....#...O..O.OO.........
..###.O.....##.....OO.O..OO.O..#...O.....#....O.O...............O.##.#.O#O#.#...O..#.OOOOO....#.#.#.
O...O....O.#.#.O#.O#..#......O#.....OO.##....OO.....O.......O....O.O.....#...O..OO#..OO..O....#OOO.#
#.#.#.O..#.O...#....#..O....O......O..#..O.OO#O......O.......O.O.........O...O.......OO.##.......#.#
O#..........O...#O.###....#O..O.#......O....#.O.O...O...O.....O#..#.O#..O.#.O..OOO#.O...#..O.#O.....
"""


main()