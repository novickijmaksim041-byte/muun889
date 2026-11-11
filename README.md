# 🐍 Мої Python-проєкти

Головна сторінка всіх моїх Python-кодів. Кожен проєкт лежить у власній папці в `projects/`.

## Проєкти

<!-- PROJECTS:START -->
| Проєкт | Опис |
|--------|------|
| _Поки порожньо. Додайте перший проєкт у `projects/`._ | |
<!-- PROJECTS:END -->

## Як додати новий проєкт

1. Скопіюйте папку `projects/_template` і дайте їй назву проєкту, наприклад `projects/calculator`.
2. Покладіть туди свій код (`main.py` та інші файли).
3. У `README.md` проєкту напишіть заголовок і одним рядком опис.
4. Запустіть:

   ```bash
   python update_index.py
   ```

   Таблиця вище оновиться автоматично.
5. Завантажте зміни на GitHub:

   ```bash
   git add .
   git commit -m "Додано проєкт calculator"
   git push
   ```

## Запуск

```bash
pip install -r requirements.txt
python projects/<назва_проєкту>/main.py
```
