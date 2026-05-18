# PyImgDuplicateFinder

PyImgDuplicateFinder scans a folder of images, detects duplicates, and moves them into a `duplicate` subfolder.

The tool supports two modes:

- `S` (soft): hash-based duplicate detection
- `H` (hard): similarity-based detection using HaarPSI and a threshold

## Requirements

- Python 3.8+

## Usage

Run from the repository root:

```bash
python move-by-fingerprint.py -dir <folder_path> -mode <S|H> [-t <threshold>]
```

Examples:

```bash
# Soft mode (faster)
python move-by-fingerprint.py -dir ./images -mode S

# Hard mode with custom similarity threshold
python move-by-fingerprint.py -dir ./images -mode H -t 0.7
```

Detected duplicates are moved to:

```text
<folder_path>/duplicate/
```

## Command Line Arguments

| Argument | Description |
|:-|:-|
| `-h`, `-help` | Show help and exit |
| `-dir DIR` | Folder to analyze |
| `-mode MODE` | Detection mode: `H` (hard) or `S` (soft) |
| `-t T` | Similarity threshold in range `[0, 1]` (hard mode only, default `0.5`) |

## Credits

HaarPSI implementation source: http://www.haarpsi.org/
