# IFC-Dataset

`IFC-Dataset` is a lightweight Python command line tool for downloading IFC dataset files from the Hugging Face Dataset repository `B0111/ifc_dataset`.

The PyPI package contains only downloader code. It does not include dataset zip files or extracted data.

## Installation

```bash
pip install IFC-Dataset
```

For local development:

```bash
pip install -e .
```

## Command Line Usage

Show package and dataset information:

```bash
IFC-Dataset info
```

Download and extract the amodal mask version:

```bash
IFC-Dataset download --variant amodal --out ./data
```

Lowercase command is also supported:

```bash
ifc-dataset download --variant original --out ./data
```

Download from a specific Hugging Face revision:

```bash
IFC-Dataset download --variant amodal --out ./data --dataset-version v0.0.1
```

Download without extraction:

```bash
IFC-Dataset download --variant amodal --out ./data --no-extract
```

Force re-download and re-extraction:

```bash
IFC-Dataset download --variant amodal --out ./data --force
```

## Supported Variants

| Variant | Hugging Face file |
| --- | --- |
| `original` | `mask/original.zip` |
| `amodal` | `mask/amodal.zip` |
| `smallest` | `mask/smallest.zip` |

Every download also includes:

```text
mask/split.zip
```

## Data Source

Hugging Face Dataset repository:

```text
B0111/ifc_dataset
```

## Build for PyPI

Install build tools:

```bash
pip install build twine
```

Build distributions:

```bash
python -m build
```

Upload when ready:

```bash
twine upload dist/*
```

