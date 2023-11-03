input_file_path = input("Enter the file path for the input text file: ")

output_file_path = input("Enter the file path for the output text file: ")

unique_lines = set()

try:
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

        with open(output_file_path, 'w') as output_file:
            for line in lines:
                clean_line = line.strip().lower()

                if clean_line not in unique_lines:
                    output_file.write(line)

                    unique_lines.add(clean_line)

    print("Duplicate lines removed. Unique lines saved in", output_file_path)

except FileNotFoundError:
    print("File not found. Please check the file paths and try again.")
except Exception as e:
    print("An error occurred:", e)
