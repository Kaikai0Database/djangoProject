from django.shortcuts import render

# Create your views here.
def multiply_by_ten(request):
    if request.method == 'POST':
        input_number = request.POST.get('input_number')
        if input_number is not None:
            try:
                input_number = float(input_number)
                a = input_number * 10
                b = input_number / 10
                return render(request, 'hello.html', {'result': a , 'ans' : b})
            except ValueError:
                error_message = "請輸入有效的數字。"
                return render(request, 'hello.html', {'error_message': error_message})

    return render(request, 'hello.html')
#此app是為了testapp而建立的，不用在settings裡面增設這個app