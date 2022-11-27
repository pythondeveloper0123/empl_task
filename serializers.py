from rest_framework import serializers
from .models import Employee, EmployeeAddress, EmployeeWorkExperience, EmployeeQualification, EmployeeProjects
from drf_writable_nested import WritableNestedModelSerializer


class EmployeeAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAddress
        fields = ('hno', 'street', 'city', 'state',)

    def create(self, validated_data):
        return EmployeeAddress.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.hno = validated_data.get('hno', instance.hno)
    #     instance.street = validated_data.get('street', instance.street)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.state = validated_data.get('state', instance.state)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    #     return EmployeeAddress.update(instance, **validated_data)


class EmployeeWorkExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkExperience
        fields = ('companyName',  'fromDate', 'toDate', 'address',)

    # def create(self, validated_data):
    #     return EmployeeWorkExperience.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     return EmployeeWorkExperience.update(instance, **validated_data)


class EmployeeQualificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeQualification
        fields = ('qualificationName', 'percentage', )

    # def create(self, validated_data):
    #     return EmployeeQualification.objects.create(**validated_data)

    # def update(self, instance, validated_data):
        # return EmployeeQualification.update(instance, **validated_data)


class EmployeeProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProjects
        fields = ('title', 'description', )

    # def create(self, validated_data):
    #     return EmployeeProjects.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     return EmployeeProjects.update(instance, **validated_data)


class EmployeeModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    EmployeeAddress = EmployeeAddressModelSerializer()
    EmployeeWorkExperience = EmployeeWorkExperienceModelSerializer(many=True)
    EmployeeQualification = EmployeeQualificationModelSerializer(many=True)
    EmployeeProjects = EmployeeProjectsModelSerializer(many=True)

    class Meta:
        model = Employee

        # fields = ('regid', 'name', 'email', 'age',
        #           'gender', 'phoneNo', 'photo',)  # 'EmployeeAddress', 'EmployeeWorkExperience', 'EmployeeQualification', 'EmployeeProjects',

        fields = ('regid', 'name', 'email', 'age',
                  'gender', 'phoneNo',  'EmployeeAddress', 'EmployeeWorkExperience', 'EmployeeQualification', 'EmployeeProjects',)  # 'photo',

    def create(self, validated_data):
        employeeAddress = validated_data.pop('EmployeeAddress')
        employeeWorkExperience = validated_data.pop('EmployeeWorkExperience')
        employeeQualification = validated_data.pop('EmployeeQualification')
        employeeProjects = validated_data.pop('EmployeeProjects')
        employee = Employee.objects.create(**validated_data)
        EmployeeAddress.objects.create(**employeeAddress, emp=employee)
        for WorkExperience in employeeWorkExperience:
            EmployeeWorkExperience.objects.create(
                **WorkExperience, emp=employee)
        for Qualification in employeeQualification:
            EmployeeQualification.objects.create(
                **Qualification, emp=employee)
        for Projects in employeeProjects:
            EmployeeProjects.objects.create(**Projects, emp=employee)
        return employee

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user
