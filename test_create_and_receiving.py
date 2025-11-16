import sender_stand_request
import data

def test_positive_assert():
    create_order = sender_stand_request.post_create_order()
    track = create_order.json()["track"]

    receiving_order = sender_stand_request.get_receiving_order(track)   

    assert create_order.status_code == 201
    assert receiving_order.status_code == 200
