# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:35:50 2026

@author: quima
"""

import os
import hashlib

def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_folder(folder_path):
    results = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            file_hash = hash_file(full_path)

            results.append({
                "file": full_path,
                "size_bytes": size,
                "sha256": file_hash
            })

    return results

if __name__ == "__main__":
    folder = input("Enter folder path to scan: ")
    output = scan_folder(folder)

    for item in output:
        print(f"{item['file']} | {item['size_bytes']} bytes | {item['sha256']}")

    