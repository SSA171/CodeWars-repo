
def bar_triang(point_a, point_b, point_c): 
    x = (point_a[0] + point_b[0] + point_c[0]) / 3.0
    y = (point_a[1] + point_b[1] + point_c[1]) / 3.0

    return [round(x,4),round(y,4)]

def main():
    while True:
        point_a = input("Point a: ").split()
        a = [float(x) for x in point_a]
        point_b = input("Point b: ").split()
        b = [float(x) for x in point_b]
        point_c = input("Point c: ").split()
        c = [float(x) for x in point_c]
        print(bar_triang(a, b, c))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
