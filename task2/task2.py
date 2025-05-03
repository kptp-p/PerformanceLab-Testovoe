import sys


def read_circle_file(path: str) -> tuple[tuple[float, float], float]:
    with open(path, "r") as f:
        lines = [tuple(map(float, line.split())) for line in f]
    center = lines[0]
    radius = lines[1][0]
    return center, radius


def read_points(path: str) -> list[tuple[float, float]]:
    with open(path, "r") as f:
        return [tuple(map(float, line.split())) for line in f]


def calculate_position_point(
    crl_points: tuple[float, float],
    radius: float,
    point_coord_list: list[tuple[float, float]]
) -> None:

    radius_sq = radius ** 2

    for point in point_coord_list:
        distance_sq = (point[0] - circle_points[0]) ** 2 + (point[1] - crl_points[1]) ** 2
        if distance_sq > radius_sq:
            print('2')
        elif distance_sq < radius_sq:
            print('1')
        else:
            print('0')


if __name__ == '__main__':
    circle_crd_file = sys.argv[1]
    point_crd_file = sys.argv[2]

    circle_points, radius = read_circle_file(circle_crd_file)
    point_coord_list = read_points(point_crd_file)

    calculate_position_point(circle_points, radius, point_coord_list)
