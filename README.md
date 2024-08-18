# Python HEIC Convert

A simple tool for converting HEIC to other image formats while preserving EXIF data in batch.

## Getting Started

### Prerequisites

* Python 3 (Tested with 3.10)

### Building

* Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

* Build executable
  ```bash
  pyinstaller --onefile convertHEIC.py
  ```

* Your executable will be placed in the `dist` directory

## Usage

* Run the exectuable via commandline
* Input directory is the folder to scan for `.heic` files
* Output directory is where to place the converted files
* Output extension is the file extension of the type of file you want to convert to (i.e. `jpg`, `png`, `bmp`, etc.)
  * Anything Pillow supports should be supported