"""Оновлює таблицю проєктів у головному README.md.

Для кожної папки в projects/ (крім тих, що починаються з _ або .) бере
опис із README.md проєкту (перший рядок тексту після заголовка).
Якщо README немає, бере docstring з main.py.
"""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).parent
PROJECTS = ROOT / "projects"
README = ROOT / "README.md"
START, END = "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->"


def describe(folder: Path) -> str:
    readme = folder / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    main = folder / "main.py"
    if main.exists():
        try:
            doc = ast.get_docstring(ast.parse(main.read_text(encoding="utf-8")))
            if doc:
                return doc.strip().splitlines()[0]
        except SyntaxError:
            pass
    return "—"


def build_table() -> str:
    folders = sorted(
        p for p in PROJECTS.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ) if PROJECTS.exists() else []
    if not folders:
        return "| Проєкт | Опис |\n|--------|------|\n| _Поки порожньо._ | |"
    rows = ["| Проєкт | Опис |", "|--------|------|"]
    for f in folders:
        rows.append(f"| [{f.name}](projects/{f.name}) | {describe(f)} |")
    return "\n".join(rows)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = f"{START}\n{build_table()}\n{END}"
    README.write_text(pattern.sub(lambda _: new, text), encoding="utf-8")
    print("README.md оновлено.")


if __name__ == "__main__":
    main()
