import os
import shutil

def copy_selected_folders(root_dir, folders_to_copy, target_dir):
    for rel_path in folders_to_copy:
        source_path = os.path.join(root_dir, rel_path.strip("\\/"))
        dest_path = os.path.join(target_dir, rel_path.strip("\\/"))

        if not os.path.exists(source_path):
            print(f"Source folder does not exist: {source_path}")
            continue

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        try:
            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
                print(f"Copied folder: {rel_path}")
            else:
                shutil.copy2(source_path, dest_path)
                print(f"Copied file: {rel_path}")
        except Exception as e:
            print(f"Failed to copy {rel_path}: {e}")

if __name__ == "__main__":
    root_directory = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6"
    target_directory = r"X:\Perpheads\winter-pack"

    folders = [
        r"\maps",
        r"\scripts",
        r"\particles",
        r"\materials\ayjay\foliage",
        r"\materials\ayjay\props\environment",
        r"\materials\ayjay\textures\flooring",
        r"\materials\Jarheads\blends",
        r"\materials\Jarheads\decals",
        r"\materials\Jarheads\floor",
        r"\materials\Jarheads\glass",
        r"\materials\Jarheads\other",
        r"\materials\Jarheads\roads",
        r"\materials\Jarheads\roof",
        r"\materials\Jarheads\tiles",
        r"\materials\materials_infra",
        r"\materials\models\jarheads\props\Pavilion",
        r"\materials\models\jarheads\props\foliage",
        r"\materials\models\jarheads\props\hospital_bayglass",
        r"\materials\models\jarheads\props\skybox",
        r"\materials\models\jarheads\props\subway_entrance",
        r"\materials\models\jarheads\props\table_umbrella",
        r"\materials\models\propper",
        r"\materials\models\props",
        r"\materials\models\props_infra",
        r"\materials\models\small_props",
        r"\materials\models\stephenpuffs",
        r"\materials\models\update1",
        r"\materials\xq\racing",
        r"\models\ayjay",
        r"\models\jarheads",
        r"\models\props",
        r"\models\props_infra",
        r"\models\static",
    ]

    copy_selected_folders(root_directory, folders, target_directory)