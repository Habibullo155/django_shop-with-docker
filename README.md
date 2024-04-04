Django shop 

This is a simple e-commerce project built using Django, Python, HTML, and CSS. Users can browse products, add them to the cart, and complete the purchase.

Features User authentication Browse products Add products to cart Update cart Remove products from cart Complete purchase

Installation To install and run this project follow these steps:

1. Clone the repository `git clone repository_url.git`
2. Navigate into the project directory: `cd django_shop-with-docker`
3. Create .env directory: `mkdir .env`
4. Add .dev file and add our configuration
5. Build  the Docker containers: `docker-compose build`
6. Aplly migrations : ` docker-compose run web python manage.py migrate `
7. Create superuser: `docker-compose run web python manage.py createsuperuser`
8. Run the Docker containers: `docker-compose up`
    Usage
 Visit the site: http://127.0.0.1:8000/ Login with superuser credentials Browse products, add them to the cart, and complete the purchase Credits
