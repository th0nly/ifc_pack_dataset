from pathlib import Path

from .config import (
    DEFAULT_REPO_ID,
    DEFAULT_REPO_TYPE,
    DEFAULT_REVISION,
    SPLIT_FILE,
    SUPPORTED_VARIANTS,
)
from .utils import ensure_dir, extract_zip, safe_print_file_info


def _supported_variants_text():
    return ", ".join(sorted(SUPPORTED_VARIANTS))


def _download_file(filename, downloads_dir, repo_id, revision, force):
    from huggingface_hub import hf_hub_download

    local_path = Path(downloads_dir) / filename

    if local_path.exists() and not force:
        print(f"Using existing download: {local_path}")
        return local_path

    if local_path.exists() and force:
        print(f"Removing existing download before re-download: {local_path}")
        local_path.unlink()

    print(f"Downloading from Hugging Face: {repo_id}/{filename}")
    downloaded_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type=DEFAULT_REPO_TYPE,
        revision=revision,
        local_dir=str(downloads_dir),
    )
    return Path(downloaded_path)


def download_dataset(
    variant: str,
    out_dir: str,
    repo_id: str = DEFAULT_REPO_ID,
    revision: str = DEFAULT_REVISION,
    extract: bool = True,
    force: bool = False,
):
    variant = variant.lower().strip()

    if variant not in SUPPORTED_VARIANTS:
        raise ValueError(
            f"Unsupported variant: {variant}. "
            f"Supported variants are: {_supported_variants_text()}."
        )

    out_dir = ensure_dir(out_dir)
    downloads_dir = ensure_dir(out_dir / "downloads")

    variant_file = SUPPORTED_VARIANTS[variant]
    files_to_download = {
        variant: variant_file,
        "split": SPLIT_FILE,
    }

    print(f"IFC dataset repo: {repo_id}")
    print(f"Revision: {revision}")
    print(f"Variant: {variant}")
    print(f"Output directory: {out_dir}")

    downloaded_files = {}
    for label, filename in files_to_download.items():
        path = _download_file(
            filename=filename,
            downloads_dir=downloads_dir,
            repo_id=repo_id,
            revision=revision,
            force=force,
        )
        downloaded_files[label] = path
        safe_print_file_info(path)

    if extract:
        print("Starting extraction...")
        for label, zip_path in downloaded_files.items():
            print(f"Extracting {label} archive.")
            extract_zip(zip_path, out_dir, force=force)
    else:
        print("Skipping extraction because extract=False.")

    print("Done.")
    return downloaded_files
