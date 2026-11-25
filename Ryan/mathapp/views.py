from django.shortcuts import render

def churn_rate(request):
    Customers_count = float(request.POST.get('present_cust', '0'))
    Initial_Customer = float(request.POST.get('initial_cust', '0'))
    churn_rate = ((Initial_Customer - Customers_count) / Initial_Customer) * 100 if request.method == 'POST' and Initial_Customer > 0 else 0

    print("Customers lost count =", Customers_count)
    print("Initial customers count =", Initial_Customer)
    print("Churn_rate =", churn_rate)

    return render(
        request,
        'mathapp/math.html',
        {'Customers_count': Customers_count, 'Initial_Customer': Initial_Customer, 'churn_rate': churn_rate}
    )