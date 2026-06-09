import ifc_dataset
from ifc_dataset.downloader import download_dataset


def test_version():
    assert ifc_dataset.version == "0.0.1"

