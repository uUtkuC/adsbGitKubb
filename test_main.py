from PlaneData import PlaneData


def test_isInit_correct():
    plane_instance = PlaneData("471f8f","WZZ4641","1710933062","27.623","40.4816","False","239.4","158.18","0")
    assert (plane_instance.longitude =="27.623")


