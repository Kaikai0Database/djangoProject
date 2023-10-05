
# Create your views here.
from django.shortcuts import render

def multiply_by_ten(request):
    if request.method == 'POST':
        input_number = request.POST.get('input_number')
        if input_number is not None:
            try:
                input_number = float(input_number)
                result = input_number * 10
                return render(request, 'hello.html', {'result': result})
            except ValueError:
                error_message = "請輸入有效的數字。"
                return render(request, 'hello.html', {'error_message': error_message})

    return render(request, 'hello.html')
