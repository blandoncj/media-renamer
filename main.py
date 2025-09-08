import os

import typer
from rich.console import Console
from tqdm import tqdm

app = typer.Typer()
console = Console()

# supported file extensions
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"}
ALLOWED_EXTS = IMAGE_EXTS | VIDEO_EXTS


@app.command()
def rename(folder: str, prefix: str | None = None, dry_run: bool = False) -> None:
    """
    Rename photos and videos in bulk inside a given folder.

    Args:
        folder (str): Path to the folder containing media files.
        prefix (str | None, optional): Custom prefix for renamed files. Defaults to None (just numeric index).
        dry_run (bool, optional): If True, simulates the renaming process without making changes. Defaults to False.
    """

    # list all files in the folder with allowed extensions
    files = [
        f
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
        and os.path.splitext(f)[1].lower() in ALLOWED_EXTS
    ]

    console.print(f"[cyan]📂 Processing {len(files)} media files in '{folder}'[/cyan]")
    counter = 1

    for file in tqdm(files, desc="Renaming files"):
        old_path = os.path.join(folder, file)
        ext = os.path.splitext(file)[1].lower()
        new_name = f"{prefix}_{counter:03d}{ext}" if prefix else f"{counter:03d}{ext}"
        new_path = os.path.join(folder, new_name)

        if dry_run:
            console.print(f"[yellow]Dry run:[/yellow] {file} → {new_name}")
        else:
            os.rename(old_path, new_path)
            console.print(f"[green]✔ {file} → {new_name}[/green]")

        counter += 1


if __name__ == "__main__":
    app()
