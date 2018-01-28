from django.shortcuts import render

class MainApp():

    def main_page(request):
        context = {
            'title': 'Recruitment App.',
            'message': 'Greetings in our Lord and Savior!'
        }
        return render(request, 'index.html', context)