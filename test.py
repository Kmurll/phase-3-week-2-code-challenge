from customer import Customer
from restaurant import Restaurant
from review import Review

customer1 = Customer("Kelvin", "Mue")
customer2 = Customer("Clinton", "Omar")

restaurant1 = Restaurant("Forodhani Eateries")
restaurant2 = Restaurant("Crave Inn")

customer1.add_review(restaurant1, 5)
customer1.add_review(restaurant2, 3.5)
customer2.add_review(restaurant1, 4)

print(f"Customer 1's full name: {customer1.full_name()}")
print(f"Customer 2's full name: {customer2.full_name()}")

for customer in [customer1, customer2]:
    print(f"The Restaurant reviewed by {customer.full_name()}: {[restaurant.get_name() for restaurant in customer.restaurants()]}")

for restaurant in [restaurant1, restaurant2]:
    print(f"The average rating for {restaurant.get_name()}: {restaurant.average_star_rating()}")

for restaurant in [restaurant1, restaurant2]:
    print(f"Customers who reviewed {restaurant.get_name()}: {[customer.full_name() for customer in restaurant.customers()]}")
    print(f"{restaurant.get_name()}'s reviews: {[review.get_rating() for review in restaurant.reviews]}")
