import geometry_utils

def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    operation = input("Enter the operation you want to perform: ").strip()

    operations_map = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    try:
        if operation not in operations_map:
            raise ValueError("Invalid operation selected.")

        if "circle" in operation:
            radius = float(input("Enter radius: "))
            result = operations_map[operation](radius)

        elif "rectangle" in operation:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations_map[operation](width, height)

        elif "triangle" in operation:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations_map[operation](base, height)

        print(f"Result: {round(result, 2)}")

    except Exception as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()