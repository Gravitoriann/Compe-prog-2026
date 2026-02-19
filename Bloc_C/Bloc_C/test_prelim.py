from Bloc_C.game_visuals import run_pygame_animation
from Bloc_C.prelim import solve
import multiprocessing
import time
import random
import copy

from Bloc_C.game_logic import Crab
from Bloc_C.game_logic import Board
from Bloc_C.game_logic import Position
from Bloc_C.game_logic import Coord
from Bloc_C.game_logic import Direction

nbr_examples = 1

def call_solve(crabs_given, board_given, moves):
    moves.extend(solve(crabs_given, board_given))

## Config 1
crab1_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab1_2 = Crab('2', Position([Coord(3, 2)]), Direction.ANY)
crab1_3 = Crab('3', Position([Coord(4, 4), Coord(4, 3), Coord(4, 2)]), Direction.VERTICAL)
config1 = [crab1_1, crab1_2, crab1_3]

## Config 2
crab2_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab2_2 = Crab('2', Position([Coord(2, 0), Coord(2, 1), Coord(2, 2)]), Direction.VERTICAL)
crab2_3 = Crab('3', Position([Coord(0, 3), Coord(1, 3), Coord(2, 3)]), Direction.HORIZONTAL)
crab2_4 = Crab('4', Position([Coord(5, 3), Coord(5, 4), Coord(5, 5)]), Direction.VERTICAL)
config2 = [crab2_1, crab2_2, crab2_3, crab2_4]

## Config 3
crab3_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab3_2 = Crab('2', Position([Coord(2, 1), Coord(2, 2)]), Direction.VERTICAL)
crab3_3 = Crab('3', Position([Coord(0, 3), Coord(1, 3), Coord(2, 3)]), Direction.HORIZONTAL)
crab3_4 = Crab('4', Position([Coord(2, 4), Coord(2, 5)]), Direction.VERTICAL)
crab3_5 = Crab('5', Position([Coord(4, 1), Coord(4, 2), Coord(4, 3)]), Direction.VERTICAL)
crab3_6 = Crab('6', Position([Coord(4, 4), Coord(5, 4)]), Direction.HORIZONTAL)
crab3_7 = Crab('7', Position([Coord(4, 0)]), Direction.ANY)
config3 = [crab3_1, crab3_2, crab3_3, crab3_4, crab3_5, crab3_6, crab3_7]

## Config 4
crab4_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab4_2 = Crab('2', Position([Coord(0, 1), Coord(1, 1)]), Direction.HORIZONTAL)
crab4_3 = Crab('3', Position([Coord(2, 1), Coord(3, 1), Coord(4, 1)]), Direction.HORIZONTAL)
crab4_4 = Crab('4', Position([Coord(0, 3), Coord(0, 4)]), Direction.VERTICAL)
crab4_5 = Crab('5', Position([Coord(0, 5), Coord(1, 5)]), Direction.HORIZONTAL)
crab4_6 = Crab('6', Position([Coord(1, 3), Coord(2, 3)]), Direction.HORIZONTAL)
crab4_7 = Crab('7', Position([Coord(2, 4), Coord(2, 5)]), Direction.VERTICAL)
crab4_8 = Crab('8', Position([Coord(4, 2), Coord(4, 3)]), Direction.VERTICAL)
crab4_9 = Crab('9', Position([Coord(4, 4), Coord(5, 4)]), Direction.HORIZONTAL)
config4 = [crab4_1, crab4_2, crab4_3, crab4_4, crab4_5, crab4_6, crab4_7, crab4_8, crab4_9]

## Config 5
crab5_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab5_2 = Crab('2', Position([Coord(0, 0), Coord(0, 1)]), Direction.VERTICAL)
crab5_3 = Crab('3', Position([Coord(1, 0), Coord(1, 1)]), Direction.VERTICAL)
crab5_4 = Crab('4', Position([Coord(2, 0), Coord(3, 0)]), Direction.HORIZONTAL)
crab5_5 = Crab('5', Position([Coord(4, 0), Coord(5, 0)]), Direction.HORIZONTAL)
crab5_6 = Crab('6', Position([Coord(3, 1), Coord(3, 2)]), Direction.VERTICAL)
crab5_7 = Crab('7', Position([Coord(4, 1), Coord(4, 2), Coord(4, 3)]), Direction.VERTICAL)
crab5_8 = Crab('8', Position([Coord(1, 3), Coord(2, 3), Coord(3, 3)]), Direction.HORIZONTAL)
crab5_9 = Crab('9', Position([Coord(4, 4)]), Direction.ANY)
config5 = [crab5_1, crab5_2, crab5_3, crab5_4, crab5_5, crab5_6, crab5_7, crab5_8, crab5_9]

