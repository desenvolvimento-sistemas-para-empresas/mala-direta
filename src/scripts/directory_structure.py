import os

IGNORE_DIRS = {".venv", ".venvArch", "objects"}  # Adicione outros diretórios que deseja ignorar

def create_tree_structure(root_path, output_file):
    with open(output_file, 'w') as file:
        generate_tree_structure(root_path, file, "", "")

def generate_tree_structure(path, file, prefix, last_prefix):
    contents = os.listdir(path)
    contents.sort()

    for i, item in enumerate(contents):
        full_path = os.path.join(path, item)
        is_last = i == len(contents) - 1

        if item not in IGNORE_DIRS:
            if os.path.isdir(full_path):
                file.write(f"{prefix}{'├── ' if not is_last else '└── '} {item}/\n")
                new_prefix = last_prefix + ("│  " if not is_last else "   ")
                generate_tree_structure(full_path, file, new_prefix, last_prefix + ("   " if not is_last else "│  "))
            else:
                file.write(f"{prefix}{'├── ' if not is_last else '└── '} {item}\n")

if __name__ == "__main__":
    root_directory = os.path.abspath(".")
    output_file = "tree_structure.md"
    
    create_tree_structure(root_directory, output_file)
    print(f"Tree structure saved to {output_file}")
