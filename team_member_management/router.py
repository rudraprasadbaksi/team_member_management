from members.viewsets import MemberViewset
from rest_framework import routers

app_name = 'members'
router = routers.DefaultRouter()
router.register('member', MemberViewset)