## Config 6
crab6_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab6_2 = Crab('2', Position([Coord(0, 3), Coord(1, 3)]), Direction.HORIZONTAL)
crab6_3 = Crab('3', Position([Coord(2, 3), Coord(3, 3)]), Direction.HORIZONTAL)
crab6_4 = Crab('4', Position([Coord(4, 0), Coord(5, 0)]), Direction.HORIZONTAL)
crab6_5 = Crab('5', Position([Coord(4, 2), Coord(4, 3)]), Direction.VERTICAL)
crab6_6 = Crab('6', Position([Coord(5, 1), Coord(5, 2), Coord(5, 3)]), Direction.VERTICAL)
crab6_7 = Crab('7', Position([Coord(4, 4), Coord(5, 4)]), Direction.HORIZONTAL)
crab6_8 = Crab('8', Position([Coord(3, 4), Coord(3, 5)]), Direction.VERTICAL)
config6 = [crab6_1, crab6_2, crab6_3, crab6_4, crab6_5, crab6_6, crab6_7, crab6_8]

## Config 7
crab7_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)
crab7_2 = Crab('2', Position([Coord(3, 0), Coord(3, 1), Coord(3, 2)]), Direction.VERTICAL)
crab7_3 = Crab('3', Position([Coord(4, 0), Coord(4, 1), Coord(4, 2)]), Direction.VERTICAL)
crab7_4 = Crab('4', Position([Coord(5, 0), Coord(5, 1), Coord(5, 2)]), Direction.VERTICAL)
crab7_5 = Crab('5', Position([Coord(0, 5), Coord(1, 5)]), Direction.HORIZONTAL)
crab7_6 = Crab('6', Position([Coord(3, 3), Coord(4, 3), Coord(5, 3)]), Direction.HORIZONTAL)
crab7_7 = Crab('7', Position([Coord(3, 4), Coord(4, 4), Coord(5, 4)]), Direction.HORIZONTAL)
crab7_8 = Crab('8', Position([Coord(3, 5)]), Direction.ANY)
crab7_9 = Crab('9', Position([Coord(4, 5)]), Direction.ANY)
crab7_10 = Crab('10', Position([Coord(5, 5)]), Direction.ANY)
config7 = [crab7_1, crab7_2, crab7_3, crab7_4, crab7_5, crab7_6, crab7_7, crab7_8, crab7_9, crab7_10]


### YOU CAN ADD CONFIGS HERE ###

## Config 8
crab8_1 = Crab('1', Position([Coord(0, 2), Coord(1, 2)]), Direction.HORIZONTAL)


config8 = [crab8_1]


### DON'T FORGET TO ADD IT TO THE LIST OF CONFIGS ###
configs = [config1, config2, config3, config4, config5, config6, config7]

def test_config_1():
    config = config1
    crabs_given = copy.deepcopy(config)
    validation_config = copy.deepcopy(config)
    visual_config = copy.deepcopy(config)

    board_given = Board(config)
    validation_board = Board(validation_config)
    visuals_board = Board(visual_config)

    manager = multiprocessing.Manager()
    moves = manager.list()
    p = multiprocessing.Process(target=call_solve, args=(crabs_given, board_given, moves))

    start_time = time.perf_counter()
    p.start()
    p.join(10) ## wait a maximum of 10 seconds for execution
    end_time = time.perf_counter()
    if p.is_alive():
        print("\nEvaluated example #1 Failed!!\nTime limit of 10 seconds exceeded!")
        p.kill()
        p.join()
        assert True

    valid_answer = validation_board.test_path(moves)
    if valid_answer:
        print("\nAnswer is valid!")
        print(f"Your solution has {len(moves)} moves!")
        print(f"Your solution executed for {end_time-start_time:.6f} seconds")
        run_pygame_animation(visuals_board, moves, f"Evaluated example #1 - Success!! {len(moves)} moves in {end_time-start_time:.6f} seconds")
    else:
        print("Invalid answer")
        run_pygame_animation(visuals_board, moves, "Evaluated example #1 - Failed!!")

