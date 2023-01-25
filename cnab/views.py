from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadForm
from .models import Upload, Cnab


def index_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        requestFile = request.FILES["file"]

        cnab_file = Upload.objects.create(file=requestFile)
        cnab_file.save()

        cnab_list = []

        types_transactions = {
            "1": "Débito",
            "2": "Boleto",
            "3": "Financiamento",
            "4": "Crédito",
            "5": "Empréstimo",
            "6": "Vendas",
            "7": "TED",
            "8": "DOC",
            "9": "Aluguel",
        }

        with open(f"uploads/{str(cnab_file.file)}", "r") as read_file:
            for file_line in read_file:
                cnab_list.append(file_line)

        for item in cnab_list:
            type = item[:1]
            year = item[1:5]
            month = item[5:7]
            day = item[7:9]
            value = item[9:19]
            cpf = item[19:30]
            card = item[30:42]
            hour = item[42:44]
            minute = item[44:46]
            second = item[46:48]
            owner = item[48:62]
            shop = item[62:81]
            type = types_transactions.get(type, "tipo não identificado")

            data = f"{day}/{month}/{year}"
            value = int(value) / 100
            time = f"{hour}:{minute}:{second}"

            reader = Cnab.objects.create(
                type=type,
                data=data,
                value=value,
                cpf=cpf,
                card=card,
                hour=time,
                owner=owner,
                shop=shop,
            )

        data = Cnab.objects.values(
            "type", "value", "data", "cpf", "hour", "owner", "shop"
        )

        return render(request, "transactions.html", context={"data": data})

    else:
        form = UploadForm()
    return render(request, "form-upload.html", {"form": form})
