import pytest
import random
from datetime import datetime


class TestMyTarget:

    @pytest.mark.API
    def test_create_segment(self, api_client):
        """
        Создаем новый сегмент, получаем его id и
        проверям наличие в списке сегментов,
        затем удаляем сегмент
        """
        name = 'Segment ' + str(random.randint(0, 999)) + ' at ' + str(datetime.now())
        segment_id = api_client.create_segment(name)['id']
        segments = api_client.segment_list()
        assert any(i['id'] == segment_id for i in segments['items'])
        api_client.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        """
        Создаем новый сегмент,
        проверяем его наличие в списке сегментов,
        удаляем сегмент и проверяем отсутствие в списке сегментов
        """
        name = 'Segment ' + str(random.randint(0, 999)) + ' at ' + str(datetime.now())
        segment_id = api_client.create_segment(name)['id']
        segments = api_client.segment_list()
        assert any(i['id'] == segment_id for i in segments['items'])
        api_client.delete_segment(segment_id)
        segments = api_client.segment_list()
        assert not any(i['id'] == segment_id for i in segments['items'])