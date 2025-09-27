# Defoult — мова програмування

Defoult — це мова програмування котра знищить всі низькорівневі та високорівневі мови програмування, проте зараз інтерпретує код з текстових файлів.  
В репозиторії є приклади коду та базові команди.

---

## 🚀 Запуск через VS Code

Якщо ти хочеш запускати код з VS Code:

1. У файлі `main.py` в блоці `if __name__ == "__main__":` додайте :
   ```python
   main('test.txt')
   ```
2. У файлі `main.py`  має бути:
   ```python
      if __name__ == "__main__":
         main('test.txt')  #start from vs code
   ```

3. Запуск програми:
   ```bash
   python3 main.py
   ```

---

## 🔨 Збірка в один виконуваний файл

Для збірки використовується **PyInstaller**.

```bash
pyinstaller --onefile --name Default main.py   --add-data "core:core"   --add-data "commands:commands"
```

📌 Перед збіркою потрібно змінити `main.py`:

У файлі `main.py` в блоці `if __name__ == "__main__":` додайте:

```python
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    main(file_path)
```

А рядок `main('test.txt')` — видаліть.

Має виглядати ось так:

      if __name__ == "__main__":
         if len(sys.argv) > 1:    # if you have app
         file_path = sys.argv[1]
         main(file_path)
   ```

Щоб запустити програму, відкрийте terminal, вкажіть шлях до зібраної програми та файл з кодом. Мова запрацює.

---

## 📂 Структура проекту
```python
.   
├── core/          # ядро мови
├── commands/      # базові команди
├── main.py        # точка входу
├── test.txt       # приклад коду
└── README.md      # це інструкція
```

---

## 📑 Приклад коду

```txt
q = Ua
x = cheknut()
print "Defoult"
print {q}, {x}
```

Вивід:

```txt
Defoult
Ua, "your text"
```
