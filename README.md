# Defoult — мова програмування

Defoult — це експериментальна мова програмування, яка інтерпретує код з текстових файлів.  
В репозиторії є приклади коду та базові команди.

---

## 🚀 Запуск через VS Code

Якщо ти хочеш запускати код напряму з вихідників:

1. У файлі `main.py` в блоці:
   ```python
   if __name__ == "__main__":
       main('test.txt')  #start from vs code
       #if len(sys.argv) > 1:    # if you have app
       #    file_path = sys.argv[1]
       #    main(file_path)
