from pathlib import Path
import zipfile


def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def extract_zip(zip_path, target_dir, force=False):
    zip_path = Path(zip_path)
    target_dir = ensure_dir(target_dir).resolve()

    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file does not exist: {zip_path}")

    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"File is not a valid zip archive: {zip_path}")

    print(f"Extracting: {zip_path}")
    print(f"Target directory: {target_dir}")

    with zipfile.ZipFile(zip_path, "r") as archive:
        for member in archive.infolist():
            target_path = (target_dir / member.filename).resolve()
            if target_dir not in target_path.parents and target_path != target_dir:
                raise ValueError(f"Unsafe zip member path: {member.filename}")
            if target_path.exists() and not force:
                print(f"Skipping existing file: {target_path}")
                continue
            archive.extract(member, target_dir)

    print(f"Extraction finished: {zip_path.name}")


def safe_print_file_info(path):
    path = Path(path)
    if not path.exists():
        print(f"File not found: {path}")
        return

    size_mb = path.stat().st_size / (1024 * 1024)
    print(f"File: {path}")
    print(f"Size: {size_mb:.2f} MB")
