from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)

def main():
    user_input = input(
        "Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): "
    )

    try:
        # Split input
        raw_list = user_input.split(",")

        # Clean whitespaces
        cleaned_strings = strip_whitespaces(raw_list)

        # Convert to float
        numbers = [float(num) for num in cleaned_strings if num != ""]

        # Remove duplicates
        unique_numbers = remove_duplicates(numbers)

        print(f"Cleaned and unique data: {unique_numbers}")
        print("--------------------")

        # Analysis
        mean_val = calculate_mean(unique_numbers)
        max_val = find_maximum(unique_numbers)
        min_val = find_minimum(unique_numbers)

        print(f"Mean: {mean_val:.2f}")
        print(f"Maximum: {max_val}")
        print(f"Minimum: {min_val}")

    except Exception as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()                                                