def test_config_2():
    config = config2
    crabs_given = copy.deepcopy(config)
    validation_config = copy.deepcopy(config)
    visual_config = copy.deepcopy(config)

    board_given = Board(config)
    validation_board = Board(validation_config)
    visuals_board = Board(visual_config)

    manager = multiprocessing.Manager()
    moves = manager.list()
    p = multiprocessing.Process(target=call_solve, args=(crabs_given, board_given, moves))

    start_time = time.perf_counter()
    p.start()
    p.join(10) ## wait a maximum of 10 seconds for execution
    end_time = time.perf_counter()
    if p.is_alive():
        print("\nEvaluated example #2 Failed!!\nTime limit of 10 seconds exceeded!")
        p.kill()
        p.join()
        assert True

    valid_answer = validation_board.test_path(moves)
    if valid_answer:
        print("\nAnswer is valid!")
        print(f"Your solution has {len(moves)} moves!")
        print(f"Your solution executed for {end_time-start_time:.6f} seconds")
        run_pygame_animation(visuals_board, moves, f"Evaluated example #2 - Success!! {len(moves)} moves in {end_time-start_time:.6f} seconds")
    else:
        print("Invalid answer")
        run_pygame_animation(visuals_board, moves, "Evaluated example #2 - Failed!!")

def test_config_3():
    config = config3
    crabs_given = copy.deepcopy(config)
    validation_config = copy.deepcopy(config)
    visual_config = copy.deepcopy(config)

    board_given = Board(config)
    validation_board = Board(validation_config)
    visuals_board = Board(visual_config)

    manager = multiprocessing.Manager()
    moves = manager.list()
    p = multiprocessing.Process(target=call_solve, args=(crabs_given, board_given, moves))

    start_time = time.perf_counter()
    p.start()
    p.join(10) ## wait a maximum of 10 seconds for execution
    end_time = time.perf_counter()
    if p.is_alive():
        print("\nEvaluated example #3 Failed!!\nTime limit of 10 seconds exceeded!")
        p.kill()
        p.join()
        assert True

    valid_answer = validation_board.test_path(moves)
    if valid_answer:
        print("\nAnswer is valid!")
        print(f"Your solution has {len(moves)} moves!")
        print(f"Your solution executed for {end_time-start_time:.6f} seconds")
        run_pygame_animation(visuals_board, moves, f"Evaluated example #3 - Success!! {len(moves)} moves in {end_time-start_time:.6f} seconds")
    else:
        print("Invalid answer")
        run_pygame_animation(visuals_board, moves, "Evaluated example #3 - Failed!!")

def test_random_configs():
    for i in range(nbr_examples):
        config = random.choice(configs)
        crabs_given = copy.deepcopy(config)
        validation_config = copy.deepcopy(config)
        visual_config = copy.deepcopy(config)

        board_given = Board(config)
        validation_board = Board(validation_config)
        visuals_board = Board(visual_config)

        manager = multiprocessing.Manager()
        moves = manager.list()
        p = multiprocessing.Process(target=call_solve, args=(crabs_given, board_given, moves))

        start_time = time.perf_counter()
        p.start()
        p.join(10) ## wait a maximum of 10 seconds for execution
        end_time = time.perf_counter()
        if p.is_alive():
            print("\nTest " + str(i) + " Failed!!\nTime limit of 10 seconds exceeded!")
            p.kill()
            p.join()
            assert False

        valid_answer = validation_board.test_path(moves)
        if valid_answer:
            print("\nAnswer is valid!")
            print(f"Your solution has {len(moves)} moves!")
            print(f"Your solution executed for {end_time-start_time:.6f} seconds")
            run_pygame_animation(visuals_board, moves, f"Test #{i} - Success!! {len(moves)} moves in {end_time-start_time:.6f} seconds")
        else:
            print("Invalid answer")
            run_pygame_animation(visuals_board, moves, "Test # " + str(i) + " - Failed!!")
    assert False

        
