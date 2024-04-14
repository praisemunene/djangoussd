from django.http import HttpResponse

def ussd_callback(request):
    # Get the POST data from the request
    session_id = request.POST.get("sessionId")
    phone_number = request.POST.get("phoneNumber")
    service_code = request.POST.get("serviceCode")
    text = request.POST.get("text")


    # Generate loan amount and processing fee
    import random
    random_number = random.randint(11000, 21000)
    rounded_number = round(random_number, -2)
    fee = rounded_number * 0.01

    # Process user input
    if text == '90':
        # Main menu if no input provided
        response = "CON Welcome to Omoka Loans. Congratulations, you qualify for a loan of up to {}:\n".format(rounded_number)
        response += "1. Borrow loan \n"
        response += "2. Withdraw loan"
    elif text == '1' or text == '2':
        # Prompt for loan amount if user chooses to borrow loan
        response = "CON Please enter the loan amount:\n"
    elif text != '' and text != '1' and text != '2':
        # Process withdrawal if user chooses to withdraw loan
        amount = fee
        phone = phone_number
        # Call function to initiate M-Pesa payment
        # initiate_mpesa_payment(phone, amount, access_token)
        response = "END {} Pay verification fee to get your loan within 24hrs\n".format(phone)

    # Send response to USSD gateway
    return HttpResponse(response, content_type='text/plain')
