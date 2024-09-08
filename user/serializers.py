from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
  
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password','confirm_password']
    
    # default user role is customer. admin can change it to employee/owner.
    # default user restaurant is foodieDelivery. admin can change it according to restaurant list.
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email=self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        #check password and confirm_password are matched
        if password != confirm_password:
            raise serializers.ValidationError({'Error': "Password doesn't Match"})
        # check is email already exists
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error': "Email is Already registered"})

        account = CustomUser(username = username, first_name=first_name, last_name = last_name, email= email)
        account.set_password(password)
        account.save()
        
        print(account)
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField( required = True)
    password = serializers.CharField( required = True)