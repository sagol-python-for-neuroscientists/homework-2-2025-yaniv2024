import filecmp
import difflib

file1 = "lorem_morse.txt"
file2 = "expected_lorem_morse.txt"

# Compare the files
are_files_identical = filecmp.cmp(file1, file2, shallow=False)

if are_files_identical:
    print("The files are identical.")
else:
    print("The files are different.\n")
    with open(file1) as f1, open(file2) as f2:
        diff = difflib.unified_diff(
            f1.readlines(),
            f2.readlines(),
            fromfile=file1,
            tofile=file2,
            lineterm=''
        )

        for line in diff:
            if line.startswith('+ ') or line.startswith('- '):
                line_type = "Added" if line.startswith('+ ') else "Removed"
                line_content = line[2:]
                print(f"{line_type}: {line_content}")
            elif line.startswith('@@'):
                # Extract line and character numbers from the diff header
                header_parts = line.split(' ')
                old_file_info = header_parts[1]
                new_file_info = header_parts[2]
                print(f"Change at {old_file_info} -> {new_file_info}")