from rest_framework.test import APITestCase

from vacancy.models import Vacancy

class VacancyAPITestCase(APITestCase):
    def setUp(self):
        vacancy = Vacancy.objects.create(
            title='Test vacancy',
            description='Test description'
            )

    def test_single_vacancy(self):
        vacancy_count = Vacancy.objects.count()
        self.assertEqual(vacancy_count, 1)
