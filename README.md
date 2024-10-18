# Simple File Storage Server with CLI

## Overview

This project provides a simple file storage server and an installable CLI to interact with it. The server allows uploading, deleting, and listing files.

## Requirements

- Docker
- Python 3.9+
- pip

## Setup and Installation

### Using Docker

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd file-storage
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t file-storage-server .
    ```

3. **Run the Docker container**:
    ```bash
    docker run -d -p 5000:5000 --name file-storage-server file-storage-server
    ```

4. **Installing the CLI Tool**:
    ```bash
    pip install --editable .
    ```

## Using the CLI

After installing, you can use the `fs-store` command directly from the terminal.

- **Upload a file**:
    ```bash
    fs-store upload-file /path/to/your/file.txt
    ```

- **Delete a file**:
    ```bash
    fs-store delete-file file.txt
    ```

- **List files**:
    ```bash
    fs-store list-files
    ```

