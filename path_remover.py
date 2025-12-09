##IMPORTANT NOTE
## THIS WILL PERMENANTLY DELETE THESE FILES RECURSIVELY

import os
import shutil

def delete_selected_folders(root_dir, folders_to_delete):
    for rel_path in folders_to_delete:
        target_path = os.path.join(root_dir, rel_path.strip("\\/"))

        if not os.path.exists(target_path):
            print(f"Target does not exist (skipped): {target_path}")
            continue

        try:
            if os.path.isdir(target_path):
                shutil.rmtree(target_path)
                print(f"Deleted folder: {rel_path}")
            else:
                os.remove(target_path)
                print(f"Deleted file: {rel_path}")
        except Exception as e:
            print(f"Failed to delete {rel_path}: {e}")

if __name__ == "__main__":
    root_directory = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\map-content-v6"

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
        r"\materials\models\jarheads\props\jarheads",
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

    delete_selected_folders(root_directory, folders)
