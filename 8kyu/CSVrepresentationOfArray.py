
def to_csv_text(array):
    return "\n".join(",".join(map(str, i)) for i in array)


def main():
    array = [[0, 1, 2, 3, 4 ],
             [10,11,12,13,14],
             [20,21,22,23,24],
             [30,31,32,33,34]]

    print(to_csv_text(array))

if __name__ == "__main__":
    main()