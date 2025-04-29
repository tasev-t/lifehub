import os

def generate_file_snapshot(start_path='.', exclude_hidden=True):
    """
    Prochází projektový adresář a vrací seznam cest ke všem souborům.
    """
    file_list = []
    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, filename), start_path)
            if exclude_hidden and any(part.startswith('.') for part in rel_path.split(os.sep)):
                continue
            file_list.append(rel_path.replace("\\", "/"))  # Windows-friendly
    return sorted(file_list)

def save_snapshot_to_file(snapshot, output_file='project_snapshot.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for path in snapshot:
            f.write(path + '\n')
