from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class EmployeeAPI(APIView):
    def get(self, request):
        try:
            employee = Employee.objects.all()
        except Employee.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []}, status=status.HTTP_404_NOT_FOUND)
        if not employee:
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        serializer = EmployeeModelSerializer(
            employee, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response(data={'msg': 'Employee Creation Failed', 'success': 'false'},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # try:
        #     try:
        #         serializer = EmployeeModelSerializer(
        #             data=request.data)
        #     except:
        #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(data={'msg': 'Employee created successfully', 'success': 'true', 'empid': request.data.get('regid')}, status=status.HTTP_201_CREATED)
        #     else:
        #         if Employee.objects.filter(email=request.data.get('email')):
        #             return Response(data={'msg': 'Employee already exist', 'success': 'false'}, status=status.HTTP_200_OK)
        #         else:
        #             return Response(data={'msg': 'invalid body request', 'success': 'false'}, status=status.HTTP_404_NOT_FOUND)
        # except:
        #     return Response(data={'msg': 'Employee Creation Failed', 'success': 'false'},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeAPIView(APIView):
    def get_object(self, pk):
        try:
            emp = Employee.objects.get(
                pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'no employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
        return emp

    def get(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeModelSerializer(employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        if pk != '':
            try:
                employee = Employee.objects.get(pk=pk)
            except:
                return Response(data={'msg': 'no employee found with this regid', 'success': 'false'}, status=status.HTTP_404_NOT_FOUND)
            employee.delete()
            return Response(data={'msg': 'employee deleted successfully', 'success': 'true'},  status=status.HTTP_200_OK)
        else:
            return Response(data={'msg': 'employee deletion failed', 'success': 'false'},  status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        try:
            try:
                employee = Employee.objects.get(
                    pk=pk)  # stu.objects.get(id=pk)
            except Employee.DoesNotExist:
                return Response(data={'msg': 'no employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeModelSerializer(
                data=request.data, instance=employee)
            print(serializer)   #
            if serializer.is_valid():
                print(serializer)   #
                serializer.save()
                return Response(data={'msg': 'employee details updated successfully', 'success': 'true'}, status=status.HTTP_200_OK)
            else:
                if Employee.objects.filter(email=request.data.get('email')) or Employee.objects.filter(regid=request.data.get('regid')):
                    return Response(data={'msg': 'employee details updation failed', 'success': 'false'}, status=status.HTTP_200_OK)
                else:
                    return Response(data={'msg': 'invalid body request', 'success': 'false'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={'msg': 'employee updation failed', 'success': 'false'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk=None):
        try:
            employee = Employee.objects.get(
                pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'Resource Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeModelSerializer(
            data=request.data, instance=employee, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
