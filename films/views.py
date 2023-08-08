# films/views.py

from django.http import JsonResponse

def ff_view(request):
    # Your view logic here
    data = {
        'message': 'This is the ff URL.',
        'data': {
            'key1': 'value1',
            'key2': 'value2',
            # Add more data as needed
        }
    }
    return JsonResponse(data)
