import sender_stand_request
import data

def test_positive_assert():
    create_order = sender_stand_request.post_create_order()
    track = create_order.json()["track"]

    receiving_order = sender_stand_request.get_receiving_order(track)   

    assert create_order.status_code == 201
    assert receiving_order.status_code == 200

    order_data = data.order_body
    
    order_info = receiving_order.json()["orders"][0]

    # assert order_info["firstName"] == order_data["firstName"]
    # assert order_info["lastName"] == order_data["lastName"]
    # assert order_info["address"] == order_data["address"]
    # assert order_info["metroStation"] == order_data["metroStation"]
    # assert order_info["phone"] == order_data["phone"]
    # assert order_info["rentTime"] == order_data["rentTime"]
    # assert order_info["deliveryDate"] == order_data["deliveryDate"]
    # assert order_info["color"] == order_data["color"]
    # assert order_info["comment"] == order_data["comment"]
