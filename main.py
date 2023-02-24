import os

folder_path = "C:\\Users\\user\\Desktop\\hud_toasts"  # Replace with the path to your folder
output_file = "file_list.txt"  # Replace with the name of your output file

count = 0

with open(output_file, "w") as f:
    for filename in os.listdir(folder_path):
        base_name, extension = os.path.splitext(filename)
        f.write(base_name + "\n")
        count += 1 # Increment the count for each file written

print(f'File Writing Complete! Wrote {count} files to {output_file}')