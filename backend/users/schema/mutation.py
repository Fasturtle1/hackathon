import graphene
from django.contrib.auth import authenticate, login, logout

from backend.users.models import User
from backend.users.schema.types import BasicUserType


class CreateUser(graphene.Mutation):
    test = graphene.String()

    class Arguments:
        a = graphene.String()

    def mutate(self, info, a):
        return a


class Login(graphene.Mutation):
    user = graphene.Field(BasicUserType)
    success = graphene.Boolean()

    class Meta:
        description = 'Вход пользователя в систему'

    class Arguments:
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        print(kwargs)
        user = authenticate(info.context, **kwargs)
        if user is not None:
            login(info.context, user)
        return Login(user=user, success=user is not None)


class Logout(graphene.Mutation):
    class Meta:
        description = 'Выход пользователя из системы'

    success = graphene.Boolean(required=True, description='Успех операции')

    @staticmethod
    def mutate(root, info):
        if info.context.user.is_authenticated:
            logout(info.context)
            return Logout(success=True)
        else:
            return Logout(success=False)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = Login.Field()
    logout = Logout.Field()
