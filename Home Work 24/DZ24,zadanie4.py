# Задание №1
# а) Напишите функцию, которая будет загружать изображение.
# б) Запустите циклом 100 таких функций, а также замерьте время.
# в) Добавьте функционал мультипроцессорного запуска, с замером времени.
import requests
import time
from concurrent.futures import ProcessPoolExecutor

def Foto(url, sohranenie):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(sohranenie, 'wb') as file:
            file.write(response.content)

        print(f"Изображение успешно загружено по пути: {sohranenie}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Juletr%C3%A6et.jpg/274px-Juletr%C3%A6et.jpg"
sohranenie = "C:/Users/Madi/Desktop/DZ24/111/image.jpg"
Foto(image_url, sohranenie)

# Одиночный запуск
start_time = time.time()
for i in range(1, 101):
    save_path = f"C:/Users/Madi/Desktop/DZ24/111/image_{i}.jpg"
    Foto(image_url, save_path)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Время выполнения для 100 функций (одиночный): {elapsed_time} секунд")

# Многопроцессорный запуск
start_time_multi = time.time()
with ProcessPoolExecutor() as executor:
    executor.map(Foto, [image_url]*100, [f"C:/Users/Madi/Desktop/DZ24/111/image_{i}.jpg" for i in range(1, 101)])

end_time_multi = time.time()
elapsed_time_multi = end_time_multi - start_time_multi

print(f"Время выполнения для 100 функций (многопроцессорный): {elapsed_time_multi} секунд")
