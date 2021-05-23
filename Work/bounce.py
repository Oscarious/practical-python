# bounce.py
#
# Exercise 1.5
if __name__ == '__main__':
    height = 100.0
    for i in range(10):
        height = 0.6 * height
        print(i+1, height, sep=" ")