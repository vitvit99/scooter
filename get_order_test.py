import sender_stand_request


# Виктор Жмакин, 12-я когорта — Финальный проект. Инженер по тестированию плюс

def test_getting_order_by_track_number():
    response = sender_stand_request.get_order()
    assert response.status_code == 200
