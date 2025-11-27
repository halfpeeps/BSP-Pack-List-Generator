#!/usr/bin/env python3
import os
import sys

def build_file_list(folder_mappings, output_txt_path, excluded_exts=None):
    if excluded_exts:
        excluded_exts = {ext.lower() for ext in excluded_exts}

    pairs = []

    for external_folder, internal_prefix in folder_mappings:
        if not os.path.isdir(external_folder):
            print(f"Warning: folder does not exist, skipping: {external_folder}", file=sys.stderr)
            continue

        for root, dirs, files in os.walk(external_folder):
            for fname in files:
                if excluded_exts:
                    _, ext = os.path.splitext(fname)
                    if ext.lower() in excluded_exts:
                        continue

                external_path = os.path.normpath(os.path.join(root, fname))
                rel = os.path.relpath(external_path, external_folder)
                internal_path = os.path.join(internal_prefix, rel).replace(os.path.sep, "/")

                pairs.append((external_path, internal_path))

    pairs.sort(key=lambda p: p[1].lower())

    with open(output_txt_path, "w", encoding="utf-8") as f:
        for external_path, internal_path in pairs:
            f.write(external_path + "\n")
            f.write(internal_path + "\n")

    print(f"Wrote file list to: {output_txt_path}")

if __name__ == "__main__":
    folder_mappings = [
        (r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6\maps", "maps"),
        (r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6\materials", "materials"),
        (r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6\models", "models"),
        (r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6\particles", "particles"),
        (r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6\scripts", "scripts"),
    ]

    excluded_exts = {".psd", ".dmx", ".bsp"}
    output_txt = r"C:\Users\samue\Documents\Github\BSP-Pack-List-Generator\file_list.txt"

    build_file_list(folder_mappings, output_txt, excluded_exts)
