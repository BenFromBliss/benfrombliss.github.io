# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_51LFPNQHT5ya30LDoRRb6WFW9S1sGBcLLQvHnp6S5PqNZmdyvkwb98RWEHIy7JeodM1wU9VlD7qL1UiHwAwKqSJrX009mswx8J4 '

# Using Django
from django.http import HttpResponse

@csrf_exempt
def my_webhook_view(request):
  payload = request.body

  # For now, you only need to print out the webhook payload so you can see
  # the structure.
  print(payload)

  return HttpResponse(status=200)