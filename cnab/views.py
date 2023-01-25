from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadForm
from .models import Upload, Cnab
from django.core.paginator import Paginator
from django.db.models import Sum

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

        with open(f"uploads/{str(cnab_file.file)}", "r", encoding="utf-8" ) as read_file:
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
            type = types_transactions.get(type, "type não identificado")

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


def cnab_list(request):
    obj = request.GET.get('obj')
    valor_total = 0
    if obj:  
        cnab = Cnab.objects.filter(shop__icontains=obj)
        for c in cnab: 
            if c.type in ['Boleto' , 'Financiamento', 'Aluguel']: 
                valor_total -= c.value 
            elif c.type in ['Débito', 'Crédito', 'Empréstimo', 'Vendas', 'TED', 'DOC']: 
                valor_total += c.value
    else:
        cnab = Cnab.objects.all()   
    
    # paginação
    paginator = Paginator(cnab, 15) # mostra 15 transações por pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'list.html', {'page_obj': page_obj, 'valor_total': valor_total })


