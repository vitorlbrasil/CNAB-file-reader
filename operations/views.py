from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from operations.models import Operation

from stores.models import Store
from .serializers import OperationSerializer


class OperationView(ListCreateAPIView):
    serializer_class = OperationSerializer
    queryset = Operation.objects.all()

    def perform_create(self, serializer):
        types = {
            1: {"description": "DÉBITO", "income": True},
            2: {"description": "BOLETO", "income": False},
            3: {"description": "FINANCIAMENTO", "income": False},
            4: {"description": "CRÉDITO", "income": True},
            5: {"description": "RECEBIMENTO EMPRÉSTIMO", "income": True},
            6: {"description": "VENDAS", "income": True},
            7: {"description": "RECEBIMENTO TED", "income": True},
            8: {"description": "RECEBIMENTO DOC", "income": True},
            9: {"description": "ALUGUEL", "income": False},
        }

        cnab_text = self.request.FILES["cnab_file"].read().decode()
        lines = cnab_text.splitlines()

        for line in lines:
            type = line[0]
            date = f"{line[1:5]}-{line[5:7]}-{line[7:9]}"
            value = int(line[9:19]) / 100
            cpf = line[19:30]
            card = line[30:42]
            hour = f"{line[42:44]}:{line[44:46]}:{line[46:48]}"
            store_owner = line[48:62].strip()
            store_name = line[62:80].strip()

            store, _ = Store.objects.get_or_create(
                store_name=store_name, store_owner=store_owner
            )

            Operation.objects.create(
                type=type,
                date=date,
                value=value,
                cpf=cpf,
                card=card,
                hour=hour,
                store=store,
            )
