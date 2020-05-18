from django.test import TestCase

# Create your tests here.

from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from .models import Member
from team_member_management.router import router
import json
from django.http import JsonResponse
from .viewsets import MemberViewset


class MemberCretateTests(APITestCase):

    def test_create_member(self):
        url = reverse('member-list')

        data = {
            'first_name': 'Rudra',
            'last_name': 'Baksi',
            'phone_number': '5566778899',
            'email': 'rudrapra@buffalo.edu',
            'role': 'Regular',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 1)
        self.assertEqual(Member.objects.get().first_name, 'Rudra')

    def test_retrieve_member(self):
        request = APIRequestFactory().get("")
        member_detail = MemberViewset.as_view({'get': 'retrieve'})
        member = Member.objects.create(first_name="bob")

        response = member_detail(request, pk=member.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_member(self):
        request = APIRequestFactory().delete("")
        member_detail = MemberViewset.as_view({'delete': 'destroy'})
        member = Member.objects.create(first_name="marley")
        response = member_detail(request, pk=member.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
