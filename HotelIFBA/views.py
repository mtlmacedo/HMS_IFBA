from django.http.response import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.serializers import Serializer
from HotelIFBA.models import *
from HotelIFBA.serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import string
import secrets
from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@swagger_auto_schema(methods=['POST'], request_body=UserSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if(request.method == 'POST'):
        body_serializer = UserSerializer(data=request.data)
        usuario = request.data['username']
        senha = request.data['password']

        user = authenticate(request, username=usuario, password=senha)
        
        if(user is not None):
            login(request, user)
            return HttpResponse("Success", status=status.HTTP_200_OK)
        else:
            return HttpResponse("Not Found", status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['POST'], request_body=UserSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def logout(resquest):
    try:
        logout(resquest)
        return HttpResponse("Success", status=status.HTTP_200_OK)
    except KeyError:
        return HttpResponse("Not Found", status=status.HTTP_404_NOT_FOUND)

user_response = openapi.Response('Response Description', UserSerializer)


empresa_response = openapi.Response('Response Description', EmpresaSerializer)
@swagger_auto_schema(method='GET', responses={200: empresa_response})
@swagger_auto_schema(methods=['POST'], request_body=EmpresaSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_empresa(request):
    if(request.method == 'GET'):
        empresa = Empresa.objects.all()
        empresa_serializer = EmpresaSerializer(empresa, many=True)
        return Response(empresa_serializer.data)
    elif(request.method == 'POST'):
        empresa_serializer = EmpresaSerializer(data=request.data)
        if(empresa_serializer.is_valid):
            empresa_serializer.save()
            return Response(empresa_serializer.data, status=status.HTTP_201_CREATED)
        return Response(empresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['PUT'], request_body=EmpresaSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_empresa(request, pk):
    try:
        empresa = Empresa.objects.get(pk=pk)
    except Empresa.DoesNotExist:
        return Response('Empresa não encontrada', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        empresa_serializer = EmpresaSerializer(empresa)
        return Response(empresa_serializer.data)

    elif request.method == 'PUT':
        empresa_serializer = EmpresaSerializer(empresa, data=request.data)
        if empresa_serializer.is_valid():
            empresa_serializer.save()
            return Response(empresa_serializer.data)
        return Response(empresa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


quartos_response = openapi.Response('Response Description', QuartoSerializer)
@swagger_auto_schema(method='GET', responses={200: quartos_response})
@swagger_auto_schema(methods=['POST'], request_body=QuartoSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_quarto(request):
    if request.method == 'GET':
        quarto = Quarto.objects.all()
        quarto_serializer = QuartoSerializer(quarto, many=True)
        return Response(quarto_serializer.data)

    elif request.method == 'POST':
        quarto_serializer = QuartoSerializer(data=request.data)
        if quarto_serializer.is_valid():
            quarto_serializer.save()
            return Response(quarto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(quarto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['PUT'], request_body=QuartoSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_quarto(request, pk):
    try:
        quarto = Quarto.objects.get(pk=pk)
    except Quarto.DoesNotExist:
        return Response('Quarto não encontrada', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        quarto_serializer = QuartoSerializer(quarto)
        return Response(quarto_serializer.data)

    elif request.method == 'PUT':
        quarto_serializer = QuartoSerializer(quarto, data=request.data)
        if quarto_serializer.is_valid():
            quarto_serializer.save()
            return Response(quarto_serializer.data)
        return Response(quarto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quarto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def quartos_disponiveis(request, capacidade):
    quarto = Quarto.objects.filter(capacidade__icontains = capacidade, disponibilidade = True).first()
    return HttpResponse(quarto.id)

def alterar_status_quarto(pk):
    quarto = Quarto.objects.get(pk=pk)

    if(quarto.disponibilidade is True):
        quarto.disponibilidade = False
        quarto.save()
        return True

colaboradors_response = openapi.Response('Response Description', ColaboradorSerializer)
@swagger_auto_schema(method='GET', responses={200: colaboradors_response})
@swagger_auto_schema(methods=['POST'], request_body=ColaboradorSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_colaborador(request):
    if(request.method == 'GET'):
        # colaborador = Colaborador.objects.all()
        colaborador_serializer = ColaboradorSerializer(Colaborador.objects.all(), many=True)
        return Response(colaborador_serializer.data)
    elif (request.method == 'POST'):
        colaborador_serializer = ColaboradorSerializer(data=request.data)
        if(colaborador_serializer.is_valid()):
            senha = request.data['senha']
            login = request.data['login']
            cargo = request.data['cargo']
            usuario = User.objects.create_user(login, "", senha)

            if(cargo == "G"):
                group = Group.objects.get(name='Gerente')
            elif(cargo == "R"):
                group = Group.objects.get(name='Recepcionista')
            
            group.user_set.add(usuario)
            usuario.is_admin = True
            usuario.is_staff = True
            usuario.save()

            colaborador_serializer.save()
            return Response(colaborador_serializer.data, status=status.HTTP_201_CREATED)
        return Response(colaborador_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['PUT'], request_body=ColaboradorSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_colaborador(request, pk):
    try:
        colaborador = Colaborador.objects.get(pk=pk)
    except Colaborador.DoesNotExist:
        return Response('colaborador não encontrado', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        colaborador_serializer = ColaboradorSerializer(colaborador)
        return Response(colaborador_serializer.data)

    elif request.method == 'PUT':
        colaborador_serializer = ColaboradorSerializer(colaborador, data=request.data)
        if colaborador_serializer.is_valid():
            colaborador_serializer.save()
            return Response(colaborador_serializer.data)
        return Response(colaborador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        colaborador.delete()
        return Response(status=status.HTTP_200_OK)

cliente_response = openapi.Response('Response Description', ClienteSerializer)
@swagger_auto_schema(method='GET', responses={200: cliente_response})
@swagger_auto_schema(methods=['POST'], request_body=ClienteSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_cliente(request):
    pass

@swagger_auto_schema(methods=['PUT'], request_body=ClienteSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_cliente(request, pk):
    pass

servicos_response = openapi.Response('Response Description', TipoServicoSerializer)
@swagger_auto_schema(method='GET', responses={200: servicos_response})
@swagger_auto_schema(methods=['POST'], request_body=TipoServicoSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_tipo_servico(request):
    pass

@swagger_auto_schema(methods=['PUT'], request_body=TipoServicoSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_tipo_servico(request, pk):
    pass

reservas_response = openapi.Response('Response Description', ReservaSerializer)
@swagger_auto_schema(method='GET', responses={200: reservas_response})
@swagger_auto_schema(methods=['POST'], request_body=ReservaSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_reserva(request):
    pass

@swagger_auto_schema(methods=['PUT'], request_body=ReservaSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_reserva(request, pk):
    pass

def createReserva(request):
    pass

estadias_response = openapi.Response('Response Description', EstadiaSerializer)
@swagger_auto_schema(method='GET', responses={200: estadias_response})
@swagger_auto_schema(methods=['POST'], request_body=EstadiaSerializer)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_estadia(request):
   pass

@swagger_auto_schema(methods=['PUT'], request_body=EstadiaSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhar_estadia(request, pk):
    pass

def criarEstadia(request):
    pass

def atualizarEstadia(reservado, reserva, estadia, quarto_id):
    pass

def gerar_fatura(request, pk):
    pass

def baixar_fatura(request, pk):
    pass

def mudar_quarto(estadia, pk):
    pass

estatistica_response = openapi.Response('Response Description', EstatisticaSerializer)
@swagger_auto_schema(method='GET', responses={200: estatistica_response})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_estatistica(request):
    if request.method == 'GET':
        estatistica = Estatistica.objects.all()
        serializer = EstatisticaSerializer(estatistica, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


