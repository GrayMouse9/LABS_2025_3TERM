import unittest
from main import Conductor, Orchestra, ConductorOrchestra, solve_b1, solve_b2, solve_b3

class TestOrchestraLogic(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных"""
        self.orchestras = [
            Orchestra(1, 'Венский филармонический'),
            Orchestra(2, 'Берлинский филармонический'),
            Orchestra(3, 'Лондонский симфонический')
        ]
        self.conductors = [
            Conductor(1, 'Караян', 100000, 2),
            Conductor(2, 'Бернстайн', 120000, 1),
            Conductor(3, 'Петров', 80000, 3),
            Conductor(4, 'Иванов', 75000, 3)
        ]
        self.links = [
            ConductorOrchestra(1, 1),
            ConductorOrchestra(1, 2),
            ConductorOrchestra(3, 3)
        ]

    def test_solve_b1_sorting(self):
        """Тест 1: Проверка сортировки по ФИО в запросе Б1"""
        result = solve_b1(self.conductors, self.orchestras)
        # Проверяем, что первый по алфавиту — Бернстайн
        self.assertEqual(result[0][0], 'Бернстайн')
        # Проверяем, что последний — Петров
        self.assertEqual(result[-1][0], 'Петров')

    def test_solve_b2_counts(self):
        """Тест 2: Проверка подсчета дирижеров в оркестрах в запросе Б2"""
        result = solve_b2(self.conductors, self.orchestras)
        # В Лондонском (id 3) два дирижера (Петров, Иванов)
        # Он должен быть первым в списке из-за reverse=True
        self.assertEqual(result[0], ('Лондонский симфонический', 2))

    def test_solve_b3_filter(self):
        """Тест 3: Проверка фильтрации фамилий на 'ов' в запросе Б3"""
        result = solve_b3(self.conductors, self.orchestras, self.links)
        # Из списка links и conductors на 'ов' заканчиваются только Петров и Иванов
        # Караян и Бернстайн должны быть отфильтрованы
        fios = [item[0] for item in result]
        for name in fios:
            self.assertTrue(name.endswith('ов'))
        self.assertIn('Петров', fios)
        self.assertNotIn('Караян', fios)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main()
