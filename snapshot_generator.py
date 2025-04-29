import os
import json
import hashlib
from datetime import datetime

# Složky, které nechceme zahrnout do snapshotu
EXCLUDE_DIRS = ['venv', '__pycache__', 'migrations', 'static', 'media', '.git']

def get_file_checksum(file_path, algorithm="sha256"):
    """Vypočítá kontrolní součet souboru pomocí zadaného algoritmu."""
    hash_func = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def create_snapshot(directory):
    """Prochází zadaný adresář rekurzivně a generuje snapshot všech souborů s vybranými příponami."""
    snapshot = {}
    for root, dirs, files in os.walk(directory, topdown=True):
        # Odebrání nežádoucích složek z průchodu
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file_name in files:
            if file_name.endswith((".py", ".js", ".html")):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    stats = os.stat(file_path)
                    last_modified = datetime.fromtimestamp(stats.st_mtime).isoformat()
                    checksum = get_file_checksum(file_path)

                    snapshot[file_path] = {
                        "content": content,
                        "last_modified": last_modified,
                        "checksum": checksum
                    }
                except Exception as e:
                    print(f"Chyba při čtení {file_path}: {e}")
    return snapshot

if __name__ == "__main__":
    directory_to_snapshot = r"C:\Users\tasev\lifehub"

    snapshot_data = create_snapshot(directory_to_snapshot)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_filename = f"snapshot_{timestamp}.json"

    output_dir = "snapshots"
    os.makedirs(output_dir, exist_ok=True)
    snapshot_filepath = os.path.join(output_dir, snapshot_filename)

    with open(snapshot_filepath, "w", encoding="utf-8") as json_file:
        json.dump(snapshot_data, json_file, ensure_ascii=False, indent=4)

    print(f"Snapshot byl úspěšně vytvořen a uložen jako {snapshot_filepath}")
