class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


def main():
    print(Ball().ball_type)
    print(Ball('super').ball_type)

if __name__ == "__main__":
    main()