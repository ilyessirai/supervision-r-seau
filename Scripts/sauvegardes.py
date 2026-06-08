import os
import shutil
from datetime import datetime

def perform_backup(source_dir, dest_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(dest_dir, backup_name)
    
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        shutil.make_archive(backup_path, 'gztar', source_dir)
        print(f"Backup created successfully: {backup_path}.tar.gz")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    # Example usage for training
    src = "../Configurations"
    dst = "../Saves"
    perform_backup(src, dst)
