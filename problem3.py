"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        number = input("Insert a list of numbers, when done type: 'done' ").strip()
        

        if number.lower() == "done":
            break

        if number.isdigit():
            numbers.append(float(number))
        else:
            print("Try again, type 'done' when you are done!")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None
    else:
        count = len(numbers)
        tot_sum = sum(numbers)
        average = tot_sum/count
        min_num = min(numbers)
        max_num = max(numbers)
        even_count = sum(1 for n in numbers if n.is_integer() and int(n) % 2 == 0)
        odd_count = sum(1 for n in numbers if n.is_integer() and int(n) % 2 != 0)


    analysis = {
        "count": count,
        "sum": tot_sum,
        "average": average,
        "minimum": min_num,
        "maximum": max_num,
        "even_count": even_count,
        "odd_count": odd_count
    }

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    print("Count:", analysis.get("count"))
    print("Sum:", analysis.get("sum"))
    print("Average:", analysis.get("average"))
    print("Minimum:", analysis.get("minimum"))
    print("Maximum:", analysis.get("maximum"))
    print("Even Count:", analysis.get("even_count"))
    print("Odd Count:", analysis.get("odd_count"))


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()
