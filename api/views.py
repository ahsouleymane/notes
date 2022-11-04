from django.http import JsonResponse

# Create your views here.

def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'methode': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'methode': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'methode': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'methode': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'methode': 'DELETE',
            'body': None,
            'description': 'Deletes and existing note'
        },
    ]

    return JsonResponse(routes, safe=False)

