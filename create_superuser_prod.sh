echo "from django.contrib.auth.models import User; User.objects.create_superuser($PROD_USER,$PROD_USER_EMAIL,$PROD_USER_PASS)" | python manage.py shell