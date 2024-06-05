import functions_framework

@functions_framework.http
def run(request):
  uri = "mongodb+srv://gauakanguyen:AOMhWKFdmlSO6kcU@transactiondata.wecxmij.mongodb.net/?retryWrites=true&w=majority&appName=transactionData"
  return uri
