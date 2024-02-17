import shutil
from pathlib import Path
from typing import Iterator

TOP_LEVEL = 4
FOLDERS_PER_LEVEL = 5
TESTS_FILES_PER_FOLDER = 5
TESTS_PER_FILE = 5

root = Path("root")
if root.is_dir():
    shutil.rmtree(root)
root.mkdir()

TEST_CONTENTS = f"""
import pytest
@pytest.mark.parametrize("i", range({TESTS_PER_FILE}))
def test(i): pass
"""


def generate_top_level(parent: Path) -> list[Path]:
    print(f"generate_top_level {parent=}")
    result = []
    for top_level_index in range(TOP_LEVEL):
        tests_dir = parent / f"dir_{top_level_index}"
        tests_dir.mkdir()
        (tests_dir / "__init__.py").touch()
        for folder_index in range(FOLDERS_PER_LEVEL):
            folder_path = tests_dir / f"folder_{folder_index}"
            folder_path.mkdir()
            (folder_path / "__init__.py").touch()
            for file_index in range(TESTS_FILES_PER_FOLDER):
                fn = folder_path / f"test_{file_index}.py"
                fn.write_text(TEST_CONTENTS)
            result.append(folder_path)
    return result


paths = generate_top_level(root)
for p in paths:
    generate_top_level(p)
