import argparse

from . import version
from .config import DEFAULT_REPO_ID, DEFAULT_REVISION, SUPPORTED_VARIANTS
from .downloader import download_dataset


def build_parser():
    parser = argparse.ArgumentParser(
        prog="IFC-Dataset",
        description="Download IFC dataset files from Hugging Face.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    download_parser = subparsers.add_parser(
        "download",
        help="Download one mask archive.",
    )
    download_parser.add_argument(
        "--mask",
        choices=sorted(SUPPORTED_VARIANTS),
        default="smallest",
        help="Mask archive to download.",
    )
    download_parser.add_argument(
        "--out",
        required=True,
        help="Output directory.",
    )
    download_parser.add_argument(
        "--repo-id",
        default=DEFAULT_REPO_ID,
        help="Hugging Face dataset repository ID.",
    )
    download_parser.add_argument(
        "--dataset-version",
        "--revision",
        dest="revision",
        default=DEFAULT_REVISION,
        help="Hugging Face revision, branch, or tag.",
    )
    download_parser.add_argument(
        "--no-extract",
        action="store_true",
        help="Only download zip files without extracting them.",
    )
    download_parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download and overwrite files during extraction.",
    )

    subparsers.add_parser(
        "info",
        help="Show package and dataset information.",
    )
    subparsers.add_parser(
        "list",
        help="List downloadable dataset files.",
    )
    return parser


def _print_downloadable_files():
    print("Available mask downloads:")
    for mask, path in SUPPORTED_VARIANTS.items():
        print(f"  {mask}: {path}")


def _print_info():
    print(f"IFC-Dataset version: {version}")
    print(f"Default Hugging Face repo: {DEFAULT_REPO_ID}")
    _print_downloadable_files()


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "info":
        _print_info()
        return 0

    if args.command == "list":
        _print_downloadable_files()
        return 0

    if args.command == "download":
        download_dataset(
            mask=args.mask,
            out_dir=args.out,
            repo_id=args.repo_id,
            revision=args.revision,
            extract=not args.no_extract,
            force=args.force,
        )
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
