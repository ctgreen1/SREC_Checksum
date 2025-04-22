# SREC Line Checksum Generator

This repository contains a lightweight Python script designed to generate the correct checksum for a single line of an [SREC (Motorola S-record)](https://en.wikipedia.org/wiki/SREC_(file_format)) file. This can be useful for manually constructing or modifying `.srec` firmware files, especially in low-level embedded systems work.

## Features

- Calculates the correct checksum for a single SREC line
- Pure Python, no dependencies
- Easy to use for scripting or manual patching workflows

## Usage

```bash
python srec_checksum.py
