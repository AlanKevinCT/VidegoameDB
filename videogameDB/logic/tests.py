from django.test import TestCase
from django.urls import reverse
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

    def test_add_vg(self):
        response = self.client.post(reverse('add_vg'), {
            'title': 'Undertale',
            'relase_date': '2015-10-21',
            'is_it_bought': False,
            'platform': 'Multiplatform',
            'story_mode': VGEnum.DONE,
            'any_percent': VGEnum.DONE
        })
        self.assertEqual(response.status_code, 302)
        videogame = Videogame.objects.get(title='Undertale')
        self.assertEqual(videogame.relase_date, date(2015, 10, 21))
        self.assertEqual(videogame.is_it_bought, False)
        self.assertEqual(videogame.platform, 'Multiplatform')
        self.assertEqual(videogame.story_mode, VGEnum.DONE)
        self.assertEqual(videogame.any_percent, VGEnum.DONE)