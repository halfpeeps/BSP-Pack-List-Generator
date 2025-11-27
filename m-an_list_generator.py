import os
import sys

def build_asset_list(root_folder, folders_to_include, output_txt_path, excluded_exts=None):
    if excluded_exts:
        excluded_exts = {ext.lower() for ext in excluded_exts}

    assets = []

    for folder_name in folders_to_include:
        full_path = os.path.join(root_folder, folder_name)
        if not os.path.isdir(full_path):
            print(f"Warning: folder does not exist: {full_path}", file=sys.stderr)
            continue

        for root, dirs, files in os.walk(full_path):
            for fname in files:
                if excluded_exts:
                    _, ext = os.path.splitext(fname)
                    if ext.lower() in excluded_exts:
                        continue

                file_path = os.path.join(root, fname)
                rel_path = os.path.relpath(file_path, root_folder)

                # set forward slashes
                rel_path = rel_path.replace(os.path.sep, "/")

                assets.append(rel_path)

    assets.sort()

    with open(output_txt_path, "w", encoding="utf-8") as f:
        for path in assets:
            f.write(path + "\n")

    print(f"Wrote asset list to: {output_txt_path}")


if __name__ == "__main__":
    root_folder = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6"

    folders_to_include = [
        "materials",
        "models",
        "maps",
        "particles",
        "scripts",
    ]

    excluded_exts = {".psd", ".dmx"}  # optional
    output_txt = r"C:\Users\samue\Documents\Github\BSP-Pack-List-Generator\all_assets.txt"

    build_asset_list(root_folder, folders_to_include, output_txt, excluded_exts)