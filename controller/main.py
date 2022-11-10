from model.point2d import Point2D

def main():
   # point = Point2D(1,6)
    point1 = Point2D(1)
    point2 = Point2D(23)
    print(point1.calculate_distance(point2))

    # Point2D.calculate_distance(point1)
    # print(hex(hash(point)))
    # print(hex(id(point)))


if __name__ == "__main__":
    main()