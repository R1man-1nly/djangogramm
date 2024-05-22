from django.test import TestCase, Client
from django.urls import reverse

from .forms import EditProfileForm
from .models import User


class UserTestClass(TestCase):
    def setUp(self):
        img = (b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\n\x00\x00\x00\x0f\x08\x02\x00\x00\x00R\x9d\xc9Y\x00'
               b'\x00\x00\x16IDATx\x9ccTy\xc4\xcf\x80\x1b0\xe1\x91\x1b\x95\x1e\x8c\xd2\x00\x12>\x013\xb77|\xdd\x00'
               b'\x00\x00\x00IEND\xaeB`\x82')

        self.user = User.objects.create_user(
            username='username1',
            email='email1@example.com',
            password='password1',
            first_name='first_name1',
            last_name='last_name1',
            bio='bio1',
        )

        self.client = Client()

    def test_authentication(self):
        login_successful = self.client.login(email='email1@example.com', password='password1')
        self.assertTrue(login_successful, 'Login unsuccessful')

        response = self.client.get(reverse('feed'))
        self.assertEqual(response.status_code, 200)

    # def test_unauthenticated_view(self):
    #     response = self.client.get(reverse('feed'))
    #     self.assertEqual(response.status_code, 302)

    def test_profile_edit_get(self):
        self.client.login(email='email1@example.com', password='password1')

        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], EditProfileForm)

    # Додайте тест для POST-запиту
    # def test_profile_edit_post(self):
    #     # Створюємо об'єкт користувача
    #     user_profile = User.objects.create_user(user=self.user, first_name='Old First Name',
    #                                             last_name='Old Last Name', bio='Old Bio')
    #
    #     # Отримуємо посилання на сторінку редагування профілю
    #     url = reverse('profile_edit')
    #
    #     # Дані для POST-запиту
    #     data = {
    #         'first_name': 'New First Name',
    #         'last_name': 'New Last Name',
    #         'bio': 'New Bio'
    #         # додайте дані для інших полів, якщо потрібно
    #     }
    #
    #     # Надсилаємо POST-запит
    #     response = self.client.post(url, data, follow=True)
    #
    #     # Перевіряємо, чи відбулося перенаправлення на сторінку профілю після оновлення
    #     self.assertRedirects(response, reverse('profile_user', args=(self.user.pk,)))
    #
    #     # Перезавантажуємо об'єкт користувача з бази даних, щоб перевірити оновлення
    #     user_profile.refresh_from_db()
    #
    #     # Перевіряємо, чи оновлені дані збереглися у базі даних
    #     self.assertEqual(self.user.first_name, 'New First Name')
    #     self.assertEqual(self.user.last_name, 'New Last Name')
    #     self.assertEqual(self.user.bio, 'New Bio')

    def test_create_post(self):
        pass

    def test_get_feed(self):
        pass

    def test_like_post(self):
        pass
