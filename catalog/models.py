import uuid
from django.db import models
from django.urls import reverse
# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text='Literary Genre (e.g. Science Finction)')

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(
        max_length=1000, help_text='A brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 character reference # ')
    genres = models.ManyToManyField(
        Genre, help_text='Select a genre for this book', related_name='books')

    def __str__(self) -> str:
        return self.title

    @property
    def get_genres(self):
        return ''.join([genre.name for genre in self.genres.all()])

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(seld.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for specific copy of book')
    book = models.ForeignKey(
        'Book', on_delete=models.SET_NULL, null=True, related_name='copies')
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)

    class LoanStatus(models.TextChoices):
        MAINTENANCE = 'm', 'Maintenance'
        ON_LOAN = 'o', 'On loan'
        AVAILABLE = 'a', 'Available'
        RESERVED = 'r', 'Reserved'

    status = models.CharField(
        max_length=1, choices=LoanStatus.choices, default=LoanStatus.MAINTENANCE)

    class Meta:
        ordering = ['due_back']

    def __str__(self) -> str:
        return f'{self.id} ({self.book.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    class LanguageChoice(models.TextChoices):
        ENGLISH = 'en', 'English'
        FRENCH = 'fr', 'French'
        SPANISH = 'es', "Spanish"
        GERMAN = 'de', 'German'

    language = models.CharField(
        max_length=2, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH)

    def __str__(self) -> str:
        return self.language
