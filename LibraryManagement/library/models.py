from django.db import models

class Book:
    def __init__(self, title, author, genre, height, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.height = height
        self.publisher = publisher

    def __str__(self):
        return self.title
