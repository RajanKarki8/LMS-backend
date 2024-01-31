from django.db import models

class User(models.Model):
    user_id         = models.AutoField(primary_key=True)
    name            = models.CharField(max_length = 255)
    email           = models.EmailField(unique = True)
    membership_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    BookId         = models.AutoField(primary_key=True)
    Title          = models.CharField(max_length = 500)
    ISBN           = models.CharField(max_length = 100, unique = True)
    Published_date = models.DateTimeField(auto_now_add = True)
    Genre          = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.Title
    
class BookDetails(models.Model):
    book_id        = models.OneToOneField(Book, on_delete = models.CASCADE)
    Details_id     = models.AutoField(primary_key = True)
    number_of_pages= models.PositiveIntegerField()
    Publisher      = models.CharField(max_length = 255)
    Language       = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return f"{self.book_id} by {self.Publisher}"
    
class BorrowedBooks(models.Model):
    user_id       = models.ForeignKey(User, on_delete = models.CASCADE)
    book_id       = models.ForeignKey(BookDetails, on_delete = models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add = True)
    returned_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"borrwed by {self.user_id}"
    
