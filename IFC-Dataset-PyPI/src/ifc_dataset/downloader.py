from pathlib import Path

from .config import (
    DEFAULT_REPO_ID,
    DEFAULT_REPO_TYPE,
    DEFAULT_REVISION,
    SUPPORTED_VARIANTS,
)
from .utils import ensure_dir, extract_zip, safe_print_file_info


def _supported_masks_text():
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
    mask: str,
    out_dir: str,
    repo_id: str = DEFAULT_REPO_ID,
    revision: str = DEFAULT_REVISION,
    extract: bool = True,
    force: bool = False,
):
    mask = mask.lower().strip()

    if mask not in SUPPORTED_VARIANTS:
        raise ValueError(
            f"Unsupported mask: {mask}. "
            f"Supported masks are: {_supported_masks_text()}."
        )

    out_dir = ensure_dir(out_dir)
    downloads_dir = ensure_dir(out_dir / "downloads")

    remote_file = SUPPORTED_VARIANTS[mask]

    print(f"IFC dataset repo: {repo_id}")
    print(f"Revision: {revision}")
    print(f"Mask: {mask}")
    print(f"Output directory: {out_dir}")

    path = _download_file(
        filename=remote_file,
        downloads_dir=downloads_dir,
        repo_id=repo_id,
        revision=revision,
        force=force,
    )
    safe_print_file_info(path)

    if extract:
        print("Starting extraction...")
        print(f"Extracting {mask} archive.")
        extract_zip(path, out_dir, force=force)
    else:
        print("Skipping extraction because extract=False.")

    print("Done.")
    return {mask: path}
