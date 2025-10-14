def main():
    print("Bouncy Ball Distance Calculator")

    try:
        initial_height = float(input("Enter the initial height (in feet): "))
        bounciness_index = float(input("Enter the bounciness index (e.g., 0.6): "))
        number_of_bounces = int(input("Enter the number of bounces: "))

        if initial_height <= 0 or not (0 < bounciness_index < 1) or number_of_bounces < 0:
            print("Please enter valid positive values (bounciness index between 0 and 1).")
            return

        total_distance = initial_height  # Drop 1
        current_height = initial_height

        for _ in range(number_of_bounces):
            bounce_height = current_height * bounciness_index
            total_distance += 2 * bounce_height  # first up and down
            current_height = bounce_height

        print(f"\nTotal distance traveled: {total_distance:.2f} feet")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
