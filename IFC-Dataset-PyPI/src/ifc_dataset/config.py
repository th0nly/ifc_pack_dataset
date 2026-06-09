DEFAULT_REPO_ID = "B0111/ifc_dataset"
DEFAULT_REPO_TYPE = "dataset"
DEFAULT_REVISION = "main"

# Central download registry.
#
# Add new downloadable mask archives here. The CLI choices, list output, and
# downloader validation all read from this mapping, so future mask changes
# should usually only require editing this file.
SUPPORTED_VARIANTS = {
    "original": "mask/original.zip",
    "amodal": "mask/amodal.zip",
    "smallest": "mask/smallest.zip",
    "split": "mask/split.zip",
}

# Reserved for future RAW dataset entries. Keep RAW configuration separate from
# mask archives so the CLI can later add a dedicated --raw option without
# rewriting mask download behavior.
SUPPORTED_RAW_FILES = {}

