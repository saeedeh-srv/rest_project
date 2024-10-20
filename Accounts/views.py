from rest_framework.response import Response
from rest_framework import generics, permissions, status, views
from .serializers import UserSerializers, ProfileSerializers, \
    ChangePasswordSerializers, PasswordResetRequestSerializer, \
    PasswordResetConfirmSerializer, UserLogoutSerializer
from .models import Profile, User

from django.utils.http import urlsafe_base64_encode, \
    urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from ProjectManagerRest.settings import DEFAULT_FROM_EMAIL


class UserCreate(generics.CreateAPIView):
    """
    This view creates a user and profile together using nested serializers.
    """
    serializer_class = ProfileSerializers

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


class UserProfileDetail(generics.ListAPIView):
    """
     get user profile
    """
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ChangePasswordUser(generics.UpdateAPIView):
    """
    change user pass
    """
    serializer_class = ChangePasswordSerializers
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                response = {
                    'status': 'Error',
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': "something went wrong",
                    'data': []
                }
                return Response(response)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()

            response = {
                'status': 'sucess',
                'code': status.HTTP_200_OK,
                'message': "password updated successfully",
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(generics.GenericAPIView):
    """
    this endpoint will do something
    """
    serializer_class = PasswordResetRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(
                reverse('accounts:password-rest-confirm', kwargs={'uidb64': uid, 'token': token})
            )
            send_mail('Password Reset Request of POJIO',
                      f'Click the link blow to rest your password: {reset_url}',
                      f'{DEFAULT_FROM_EMAIL}',
                      [email],
                      fail_silently=False, )
        return Response({'detail': 'Password reset link has ben sent'}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(generics.GenericAPIView):
    """
    shoma nminevisin
    """
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, uidb64=None, token=None, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and default_token_generator.check_token(user, token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user)
            return Response({"detail": 'Password have been reset with the new pass'})
        else:
            return Response({"detail": 'Password have been reset'})


class UserLogoutViews(views.APIView):
    """
    nimizarid
    """
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Successful logout", status=status.HTTP_200_OK)
