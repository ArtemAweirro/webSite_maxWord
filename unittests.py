import unittest

from flask_testing import TestCase
from main import app


class MyTest(TestCase):
    def create_app(self):
        app.config["TEST"] = True
        return app

    def test_file_test0(self):  # просто слова с пробелами
        url = '/upload'
        files = {'file': open('tests/test0.txt', 'rb')}  # Путь к unit-тесту 0
        response = self.client.post(url, data=files)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = 'Самое повторяющееся слово: Кокос<br>Количество его повторений: 3'  # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())

    def test_file_test1(self):  # слова со знаками препинания
        url = '/upload'
        files = {'file': open('tests/test1.txt', 'rb')}  # Путь к unit-тесту 1
        response = self.client.post(url, data=files)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = 'Самое повторяющееся слово: Кокос<br>Количество его повторений: 3'  # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())

    def test_file_test2(self):  # два слова повторяются одинаковое количество раз
        url = '/upload'
        files = {'file': open('tests/test2.txt', 'rb')}  # Путь к unit-тесту 2
        response = self.client.post(url, data=files)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = ("Самые повторяющиеся слова:<br>Слово: Ананас&emsp;Количество повторений: 3<br>Слово: "
                            "Кокос&emsp;Количество повторений: 3")  # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())

    def test_file_test3(self):  # три слова повторящихся одинаковое количество раз
        url = '/upload'
        files = {'file': open('tests/test3.txt', 'rb')}  # Путь к unit-тесту 3
        response = self.client.post(url, data=files)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = ("Самые повторяющиеся слова:<br>Слово: Ананас&emsp;Количество повторений: 3<br>Слово: "
                            "Кокос&emsp;Количество повторений: 3<br>Слово: Манго&emsp;Количество повторений: 3")  #
        # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())

    def test_file_test4(self):  # пустой файл
        url = '/upload'
        files = {'file': open('tests/test4.txt', 'rb')}  # Путь к unit-тесту 4
        response = self.client.post(url, data=files)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = "Загруженный файл - пуст"  # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())

    def test_file_test5(self):  # не передается никакой файл
        url = '/upload'
        response = self.client.post(url, data=None)

        # Проверяем, что загрузка прошла успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что ответ содержит ожидаемое содержимое
        expected_content = "Файл не найден"  # ожидаемый результат
        self.assertIn(expected_content, response.data.decode())


if __name__ == '__main__':
    unittest.main()
