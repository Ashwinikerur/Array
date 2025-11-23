import sys

def main():
    if len(sys.argv) < 2:
        print("Error: No scores provided. Pass values like: python array.py \"10 20 30\"")
        return

    try:
        numbers = list(map(int, sys.argv[1].split()))
        
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        print("Scores:", numbers)
        print("Sum:", total)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)


    except ValueError:
        print("Error: Please enter only numbers separated by spaces")

if __name__== "__main__":
    main()