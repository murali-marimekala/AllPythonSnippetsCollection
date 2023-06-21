#Generate Pascals triangle

def genreate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                print(f"adding {triangle[i-1][j-1]} and {triangle[i-1][j]}")
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle

num_rows = int(input("Enter the number of rows: "))
pascals_triangle = genreate_pascals_triangle(num_rows)

print("Pascals Triangle: ")
for row in pascals_triangle:
    print(*row)