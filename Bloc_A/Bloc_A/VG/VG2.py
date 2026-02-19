## This is the template for VG2, full problem in the rulebook ##


def solve(sphere: tuple[int, int, int, int], cube: tuple[int, int, int, int]):
    """
    Verify if the sphere and the cube are colliding

    Parameters:
        sphere tuple[int, int, int, int]: The spehere's center's position in 3D and radius
        cube tuple[int, int, int, int]: The cube's center's position in 3D and cube side length

    Returns:
        bool: Is the sphere and the cube colliding
    """
    overlap = 0
    ### YOUR CODE GOES HERE ###
    distance = (((sphere[0]-cube[0])**2)+((sphere[1] - cube[1])**2)+((sphere[3]-cube[3])**2))**(1/2)
    print(distance)
    if distance <= (sphere[3] + cube[3]):
        overlap = 1




    return overlap
print(solve((11,14,3,3), (9,12,11,6)))