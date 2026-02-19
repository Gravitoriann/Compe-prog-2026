## This is the template for DS2, full problem in the rulebook ##
import itertools

def solve(n: int, a: list[int], v: list[int]):
    """
    Find the maximum amount of payload (bytes) succesfully dilevered

    Parameters:
        n int: the number of machines in the network
        a list[int]: target machines (from 1 to n)
        v list[int]: number of bytes of each payload sizes

        
    Returns:
        int: the maximum payload (bytes) that can be succesfully delivered
    """
    total_bytes = 0
    ## YOUR CODE GOES HERE ##
    ## VOTRE CODE VA ICI ##
    machines = [i for i in range(1, n+1)]
    tries = list(itertools.permutations(machines))

    for attempt in tries:
        closed = []
        test_bytes = 0
        for step in attempt:
            if step not in closed:
                if a[step-1] not in closed:

                    test_bytes += v[step-1]
            closed.append(step)
        if test_bytes > total_bytes:
            total_bytes = test_bytes





    return total_bytes
