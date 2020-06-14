import uuid
from django.db import models


class Genre(models.Model):
    """Model representing Book Genre"""
    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction")

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model represnting a book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(
        max_length=1e3, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 character ISBN number')

    genre = models.ManyToManyField(
        'Genre', help_text='Select a genre for this book', related_name='books')

    def __str__(self):
        return self.title

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Model represnting a specific copy of a book"""
    # DEFINE CONSTANTS
    #  I take this more verbose apporach to model constants because
    # I find it is easier to adjust later on and keep track of hard coded values
    MAINTENANCE = 'm'
    ON_LOAN = 'o'
    AVAILABLE = 'a'
    RESERVED = 'r'

    LOAN_STATUS = (
        (MAINTENANCE, 'Maintenance'),
        (ON_LOAN, 'On Loan'),
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved')
    )
    # DEFINE FIELDS
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique iD for this particular book copy.")
    book = models.ForeignKey(
        'Book', on_delete=models.SET_NULL, null=True, related_name='copies')
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default=MAINTENANCE, help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f"{self.id} ({self.book.title})"

    def display_title(self):
        return self.book.title


class Author(models.Model):
    """Model representing book author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
