from django.test import TestCase
from django.contrib.auth import get_user_model

from .. import models


def sample_user(email='test@testing.com', password='password123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating a new user with email is successful"""
        email = 'test@testing.com'
        password = 'Testpass!23'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TESTING.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creatinguser with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@testing.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        user = sample_user()
        tag = models.Tag.objects.create(name='testing',
                                        user=user
                                        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        """Test the ingredient string representation"""
        user = sample_user()
        ingredient = models.Ingredient.objects.create(name='garlic',
                                                      user=user, )

        self.assertEqual(str(ingredient), ingredient.name)
