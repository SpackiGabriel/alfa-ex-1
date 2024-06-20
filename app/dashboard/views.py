from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dashboard.models import Ticket
from dashboard.serializers import TicketSerializer
from dashboard.utils import count_by, group_by


class DashboardView(APIView):
    """
    A view class for handling dashboard-related API requests.

    This class provides the implementation for the GET and POST methods
    to retrieve and create tickets for the dashboard.

    Attributes:
        None

    Methods:
        get(request): Retrieves tickets based on the provided month and year.
        post(request): Creates a new ticket based on the provided data.
    """

    def get(self, request):
        """
        Retrieves tickets based on the provided month and year.

        Returns:
            Response: The HTTP response object containing the retrieved tickets,
            along with the count of tickets grouped by client and module.
        """
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not month or not year:
            return Response(
                {'error': 'Mês e ano são parâmetros obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            tickets = Ticket.objects.filter(opening_date__month=month, opening_date__year=year)
        except ValueError:
            return Response(
                {'error': 'Formato de mês ou ano inválido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TicketSerializer(tickets, many=True)

        count_by_client = count_by(group_by(lambda item: item['client']['name'], serializer.data))
        count_by_module = count_by(group_by(lambda item: item['module']['name'], serializer.data))

        return Response(
            {
                'tickets': serializer.data,
                'count_by_client': count_by_client,
                'count_by_module': count_by_module
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Creates a new ticket based on the provided data.

        Returns:
            Response: The HTTP response object containing the created ticket,
            along with a success message.
        """
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'ticket': serializer.data,
                    'message': 'Ticket aberto com sucesso.'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
