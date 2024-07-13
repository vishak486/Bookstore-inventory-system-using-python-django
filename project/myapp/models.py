from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname
    
class customer_details(models.Model):
    # id
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    addr = models.CharField(max_length=1000)
    pin = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10)


class category_master(models.Model):
    #id
    category_name= models.CharField(max_length=150)

class book_master(models.Model):
    #id
    book_name = models.CharField(max_length=50)
    category_name= models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    pic = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    author = models.CharField(max_length=30)
    keywords = models.CharField(max_length=500)
    status = models.CharField(max_length=10)


class shopping_cart(models.Model):
    # id
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=50)
    qty = models.IntegerField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

#9. bill_master - id, user_id, bill_no, bill_addr, total_amt, dt, tm
class bill_master(models.Model):
    #id
    user_id = models.IntegerField()
    bill_no = models.CharField(max_length=50)
    bill_addr = models.CharField(max_length=500)
    total_amt = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

#10. payment_master - id, user_id, bill_id, amt, card_no, cvv, dt, tm, status
class payment_master(models.Model):
    # id
    user_id = models.IntegerField()
    bill_id =models.IntegerField()
    amt = models.FloatField()
    card_no = models.CharField(max_length=50)
    cvv = models.CharField(max_length=10)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

#11. bill_details - id, bill_id, product_id, qty, amt
class bill_details(models.Model):
    # id
    bill_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    amt = models.FloatField()

