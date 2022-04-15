from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FamilyChildSerializers, FamilySerializers, ChildSerializers

from .models import Family, Child

@api_view(['GET'])
def apiOverview(request):
    data = [
        {
            'status': 'success',
            'msg': 'CRUD operations on families and their children'
        },
        [{
            'list family with child': 'http://127.0.0.1:8000/api/family-child/',
            'list family': 'http://127.0.0.1:8000/api/family/',
            'list child': 'http://127.0.0.1:8000/api/child/',
            'create family': 'http://127.0.0.1:8000/api/family/create/',
            'create child': 'http://127.0.0.1:8000/api/child/create',

            'update family': 'http://127.0.0.1:8000/api/family/update/<enter id>',
            'update child': 'http://127.0.0.1:8000/api/child/update/<enter id>',
            'delete family': 'http://127.0.0.1:8000/api/family/delete/<enter id>',
            'delete child': 'http://127.0.0.1:8000/api/child/delete/<enter id>'
        }]
    ]
    return Response(data)

@api_view(['GET'])
def familyChildList(request):
    families = Family.objects.all()
    serializer = FamilyChildSerializers(families, many=True)
    data = [
        {
            'status': 'success',
            'msg': 'list of families and their children'
        },
        serializer.data
    ]
    return Response(data)

@api_view(['GET'])
def familyList(request):
    families = Family.objects.all()
    serializer = FamilySerializers(families, many=True)

    for i in serializer.data:
        i.update({ 'update_url': 'http://127.0.0.1:8000/api/family/update/' + str(i['_id']) })
        i.update({ 'delete_url': 'http://127.0.0.1:8000/api/family/delete/' + str(i['_id']) })

    data = [
        {
            'status': 'success',
            'msg': 'list of families'
        },
        serializer.data
    ]
    return Response(data)

@api_view(['GET'])
def childList(request):
    children = Child.objects.all()
    serializer = ChildSerializers(children, many=True)

    for i in serializer.data:
        i.update({ 'update_url': 'http://127.0.0.1:8000/api/child/update/' + str(i['_id']) })
        i.update({ 'delete_url': 'http://127.0.0.1:8000/api/child/delete/' + str(i['_id']) })

    data = [
        {
            'status': 'success',
            'msg': 'list of  children'
        },
        serializer.data
    ]
    return Response(data)

@api_view(['GET', 'POST'])
def createFamily(request):
    if request.method == 'POST':
        serializer = FamilySerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = [
                {
                    'status': 'success',
                    'msg': 'newely created object of family'
                },
                serializer.data
            ]
            return Response(data)
        else:
            data = [
                {
                    'status': 'failure',
                    'msg': 'object creation failed'
                },
                serializer.errors
            ]
            return Response(data)
    else:
        data = [
            {
                'status': 'success',
                'msg': 'format for data entry is following'
            },
            [{
                'surname': 'new surname',
                'parent1': 'parent 1 name',
                'parent2': 'parent 2 name',
            }]
        ]
        return Response(data)

@api_view(['GET', 'POST'])
def createChild(request):
    if request.method == 'POST':
        serializer = ChildSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = [
                {
                    'status': 'success',
                    'msg': 'newely created object of child'
                },
                serializer.data
            ]
            return Response(data)
        else:
            data = [
                {
                    'status': 'failure',
                    'msg': 'object creation failed'
                },
                serializer.errors
            ]
            return Response(data)
    else:
        data = [
            {
                'status': 'success',
                'msg': 'format for data entry is following'
            },
            [{
                'name': 'child name',
                'family': 'child family id/key'
            }]
        ]
        return Response(data)

@api_view(['GET', 'POST'])
def familyUpdate(request, pk):
    if request.method == 'POST':
        family = Family.objects.get(_id=pk)
        serializer = FamilySerializers(instance=family, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = [
                {
                    'status': 'success',
                    'msg': 'updated object of family'
                },
                serializer.data
            ]
            return Response(data)
        else:
            data = [
                {
                    'status': 'failure',
                    'msg': 'object updation failed'
                },
                serializer.errors
            ]
            return Response(data)
    else:
        data = [
            {
                'status': 'success',
                'msg': 'format for data entry is following'
            },
            [{
                'surname': 'new surname',
                'parent1': 'parent 1 name',
                'parent2': 'parent 2 name'
            }]
        ]
        return Response(data)

@api_view(['GET', 'POST'])
def childUpdate(request, pk):
    if request.method == 'POST':
        child = Child.objects.get(_id=pk)
        serializer =  ChildSerializers(instance=child, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = [
                {
                    'status': 'success',
                    'msg': 'updated object of child'
                },
                serializer.data
            ]
            return Response(data)
        else:
            data = [
                {
                    'status': 'failure',
                    'msg': 'object updation failed'
                },
                serializer.errors
            ]
            return Response(data)
    else:
        data = [
            {
                'status': 'success',
                'msg': 'following is a dictionary for example',
            },
            [{
                'name': 'child name',
                'family': 'child family id/key'
            }]
        ]
        return Response(data)

@api_view(['GET'])
def familyDelete(request, pk):
    if Family.objects.filter(_id=pk).exists():
        family = Family.objects.get(_id=pk).delete()

        data = [
            {
                'status': 'success',
                'msg': 'object deleted'
            },
            family
        ]
        return Response(data)
    else:
        return Response([{ 'status': 'failure', 'msg': 'Object does not exists' }, []])

@api_view(['GET'])
def childDelete(request, pk):
    if Child.objects.filter(_id=pk).exists():
        child = Child.objects.get(_id=pk).delete()
        
        data = [
            {
                'status': 'success',
                'msg': 'object deleted'
            },
            child
        ]
        return Response(data)
    else:
        return Response([{ 'status': 'failure', 'msg': 'Object does not exists' }, []])

@api_view(['GET'])
def warn(request):
    return Response([{ 'status': 'failure', 'msg': 'incomplete url' }, []])