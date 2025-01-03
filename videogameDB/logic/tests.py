from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from datetime import date
from .models import *

class VidegamesTest(TestCase):
    def setUp(self):
        Videogame.objects.create(
            title='The Legend of Zelda',
            relase_date='1986-02-21',
            is_it_bought=True,
            platform='NES',
            story_mode=VGEnum.DONE,
            any_percent=VGEnum.IN_PROGRESS
        )
        Videogame.objects.create(
            title='Super Mario Bros',
            relase_date='1985-09-13',
            is_it_bought=False,
            platform='NES',
            story_mode=VGEnum.NOT_STARTED,
            any_percent=VGEnum.NOT_STARTED
        )

    def test_enlist(self):
        response = self.client.get(reverse('enlist_vg'))
        self.assertEqual(response.status_code, 200)
        games = Videogame.objects.all()
        self.assertEqual(games.count(), 2)
        expected_data = [
            {
                'title': 'The Legend of Zelda',
                'relase_date': date(1986, 2, 21),
                'is_it_bought': True,
                'platform': 'NES',
                'story_mode': VGEnum.DONE,
                'any_percent': VGEnum.IN_PROGRESS
            },
            {
                'title': 'Super Mario Bros',
                'relase_date': date(1985, 9, 13),
                'is_it_bought': False,
                'platform': 'NES',
                'story_mode': VGEnum.NOT_STARTED,
                'any_percent': VGEnum.NOT_STARTED
            },
        ]
        actual_data = list(
            games.values('title', 'relase_date', 'is_it_bought', 'platform', 'story_mode', 'any_percent')
        )
        self.assertEqual(actual_data, expected_data)

    def test_addVG(self):
        Videogame = {     
            'title': 'Undertale',
            'relase_date': date(2015, 10, 21),
            'is_it_bought': False,
            'platform': 'Multiplatform',
            'story_mode': VGEnum.DONE,
            'any_percent': VGEnum.DONE
        }
        response = self.client.post(reverse('post_vg'), Videogame, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Undertale")
        self.assertEqual(response.data["release_date"], "2015-10-21")
        self.assertEqual(response.data["is_it_bought"], False)
        self.assertEqual(response.data["story_mode"], VGEnum.DONE)
        self.assertEqual(response.data["any_percent"], VGEnum.DONE)
