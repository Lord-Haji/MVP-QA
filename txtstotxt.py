import os

folder_path = "transcripts"
output_file = "output.txt"

# Open the output file in write mode
with open(output_file, "w") as output:
    # Iterate over the root folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Get the full file path
            file_path = os.path.join(root, file_name)

            # Extract the heading from the file name
            heading = os.path.splitext(file_name)[0].replace("_", " ").title() + ":"

            # Read the content of the file
            with open(file_path, "r") as file:
                content = file.read()

            # Write the heading and content to the output file
            output.write(heading + " " + content + "\n")

            print(f"Content from {file_name} added to the output file.")

print("Extraction completed.")
